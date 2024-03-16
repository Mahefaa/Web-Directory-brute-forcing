import itertools
import multiprocessing
import uuid
from concurrent.futures import ProcessPoolExecutor

from core.api import does_path_exist_on_api
from core.file import read_to_list_line_by_line
from core.list import split


def find_existing_path_from(api_base_url, word_list, verbose) -> list:
    """
    :param word_list: list of words to test
    :return: a portion of the list where the path was found on the server
    """
    res = [path for word in word_list if
           (path := word.rstrip()) and does_path_exist_on_api(baseUrl=api_base_url, path=path)]
    if verbose: print(f"thread {str(uuid.uuid4())} res = {res}")
    return res


def dir_trav_vuln(api_base_url, word_list_path, verbose=False) -> list:
    """
    :param word_list_path: given a word_list_path, it will read the file and split the content into multiple sublists of a certain size then submit read_word_list_and_get_with_api for each sublist to a thread
    :return: the list of (possible) vulnerable paths
    """
    words = read_to_list_line_by_line(word_list_path)
    '''Returns the number of CPUs in the system'''
    number_of_workers = multiprocessing.cpu_count()
    '''creates a PoolExecutor with number_of_workers threads'''
    with ProcessPoolExecutor(number_of_workers) as executor:
        futures = [executor.submit(find_existing_path_from, api_base_url, sublist, verbose) for sublist in
                   split(words, number_of_workers)]
        return list(itertools.chain.from_iterable([future.result() for future in futures]))
