from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from blog import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from blog.repository import blog

router = APIRouter(
    prefix = "/blog",
    tags=['blogs']
)

@router.get('/{id}', status_code = status.HTTP_200_OK, response_model= schemas.ShowBlog)
def show(id, response: Response, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)

@router.post('/', status_code= status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(request, db)

@router.get('/', response_model= List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)