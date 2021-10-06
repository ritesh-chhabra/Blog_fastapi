from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from blog import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from blog.hashing import Hash
from blog.repository import user

router = APIRouter(
    prefix = "/user",
    tags=['user']
)

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.create(request, db)

@router.get('/', response_model= List[schemas.ShowUser])
def all_users(db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.all(db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.get(id, db)