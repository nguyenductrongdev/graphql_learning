from schema import schema
import json

# query_with_argument = 'query { students(age: 2) }'
query_string = '''
    query {
        student(id: 3) {
            name
            age
            readed_bood
        }
    }
'''

query_string_books = '''
    query {
        books {
            title
        }
    }
'''

mutation_string = '''
    mutation {
        createStudent(name: "Peter", age: 100) {
            student {
                name
                age
            }
            ok
        }
    }
'''

result = schema.execute(query_string)
print(json.dumps(result.data, indent=3))
