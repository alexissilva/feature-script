import argparse
import os
from feature_script import create_file_or_directory


base_code_path = "/Users/alexissilva/Documents/Mach/maas/qrBip/src/main/java"

script_path = os.path.dirname(os.path.abspath(__file__))
feature_template_path = os.path.join(script_path, "templates/maas/prefix")


def create_feature(feature_name: str):
    print(f"Creating feature: {feature_name}...")
    print(f"Directories and files created:")
    
    current_path = os.getcwd()
    create_file_or_directory(current_path, feature_template_path, feature_name, base_code_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a new feature.')
    parser.add_argument('feature_name', type=str, help='Name of the feature to create')
    args = parser.parse_args()
    create_feature(args.feature_name)