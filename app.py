from crypt import methods

from flask import Flask, render_template, request, redirect, url_for
import json
import os
import uuid


app = Flask(__name__)

file_path = os.path.join(os.path.dirname(__file__), 'Storage', 'blogposts.json')

@app.route('/')
def index():

    with open(file_path, 'r') as fileobj:
        blogposts = json.load(fileobj)

    return render_template('index.html', posts=blogposts)


@app.route('/add', methods=['GET', 'POST'])
def add():

    title = request.form.get('title')
    author = request.form.get('author')
    content = request.form.get('content')
    post_id = str(uuid.uuid4())

    if request.method == 'POST':

        with open(file_path, 'r') as fileobj:
            #list of dicts
            blogposts = json.load(fileobj)

        new_post = {}

        new_post['id'] = post_id
        new_post['title'] = title
        new_post['author'] = author
        new_post['content'] = content

        blogposts.append(new_post)


        with open(file_path, 'w') as fileobj:
            json.dump(blogposts, fileobj, indent=4)

        print(f"new post '{title}' successfully added by {author}")

        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<post_id>', methods=['GET', 'POST'])
def delete_post(post_id):

    if request.method == 'POST':

        with open(file_path, 'r') as fileobj:
            # list of dicts
            blogposts = json.load(fileobj)

            index_to_be_deleted = None

            for i, post in enumerate(blogposts):
                if post['id'] == post_id:
                    index_to_be_deleted = i

            blogposts.pop(index_to_be_deleted)

        with open(file_path, 'w') as fileobj:
            json.dump(blogposts, fileobj, indent=4)

        print(f"Post '{post_id}' successfully removed")
        return redirect(url_for('index'))

    return render_template('deleted_note.html')







if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)