def iterateDictionary(some_list):
    for i in some_list:
        print("first_name - " + i["first_name"] + ", last_name - " + i["last_name"])

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
iterateDictionary(students) 