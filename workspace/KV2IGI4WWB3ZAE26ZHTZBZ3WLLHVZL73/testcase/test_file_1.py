import sys
sys.path.append('../')

import pytest, os
from src.test_file_1 import *

print(os.getcwd())
# testcase for addition
def test_addition():

	# replace with value
	n1 = int(5)
	n2 = int(6)

	# assert happy path
	assert addition(n1, n2) == int(111)
	assert type(addition(n1, n2)) == int

	# assert raise (Change exception as per requirement)
	with pytest.raises(TypeError):
		addition("None", "None")