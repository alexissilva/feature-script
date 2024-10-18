import argparse
import os
from feature_script import create_file_or_directory
from constants import *
from directories import feature_directory


module_code_path = os.path.join(PROJECT_ROOT_PATH, MODULE, CODE_PATH)
absolute_package_path = os.path.join(module_code_path, PACKAGE_PATH)


def create_feature(feature_name: str):
    """
    Creates a new feature within the specified package.
    """

    print(f"Creating feature: {feature_name}...")
    print(f"Path: {absolute_package_path}\n")
    print(f"Directories and files created:")
    create_file_or_directory(absolute_package_path, feature_directory, feature_name, module_code_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a new feature.')
    parser.add_argument('feature_name', type=str, help='Name of the feature to create')
    args = parser.parse_args()
    create_feature(args.feature_name)