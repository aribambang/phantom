from pydantic import BaseModel, Field, EmailStr

class PostRegisterDto(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length=6)

class PostRegisterResponseDto(BaseModel):
    id: int
    name: str
    email: EmailStr