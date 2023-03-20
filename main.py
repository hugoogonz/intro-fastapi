from fastapi import FastAPI, Body, Path, Query
# JSONResponse me permite enviar contenido en formato JSON hacia el cliente
from fastapi.responses import HTMLResponse, JSONResponse

# me permite crear el esquema de datos
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()

app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"


class Movie(BaseModel):
    id: Optional[int] = None  # campo opcional
    title: str = Field(min_length=5, max_length=15)  # campo maximo de 15 digitos
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2025) # menor a 2025
    rating:float = Field(default=10, ge=1, le=10)
    category:str = Field(default='Categoria', min_length=5, max_length=15)
    
	# Clase donde añado una propiedad llamada schema_extra
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Avatar",
                "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
                "year": "2009",
       	 		"rating": 7.8,
        		"category": "Accion"
			}
		}


movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Accion"
    },
    {
        "id": 2,
        "title": "Lalaland",
        "overview": "Mia & Sebastian...",
        "year": "2016",
        "rating": 10,
        "category": "Romantico"
    }
]


@app.get('/', tags=['home'])
async def root():
    return HTMLResponse('<h1>Hi from FastAPI!</>')

# response_model=List[Movie] -> indicamos que devolvemos una Lista de tipo Movie
@app.get('/movies', tags=['movies'], response_model=List[Movie])
async def get_movies() -> List[Movie]: # la func retorna una Lista de tipo Movie
    return JSONResponse(content=movies)  # retorna un contenido de movies en formato JSON

# http://127.0.0.1:5000/movies/2
@app.get('/movies/{id}', tags=['movies'], response_model=Movie)
async def get_movie_by_id(id: int = Path(ge=1, le=2000)) -> Movie:
    for item in movies:
        if item['id'] == id:
            return JSONResponse(content=item)

    return JSONResponse(content={"message": "Movie not found"})


# http://127.0.0.1:5000/movies/?category=Romantico
@app.get('/movies/', tags=['movies'], response_model=List[Movie])
async def get_movie_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:
    data = list(filter(lambda item: item['category'] == category, movies))
    return JSONResponse(content=data)


@app.post('/movies', tags=['movies'], response_model=dict)
async def create_movie(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(content={"message": "The movie was saved successfully."})

# response_model=dict -> la respuesta sera un diccionario
@app.put('/movies/{id}', tags=['movies'], response_model=dict)
async def update_movie(id: int, movie: Movie) -> dict: # la funcion devolvera un diccionario 
    for item in movies:
        if item["id"] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            return JSONResponse(content={"message": "The movie has been modified."})


# http://127.0.0.1:5000/movies/2
@app.delete('/movies/{id}', tags=['movies'], response_model=dict)
async def delete_movie(id: int) -> dict:
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return JSONResponse(content={"message": "The movie has been removed."})
