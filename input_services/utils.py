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
        request_body = item["request"]["body"]["raw"]
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