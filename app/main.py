from fastapi import FastAPI , status ,HTTPException,APIRouter
from .routers import users,auth,orders
app = FastAPI()
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(orders.router)
@app.get("/")
def test ():
    return {"testing":"git testing"}