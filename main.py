from fastapi import FastAPI

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
	}
]

@app.get('/', tags=['home'])
async def root():
    return 'Hi from FastAPI'


@app.get('/movies', tags=['movies'])
async def get_movies():
    return movies