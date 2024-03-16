from os import path


def read_to_list_line_by_line(file_path):
    """
    :param file_path: a path to read lines from
    :return: a list of each line without the endline character from the file
    """
    with (open(file_path, 'r')) as file:
        lines = file.readlines()
        print(f"reading {file_path} with {len(lines)} lines")
        return [line.rstrip() for line in lines]


def exists(file_path):
    """
    :param file_path:  supposedly existing file_path to check on the os
    :return: True if file exists on the os, False otherwise
    """
    return path.exists(file_path)
