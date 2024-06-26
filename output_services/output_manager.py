import os
import re
import json

from .utils import format_file_name, format_class_name, camel_to_snake, requires_permission, \
    replace_path_parameters, format_function_name, generate_request_body_models, generate_query_parameter_models

def generate_imports(tag, permission_required):
    code = "import os\n"
    code += "from abc import ABC\n"
    code += "import requests\n"
    code += "from rest_framework.exceptions import PermissionDenied\n"
    code += "from requests.exceptions import RequestException\n"

    param_keys = []
    for endpoint in tag.get('endpoints', []):
        query_parameters = endpoint.get('query_parameters', [])
        path_parameters = endpoint.get('path_parameters', [])
        request_body = endpoint.get('request_body', '')

        if isinstance(request_body, dict):
            request_body_keys = request_body.keys()
            param_keys.extend([key.lower() for key in request_body_keys])

        param_keys.extend([param['key'].lower() for param in query_parameters])
        param_keys.extend([param.lower() for param in path_parameters])

    if any("date" in key for key in param_keys):
        code += "from datetime import datetime\n"

    return code

def generate_query_parameter_code(query_parameters):
    result = ""
    for param in query_parameters:
        key = camel_to_snake(param['key'])
        result += f"        {key} = kwargs.get('{key}', None) \n"

    return result

def generate_url(endpoint, is_query_params=False):
    uri = endpoint['url']
    uri = uri.lstrip('/')

    uri = replace_path_parameters(uri)
    
    if is_query_params:
        query_params = endpoint['query_parameters']
        param_strings = uri.split("?", 1)[1].split('&')
        for i, param_string in enumerate(param_strings):
            for query_param in query_params:
                if query_param['key'] in param_string:
                    matched_key = query_param['key']
                    param_var = camel_to_snake(matched_key)
                    param_value_match = re.search(r'{(.*?)}', param_string)
                    if not param_value_match:
                        # If no match is found between '{' and '}', look for '<' and '>'
                        param_value_match = re.search(r'<(.*?)>', param_string)
                        if param_value_match:
                            param_value = param_value_match.group(1)
                            param_string = param_string.replace(f'<{param_value}>', f'{{{param_value}}}')
                    if param_value_match:
                        param_value = param_value_match.group(1)
                        param_strings[i] = param_string.replace(f'{{{param_value}}}', f'{{{param_var}}}')
                    break
        uri = '&'.join(param_strings)

    def replace_with_snake(match):
        key = match.group(1)
        return f"{{{camel_to_snake(key)}}}"

    uri = re.sub(r'{([^}]*)}', replace_with_snake, uri)
    url = f"        uri = f\"{uri}\"\n" + f"        uri = self.HOST + uri\n"
    return url

def initialize_class(tag, class_name, permission_required):
    permission_code = ", permission=Permission" if permission_required else ""
    code = f"\n\nclass {class_name}(ABC):\n"
    code += f"    def __init__(self{permission_code}):\n"
    code += f"        super().__init__()\n"

    if permission_required:
        code += f"        api_keys = permission.api_keys if permission else None\n"
        code += f"        if not api_keys or not api_keys.get('api_key', None) or not api_keys.get('secret', None):\n"
        code += f'            raise PermissionDenied("Your account has not been yet configure to perform {class_name} API operations")\n'
    return code

def generate_function_definition(endpoint, is_request_body, is_path_params, is_query_params):
    function_name = format_function_name(endpoint)
    parameters = []
    
    if is_request_body:
        parameters.append('validated_data')
    
    if is_path_params:
        for param in endpoint['path_parameters']:
            parameters.append(camel_to_snake(param))
    
    if is_query_params:
        parameters.append('**kwargs')
    
    parameters_str = ', '.join(parameters)
    
    if not any([is_request_body, is_path_params, is_query_params]):
        function_definition = f"    def {function_name}(self):\n"
    else:
        function_definition = f"    def {function_name}(self, {parameters_str}):\n"
    
    return function_definition

def generate_headers(endpoint):
    headers = endpoint['headers']
    formatted_headers = "        headers = {\n"
    for header in headers:
        key = header['key']
        value = header['value']

        if any(keyword in key.lower() for keyword in ['auth', 'access', 'token']):
            formatted_headers += f"            '{key}': 'Bear token'\n"
        else:
            formatted_headers += f"            '{key}': '{value}',\n"

    return formatted_headers + "        }\n"

def generate_request(endpoint, is_request_body):
    request_body = ""
    validated_data = ""
    if is_request_body:
        request_body = "json=validated_data,"
        validated_data = ", validated_data"
    raise_request_code = f"        response = request.{endpoint['request_method'].lower()}(\n"
    request_content_code = f"            uri, {request_body}headers=headers)\n"
    response_status_code = f"        response.raise_for_status()\n"
    return_response_code = f"        return response{validated_data}\n"
    
    return raise_request_code + request_content_code + response_status_code + return_response_code

def generate_model(endpoint, is_request_body, is_query_params, models):
    models = ""
    if is_request_body:
        models += generate_request_body_models(endpoint, models)
    if is_query_params:
        models += generate_query_parameter_models(endpoint, models)
    return models

def generate_code(endpoints_data):
    code_list = []
    for tag in endpoints_data:
        requests = ""
        models = "from rest_framework import serializers\n"
        tag_name = tag.get('name')
        class_name = format_class_name(tag_name) + 'Service'
        permission_required = any(requires_permission(endpoint) for endpoint in tag.get('endpoints', []))
        imports = generate_imports(tag, permission_required)
        initialized_class = initialize_class(tag, class_name, permission_required)

        class_name_snake = camel_to_snake(class_name)
        for endpoint in tag['endpoints']:
            is_query_params = bool(endpoint.get('query_parameters'))
            is_path_params = bool(endpoint.get('path_parameters'))
            is_request_body = bool(endpoint.get('request_body'))

            endpoint_func_def = generate_function_definition(endpoint, is_request_body, is_path_params, is_query_params)
            endpoint_url = generate_url(endpoint, is_query_params)
            query_parameters = generate_query_parameter_code(endpoint['query_parameters']) if is_query_params else ""
            headers = generate_headers(endpoint)
            request_and_response = generate_request(endpoint, is_request_body)

            requests += "\n" + endpoint_func_def + query_parameters + endpoint_url + headers + request_and_response
            models += generate_model(endpoint, is_request_body, is_query_params, models)

        code_list.append({
            "name": class_name_snake,
            "code": imports + initialized_class + requests,
            "models": models
        })

    return code_list

def write_files(code_list, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    for tag in code_list:
        class_name = tag["name"]
        code = tag["code"]
        models = tag['models']
        class_dir = os.path.join(output_dir, class_name)  # Path to the class directory under output_dir
        os.makedirs(class_dir, exist_ok=True)  # Create the class directory
        filename = os.path.join(class_dir, f"{class_name}.py")
        with open(filename, 'w') as file:
            file.write(code)
            file.write("\n\n")
        model_filename = os.path.join(class_dir, f"{class_name}_models.py")
        with open(model_filename, 'w') as file:
            file.write(models)
            file.write("\n\n")
            