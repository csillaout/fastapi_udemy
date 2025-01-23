from fastapi import FastAPI #import the classe

app = FastAPI() #create an object/instance from the fastAPI

@app.get('/') #endpoint, this provides our path
def index():  #function
    return "Hello World!"