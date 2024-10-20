import os

SOURCE_PATH_CHUNK = "src/main/java"  # Path for main source code relative to the root of the module/project
TEST_PATH_CHUNK = "src/test/java"  # Path for test code relative to the root of the module/project

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_TEMPLATE_PATH = os.path.join(SCRIPT_PATH, "exampleTemplates/android/mach")
FEATURE_TEMPLATE_PATH = os.path.join(ROOT_TEMPLATE_PATH, "feature/main/prefix")
SCREEN_TEMPLATE_PATH = os.path.join(ROOT_TEMPLATE_PATH, "screen")
FEATURE_TEST_TEMPLATE_PATH = os.path.join(ROOT_TEMPLATE_PATH, "feature/test/prefix")

PREFIX_KEYWORD = "Prefix"
FEATURE_KEYWORD = "Feature"


IGNORE_FILES = {
    ".DS_Store"
}