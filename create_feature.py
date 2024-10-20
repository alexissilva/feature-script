import argparse
import os
from feature_script import create_component
from config import *
from utils import *

def create_feature(feature_name: str, with_tests: bool):
    destination_path = os.getcwd()
    base_package = get_package_of_path(destination_path)

    keywords = [KeywordScript(PREFIX_KEYWORD, feature_name)]
    test_template_path = FEATURE_TEST_TEMPLATE_PATH if with_tests else None

    create_component(destination_path, FEATURE_TEMPLATE_PATH, keywords, base_package, feature_name, "feature", test_template_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a new feature.')
    parser.add_argument('feature_name', type=str, help='Name of the feature to create.')
    parser.add_argument('-t', '--with-tests', action='store_true', help='Include test files in the feature creation.')

    args = parser.parse_args()
    create_feature(args.feature_name, args.with_tests)