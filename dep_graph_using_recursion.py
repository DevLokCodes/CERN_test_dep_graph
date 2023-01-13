
import os
import json
import pathlib



def tree_builder(json_dir_list: list[str], json_list: list[str], depth: int) -> str:
    """
    input :
        json_dir_list : is a list containing the list of all the current values fof the key mentioned
        json_list : is a list of all the key and value pair from the given JSON file
        depth : is needed for calculate the indentation of the heirarchy

    output :
        prints out the directory hirerchy in the necessary readable format

    working :
        you transverse through all the element present in the JSON file and its key value elements. It then creates a formatted output while appending the elements as a stdio output. Lastly it recursively calls the tree builder function to calculate the sub directories and internal graph connections.

    """

    for elements in json_dir_list:
        print("-"* depth + '-' + elements)
        if elements in json_list.keys() and json_list.get(elements):        # checks for if the current key has values and is not None.
            tree_builder(json_list.get(elements), json_list, depth + 1)     # calls the tree builder function to recurvsively solve for sub categories and internal grapph connection


def dep_graph(filename: str) -> tree_builder:

    """

    input :  filename: is a string of the relative location of the json file which contains data with keys and values.

    returns : json_list elements from the values of the dictionary

    working : this function first checks if there is a file existing on the location received from the system argument. it then traverses through the keys and elements and passes the list data to the tree builder function.

    """
    cwd = os.getcwd()
    path = cwd + filename                               # concatinating the current working directory and the relative file path which was recieved from the system argument.
    with open(cwd + filename) as json_data:             # checks if the file exists so that it does not return an exception (eg: file not found)
      json_list = json.load(json_data)

    depth = 0
    for key_name in json_list:
        print("-" + key_name)
        if json_list.get(key_name):
            tree_builder(json_list.get(key_name), json_list, depth + 1)

