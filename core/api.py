import requests


def does_path_exist_on_api(baseUrl, path, params=None):
    """
    :param baseUrl: apiUrl to test for a path
    :param path: the path you'd like to know whether it exists or not
    :param params:  params for the api request
    :return: True if the path exists, False otherwise
    """
    response = requests.get(format_to_url(baseUrl, path), verify=False, params=params)
    return response.status_code != 404


def format_to_url(baseUrl, path):
    return f"{baseUrl}/{path}"
