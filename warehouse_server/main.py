from fastapi import FastAPI , status ,HTTPException,APIRouter
from fastapi.middleware.cors import  CORSMiddleware
from starlette.requests import Request
from schema import Order
import json
import requests
import kafka
from kafka import KafkaConsumer
from consumer import event_driver
# from kafka import KafkaConsumer
from config import curso



app = FastAPI()
origins = ["http://0.0.0.0:8000/"]

app.add_middleware(
    CORSMiddleware ,
    allow_origins = origins ,
    allow_credentials = True ,
    allow_methods = ["*"] ,
    allow_headers = ["*"]
)

@app.get("/ingredient")
async def ingredient(new_order : Order):
    if new_order.flavour == 'pepperoni':
        if new_order.pizza_size == 's':
            i = {
                "flour" : float(0.25),
                "tomato sauce" : float(0.12),
                "mozzarella" : float(0.1) ,
                "pepperoni":float(0.05)
            }
        if new_order.pizza_size == 'm' :
            i = {
                "flour" : float(0.3),
                "tomato sauce" : float(0.144),
                "mozzarella" : float(0.12) ,
                "pepperoni":float(0.06)
            }
        if new_order.pizza_size == 'l' :
            i = {
                "flour" : float(0.36),
                "tomato sauce" : float(0.180),
                "mozzarella" : float(0.144) ,
                "pepperoni":float(0.075)
            } 
    if  new_order.flavour == 'bacon':
        if new_order.pizza_size == 's':
            i = {
                "flour" : float(0.25),
                "tomato sauce" : float(0.12),
                "mozzarella" : float(0.1) ,
                "bacon":float(0.05)
            }
        if new_order.pizza_size == 'm' :
            i = {
                "flour" : float(0.3),
                "tomato sauce" : float(0.144),
                "mozzarella" : float(0.12) ,
                "bacon":float(0.06)
            }
        if new_order.pizza_size == 'l' :
            i = {
                "flour" : float(0.36),
                "tomato sauce" : float(0.180),
                "mozzarella" : float(0.144) ,
                "bacon":float(0.075)
            }
    if  new_order.flavour == 'mushrooms':
        if new_order.pizza_size == 's':
            i = {
                "flour" : float(0.25),
                "tomato sauce" : float(0.12),
                "mozzarella" : float(0.1) ,
                "mushrooms":float(0.05)
            }
        if new_order.pizza_size == 'm' :
            i = {
                "flour" : float(0.3),
                "tomato sauce" : float(0.144),
                "mozzarella" : float(0.12) ,
                "mushrooms":float(0.06)
            }
        if new_order.pizza_size == 'l' :
            i = {
                "flour" : float(0.36),
                "tomato sauce" : float(0.180),
                "mozzarella" : float(0.144) ,
                "mushrooms":float(0.075)
            }
    i.update({"quantity" : int(new_order.quantity)}) 
    return json.dumps(i)

@app.get("/views")
def views():
    db = curso()
    c = db.cursor()
    sql = f"""SELECT * FROM "pizza-warehouse" ; """
    c.execute(sql)
    v = c.fetchall()       
    return {"data" : v}


