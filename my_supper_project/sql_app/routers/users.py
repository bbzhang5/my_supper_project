from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, models, database, hashing
from typing import List
from sqlalchemy.orm import Session


router = APIRouter(prefix='/user', tags=['Users'])
get_db = database.get_db


@router.post('/')   # sign in
def create_user(request: schemas.CreateUser, db: Session = Depends(get_db)):
    hashedPassword = hashing.pwd_cxt.hash(request.password)
    new_user = models.User(username=request.username,  hashed_password=hashedPassword,
                           nickname=request.nickname, profile_photo=request.profile_photo)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(uid: int, db: Session = Depends(get_db)):
    users = db.query(models.User).filter(models.User.uid == uid).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the {uid} is not found')
    return users


@router.get('/', response_model=List[schemas.ShowUser])
def selectAllUser(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users