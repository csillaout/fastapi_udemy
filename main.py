from fastapi import FastAPI
from router import blog_get, blog_post
app = FastAPI() #create an object/instance from the fastAPI
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/hello') #endpoint, this provides our path
def index():  #function
    return {'message':"Hello World!"}
