import argparse
import os
from feature_script import create_component
from config import *
from utils import *

def create_screen(screen_name: str, feature_name: str) -> None:
    destination_path = os.getcwd()
    base_package = get_package_of_path(destination_path)

    keywords = [
        KeywordScript(PREFIX_KEYWORD, screen_name),
        KeywordScript(FEATURE_KEYWORD, feature_name)
    ]

    for sub_path in os.listdir(SCREEN_TEMPLATE_PATH):
        abs_sub_path = os.path.join(SCREEN_TEMPLATE_PATH, sub_path)
        create_component(destination_path, abs_sub_path, keywords, base_package, screen_name, "{sub_path} of screen")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a new screen within a feature.')
    parser.add_argument('feature_name', type=str, help='The name of the feature where the screen will be created.')
    parser.add_argument('screen_name', type=str, help='The name of the screen to be created.')

    args = parser.parse_args()
    create_screen(args.screen_name, args.feature_name)