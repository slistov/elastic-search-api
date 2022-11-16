from fastapi import FastAPI

from .routers import quotes_router

app = FastAPI()

app.include_router(quotes_router)
