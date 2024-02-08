from fastapi import FastAPI

app = FastAPI()

app.title = "APIs documentacion con fastAPI"
app.version = "1.0.0"

"""
@app.get('/')
def message():
    return 'hola mundo web con python y fastAPI'
"""


@app.get('/', tags=['home'])
def message():
    return 'hola mundo web con python y fastAPI'
