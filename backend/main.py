from fastapi.middleware.cors import CORSMiddleware
from config import SERVER_HOST, SERVER_PORT
from fastapi import FastAPI

import uvicorn

from api.auth import router as auth
from api.user import router as user
from api.dog import router as dog
from api.feed import router as feed
from api.tester import router as tester


app = FastAPI(
    title = "СЕРВИС ГАВ!",
    description= 'Веб-приложение Tinder для собак',
)
app.include_router(auth)
app.include_router(user)
app.include_router(dog)
app.include_router(feed)
app.include_router(tester)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host= SERVER_HOST,
        port= SERVER_PORT,
        reload = True,
    )