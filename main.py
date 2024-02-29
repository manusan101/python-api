from __future__ import annotations

from fastapi import FastAPI
import mysql.connector

# uvicorn main:app --reload

app = FastAPI()

cnx = mysql.connector.connect(user='root', database='family', host='localhost', password='1234')
cursor = cnx.cursor()

query = ("SELECT * FROM casa;")


@app.get('/hola')
def root():
    cursor.execute(query)
    for (id) in cursor:
        print("{} de la tabla CASA".format(id))

    cursor.close()
    cnx.close()
    return {'message': 'hello world'}