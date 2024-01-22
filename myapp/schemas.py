from pydantic import BaseModel

class UserCreate(BaseModel):
    id: int
    username: str
    email: str
    departement: str
    roll_no: int
    class Config:
        orm_mode = True


class UserBase(UserCreate):
    class Config:
        orm_mode = True


class UserProfileCreate(BaseModel):
    id: int
    user_id: int
    address: str
    city: str
    country: str

    class Config:
        orm_mode = True


class UserProfileBase(UserProfileCreate):
    class Config:
        orm_mode = True