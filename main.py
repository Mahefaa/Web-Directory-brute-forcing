import sys

from core.api import format_to_url
from core.args import is_valid_api_base_url, does_file_path_exists
from core.dir_trav import dir_trav_vuln
from pretty_print import pretty_print_list


def dir_trav_api_url(api_base_url, word_list_path, verbose):
    """
    :param api_base_url: api_url to test
    :param word_list_path: word_list_path to test
    :param verbose: log steps or not
    :return: list of paths formatted to api_paths because dir_trav_vuln does not append the baseUrl to the path yet
    """
    return map(lambda path: format_to_url(api_base_url, path), dir_trav_vuln(api_base_url, word_list_path, verbose))


if __name__ == '__main__':
    args = sys.argv
    if (length := len(args)) and 3 != len(args) != 4:
        print("optional parameters are put between parenthesis hence they are not counted for this error")
        raise RuntimeError("usage: main.py api_base_url word_list_path (verbose) ")
    api_base_url = args[1]
    if not is_valid_api_base_url(api_base_url):
        raise RuntimeError(f"api_base_url {api_base_url} must not end with '/'")
    word_list_path = args[2]
    if not does_file_path_exists(word_list_path):
        raise RuntimeError(f"path {word_list_path} does not exist")
    verbose = False
    if length == 4:
        verbose = bool(args[3])
    res = dir_trav_api_url(api_base_url, word_list_path, verbose)
    pretty_print_list(res)
