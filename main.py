from fastapi import FastAPI, Body
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

# http://localhost:5000/movies/2
@app.get('/movies/{id}', tags=['movies'])
async def get_movie_by_id(id: int):
    for item in movies:
         if item['id'] == id:
              return item
         
    return {"message": "Movie not found"}


# http://localhost:5000/movies/?category=Romantico
@app.get('/movies/', tags=['movies'])
async def get_movie_by_category(category: str):
    return list(filter(lambda item: item['category'] == category, movies))
	

@app.post('/movies', tags=['movies'])
async def create_movie(id: int = Body(), title: str = Body(), overview:str = Body(), year:int = Body(), rating: float = Body(), category: str = Body()):
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
async def update_movie(id: int, title: str = Body(), overview:str = Body(), year:int = Body(), rating: float = Body(), category: str = Body()):
	for item in movies:
		if item["id"] == id:
			item['title'] = title,
			item['overview'] = overview,
			item['year'] = year,
			item['rating'] = rating,
			item['category'] = category
			return movies

# http://localhost:5000/movies/2
@app.delete('/movies/{id}', tags=['movies'])
async def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return movies