import re
import json

def format_file_name(class_name):
    words = re.findall('[A-Z][a-z]*', class_name)
    file_name = '_'.join(words).lower()
    return file_name

def format_class_name(tag_name):
    # Replace special characters and numbers with space
    # Split the string by spaces
    # Capitalize the first letter of each splitted string, then concat them into 1 string
    cleaned_tag_name = ''.join([' ' if (not char.isalpha() and char != ' ') else char for char in tag_name])
    formatted_words = [word.capitalize() for word in cleaned_tag_name.split()]
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

def generate_serializer(request_body, class_name=''):
    # Recursive function that generates serializers
    sub_model_class_string = f"\nclass {format_class_name(class_name)}Serializer(serializers.Serializer):\n"
    sub_models = []
    
    data = None

    if isinstance(request_body, list):
        data = request_body[0]
    else:
        data = request_body

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

def generate_request_body_models(endpoint, models):
    
    request_body = json.loads(endpoint["request_body"])
    serializer_string, sub_models = generate_serializer(request_body, endpoint["name"])

    models += serializer_string
    for sub_model in sub_models:
        models += sub_model

    models = models + "\n\nrequest_body_sample = " + endpoint["request_body"]
    return models

def generate_query_parameter_models(endpoint, models):
    models += f"\nclass {format_class_name(endpoint['name'])}QueryParameterSerializer(serializers.Serializer):\n"

    for param in endpoint['query_parameters']:
        key = param['key']
        value = param['value']
        
        if 'string' in value.lower():
            field_type = "serializers.CharField()"
        elif 'true' in value.lower() or 'false' in value.lower():
            field_type = "serializers.BooleanField()"
        else:
            field_type = f"serializers.CharField() #{value}"
        
        models += f"    {camel_to_snake(key)} = {field_type}\n"
    return models
