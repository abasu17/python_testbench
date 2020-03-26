import sys
sys.path.append("..")

from plugins import *

def analyze_functions(path):

    # initilize defination list
    defination_list = list()
    meta_list = list()

    # read the function file
    lines = open(path, "r")

    # append all the defination lines
    for line in lines:
        if "def" in line:
            defination_list.append(line)

    for each_def in defination_list:
        idx_1 = each_def.index('f') # index of f
        idx_2 = each_def.index('(') # index of (
        idx_3 = each_def.index(')') # index of )
        idx_4 = each_def.index('>') # index of >
        function_dict = dict()
        function_dict["function_name"] = each_def[idx_1 + 1:idx_2].strip()
        function_dict["return_type"] = each_def[idx_4 + 1: -2].strip()
        arguments = list()
        for each_arg in each_def[idx_2 + 1:idx_3].split(","):
            arguments.append(tuple(each_arg.strip().split(":")))
        function_dict["arguments"] = dict(arguments)

        meta_list.append(function_dict)

    return meta_list

print(analyze_functions("/home/aniket/PycharmProjects/python_testbench/workspace/KV2IGI4WWB3ZAE26ZHTZBZ3WLLHVZL73/src/test_file_1.py"))