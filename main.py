from typing import Union

from fastapi import Request, FastAPI, Depends, HTTPException
from pydantic import BaseModel

from sqlalchemy.orm import Session
# from testapp import crud, models, schemas
# from .database import SessionLocal, engine

app = FastAPI()

# #db stuff
# models.Base.metadata.create_all(bind=engine)

# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.get("/authors/", response_model=list[schemas.Author])
# def read_users(skip:int=0, limit:int=100, db:Session = Depends(get_db)):
#     authors = crud.get_authors(db, skip=skip, limit=limit)
#     return authors

# @app.get("/author/{id}", response_model=schemas.Author)
# def read_author(id:int, db:Session = Depends(get_db)):
#     author = crud.get_author(db, user_id=id)
#     if author is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return author

    






class HealthCheck(BaseModel):
    status: str = "OK"


class Explanation(BaseModel):
    manuscript_id: str
    reviewer_id: str
    explanation: str = "Here's why..."

# class Request(BaseModel):
#     manuscript_id: str
#     reviewer_id: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def check_health() -> HealthCheck:
    return HealthCheck(status="OK")

#given a manuscript_id (string) and an id (string), ultimately, return a string that is the explanation
#this will be a post method - needs a POST? as this will 'create' an explanation resource? Do we want to save these? I'd say yes.

@app.post("/explanation/", response_model=Explanation)
async def get_explanation(request:Request) -> Explanation:
    # return {"manuscript_id":manuscript_id, "reviewer_id":reviewer_id}
    return await request.json()
#looking at the terminal which runs the server for errors -> the return value is json that is mapped to an Explanation (reponse model)
