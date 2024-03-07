from __future__ import annotations

from fastapi import FastAPI,Request
import mysql.connector

# uvicorn main:app --reload

app = FastAPI()

cnx = mysql.connector.connect(user='root', database='family', host='localhost', password='1234')
cursor = cnx.cursor()

query = ("SELECT * FROM casa;")
create_query= ("insert into casa (id,name,weight) values ({},'{}',{});")

@app.get('/get-users')
def root():
    cursor.execute(query)
    for (id) in cursor:
        print("{} de la tabla CASA".format(id))

    return {'message': 'hello world'}

@app.post('/create-user')
def root(request:Request):
    id= request.query_params['id']
    name = request.query_params['name']
    weight = request.query_params['weight']
    create_query2= create_query.format(id,name, weight)
    cursor.execute(create_query2)
    cnx.commit()
    return {'message': 'created'}
