from flask import Flask

puzzle = Flask(__name__)

@puzzle.route('/')
def hello_world():
    return 'Hello world'