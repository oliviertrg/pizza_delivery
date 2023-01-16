from fastapi import FastAPI ,Response, status ,HTTPException,APIRouter,Depends
from app.schema import Order,update_order
from app.config import curso
from app import auth2
# import numpy as np

router = APIRouter (
    prefix = "/orders" ,
    tags = ["orders"]
)

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=Order)
def create_order(new_order : Order,current_user : int = Depends(auth2.get_current_user)):
 db = curso()
 c = db.cursor()
 sql = '''insert into orders(user_id,pizza_size,flavour,quantity) 
 values(%s,%s,%s,%s) ;'''
 x = (int(current_user.id),new_order.pizza_size,new_order.flavour,new_order.quantity)
 c.execute(sql,x)
 db.commit()
 return new_order

@router.get('/views')
def view_orders(current_user : int = Depends(auth2.get_current_user)):
    db = curso()
    c = db.cursor()
    sql = f'''select order_id,usersname,order_status,flavour,pizza_size,quantity,orders.create_at  
              from "orders" left join "users" on orders.user_id = users.user_id 
              where orders.user_id = {int(current_user.id)} ;'''
    c.execute(sql)
    view  = c.fetchall()
    model_view = list()
    for i in view :
     model_view.append({"order_id" : i[0],"user_name":i[1],"order_status":i[2],"flavour":i[3],"pizza_size":i[4],"quantity":i[5],"create_at":i[6]})
    return model_view

@router.put('/update/{order_id}',response_model=update_order)
def update_order(order_id : int,new_order : update_order,current_user : int = Depends(auth2.get_current_user)) :
    db = curso()
    c = db.cursor()
    sql = f'''select * from "orders" where "order_id" = {order_id} ; '''
    c.execute(sql)
    x = c.fetchall()
    if len(x) == 0 :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"order with id: {order_id} does not exist")
    if x[0][1] != int(current_user.id) :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    else:
        sql1 = f'''UPDATE "orders" SET 
                  pizza_size = (%s) ,
                  flavour = (%s) ,
                  quantity = (%s)
                  WHERE order_id = {order_id};'''
        x = (new_order.pizza_size,new_order.flavour,new_order.quantity)
        c.execute(sql1,x)
        db.commit()
    return new_order

@router.delete('/delete/{order_id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id : int,current_user : int = Depends(auth2.get_current_user)):
    db = curso()
    c = db.cursor()
    sql = f'''select * from "orders" where "order_id" = {order_id} ; '''
    c.execute(sql)
    x = c.fetchall()
    if len(x) == 0 :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"order with id: {order_id} does not exist")
    if x[0][1] != int(current_user.id) :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    else:
        sql1 = f'''delete from "orders" where "order_id" = {order_id} ;'''
        c.execute(sql1)
        db.commit()
    print("newupdate")
        
    return Response(status_code=status.HTTP_204_NO_CONTENT)