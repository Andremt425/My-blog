from fastapi import FastAPI
from pydantic import BaseModel

BlogPosts: PostModel = []

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Blog Backend!"}

@app.get("/posts")
def get_posts():
    return BlogPosts

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    if 0 <= post_id < len(BlogPosts):
        return BlogPosts[post_id]
    return {"error": "Post not found"}, 404

@app.post("/posts")
def create_post(post: BaseModel):
    BlogPosts.append(post.dict())
    return {"message": "Post created successfully", "post": post}

app.put("/posts/{post_id}")
def update_post(post_id: int, post: BaseModel):
    if 0 <= post_id < len(BlogPosts):
        BlogPosts[post_id] = post.dict()
        return {"message": "Post updated successfully", "post": post}
    return {"error": "Post not found"}, 404