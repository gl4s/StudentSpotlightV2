from fastapi import APIRouter, HTTPException
from .models import Student
from .db import db

router = APIRouter()

@router.post("/students")
async def create_student(student: Student):
    student_dict = student.dict()
    result = await db.students.insert_one(student_dict)
    if result.inserted_id:
        return {"message": "Student created successfully", "student_id": str(result.inserted_id)}
    raise HTTPException(status_code=400, detail="Failed to create student")

@router.get("/students/{student_id}")
async def get_student(student_id: str):
    student = await db.students.find_one({"_id": student_id})
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student not found")

# You can add more CRUD operations here (update, delete)
