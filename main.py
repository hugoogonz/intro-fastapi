from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"

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
