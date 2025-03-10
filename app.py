from flask import Flask, render_template, request, redirect, url_for
import json
import os


app = Flask(__name__)


@app.route('/')
def index():
    file_path = os.path.join(os.path.dirname(__file__), 'Storage', 'blogposts.json')

    with open(file_path, 'r') as fileobj:
        blogposts = json.load(fileobj)

    return render_template('index.html', posts=blogposts)


@app.route('/add', methods=['GET', 'POST'])
def add():

    title = request.form.get('title')
    author = request.form.get('author')
    content = request.form.get('content')

    if request.method == 'POST':
        print(f"new post '{title}' added by {author}")

        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)