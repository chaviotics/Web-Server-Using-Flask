from flask import Flask
app = Flask(__name__)
print(__name__)

@app.route('/') # a decorator
def hello_world():
    return 'Hello, CHAVIIIU hihihihi!'