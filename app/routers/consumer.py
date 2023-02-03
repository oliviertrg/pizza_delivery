from kafka import KafkaConsumer
from fastapi import FastAPI
from fastapi import FastAPI ,Response, status ,HTTPException,APIRouter,Depends
import json
from fastapi import FastAPI ,Response, status ,HTTPException,APIRouter,Depends
from app.schema import Order,update_order,update_order_status
from app.config import curso
from app import auth2
# import numpy as np
import typing

router = APIRouter ()
ORDER_KAFKA_TOPIC = "order_details"

ORDER_CONFIRMED_KAFKA_TOPIC = "order_confirmed"


consumer = KafkaConsumer(ORDER_KAFKA_TOPIC,bootstrap_servers=['localhost:9093'],api_version=(0,11,5))

# data = list()

# print(consumer)
# print(consumer["value"])




a = list()
print("sending----")
for i in consumer:
    t = i.value
    a.append(t)
    # print(type(i.value))
    print({"data":i.value})
    print(a)
@router.get("/consumer")
def test():

    return {"data":t}