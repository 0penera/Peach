
# == Equal != not equal > < >= <=  is object identity 

language = "Python"

if language == "Python":
    print('language is python')
elif language == "Java":
    print('language is java')
else:
    print('no match')
    
# and   or    not
user = 'admin'
logged_in = True

if user == 'admin' and logged_in:
    print('admin page')
else:
    print('bad creds')
    
if not logged_in:
    print('admin page')
else:
    print('bad creds')
    

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)
print(f'id of a: {id(a)}, id of b: {id(b)}')

# false values: 
    # False
    # None
    # Zero of any numeric type
    # any empty sequence, for example, '', (), []
    # any empty mapping,  for example, {}

condition = []
print('Evaluated in True') if condition else print('Evaluated to False')
if condition: print('True')
