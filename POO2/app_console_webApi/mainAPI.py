from fastapi import FastAPI, Body

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


@app.get('/', tags=['client'])
def message():
    return 'hola mundo web con python y fastAPI'



@app.post('/apis', tags=['client'])
def message():
    return {"mensaje":"hola mundo web con python y fastAPI post", "CODE":"0", "status": "true"}


@app.get('/movies', tags=['movies'])
def getmovies():
    return movies

#parametro de ruta, variable en la uri
@app.get('/movies/{id}', tags=['movies'])
def getmovies(id:int):
    for item in movies:
        if item["id"] == id:
            return item
    return []


#parametro query variable en la funcion
@app.get('/movies/', tags=['movies'])
def getMoviesByCaterory(category: str, year: int):
    return category


#parametro de ruta, variable en la uri
@app.get('/movies/query/', tags=['movies'])
def getmoviesCaterogyQuery(caterogy: str):
    for item in movies:
        if item["category"] == caterogy:
            return item
    return []


#
#METODOS POST

@app.post('/movies/', tags=['movies'])
def createMovie(id: int = Body(), title: str = Body(), overview:str = Body(), year:int = Body(), rating:float = Body(), category: str = Body()):
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return movies


@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, title: str = Body(), overview:str = Body(), year:int = Body(), rating: float = Body(), category: str = Body()):
	for item in movies:
		if item["id"] == id:
			item['title'] = title,
			item['overview'] = overview,
			item['year'] = year,
			item['rating'] = rating,
			item['category'] = category
			return movies


@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return movies