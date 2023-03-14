from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

# me permite crear el esquema de datos
from pydantic import BaseModel, Optional

app = FastAPI()

app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"

class Movie(BaseModel):
     id: Optional[int] = None # campo opcional
     title: str
     overview: str
     year: int
     rating: float
     category: str

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


@app.get('/movies', tags=['movies'])
async def get_movies():
    return movies

# http://127.0.0.1:5000/movies/2
@app.get('/movies/{id}', tags=['movies'])
async def get_movie_by_id(id: int):
    for item in movies:
         if item['id'] == id:
              return item
         
    return {"message": "Movie not found"}


# http://127.0.0.1:5000/movies/?category=Romantico
@app.get('/movies/', tags=['movies'])
async def get_movie_by_category(category: str):
    return list(filter(lambda item: item['category'] == category, movies))
	

@app.post('/movies', tags=['movies'])
async def create_movie(movie: Movie):
    movies.append(movie)
    return movies

@app.put('/movies/{id}', tags=['movies'])
async def update_movie(id: int, movie: Movie):
	for item in movies:
		if item["id"] == id:
			item['title'] = movie.title
	 		item['overview'] = movie.overview
	 		item['year'] = movie.year
	 		item['rating'] = movie.rating
	 		item['category'] = movie.category
	 		return movies

            

# http://127.0.0.1:5000/movies/2
@app.delete('/movies/{id}', tags=['movies'])
async def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return movies