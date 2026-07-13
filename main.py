from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
import database, models, schemas, AccountService

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


@app.get("/", tags=["Students"])
def read_root():
    return {"msg": "API đang chạy", "data": None}


@app.post(
    "/students",
    response_model=schemas.StudentRespone,
    status_code=201,
    tags=["Students"],
)
def create_new_student(
    stu: schemas.StudentCreate, db: Session = Depends(database.get_db)
):
    return AccountService.create_student(db=db, stu=stu)


@app.get("/students", response_model=List[schemas.StudentRespone], tags=["Students"])
def read_all_students(db: Session = Depends(database.get_db)):
    return AccountService.get_students(db=db)


@app.get(
    "/students/search", response_model=List[schemas.StudentRespone], tags=["Students"]
)
def search_students(
    class_name: str = Query(...), db: Session = Depends(database.get_db)
):
    return AccountService.search_students_by_classname(db=db, class_name=class_name)


@app.get(
    "/students/{student_id}", response_model=schemas.StudentRespone, tags=["Students"]
)
def read_student_detail(student_id: int, db: Session = Depends(database.get_db)):
    db_std = AccountService.get_student_by_id(db=db, student_id=student_id)
    if not db_std:
        raise HTTPException(
            status_code=404, detail=f"Không tìm thấy sinh viên có ID {student_id}"
        )
    return db_std


@app.put(
    "/students/{student_id}", response_model=schemas.StudentRespone, tags=["Students"]
)
def update_existing_student(
    student_id: int,
    std_data: schemas.StudentCreate,
    db: Session = Depends(database.get_db),
):
    db_std = AccountService.get_student_by_id(db=db, student_id=student_id)
    if not db_std:
        raise HTTPException(
            status_code=404, detail=f"Không tìm thấy sinh viên có ID {student_id}"
        )
    return AccountService.update_student(db=db, db_std=db_std, std_data=std_data)


@app.delete(
    "/students/{student_id}", tags=["Students"]
)
def delete_existing_student(student_id: int, db: Session = Depends(database.get_db)):
    db_std = AccountService.get_student_by_id(db=db, student_id=student_id)
    if not db_std:
        raise HTTPException(
            status_code=404, detail=f"Không tìm thấy sinh viên có ID {student_id}"
        )
    return AccountService.delete_student(db=db, db_std=db_std)
