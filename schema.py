from email.policy import default
import graphene
from graphene import ObjectType, ID, String, Schema, Int, List, NonNull, Field


class Book(ObjectType):
    title = String(required=True)


class Student(ObjectType):
    id = ID()
    name = String()
    age = Int()
    readed_bood = List(Book)


STUDENT_LIST = [
    Student(id=i, name=f"the student {i}", age=i, readed_bood=[])
    for i in range(5)
]


class Query(ObjectType):
    students = List(Student)
    student = Field(Student, id=Int(required=True))

    @staticmethod
    def resolve_students(root, info, **params):
        return STUDENT_LIST

    @staticmethod
    def resolve_student(root, info, **params):
        return next((student for student in STUDENT_LIST if str(student.id) == str(params["id"])), {})

# Mutation


class CreateStudent(graphene.Mutation):
    class Arguments:
        name = String()

    def mutate(root, info, name):
        student = Student(name=name)
        ok = True
        return CreateStudent(student=student, ok=ok)


class Mutations(ObjectType):
    create_student = CreateStudent.Field()


schema = Schema(query=Query)
