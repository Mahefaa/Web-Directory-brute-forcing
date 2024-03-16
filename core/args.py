from core.file import exists


def is_valid_api_base_url(url):
    """
    :param url: a api_url to check whether it satisfies our conditions or not
    :return: True if the api_url is convenient, false otherwise
    """
    return not url.endswith("/")


def does_file_path_exists(path):
    """
    :param path: supposedly existing file_path to check
    :note: this function is set here to apply abstraction because we might also want to check whether a file exists on a cloud storage instead of os only
    :return: True if path exists, False otherwise
    """
    return exists(path)
