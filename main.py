from fastapi import FastAPI


app=FastAPI()

@app.get("/")
def index():
    print('hola')
    return "hola"

app.run() 