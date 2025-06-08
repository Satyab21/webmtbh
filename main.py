# from unittest import result
# from multiprocessing import context
# from os import access
import json
# from urllib import request
from fastapi import FastAPI, Request, Form
# from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import  Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, status # Assuming you have the FastAPI class for routing
# from fastapi.responses import RedirectResponse, HTMLResponse
# from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi_login import LoginManager #Loginmanager Class
from fastapi_login.exceptions import InvalidCredentialsException #Exception class
# from api.helpers import helpers
import jinja_partials
# from pydantic import BaseModel
# from deta import Deta
from flask import jsonify


# Deta-Base
# deta_projectkey = 'b0ejt296_yuyQMifB8Z1P8LUg5sKauNMerCTv1h9j'
# deta = Deta(deta_projectkey)
# db_cred = deta.Base('db_login_cred')





# # Approach 1: Auth 
# SECRET = "secret_key"
# manager = LoginManager(SECRET, token_url="/login", use_cookie=True)
# manager.cookie_name = "best_cookie"
# DB = {"username" : {"password":"mtbh"}}
# @manager.user_loader()
# def load_user(username:str):
#     user = DB.get(username)
#     return user


app = FastAPI()
templates = Jinja2Templates(directory="api/templates/")
jinja_partials.register_starlette_extensions(templates)
app.mount("/api/static", StaticFiles(directory="api/static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# @app.get("/items/")
# async def read_items(token: str = Depends(oauth2_scheme)): 
#     return {"token": token}
# class User(BaseModel):
#     username: str
#     email: str | None = None
#     full_name: str | None = None
#     disabled: bool | None = None

# def fake_decode_token(token):
#     return User(
#         username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
#     )
# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     user = fake_decode_token(token)
#     return user
# @app.get("/users/me")
# async def read_users_me(current_user: User = Depends(get_current_user)):
#     return current_user
# @app.post("/login")
# def login(data:OAuth2PasswordRequestForm = Depends()):
#     username = data.username
#     password = data.password
#     user = load_user(username)
#     if not user:
#         raise InvalidCredentialsException
#     elif password != user["password"]:
#         raise InvalidCredentialsException
#     access_token = manager.create_access_token(data={"sub" : username}) 
#     resp = RedirectResponse(url="/portal", status_code=status.HTTP_302_FOUND)
#     manager.set_cookie(resp,access_token)
#     return resp
# @app.get("/portal")
# def get_PrivatePortal_endpoint(_=Depends(manager)):
#     # return "You are an authenticated user"
#     return templates.TemplateResponse('portal.html', context={'request': request})




### HomePage ###
@app.get('/')
async def get_homepage(request: Request):
    return templates.TemplateResponse('homepage.html', context={'request': request})
@app.get('/api/templates/homepage.html')
async def get_homepage(request: Request):
    return templates.TemplateResponse('homepage.html', context={'request': request})


### Knowledge ###
@app.get('/knowledge')
def get_knowledge(request: Request):
    return templates.TemplateResponse('knowledge.html', context={'request': request})

### Projects ###
@app.get('/projects')
def get_projects(request: Request):
    return templates.TemplateResponse('projects.html', context={'request': request})

### Journey ###
@app.get('/journey')
def get_journey(request: Request):
    return templates.TemplateResponse('journey.html', context={'request': request})

### Interests ###
@app.get('/interests')
def get_interests(request: Request):
    return templates.TemplateResponse('interests.html', context={'request': request})

### User-Login ###
@app.get('/login')
def get_login(request: Request):
    return templates.TemplateResponse('login.html', context={'request': request})

#Submit Login Form
# @app.post('/login')
# def create_user(request: Request):
#     username = request.json.get("username")
#     password = request.json.get("password")

#     user_cred = {
#         "username" : username, 
#         "password" : password
#         }

#     user = db_cred.put(user_cred)

#     return jsonify(user, 201)
    




###################
### OTHER PAGES ###
###################
# Apple (index1) #
@app.get('/index1')
async def read_index(request: Request):
    return templates.TemplateResponse('index1.html', context={'request': request})
#-- FORM --#
# Form
@app.get('/form')
async def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})
# Form
@app.post('/form')
async def form_post(request: Request, num: int = Form(...)):
    result = num*num
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


# ###-RUN-###
if __name__ == "__main__":
    import uvicorn
    print("main.py")
    # while True:
    uvicorn.run("main:app", reload=True, port=5000)
#  C:\Users\satya\AppData\Local\Programs\Python\Python312\python.exe E:\Azrael2_SilverHDD\webmtbh\main.py
