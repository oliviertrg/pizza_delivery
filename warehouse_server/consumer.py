from kafka import KafkaConsumer
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
  print("sending ","="*200,">>>>>>>>>>>>>>>>>>>>>>")
  try: 
    db = curso()
    print(db)
    c = db.cursor()
    for i in consumer:
      print(i)
      b = json.loads(i[6].decode())
      a = json.loads(b)
      l = list(i for i in a )
      f = float(a["flour"])*int(a["quantity"])
      t = float(a["tomato sauce"])*int(a["quantity"])
      m = float(a["mozzarella"])*int(a["quantity"])
      x = float(a[l[3]])*int(a["quantity"])
    
      
      sql = f""" UPDATE "pizza-warehouse" SET "quantity/(kg)" = "quantity/(kg)" - {m}
                where "ingredient" = 'mozzarella' ;
                UPDATE "pizza-warehouse" SET "quantity/(kg)" = "quantity/(kg)" - {f} 
                where "ingredient" = 'flour' ;
                UPDATE "pizza-warehouse" SET "quantity/(kg)" = "quantity/(kg)" - {t} 
                where "ingredient" = 'tomato_sauce' ;
                UPDATE "pizza-warehouse" SET "quantity/(kg)" = "quantity/(kg)" - {x}
                where "ingredient" = '{l[3]}' ; """
                
  
      c.execute(sql)
      db.commit()
  except Exception as e:
      print(f"Error {e}")  


if __name__ == "__main__":
     event_driver()
