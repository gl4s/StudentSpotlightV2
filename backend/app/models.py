from pydantic import BaseModel

# Define a Pydantic model for validation
class Student(BaseModel):
    name: str
    age: int
    grade: str
