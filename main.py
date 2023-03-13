from fastapi import FastAPI

app = FastAPI()

app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1" 

@app.get('/', tags=['home'])
async def root():
    return 'Hi from FastAPI'