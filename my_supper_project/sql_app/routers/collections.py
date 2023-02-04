from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, models, database, oaut2
from typing import List
from sqlalchemy.orm import Session


router = APIRouter(prefix='/collections', tags=['Collections'])
get_db = database.get_db


# 当用response model来返回一个list/多个结果时，应该用 response_model= List[schemas.ShowWallet],否则会报field required错
# collections
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_collection(request: schemas.Collection, db: Session = Depends(get_db),
                      current_user: schemas.User = Depends(oaut2.get_current_user)):
    new_collection = models.Collection(owner_uid=request.owner_uid, cid=request.cid)
    db.add(new_collection)
    db.commit()
    db.refresh(new_collection)
    return new_collection


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
def delete_collection(cid, db: Session = Depends(get_db), current_user: schemas.User = Depends(oaut2.get_current_user)):
    collection = db.query(models.Collection).filter(models.Collection.cid == cid)
    if not collection.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Collection with {cid} not found')

    collection.delete(synchronize_session=False)
    db.commit()
    return 'done'


@router.get('/', response_model=List[schemas.Collection])
def selectAllCollection(db: Session = Depends(get_db),
                        current_user: schemas.User = Depends(oaut2.get_current_user)):
    collections = db.query(models.Collection).all()
    return collections