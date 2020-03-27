import sys
sys.path.append('../')

import pytest
from src.test_file_1 import *


# testcase for addition
def test_addition():

	# replace with value
	n1 = int()
	n2 = int()

	# assert happy path
	assert addition(n1, n2) == int()
	assert type(addition(n1, n2)) == int

	# assert raise (Change exception as per requirement)
	with pytest.raises(TypeError):
		addition(None, None)


# testcase for sub
def test_sub():

	# replace with value
	n1 = int()
	n2 = int()

	# assert happy path
	assert sub(n1, n2) == int()
	assert type(sub(n1, n2)) == int

	# assert raise (Change exception as per requirement)
	with pytest.raises(TypeError):
		sub(None, None)


