from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get('/api/home')
async def home():
    return {'message': 'Hola', 'state': 200, 'day': datetime.now()}
