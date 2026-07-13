from pydantic import BaseModel


class StudentBase(BaseModel):
    full_name: str
    class_name: str
    email: str
    phone_number: str


class StudentCreate(StudentBase):
    pass


class StudentRespone(StudentBase):
    id: int

    class Config:
        from_attributes = True
