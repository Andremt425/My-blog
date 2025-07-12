from pydantic import BaseModel

class Comment(BaseModel):
    comment : str

class Post(BaseModel):
    title: str 
    content: str
    author: str
    created_at: str
    likes: int
    comments: Comment = []

