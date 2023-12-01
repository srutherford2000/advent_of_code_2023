import argparse
import os

def validate_file_path(path):
    if not os.path.exists(path):
        raise argparse.ArgumentTypeError(f"The file '{path}' does not exist.")
    return path

def only_filepath_argparse():
    parser = argparse.ArgumentParser(description="Script to work with a file.")

    # Define the command-line argument for the file path
    parser.add_argument(
        "filepath",
        type=validate_file_path,
        help="Path to the file that you want to process."
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the validated file path
    file_path = args.filepath

    return file_path