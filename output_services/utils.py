import re
import json

def format_file_name(class_name):
    words = re.findall('[A-Z][a-z]*', class_name)
    file_name = '_'.join(words).lower()
    return file_name


def format_class_name(tag_name):
    while tag_name and (not tag_name[0].isalpha()):
        tag_name = tag_name[1:]

    formatted_tag_name = ''.join(char for char in tag_name if char.isalnum() or char.isspace())

    words = formatted_tag_name.split()
    formatted_words = [word.capitalize() for word in words]
    class_name = ''.join(formatted_words)
    return class_name

def camel_to_snake(camel_str):
    snake_str = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_str)
    snake_str = snake_str.lower()
    return snake_str

def requires_permission(endpoint):
    headers = endpoint.get('headers', [])
    for header in headers:
        key = header.get('key', '').lower()
        if 'auth' in key or 'token' in key or 'access' in key:
            return True
    return False

def replace_path_parameters(uri):
    path_list = uri.split("/")
    
    for i, path in enumerate(path_list):
        if path.startswith(":"):
            path_list[i] = "{" + camel_to_snake(path[1:]) + "}"
    
    return "/".join(path_list)

def format_function_name(endpoint):
    name_without_special_chars = re.sub(r'[^a-zA-Z\s]', '', endpoint['name'])
    return endpoint['request_method'].lower() + '_' + name_without_special_chars.replace(' ', '_').lower()

def generate_serializer(data, class_name=''):
    sub_model_class_string = f"\nclass {format_class_name(class_name)}Serializer(serializers.Serializer):\n"
    sub_models = []

    for key, value in data.items():
        if isinstance(value, dict):
            sub_class_name = camel_to_snake(key.capitalize())
            sub_model_string, sub_sub_models = generate_serializer(value, sub_class_name)
            sub_models.append(sub_model_string)
            sub_models.extend(sub_sub_models)
            sub_model_class_string += f"    {camel_to_snake(key)} = {format_class_name(sub_class_name)}Serializer()\n"
        elif isinstance(value, int) or isinstance(value, float):
            sub_model_class_string += f"    {camel_to_snake(key)} = serializers.FloatField()\n"
        elif isinstance(value, str):
            if "<" in value and ">" in value and value[value.index("<") + 1:value.index(">")] == "float":
                    sub_model_class_string += f"    {camel_to_snake(key)} = serializers.FloatField()\n"
            else:
                sub_model_class_string += f"    {camel_to_snake(key)} = serializers.CharField()\n"

    return sub_model_class_string, sub_models

def generate_request_body_models(endpoint):
    models = "from rest_framework import serializers\n"

    # Remove introductory line if present
    input_string = re.sub(r'^----.*?----\s*', '', endpoint["request_body"], flags=re.DOTALL)

    # Extract JSON content from the input string
    json_pattern = r'\{[^{}]*\}'
    json_match = re.search(json_pattern, input_string, re.DOTALL)

    if json_match:
        json_content = json_match.group()

        # Use the extracted JSON content directly
        request_body = json.loads(json_content)
        serializer_string, sub_models = generate_serializer(request_body, endpoint["name"])

        # Add sub-models to the models string
        models += serializer_string
        for sub_model in sub_models:
            models += sub_model
    else:
        models += "# Error: No JSON content found\n"

    return models