from email.policy import default
import graphene
from graphene import ObjectType, ID, String, Schema, Int, List, NonNull, Field


class Book(ObjectType):
    id = ID()
    title = String(required=True)


BOOK_LIST = [
    Book(id=i, title=f'book_{i}')
    for i in range(5)
]


class Student(ObjectType):
    id = ID()
    name = String()
    age = Int()
    readed_bood = List(Book)


STUDENT_LIST = [
    Student(
        id=i,
        name=f"the student {i}",
        age=i,
        readed_bood=[BOOK_LIST[i]]
    )
    for i in range(5)
]


# Mutation


class CreateStudent(graphene.Mutation):
    class Arguments:
        name = String()
        age = Int()

    ok = graphene.Boolean()
    student = graphene.Field(Student)
    age = graphene.Int()

    def mutate(root, info, **student_info):
        student = Student(id=len(STUDENT_LIST), **student_info)
        ok = True
        return CreateStudent(student=student, ok=ok)


class Mutations(ObjectType):
    create_student = CreateStudent.Field()

# Query


class Query(ObjectType):
    students = List(Student)
    student = Field(Student, id=Int(required=True))
    books = List(Book)
    book = Field(Book, id=Int(required=True))

    @staticmethod
    def resolve_students(root, info, **params):
        return STUDENT_LIST

    @staticmethod
    def resolve_student(root, info, **params):
        return next((student for student in STUDENT_LIST if str(student.id) == str(params["id"])), {})

    @staticmethod
    def resolve_books(root, info, **params):
        return BOOK_LIST

    @staticmethod
    def resolve_book(root, info, **params):
        return next((book for book in BOOK_LIST if str(book.id) == str(params["id"])), {})


schema = Schema(query=Query, mutation=Mutations)
