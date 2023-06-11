from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, auth,vote
from pydantic import BaseSettings
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

print(settings.database_username)

# models.Base.metadata.create_all(bind = engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return{"message": "Hello Bloggers , Welcome to my API"}



















































