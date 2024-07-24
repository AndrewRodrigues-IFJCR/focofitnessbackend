import asyncio

import uvicorn
from fastapi import FastAPI

from .routes import auth

app = FastAPI()

app.include_router(auth, prefix='/auth')


@app.get('/ping')
async def _():
    await asyncio.sleep(10)
    return {'message': 'pong'}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')
