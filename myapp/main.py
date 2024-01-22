from fastapi import FastAPI, Depends
from starlette import status
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from . import models, schemas
from .database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/hello/post", status_code=status.HTTP_201_CREATED, response_model=schemas.UserCreate)
def add_data(request: schemas.UserCreate, db: Session = Depends(get_db)):
    user = models.User(email=request.email, username=request.username, roll_no=request.roll_no, departement=request.departement)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get('/hello/datas/', status_code=status.HTTP_200_OK)
def get_all_data(db: Session = Depends(get_db)):
    all_users = db.query(models.User).all()
    return all_users

@app.post("/hello/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.UserProfileCreate)
def add_profile(request: schemas.UserProfileCreate, db: Session = Depends(get_db)):
    user_profile = models.UserProfile(**request.dict())
    db.add(user_profile)
    db.commit()
    db.refresh(user_profile)
    return user_profile

@app.get('/hello/profiles/', status_code=status.HTTP_200_OK)
def show_profiles(db: Session=Depends(get_db)):
    profiles = db.query(models.UserProfile).options(joinedload(models.UserProfile.user)).all()
    return profiles


