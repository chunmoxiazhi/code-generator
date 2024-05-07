import re

from .schema import ParameterSchema, EndpointSchema

def extract_query_parameters(request_url):
    query_parameters = []
    for param in request_url.get("query", []):
        parameter_data = {
            "key": param.get("key"),
            "value": param.get("value", "")
        }
        query_parameters.append(parameter_data)

    return query_parameters


def extract_path_parameters(request_url):
    url_path = request_url.get("raw", "")
    path_parameters = [param for param in re.findall(r"{([A-Za-z]+)}", url_path)]
    return path_parameters

def extract_request_body(item):
    request_body = ""
    if "body" in item["request"]:
        request_body_str = item["request"]["body"]["raw"]
        start_index = min(request_body_str.find('{'), request_body_str.find('['))
        end_index = max(request_body_str.rfind('}'), request_body_str.rfind(']'))
        
        if start_index != -1 and end_index != -1:
            request_body = request_body_str[start_index:end_index+1]
    return request_body

def extract_headers(item):
    headers = {}
    if "request" in item:
        request = item["request"]
        if "header" in request:
            headers = request["header"]
    return headers

def remove_empty_tags(api_response):
    # Filter out tags with an empty list of endpoints
    filtered_tags = [tag for tag in api_response if tag['endpoints']]
    return filtered_tags

def convert_to_endpoint(item):
    query_parameters = extract_query_parameters(item["request"]["url"])
    path_parameters = extract_path_parameters(item["request"]["url"])
    request_body = extract_request_body(item)
    headers = extract_headers(item)

    endpoint_data = {
        "name": item["name"],
        "request_method": item["request"]["method"],
        "url": item["request"]["url"].get("raw", ""),
        "query_parameters": query_parameters,
        "path_parameters": path_parameters,
        "request_body": request_body,
        "headers": headers,
    }
    return endpoint_data