class Storage:
    def __init__(self, title, id, author, content):

        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if not isinstance(id, int):
            raise ValueError("ID must be a whole number")
        if not isinstance(author, str):
            raise ValueError("Author name must be a string")
        if not isinstance(content, str) and len(content) <= 5:
            raise ValueError("Blog post must be a sring and min. of 5 characters")

        self.title = title
        self.id = id
        self.author = author
        self.content = content