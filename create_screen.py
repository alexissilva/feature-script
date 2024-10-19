import argparse
import os
from feature_script import create_file_or_directory
from config import *
from utils import *

def create_screen(screen_name: str) -> None:
    destination_path = os.getcwd()
    root_code_path = get_root_code_path(ROOT_PROJECT_PATH, MODULE, CODE_PATH)

    if not is_destination_path_valid(root_code_path, destination_path):
        return

    print(f"Creating screen '{screen_name}'...")
    print("Creating directories and files:")
    
    try:
        for sub_path in os.listdir(SCREEN_TEMPLATE_PATH):
            abs_sub_path = os.path.join(SCREEN_TEMPLATE_PATH, sub_path)
            create_file_or_directory(destination_path, abs_sub_path, screen_name, root_code_path)
        print(f"Screen '{screen_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the screen: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a new screen within a feature.')
    parser.add_argument('screen_name', type=str, help='Name of the screen to create.')

    args = parser.parse_args()
    create_screen(args.screen_name)