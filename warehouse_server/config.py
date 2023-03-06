import os
import psycopg2

# 1. Import the config object from decouple.
from decouple import config

async def curso():
 try :
    conn = psycopg2.connect(
        host = "postgres-warehouse",
        database = "db-warehouse",
        user = config('POSTGRES_USER'),
        password = config('POSTGRES_PASSWORD')
    )
    print("conecting susseccefull")
   

 except Exception as e :
    print("Connecting to database failed")
    print(f"Error {e}" )
 return conn

if __name__ == "__main__":
          curso()