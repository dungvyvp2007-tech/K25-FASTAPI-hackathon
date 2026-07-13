from sqlalchemy.orm import Session
import models, schemas


def get_students(db: Session):
    return db.query(models.StudentModel).all()


def get_student_by_id(db: Session, student_id: int):
    return (
        db.query(models.StudentModel)
        .filter(models.StudentModel.id == student_id)
        .first()
    )


def create_student(db: Session, stu: schemas.StudentCreate):
    db_std = models.StudentModel(
        full_name=stu.full_name,
        class_name=stu.class_name,
        email=stu.email,
        phone_number=stu.phone_number,
    )
    db.add(db_std)
    db.commit()
    db.refresh(db_std)
    return db_std


def update_student(
    db: Session, db_std: models.StudentModel, std_data: schemas.StudentCreate
):
    db_std.full_name = std_data.full_name
    db_std.class_name = std_data.class_name
    db_std.email = std_data.email
    db_std.phone_number = std_data.phone_number
    db.commit()
    db.refresh(db_std)
    return db_std


def delete_student(db: Session, db_std: models.StudentModel):
    db.delete(db_std)
    db.commit()
    return {"message": f"Xóa thành công sinh viên mang ID {db_std.id}"}


def search_students_by_classname(db: Session, class_name: str):
    return (
        db.query(models.StudentModel)
        .filter(models.StudentModel.class_name.like(f"%{class_name}%"))
        .all()
    )
