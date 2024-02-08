from fastapi import FastAPI

app = FastAPI()

app.title = "APIs documentacion con fastAPI"
app.version = "1.0.0"

movies = [
    {
    "id":1,
    "title":"Avengers 1",
    "overview": "Primer encuentro de los vengadores",
    "year": 2020,
    "rating": 7.8,
    "category": "Accion"
    },
    {
    "id":2,
    "title":"Avengers 2",
    "overview": "vengadores la era de ultron",
    "year": 2015,
    "rating": 9.8,
    "category": "Accion"
    }
]

"""
@app.get('/')
def message():
    return 'hola mundo web con python y fastAPI'
"""


@app.get('/', tags=['home'])
def message():
    return 'hola mundo web con python y fastAPI'



@app.post('/apis', tags=['client'])
def message():
    return {"mensaje":"hola mundo web con python y fastAPI post", "CODE":"0", "status": "true"}


@app.get('/movies', tags=['movies'])
def getmovies():
    return movies


@app.get('/movies/{id}', tags=['movies'])
def getmovies(id:int):
    for item in movies:
        if item["id"] == id:
            return item

