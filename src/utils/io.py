import json

def read_json(file_path: str):
    """read a json file

    :param file_path: the path of the file
    :return: return data in string format
    """
    with open(file_path) as f:
        return json.load(f)


    