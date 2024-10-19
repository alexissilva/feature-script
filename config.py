import os


SOURCE_CODE_PATH_SEGMENT = "src/main/java"

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_TEMPLATE_PATH = os.path.join(SCRIPT_PATH, "templates/maas")
FEATURE_TEMPLATE_PATH = os.path.join(ROOT_TEMPLATE_PATH, "feature/prefix")
SCREEN_TEMPLATE_PATH = os.path.join(ROOT_TEMPLATE_PATH, "screen")
PREFIX_KEYWORD = "Prefix"
FEATURE_KEYWORD = "Feature"

IGNORE_FILES = {
    ".DS_Store"
}