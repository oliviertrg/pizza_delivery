import os
import psycopg2


def convert(val):
    if type(val) != str:
        return val

    if val.isnumeric():
        return int(val)
    elif val == 'True':
        return True
    elif val == 'False':
        return False
    else:
        return val

def get_authen():
        secret_key = convert(os.environ.get('SECRET_KEY'))
        password = convert(os.environ.get('postgres_db'))
        algo = convert(os.environ.get('ALGORITHM'))
        access_time = convert(os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES'))
        return {
            'SECRET_KEY' : secret_key,
            'password'   : password,
            'ALGORITHM' : algo ,
            'ACCESS_TOKEN_EXPIRE_MINUTES' : access_time
        }

def curso():
 try :
    a =  get_authen()
    conn = psycopg2.connect(
        host = 'localhost',
        database = "pizza_delivery",
        user = "postgres",
        password = a["password"]
    )

 except Exception as e :
    print("Connecting to database failed")
    print(f"Error {e}" )
 return conn


if __name__ == "__main__":
    curso()