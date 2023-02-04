# from pydantic import BaseModel
#
#
# class CollectionBase(BaseModel):
#     pass
#
#
# class CollectionCreate(CollectionBase):
#     pass
#
#
# class Collection(CollectionBase):
#     cid: int
#     owner_wid: int
#
#     class Config:
#         orm_mode = True
#
#
# class WalletBase(BaseModel):
#     pass
#
#
# class WalletCreate(WalletBase):
#     address: str
#     private_key: str
#
#
# class Wallet(WalletBase):
#     wid: int
#     owner_uid: int
#     collections: list[Collection] = []
#
#     class Config:
#         orm_mode = True
#
#
# class UserBase(BaseModel):
#     username: str
#     nickname: str
#     profile_photo: str
#
#
# class UserCreate(UserBase):
#     password: str
#     create_time: str
#
#
# class User(UserBase):
#     uid: int
#     last_updated_time: str
#     is_active: bool
#     is_available: bool
#     wallets: list[Wallet] = []
#
#     class Config:
#         orm_mode = True


# python 的顺序是从上往下的每行进行的，如果想要的在一个类A里面引入另一个类B，
# 则需要把B放在A之前
from pydantic import BaseModel
from typing import List, Optional


class Collection(BaseModel):
    cid: int
    owner_uid: int

    class Config:
        orm_mode = True

# 当model是orm时，记得加上最后这个orm mode = true


class Wallet(BaseModel):
    owner_uid: int   #declare whose wallet while creating
    wid: int
    address: str
    private_key: str

    collections: List[Collection] = []

    class Config:
        orm_mode = True


class CreateWallet(BaseModel):
    owner_uid: int

    class Config:
        orm_mode = True


class User(BaseModel):
    uid: int
    username: str
    password: str
    nickname: str
    profile_photo: str
    create_time: str
    last_updated_time: str
    is_available: bool
    is_active: bool

    wallets: List[Wallet] = []

    class Config:
        orm_mode = True


class CreateUser(BaseModel):

    username: str
    password: str
    nickname: str
    profile_photo: str
    # wallets: List[Wallet] = []

    class Config:
        orm_mode = True


class ShowWallet(BaseModel):
    wid: int
    owner_uid: int

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    uid: int
    username: str
    nickname: str
    profile_photo: str
    wallets: List[ShowWallet] = []

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


