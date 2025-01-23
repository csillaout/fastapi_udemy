# FastAPI Udemy

practicing fastAPI

Get method:

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
