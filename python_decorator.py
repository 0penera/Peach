# closure

# def outer_function(msg):
#     message = msg
    
#     def inner_function(name):
#         print(f'{message} {name} !')
#     return inner_function

# hi_func = outer_function('hi')
# bye_func = outer_function('bye')
# hi_func('corey')
# bye_func('bok')

#--------------------------------------------------------------

# # Decorators function
# '''more often using decorator function'''

# def decorator_function(original_function):
#     def wrapper_function(*args, **kwarges):
#         print('wrapper executed this before {}'.format(original_function.__name__))
#         return original_function(*args, **kwarges)
#     return wrapper_function

# @decorator_function  #display = decorator_function(display)
# def display():
#     print('display function ran')

# @decorator_function
# def display_info(name, age):
#     print('display_info ran with argumenets({}, {})'.format(name, age))
        
# display()

# display_info('John', 23)


# -------------------------------------------------------------
# # decorator class
# '''more less using decorator class'''

# class decorator_class(object):
#     def __init__(self, original_function):
#         self.original_function = original_function
        
#     def __call__(self, *args, **kwargs):
#         print('call method executed this before {}'.format(self.original_function.__name__))
#         return self.original_function(*args, **kwargs)
    
# @decorator_class  #display = decorator_class(display)
# def display():
#     print('display function ran')

# @decorator_class
# def display_info(name, age):
#     print('display_info ran with argumenets({}, {})'.format(name, age))
        
# display()

# display_info('John', 23)


# ---------------------------------------------------------
# practical example of decorator
'''more common use case of decorator'''

# from functools import wraps

# def my_logger(orig_func):
#     # decorator save loginfo
#     import logging
#     logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    
#     @wraps(orig_func)
#     def wrapper(*args, **kwargs):
#         logging.info(
#             'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
#         return orig_func(*args, **kwargs)
    
#     return wrapper

# @my_logger
# def display_info(name, age):
#     print('display_info ran with argumenets({}, {})'.format(name, age))
        
# display_info('John', 23)


# def my_timer(orig_func):
#     # show function running time

#     import time
    
#     @wraps(orig_func)
#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = orig_func(*args, **kwargs)
#         t2 = time.time() - t1
#         print('{} ran in: {} sec'.format(orig_func.__name__, t2))
#         return result
    
#     return wrapper

# import time

# @my_timer
# def display_info(name, age):
#     time.sleep(1)
#     print('display_info ran with argumenets({}, {})'.format(name, age))
        
# display_info('John', 23)


# @my_logger
# @my_timer
# def display_info(name, age):
#     time.sleep(1)
#     print('display_info ran with argumenets({}, {})'.format(name, age))
        
# display_info('John', 23)


# display_info = my_timer(display_info)
# print(display_info.__name__)

# -------------------------------------------------------
'''decorator arguments'''


def  prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed Before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, 'Executed After', original_function.__name__)
            return result
        return wrapper_function
    return decorator_function

@prefix_decorator('TESTING:')
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))
    

display_info('john', 25)
