from fastapi import FastAPI
from . import models
from .database import engine
from fastapi.responses import JSONResponse
from .routers import collections, users, authentication

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(authentication.router)
app.include_router(collections.router)
app.include_router(users.router)


# Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# 用来hashing password
# pwd_cxt = CryptContext(schemes= ['bcrypt'], deprecated='auto')


# 用来检测代码出错原因
@app.exception_handler(ValueError)
async def value_error_exception_handler(exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )


# users
# @app.post('/user', tags=['users'])   # sign in
# def create_user(request: schemas.CreateUser, db: Session = Depends(get_db)):
#     hashedPassword = pwd_cxt.hash(request.password)
#     new_user = models.User(username=request.username,  hashed_password=hashedPassword,
#                            nickname=request.nickname, profile_photo=request.profile_photo)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user
#
#
# @app.get('/user/{id}', response_model=schemas.ShowUser, tags=['users'])
# def get_user(uid: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.uid == uid).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'User with the {uid} is not found')
#     return user


# # wallets
# # 当用response model来返回一个list/多个结果时，应该用 response_model= List[schemas.ShowWallet],否则会报field required错
# @app.post('/wallets',  response_model=List[schemas.ShowWallet], tags=['wallets'])
# def create_wallet(request: schemas.CreateWallet, db: Session = Depends(get_db)):
#     new_wallet = models.Wallet(owner_uid=request.owner_uid)
#     db.add(new_wallet)
#     db.commit()
#     db.refresh(new_wallet)
#     return new_wallet
#
#
# # collections
# @app.post('/collections', tags=['collections'])
# def create_collection(request: schemas.Collection, db: Session = Depends(get_db)):
#     new_collection = models.Collection(owner_wid=request.owner_wid)
#     db.add(new_collection)
#     db.commit()
#     db.refresh(new_collection)
#     return new_collection


# # get all blog
# @app.get('/blog')
# def all_blogs(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


# # get one blog through id
# @app.get('/blog/{id}')
# def show(id, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     return blog


# delete a blog
# @app.delete('/blog/{id}', status_code = status.HTTP_204_NO_CONTENT)
# def delete(id, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
#     db.commit()
#     return f'the {id} blog have been deleted'


# update a blog   ......
# @app.post("/users/", response_model=schemas.User)
# def creat_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_username(db, username=user.username)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Userid already registered")
#     return crud.create_user(db=db, user=user)
#
#
# @app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users
#
#
# @app.get("/users/{user_uid}", response_model=schemas.User)
# def read_user(user_uid: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_uid(db, user_uid=user_uid)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
#
#
# @app.post("/users/{user_uid}/wallets/", response_model=schemas.Wallet)
# def create_wallet_for_user(
#     user_uid: int, wallet: schemas.WalletCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_wallet(db=db, wallet=wallet, user_uid=user_uid)
#
#
# @app.get("/wallets/", response_model=list[schemas.Wallet])
# def read_wallets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     wallets = crud.get_wallets(db, skip=skip, limit=limit)
#     return wallets
