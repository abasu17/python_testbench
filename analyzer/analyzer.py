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


def function_builder(data_list, path):

    string_build = str("import sys\nsys.path.append('../')\n\n" + "import pytest\nfrom src." + path.split("/")[-1].replace(".py", "") + " import *\n\n\n")

    for each in data_list:
        string_build += (
            '# testcase for ' + each['function_name'] + "\n"
            'def test_' + each['function_name'] + "():\n\n\t" +
            '# replace with value\n\t' +
            '\n\t'.join([arg[0] + ' = ' + arg[1]+"()" for arg in each['arguments'].items()]) + "\n\n\t" +
            '# assert happy path' + "\n\t" +
            "assert " + each['function_name'] + "("+ ', '.join(each['arguments'].keys()) +") == " + each['return_type'] + "()\n\t" +
            "assert type(" + each['function_name'] + "(" + ', '.join(each['arguments'].keys()) + ")) == " + each['return_type'] + "\n\n\t" +
            '# assert raise (Change exception as per requirement)' + "\n\t" +
            'with pytest.raises(Error):\n\t\t' +
            each['function_name'] + "(" + ', '.join('None'.split("  ") * len(each['arguments'].keys())) + ")\n\n\n"
          )

    return string_build


def process_analyze(path):
    analyze_data = analyze_functions(path)
    return function_builder(analyze_data, path)
