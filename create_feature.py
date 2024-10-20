import argparse
import os
from feature_script import create_file_or_directory
from config import *
from utils import *

def create_feature(feature_name: str, with_tests: bool) -> None:
    destination_path = os.getcwd()
    root_code_path = get_source_path_until_chunk(destination_path, SOURCE_PATH_CHUNK)

    if not is_destination_path_valid(root_code_path, destination_path):
        return
    

    if with_tests:
        test_destination = get_test_path_from_source_path(destination_path)
        test_root = get_test_path_from_source_path(root_code_path)

    print(f"Creating feature '{feature_name}'...")
    print("Creating directories and files:")

    keywords = [
        KeywordScript(PREFIX_KEYWORD, feature_name),
    ]

    try:
        create_file_or_directory(destination_path, FEATURE_TEMPLATE_PATH, keywords, root_code_path)
        print(f"Feature '{feature_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the feature: {e}")


    if with_tests:
        test_destination = get_test_path_from_source_path(destination_path)
        test_root = get_test_path_from_source_path(root_code_path)

        print(f"Creating test of '{feature_name}'...")
        print("Creating directories and files:")
        try:
            create_file_or_directory(test_destination, FEATURE_TEST_TEMPLATE_PATH, keywords, test_root)
            print(f"Test of feature '{feature_name}' created successfully.")
        except Exception as e:
            print(f"An error occurred while creating tests: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a new feature.')
    parser.add_argument('feature_name', type=str, help='Name of the feature to create.')
    parser.add_argument('--with-tests', action='store_true', help='Include test files in the feature creation.')

    args = parser.parse_args()
    create_feature(args.feature_name, args.with_tests)