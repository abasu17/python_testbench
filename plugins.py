import string
import random
import hashlib
import time
import os
import subprocess
from jinja2 import Environment

WORKSPACE_PATH = "./workspace/"


def uuid(size=32, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


def get_time():
    t = time.localtime()
    return str(t.tm_hour) + ":" + str(t.tm_min) + ":" + str(t.tm_sec) + "  " + str(t.tm_mday) + "-" + str(
        t.tm_mon) + "-" + str(t.tm_year)


def split_space(string):
    return string.strip().split()


def split_dot(string):
    return string.replace('.', '%!.').strip().split('%!')


def replace_tokens(string, data):
    if string is not None:
        string = Environment().from_string(string).render({'data': data})
    return string


def remove_workspace(workspace_path):
    env_remove = subprocess.Popen(['rm', '-rf', workspace_path], stdout=subprocess.PIPE)
    if env_remove.communicate()[0] != b'':
        return False
    else:
        return True


def create_workspace(workspace_name):
    workspace_path = os.path.abspath(WORKSPACE_PATH + workspace_name)
    if not os.path.exists(workspace_path):
        env_create = subprocess.Popen(['virtualenv', workspace_path + "/venv", '-p', 'python3'], stdout=subprocess.PIPE)

        if env_create.communicate()[0] != b'':
            env_create_project = subprocess.Popen(['mkdir', workspace_path + "/src", workspace_path + "/testcase"],
                                                  stdout=subprocess.PIPE)
            if env_create_project.communicate()[0] == b'':
                return workspace_path
        else:
            remove_workspace(workspace_path)
            return None


def get_dir(path):
    dict_dir = dict()
    for root, dirs, files in os.walk(path):
        for d in dirs:
            dict_dir[os.path.join(root, d)] = (d, None)
        for f in files:
            dict_dir[os.path.join(root, f)] = (f, os.path.join(root, f).split(path + "/")[-1])

    return dict_dir


def create_pkg(path, type="package"):

    file_content = "import sys\nsys.path.append('../')\n\n" + "from src." + path.split("/")[-1].replace(".py", "") + " import *"

    if type == "package":
        pkg_create = subprocess.Popen(['touch', path], stdout=subprocess.PIPE)
    else:
        pkg_create = subprocess.Popen(['touch', path], stdout=subprocess.PIPE)
        test_file = open(path, "a")
        test_file.write(file_content)
        test_file.close()


    if pkg_create.communicate()[0] == b'':
        return True

    return False


def create_folder(path):
    env_folder = subprocess.Popen(['mkdir', path], stdout=subprocess.PIPE)

    if env_folder.communicate()[0] == b'':
        return path

    return None


def delete_pkg(path):
    delete_package = subprocess.Popen(['rm', path], stdout=subprocess.PIPE)

    if delete_package.communicate()[0] == b'':
        return True

    return False

def read_file(path):
    file_open = open(path, "r")
    return file_open.read()


def write_file(path, data):
    try:
        file_open = open(path, "w")
        file_open.write(data)
        file_open.close

    except:
        return False

    return True