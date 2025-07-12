class post:
    def __init__(self, title, content, author, created_at, likes=0, comments=None):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = created_at
        self.likes = likes
        self.comments = comments if comments is not None else []

    def add_comment(self, comment):
        self.comments.append(comment)
    
    def add_like(self):
        self.likes += 1
    
    def update_content(self, new_content):
        self.content = new_content