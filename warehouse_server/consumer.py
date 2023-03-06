from kafka import KafkaConsumer
from fastapi import FastAPI
from fastapi import FastAPI ,Response, status ,HTTPException,APIRouter,Depends
import json
from config import curso

ORDER_KAFKA_TOPIC = "order_details"

ORDER_CONFIRMED_KAFKA_TOPIC = "ingredient_confirmed"


consumer = KafkaConsumer(
                        ORDER_KAFKA_TOPIC,
                        bootstrap_servers=['host.docker.internal:9093'],
                        api_version=(0,11,5)
                        )

def event_driver():
#  db = curso()
#  c = db.cursor()
 print("sending",300*"-")
 print(consumer)
 a = list()
 for i in consumer:
    print("sending",300*"-")
    print(i)
    print("checking this type ======>>>> ",type(i))
    print(i[6])
    b = json.loads(i[6].decode())
    a = json.loads(b)
    # print(a["flavour"])
    # print(a["id"])
    # sql = f""" UPDATE products SET prices = {a["prices"] - x}   WHERE id = {a["id"]} ;  """
    # c.execute(sql)
    # db.commit()
    b = str(a["flour"])
    print(type(b)) 
   
if __name__ == "__main__":
     event_driver()
