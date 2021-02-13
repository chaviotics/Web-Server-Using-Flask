from flask import Flask, render_template, url_for
app = Flask(__name__)
# print(__name__)

@app.route('/<username>/<int:post_id>') # using URL parameters; Variables Rules in Flask
def hello_world(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)
    # Nawala ang color diri though :/

# @app.route('/') # a decorator
# def hello_world():
#     return render_template('index.html') # finds a folder named "templates" and gets the html file

@app.route('/about.html') 
def about():
    return render_template('about.html')

@app.route('/blog') 
def blog():
    return 'This is a blog.'

@app.route('/blog/2020/dogs') 
def blog_dogs():
    return 'This is a blog OF A DOG LAST 2020.'