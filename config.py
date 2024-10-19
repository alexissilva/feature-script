import os

ROOT_PROJECT_PATH = "/Users/alexissilva/Documents/Mach/maas"  # Root path of the project
MODULE = "qrBip"  # Name of the specific module
CODE_PATH = "src/main/java"  # Source code path, remains unchanged
# Example of a root code path generated by concatenating path constants: 
# /Users/alexissilva/Documents/Mach/maas/qrBip/src/main/java



SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_TEMPLATE_PATH = os.path.join(SCRIPT_PATH, "templates/maas")
FEATURE_TEMPLATE_PATH = os.path.join(ROOT_TEMPLATE_PATH, "feature/prefix")
SCREEN_TEMPLATE_PATH = os.path.join(ROOT_TEMPLATE_PATH, "screen")
PREFIX_KEYWORD = "Prefix"
FEATURE_KEYWORD = "Feature"

IGNORE_FILES = {
    ".DS_Store"
}