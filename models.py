from database import Base
from sqlalchemy import Column, String, Integer


class StudentModel(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(50), nullable=False)
    class_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    phone_number = Column(String(50), nullable=False)
