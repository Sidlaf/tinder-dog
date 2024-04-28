from config import SERVER_HOST, SERVER_PORT
from fastapi import FastAPI
from fastapi.middleware import cors
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from api.email import router as emailer
from api.profile import router as profile

app = FastAPI(
    title = "СЕРВИС ГАВ!",
    description= 'Веб-приложение Tinder для собак',
)

app.include_router(emailer)
# app.include_router(profile)

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