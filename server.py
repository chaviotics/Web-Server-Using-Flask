from flask import Flask, render_template, url_for
app = Flask(__name__)
# print(__name__)

# @app.route('/<username>/<int:post_id>') # using URL parameters; Variables Rules in Flask
# def hello_world(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)
#     # Nawala ang color diri though :/

# @app.route('/') # a decorator
# def hello_world():
#     return render_template('index.html') # finds a folder named "templates" and gets the html file

@app.route('/') 
def my_home():
    return render_template('index.html')

# find a way for same .html file but different routes.

@app.route('/works.html') 
def works():
    return render_template('works.html')

@app.route('/about.html') 
def about_me():
    return render_template('about.html')

@app.route('/contact.html') 
def contact():
    return render_template('contact.html')

@app.route('/components.html') 
def components():
    return render_template('components.html')


