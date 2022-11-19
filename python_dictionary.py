#how to use dictionary

#create dictionary
student = {'name': 'John', 'age': 25, 'courses': ['math', 'compsci']\
            ,1: 111}
#insert new key and value
student['phone'] = '555-5555'
student['name'] = 'Jane'
student.update({'name': 'Jane', 'age': 26, 'phone': '666-3333'})

#delete value and key
age = student.pop('age')
student['age'] = 50
del student['age']

#get dictionary size, keys, values and itterate 
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
print(student)
print(student.get('phone', 'not found'))
print(age)

for key, value in student.items():
    print(key, value)