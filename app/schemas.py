from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
   
from pydantic.types import conint



class BlogBase(BaseModel):
    
    title : str
    content : str
    published : bool 
    
   
class BlogCreate(BlogBase):
    pass

class UserOut(BaseModel):
   id : int
   email: EmailStr    
   created_at: datetime
   
   class Config:
     orm_mode = True


class Blog(BlogBase):
    id : int
    created_at: datetime
    owner_id : int
    owner: UserOut

    class Config:
     orm_mode = True

class BlogOut(BaseModel):
   Blog: Blog
   votes: int

   class Config:
      orm_mode = True


class UserCreate(BaseModel):
   email: EmailStr
   password: str    


class UserLogin(BaseModel):
   email : EmailStr
   password: str

class Token(BaseModel):
   access_token : str
   token_type: str


class TokenData(BaseModel):
   id: Optional[str]= None 

class Vote(BaseModel):
   blog_id: int
   dir: conint (le=1)    