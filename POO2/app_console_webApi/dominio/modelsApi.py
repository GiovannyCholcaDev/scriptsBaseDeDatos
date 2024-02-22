from typing import Optional
from pydantic import BaseModel, Field

class User(BaseModel):
    email:str = "admin@gmail.com"
    password:str = "admin"


class MovieClass(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2022)
    rating:float = Field(ge=1, le=10)
    category:str = Field(min_length=5, max_length=15)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "title": "Mi Pelicula",
                    "overview": "Mi Descripcion pelicula",
                    "year": 2022,
                    "rating": 9.8,
                    "category" : "Acción"                    
                }
            ]
        }
    }

movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	},
    {
		"id": 2,
		"title": "Avengers",
		"overview": "todos los vengadores por primera vez",
		"year": "2020",
		"rating": 10.0,
		"category": "Acción"
	},
    {
		"id": 3,
		"title": "Ironman",
		"overview": "Tony Stark crea su traje de super heroe",
		"year": "2010",
		"rating": 10.0,
		"category": "Ciencia Acción"
	}
]
