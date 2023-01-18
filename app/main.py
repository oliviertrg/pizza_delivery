from fastapi import FastAPI , status ,HTTPException,APIRouter
from .routers import users,auth,orders
from fastapi.middleware.cors import  CORSMiddleware


app = FastAPI()

origins = ["http://127.0.0.1:8000/"]

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

@app.get("/")
def test ():
    return {"testing":"another changing"}