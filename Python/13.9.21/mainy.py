import motor


MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.students
student_collection = database.get_collection("students_collection")

def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"]

    }
async def retrieve_students():
     students = []
     async for student in student_collection.find():
        students.append(student_helper(student))
     return students
# Add a new student into to the database l
async def add_student(student_data: dict) -> dict:
     student = await student_collection.insert_one(student_data)
     new_student = await student_collection.find_one({"_id": student.inserted_id})
     return student_helper(new_student)