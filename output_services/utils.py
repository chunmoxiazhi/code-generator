import re

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