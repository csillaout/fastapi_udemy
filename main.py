from typing import Optional
from fastapi import FastAPI #import the class
from enum import Enum

app = FastAPI() #create an object/instance from the fastAPI

#predefine paramaters:
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/hello') #endpoint, this provides our path
def index():  #function
    return {'message':"Hello World!"}

#@app.get('/blog/all')
#def get_all_blogs():
#    return {'message':'All blogs provided'}
@app.get('/blog/all')
def get_blogs(page=1, page_size: Optional[int] = None):
    return {'message': f"All {page_size} blogs on page {page}"}

@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message': f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}"}

@app.get('/blog/type/{type}')
def blog_type(type: BlogType):
    return {'message': f"Blog type: {type}"}

@app.get('/blog/{id}')
def get_blog(id: int):
    return {'message':f"blog with id {id}!"}

