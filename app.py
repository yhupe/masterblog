from flask import Flask, render_template, request
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
    if request.method == 'POST':
        # We will fill this in the next step
        pass
    return render_template('add.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)