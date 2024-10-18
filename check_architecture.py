import argparse
import os
from feature_script import check_directory
from constants import *
from directories import feature_directory


module_code_path = os.path.join(PROJECT_ROOT_PATH, MODULE, CODE_PATH)
absolute_package_path = os.path.join(module_code_path, PACKAGE_PATH)


def check_architecture(feature_name: str) -> bool:
    """Check if the architecture of the given feature is correct."""
    
    print(f"Checking architecture of feature: {feature_name}...")
    is_ok = check_directory(absolute_package_path, feature_directory, feature_name)
    
    if is_ok:
        print(f"Architecture for '{feature_name}' is correct.")
    else:
        print(f"Architecture for '{feature_name}' is incorrect.")
    
    return is_ok


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check architecture of a feature.')
    parser.add_argument('feature_name', type=str, help='Name of the feature to check')
    args = parser.parse_args()
    check_architecture(args.feature_name)