# from sqlalchemy.orm import Session
#
# from . import models, schemas
#
#
# # read a single user by uid
# def get_user_by_uid(db: Session, user_uid: int):
#     return db.query(models.User).filter(models.User.uid == user_uid).first()
#
#
# # read a single user by username
# def get_user_by_username(db: Session, username: str):
#     return db.query(models.User).filter(models.User.username == username).first()
#
#
# # read multiple users
# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()
#
#
# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password
#     db_user = models.User(username=user.username, hashed_password=fake_hashed_password,
#                           nickname=user.nickname, profile_photo=user.profile_photo)
#                         # ? if need the rest parametres; if use the schemas.UserCreate
#     db.add(db_user)   # add that instance object to your database session.
#     db.commit()       # commit the changes to the database (so that they are saved).
#     db.refresh(db_user)  # refresh your instance (so that it contains any new data from the database).
#     return db_user
#
#
# # read multiple items
# def get_wallets(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Wallet).offset(skip).limit(limit).all()
#
#
# def create_wallet(db: Session, wallet: schemas.WalletCreate, user_uid: int,
#                        wallet_address: str, wallet_private_key: str):
#     db_wallet = models.Wallet(**wallet.dict(), owner_uid=user_uid,
#                               address=wallet_address, private_key=wallet_private_key)
#     db.add(db_wallet)
#     db.commit()
#     db.refresh(db_wallet)
#     return db_wallet
#
#
# def get_collections(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Collection).offset(skip).limit(limit).all()
#
#
# def create_collection(db: Session, collection: schemas.CollectionCreate, wallet_wid: int):
#     db_collection = models.Collection(**collection.dict(), owner_wid=wallet_wid)
#     db.add(db_collection)
#     db.commit()
#     db.refresh(db_collection)
#     return db_collection