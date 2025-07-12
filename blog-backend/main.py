from fastapi import FastAPI, HTTPException
from models.Post import Post

BlogPosts = []

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Blog Backend!"}

@app.get("/posts", response_model=list[Post]) 
def get_posts():
    if not BlogPosts:
        return {"message": "No posts available"}
    BlogPosts.append(Post(title="Sample Post", content="This is a sample post", author="Author", created_at="2023-10-01T00:00:00Z", likes=0, comments=[]).dict())
    return BlogPosts

@app.get("/posts/{post_id}", response_model=Post)
def get_post(post_id: int):
    if 0 <= post_id < len(BlogPosts):
        return BlogPosts[post_id]
    else:
        raise HTTPException(status_code=404, detail="Post not found") 

@app.post("/posts")
def create_post(post: Post):
    BlogPosts.append(post.dict())
    return {"message": "Post created successfully", "post": post}

@app.put("/posts/{post_id}")
def update_post(post_id: int, post: Post):
    if 0 <= post_id < len(BlogPosts):
        BlogPosts[post_id] = post.dict()
        return {"message": "Post updated successfully", "post": post}
    else:
        raise HTTPException(status_code=404, detail="Post not found") 
    
@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    if 0 <= post_id < len(BlogPosts):
        deleted_post = BlogPosts.pop(post_id)
        return {"message": "Post deleted successfully", "post": deleted_post}
    else:
        raise HTTPException(status_code=404, detail="Post not found")
    
@app.put("/posts/{post_id}/like")
def like_post(post_id: int):
    if 0 <= post_id < len(BlogPosts):
        BlogPosts[post_id]['likes'] += 1
        return {"message": "Post liked successfully", "likes": BlogPosts[post_id]['likes']}
    else:
        raise HTTPException(status_code=404, detail="Post not found")