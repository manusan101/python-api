from __future__ import annotations

from fastapi import FastAPI,Request
import mysql.connector

# uvicorn main:app --reload

app = FastAPI()

cnx = mysql.connector.connect(user='root', database='family', host='localhost', password='1234')
cursor = cnx.cursor()

query = ("SELECT * FROM casa;")
create_query= ("INSERT INTO casa (id,name,weight) VALUES ({},'{}',{});")
update_query= ("UPDATE casa SET name='{}', weight={} WHERE id={};")
delete= ("DELETE FROM casa WHERE id={};")

@app.get('/get-users')
def root():
    cursor.execute(query)
    for (id) in cursor:
        print("{} de la tabla CASA".format(id))

    return {'message': 'geted'}

@app.post('/create-user')
def root(request:Request):
    id= request.query_params['id']
    name = request.query_params['name']
    weight = request.query_params['weight']
    create_query2= create_query.format(id,name, weight)
    cursor.execute(create_query2)
    cnx.commit()
    return {'message': 'created'}

@app.put('/update-user')
def root(request:Request):
    id= request.query_params['id']
    name = request.query_params['name']
    weight = request.query_params['weight']
    update_query2= update_query.format(name,weight,id)
    cursor.execute(update_query2)
    cnx.commit()
    return {'message': 'updated'}

@app.delete('/delete-user')
def root(request:Request):
    id= request.query_params['id']    
    delete_query2=delete.format(id)
    cursor.execute(delete_query2)
    return {'message': 'deleted'}