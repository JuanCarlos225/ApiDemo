from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/personas")
def get.personas():
    return {"id":1, "nombre":"Dejah"}

