import importlib
import importlib.resources
from .. import __package__ as __package__name__
from ..meta import ExampleData
from .. import __name__, __package__


_source_ = __package__name__

with importlib.resources.path(_source_, 'data') as data_path:

    __data_path__ = data_path
    __csv_file__ = data_path / ExampleData.CSV_FILE_NAME.value
    __json_file__ = data_path / ExampleData.JSON_FILE_NAME.value
    __text_file__ = data_path / ExampleData.TEXT_FILE_NAME.value
    __prompt_text_file__ = data_path / ExampleData.TEXT_PROMPT_FILE_NAME.value
