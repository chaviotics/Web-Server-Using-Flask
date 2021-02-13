from flask import Flask, render_template, url_for
app = Flask(__name__)
print(__name__)

@app.route('/') # a decorator
def hello_world():
    # print(url_for('static', filename='Cat icon.ico'))
    return render_template('index.html') # finds a folder named "templates" and gets the html file

@app.route('/about.html') 
def about():
    return render_template('about.html')

@app.route('/blog') 
def blog():
    return 'This is a blog.'

@app.route('/blog/2020/dogs') 
def blog_dogs():
    return 'This is a blog OF A DOG LAST 2020.'