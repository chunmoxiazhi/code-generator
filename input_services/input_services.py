from .input_manager import read_file, extract_endpoints
from .utils import remove_empty_tags

def extract_input_file(input_file):
    try:
        input_content = read_file(input_file)

        extracted_content = extract_endpoints(input_content)
        categorized_endpoints_data = remove_empty_tags(extracted_content)

        return categorized_endpoints_data
    except IOError as e:
        print(e)
        exit(1)