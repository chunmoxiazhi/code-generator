import os
import re
import json

from .schema import ParameterSchema, EndpointSchema
from .utils import extract_query_parameters, extract_path_parameters, extract_request_body, extract_headers
def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
        return content
    except IOError:
        raise IOError(f"Error: Could not read from file '{file_path}'.")

def extract_endpoints(api_content):
    tags = []
    api_data = api_content if isinstance(api_content, dict) else json.loads(api_content)

    def extract_items(items):
        endpoints = []
        for item in items:
            if "request" in item:
                # Extracting data
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

                endpoints.append(endpoint_data)

            if "item" in item:
                # Recursively extract items
                nested_endpoints = extract_items(item["item"])
                endpoints.extend(nested_endpoints)

        return endpoints

    if "item" in api_data:
        tags = [{
            "name": tag.get("name", ""),
            "endpoints": extract_items(tag["item"]) if "item" in tag else []
        } for tag in api_data["item"]]

    return tags