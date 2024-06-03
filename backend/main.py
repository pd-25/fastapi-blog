from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base

from apis.base import api_router

def include_router(app):
    app.include_router(api_router)

# this method is not standared, this is for knowldge purpose, we will use alembic to create table
# def create_tables():
#     Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(app)
    # create_tables()
    return app

app = start_application()

@app.get("/")
def hello():
    return {"msg": "Hello"}