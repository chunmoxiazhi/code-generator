from .output_manager import generate_code, write_files

def output_files(categorized_endpoints_data, output_dir):
    code_list = generate_code(categorized_endpoints_data)
    write_files(code_list, output_dir)