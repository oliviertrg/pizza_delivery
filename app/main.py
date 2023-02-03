from fastapi import FastAPI , status ,HTTPException,APIRouter
from .routers import users,auth,orders
from fastapi.middleware.cors import  CORSMiddleware
from starlette.requests import Request
import requests

app = FastAPI()

origins = ["http://127.0.0.1:8001/"]

app.add_middleware(
    CORSMiddleware ,
    allow_origins = origins ,
    allow_credentials = True ,
    allow_methods = ["*"] ,
    allow_headers = ["*"]
)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(orders.router)
# app.include_router(consumer.router)


@app.get("/")
def test ():
    return {"testing":"another changing"}

@app.get('/test')
async def creates (request : Request):
    body = await request.json()
    req = requests.get("http://127.0.0.1:8000/product/%s" % body["id"])
    return req.json()

@app.get('/testd')
async def create (request : Request):
    body = await request.json()
    print(body)
    req = requests\
        .post("http://127.0.0.1:8000/product/post/",json=body )
    return req.json()