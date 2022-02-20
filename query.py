from schema import schema
import json

# query_with_argument = 'query { students(age: 2) }'
query_string = '''
    query {
        student(id: 3) {
            name
            age
        }
    }
'''

mutation_string = '''
    mutation {
        createStudent(name: "Peter") {
            student {
                name
            }
            ok
        }
    }
'''

result = schema.execute(query_string)
print(json.dumps(result.data, indent=3))
