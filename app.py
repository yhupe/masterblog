from flask import Flask, render_template
import json
import os


app = Flask(__name__)


@app.route('/')
def index():
    file_path = os.path.join(os.path.dirname(__file__), 'Storage', 'blogposts.json')

    with open(file_path, 'r') as fileobj:
        blogposts = json.load(fileobj)

    return render_template('index.html', posts=blogposts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)