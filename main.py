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
		"category": "Acción"
	},
    {
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2016",
		"rating": 8.8,
		"category": "Acción"
	}
]

@app.get('/', tags=['home'])
async def root():
    return HTMLResponse('<h1>Hi from FastAPI!</>')


@app.get('/movies', tags=['movies'])
async def get_movies():
    return movies


@app.get('/movies/{id}', tags=['movies'])
async def get_movie_by_id(id: int):
    for item in movies:
         if item['id'] == id:
              return item
         
    return {"message": "Movie not found"}


	


# def search_movie(id):
#     movie = list(filter(lambda item: item['id'] == id, movies))

# 	try:
# 		return movie[0]
# 	except:
# 		return {"message": "Movie not found"}

