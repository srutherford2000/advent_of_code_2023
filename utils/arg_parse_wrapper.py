import argparse
import os

def validate_file_path(path):
    if not os.path.exists(path):
        raise argparse.ArgumentTypeError(f"The file '{path}' does not exist.")
    return path

def validate_int(possible_int):
    try:
        return int(possible_int)
    except:
        raise argparse.ArgumentTypeError(f"The argument '{possible_int}' is not a valid int")

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


def filepath_and_int_argparse():
    parser = argparse.ArgumentParser(description="Script to work with a file.")

    # Define the command-line argument for the file path
    parser.add_argument(
        "filepath",
        type=validate_file_path,
        help="Path to the file that you want to process."
    )
    
    parser.add_argument(
        "target_number",
        type=validate_int,
        help="A target number that will be needed for the script."
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the validated file path
    file_path = args.filepath
    target_number = int(args.target_number)

    return (file_path,target_number)