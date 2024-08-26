"""
This module provides functions for handling file operations including appending to files,
counting words in files, and reading JSON data from files.
"""

import json

# Constants
TEST_FILE_PATH = "test.txt"
EXAMPLE_TEXT = "Hello, world!"
JSON_FILE_PATH = "date.json"


def append_to_file(file_path, text):
    """
    Append text to a file and return the content of the file.

    Args:
        file_path (str): The path to the file.
        text (str): The text to append to the file.

    Returns:
        str: The content of the file after appending the text.
    """
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(text)

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    return content


# Example usage
result = append_to_file(TEST_FILE_PATH, EXAMPLE_TEXT)
print(result)


def count_words(file_path):
    """
    Count the number of words in a file and print the result.

    Args:
        file_path (str): The path to the file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            words = text.split()
            num_words = len(words)
            print(f"Цей файл '{file_path}' містить {num_words} слів.")
    except FileNotFoundError:
        print(f"Помилка: файл '{file_path}' не знайдено.")


count_words(TEST_FILE_PATH)


def read_json_file(file_path):
    """
    Read and return the contents of a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The content of the JSON file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        json_data = json.load(file)
    return json_data


# Example usage
data_from_json = read_json_file(JSON_FILE_PATH)
print(data_from_json)
