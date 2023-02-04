from sqlalchemy import Boolean, BLOB, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    uid = Column(Integer, primary_key=True, index=True)
    username = Column(String(length=252), unique=True)
    hashed_password = Column(String(length=252))
    nickname = Column(String(length=252))
    profile_photo = Column(String(length=252))  # BLOB
    create_time = Column(String(length=252), default='1')    # DateTime   #time of creating the account
    last_updated_time = Column(String(length=252), default='1')   # DateTime  #time of latest operation
    is_available = Column(Boolean, default=True)  # detected the account if could be use
    is_active = Column(Boolean, default=True)  # detected the account if online

    collections = relationship("Collection", back_populates="collection_owner")


# class Wallet(Base):
#     __tablename__ = "wallets"
#
#     wid = Column(Integer, primary_key=True, index=True)
#     owner_uid = Column(Integer, ForeignKey("users.uid"))
#     address = Column(String, default=1)
#     private_key = Column(String, default=1)
#
#     wallet_owner = relationship("User", back_populates="wallets")
#     collections = relationship("Collection", back_populates="collection_owner")
#

class Collection(Base):
    __tablename__ = "collections"

    cid = Column(Integer, primary_key=True, index=True)
    owner_uid = Column(Integer, ForeignKey("users.uid"))

    collection_owner = relationship("User", back_populates="collections")
