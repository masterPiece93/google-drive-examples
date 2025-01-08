from enum import Enum


__all__ = [
    'ExampleData',
]


class ExampleData(Enum):

    CSV_FILE_NAME = 'example_csv_file.csv'
    JSON_FILE_NAME = 'example_json_file.json'
    TEXT_FILE_NAME = 'example_text_file.txt'
    TEXT_PROMPT_FILE_NAME = 'example_prompt.txt'
