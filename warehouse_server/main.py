from fastapi import FastAPI , status ,HTTPException,APIRouter
from fastapi.middleware.cors import  CORSMiddleware
from starlette.requests import Request
from warehouse_server.schema import Order
import json
import requests
import kafka
from kafka import KafkaConsumer
# from kafka import KafkaConsumer
from warehouse_server.config import curso


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
                "Pizza Sauce" : float(0.12),
                "mozzarella" : float(0.1) ,
                "sausage":float(0.05)
            }
        if new_order.pizza_size == 'm' :
            i = {
                "flour" : float(0.3),
                "Pizza Sauce" : float(0.144),
                "mozzarella" : float(0.12) ,
                "sausage":float(0.06)
            }
        if new_order.pizza_size == 'l' :
            i = {
                "flour" : float(0.36),
                "Pizza Sauce" : float(0.180),
                "mozzarella" : float(0.144) ,
                "sausage":float(0.075)
            } 
    if  new_order.flavour == 'bacon':
        if new_order.pizza_size == 's':
            i = {
                "flour" : float(0.25),
                "Pizza Sauce" : float(0.12),
                "mozzarella" : float(0.1) ,
                "Bacon":float(0.05)
            }
        if new_order.pizza_size == 'm' :
            i = {
                "flour" : float(0.3),
                "Pizza Sauce" : float(0.144),
                "mozzarella" : float(0.12) ,
                "Bacon":float(0.06)
            }
        if new_order.pizza_size == 'l' :
            i = {
                "flour" : float(0.36),
                "Pizza Sauce" : float(0.180),
                "mozzarella" : float(0.144) ,
                "Bacon":float(0.075)
            }
    if  new_order.flavour == 'mushrooms':
        if new_order.pizza_size == 's':
            i = {
                "flour" : float(0.25),
                "Pizza Sauce" : float(0.12),
                "mozzarella" : float(0.1) ,
                "mushrooms":float(0.05)
            }
        if new_order.pizza_size == 'm' :
            i = {
                "flour" : float(0.3),
                "Pizza Sauce" : float(0.144),
                "mozzarella" : float(0.12) ,
                "mushrooms":float(0.06)
            }
        if new_order.pizza_size == 'l' :
            i = {
                "flour" : float(0.36),
                "Pizza Sauce" : float(0.180),
                "mozzarella" : float(0.144) ,
                "mushrooms":float(0.075)
            }
     
    return json.dumps(i)        

