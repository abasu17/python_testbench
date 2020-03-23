from flask import Flask
import sys
from plugins import *


sys.dont_write_bytecode = True


app = Flask(__name__)
app.config.from_pyfile('config.py')

from route import *
    
if __name__ == '__main__':
	app.jinja_env.filters['split_space'] = split_space
	app.jinja_env.filters['replace_tokens'] = replace_tokens
	app.jinja_env.filters['split_dot'] = split_dot

	app.run(host='0.0.0.0', debug=True, port=5000, use_reloader=True)
