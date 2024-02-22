from fastapi import Depends, FastAPI, Body, HTTPException, Path, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security.http import HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from typing import Coroutine, Optional, List
from dominio.modelsApi import User, MovieClass, movies
from fastapi.security import HTTPBearer
from fastapi.encoders import jsonable_encoder

from config.database import Session, engine, Base
from dominio.entities.movie import Movie

app = FastAPI()
app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)


@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')


@app.get('/moviesAll', tags=['movies'], response_model=List[MovieClass], status_code=200)
def get_movies() -> List[MovieClass]:
    db = Session()
    result = db.query(Movie).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@app.get('/movies', tags=['movies'], response_model=List[MovieClass], status_code=200)
def get_movies() -> List[MovieClass]:
    db = Session()
    result = db.query(Movie).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@app.get('/movies/{id}', tags=['movies'], response_model=MovieClass)
def get_movie(id: int = Path(ge=1, le=2000)) -> MovieClass:
    db = Session()
    result = db.query(Movie).filter(Movie.id == id).first()
    db.close()
    if not result:
        return JSONResponse(status_code=404, content={'message':'No encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@app.get('/movies/', tags=['movies'], response_model=List[MovieClass])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[MovieClass]:
    db = Session()
    result = db.query(Movie).filter(Movie.category == category).all()
    db.close()
    if not result:
        return JSONResponse(status_code=404, content={'message':'No encontrado'})
    return JSONResponse(content=jsonable_encoder(result))



@app.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: MovieClass) -> dict:
    db = Session()
    newMovie = Movie(**movie.model_dump())
    db.add(newMovie)
    db.commit()
    db.close()

    #movies.append(movie)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la película"})



@app.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: MovieClass)-> dict:
    db = Session()
    result = db.query(Movie).filter(Movie.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se han encontrado la película"})
    
    result.title = movie.title
    result.overview = movie.overview
    result.year = movie.year
    result.rating = movie.rating
    result.category = movie.category
    db.commit()
    db.close()
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la película"})



@app.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id: int)-> dict:
    db = Session()
    result = db.query(Movie).filter(Movie.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se han encontrado la película"})
    
    db.delete(result)
    db.commit()
    db.close()
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película"})
        

