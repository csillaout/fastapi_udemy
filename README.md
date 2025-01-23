# FastAPI Udemy

practicing fastAPI

1. Get method:

- path parameters - value that we pass on the path and we can use it in our function like:

  @app.get('/blog/{id}')
  def index(id: int): - this is a type validation
  return {'message':f"Blog with id {id}"}

- predefined values: with Enum

  class BlogType(str, Enum):
  short = 'short'
  story = 'story'
  howto = 'howto'

  @app.get('/blog/type/{type}')
  def blog_type(type: BlogType):
  return {'message': f"Blog type: {type}"}

- query parameters: everything you write fater the / separated by ? and &
  (any function not part of the path are query parameters)
  it can be page_size, page
  @app.get('/blog/all')
  def get_blogs(page, page_size):
  return {'message': f"All {page_size} blogs on page {page}"}

---

2. Operation description overview

- Status code: indicates the outcome of an operation, front end heavily relies on it: there are a few ways of doing this(for this you need to import status)
  @app.get('/blog/{id}', status_code=404)
  def get_blog(id: int):
  if id>5:
  return {'error': f"Blog{id} not found"}
  else:
  return {'message':f"blog with id {id}!"}

  other way(we need to import Response):
  @app.get('/blog/{id}', status_code=status.HTTP_200_OK)
  def get_blog(id: int, response: Response):
  if id>5:
  response.status_code = status.HTTP_404_NOT_FOUND
  return {'error': f"Blog {id} not found"}
  else:
  response.status_code=status.HTTP_200_OK
  return {'message':f"blog with id {id}!"}

- Tags:
  - Categorize operations: @app.get('/blog/all', tags=['blog'])
  - Multiple categories
- Summary and description: info regarding operation
  - @app.get(
    '/blog/all',
    tags=['blog'],
    summary="Retrieve all blogs",
    description='This API call simulates fetching all blogs')
    -"""
    Simulates retrieving a comment of a blog
    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query prameter
    - **username** optional query prameter
      """
- Response description: info about the output

---

3. Routers: - structure your application/operations into files and components - allow us to share a prefix btw multiple opeartions(if we have different blogs, different users) - allows us to share tags between operations
   from fastapi import APIRouter
   router = APIRouter(prefix='/blog', tags=['blog'])

   ## @router.get('/')

   from routers import blog
   app = fastAPI()
   app.include.router(blog.router)

- Routers
- Refactoring the app into logical components
- Adding a second router
