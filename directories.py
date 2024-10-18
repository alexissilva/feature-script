from fs_node import FSNode
from constants import *


# Architecture directory structure
_data_directory = FSNode(
    name="data",
    sub_nodes=[
        FSNode(name="model"),
        FSNode(
            name="remote",
            sub_nodes=[
                FSNode(name=f"{NAME_PREFIX}WebService.kt", is_file=True)
            ]
        ),
        FSNode(
            name="source",
            sub_nodes=[
                FSNode(name=f"{NAME_PREFIX}Remote.kt", is_file=True)
            ]
        ),
        FSNode(name=f"{NAME_PREFIX}Repository.kt", is_file=True)
    ]
)

_di_directory = FSNode(name="di")

_presentation_directory = FSNode(
    name="presentation",
    sub_nodes=[
        FSNode(name=f"{NAME_PREFIX}ViewModel.kt", is_file=True, template_file="ViewModelTemplate.kt"),
        FSNode(
            name=NAME_PREFIX_LOWERCASE,
            sub_nodes=[
                FSNode(name=f"{NAME_PREFIX}Contract.kt", is_file=True),
                FSNode(name=f"{NAME_PREFIX}Processor.kt", is_file=True),
                FSNode(name=f"{NAME_PREFIX}Reducer.kt", is_file=True)
            ]
        )
    ]
)

_ui_directory = FSNode(name="ui", sub_nodes=[
    FSNode(name=f"{NAME_PREFIX}Screen.kt", is_file=True, template_file="ScreenTemplate.kt"),
])

feature_directory = FSNode(
    name=NAME_PREFIX_LOWERCASE,
    sub_nodes=[
        _data_directory,
        _di_directory,
        _presentation_directory,
        _ui_directory,
    ]
)

screen_directories = [
    _presentation_directory,
    _ui_directory
]