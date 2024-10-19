import argparse
import os
from feature_script import create_file_or_directory
from config import *
from utils import *

def create_feature(feature_name: str):
    destination_path = os.getcwd()
    root_code_path = get_root_code_path(ROOT_PROJECT_PATH, MODULE, CODE_PATH)

    if not is_destination_path_valid(root_code_path, destination_path):
        return

    print(f"Creating feature: {feature_name}...")
    print(f"Directories and files created:")
    create_file_or_directory(destination_path, FEATURE_TEMPLATE_PATH, feature_name, root_code_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a new feature.')
    parser.add_argument('feature_name', type=str, help='Name of the feature to create')
    args = parser.parse_args()
    create_feature(args.feature_name)