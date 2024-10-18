import argparse
import os
from feature_script import create_file_or_directory
from constants import *
from directories import screen_directories


module_code_path = os.path.join(PROJECT_ROOT_PATH, MODULE, CODE_PATH)
absolute_package_path = os.path.join(module_code_path, PACKAGE_PATH)


def create_screen(feature_path: str, screen_name: str):
    """
    Creates a new screen directory structure and files based on the provided screen name and feature path.
    """
    absolute_feature_path = os.path.join(absolute_package_path, feature_path)
    print(f"Creating screen: {screen_name}...")
    print(f"Path: {absolute_feature_path}\n")
    print(f"Directories and files created:")

    for screen_dir in screen_directories:
        create_file_or_directory(absolute_feature_path, screen_dir, screen_name, module_code_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a new feature screen.')
    parser.add_argument('feature_path', type=str, help='Path of the feature relative to the package')
    parser.add_argument('screen_name', type=str, help='Name of the screen to create')

    args = parser.parse_args()
    create_screen(args.feature_path, args.screen_name)