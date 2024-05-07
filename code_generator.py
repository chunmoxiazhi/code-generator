import argparse
from input_services.input_services import extract_input_file
from output_services.output_services import output_files
def parse_arguments():
    default_output_dir = "output_dir"

    parser = argparse.ArgumentParser(description="OpenAPI Code Generator")
    parser.add_argument("-i", "--input", required=True, help="Path to the OpenAPI Specification file")
    parser.add_argument("-o", "--output-dir", default=default_output_dir, help="Output directory for generated code")
    return parser.parse_args()

def main(input_file, output_dir):
    categorized_endpoints_data = extract_input_file(input_file)

    output_files(categorized_endpoints_data, output_dir)

if __name__ == "__main__":
    # Parse command-line arguments
    args = parse_arguments()
    input_file = args.input
    output_dir = args.output_dir or "./output_folder"

    main(input_file, output_dir)