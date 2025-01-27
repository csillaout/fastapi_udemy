from typing import Optional, List, Dict
from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class Image(BaseModel):
    url: str
    alias: str

class BlogModul(BaseModel):
    title: str
    content: str
    date: int
    published: Optional[bool]
    tags: List[str]=[] 
    metadata: Dict[str, str]={'key':'val1'}
    image: Optional[Image] = None


@router.post('/new/{id}')
def create_blog(blog: BlogModul, id: int, version: int=1):
    return {
        "id": id,
        "data": blog,
        "version": version
        }

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog:BlogModul, id: int, 
comment_title: int=Query(None,  #query parameters
title="Title of the comment", 
description='Some description for comment_title', alias='commentTitle',
deprecated=True
), 
content: str = Body(...,  #body parameters
min_length=10, #validator
max_length=50, #validator
regex='^[a-z\s]*$' #validator
) ,
v: Optional[List[str]] = Query(['1.0', '1.1', '1.2']),
comment_id: int = Path(..., gt=5, le=10) 
): 
    return {
        'blog': blog,
        'id': id,
        'comment_title': comment_title, 
        'content': content,
        'v':v,
        'comment_id':comment_id
    }