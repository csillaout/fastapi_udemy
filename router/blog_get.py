from router.blog_post import required_functionality
from fastapi import APIRouter, status, Response, Depends
from typing import Optional
from enum import Enum


#integrating router
router = APIRouter(
    prefix='/blog', #as we have the prefix, we can remove it from the operations
    tags=['blog']
)

#@app.get('/blog/all')
#def get_all_blogs():
#    return {'message':'All blogs provided'}

@router.get(
    '/all', 
    summary="Retrieve all blogs",
    description='This API call simulates fetching all blogs', 
    response_description= "The list of available blogs")
def get_blogs(page=1, page_size: Optional[int] = None, req_parameter: dict = Depends(required_functionality)):
    return {
        'message': f"All {page_size} blogs on page {page}", 
        "message": req_parameter['message']
        }

@router.get('/{id}/comments/{comment_id}', tags=['comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None, req_parameter: dict = Depends(required_functionality)):
    """
    Simulates retrieving a comment of a blog
    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query prameter
    - **username** optional query prameter
    """
    return {'message': f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}",
    'additional message': req_parameter['message']
    }

#predefine paramaters:
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get('/type/{type}')
def blog_type(type: BlogType):
    return {'message': f"Blog type: {type}"}

@router.get('/{id}',status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id>5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f"Blog {id} not found"}
    else:
        response.status_code=status.HTTP_200_OK
        return {'message':f"blog with id {id}!"}

