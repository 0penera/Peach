def hello_func():
    return 'hello_function!'

print(hello_func().upper())

def hello_func2(greeting):
    return '{} function.'.format(greeting)

print(hello_func2('hi'))

def hello_func3(greeting, name = 'you'):
    return '{}, {}'.format(greeting, name)

print(hello_func3('hi', name='corey'))

def student_info(*args, **kwargs):
    print(args)  #tuple
    print(kwargs)  #dictionary
    
student_info('math', 'art', name='john', age=22)

courses =['math', 'art', 'comp_sci']
info = {'name': 'corey', 'age':30}
# student_info(courses, info)
# student_info(*courses, **info)

#------------------------------------------------------
#number of days per month, first value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """return true for leap years, false for non leap years"""
    
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """return number of days in that month in that year"""
    
    if not 1 <= month <= 12:
        return 'invalid month'
    
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]

print(is_leap(2020))
print(days_in_month(2020, 2))


