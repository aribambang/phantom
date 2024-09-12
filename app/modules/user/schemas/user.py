from pydantic import BaseModel, Field, EmailStr

class UserCreateDto(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length=6)

class UserResponseDto(BaseModel):
    id: int
    name: str
    email: EmailStr