# file handling

# f = open('sample_test.txt', 'w')
# f.write('Lorem ipsum dolor sit amet')
# f.close()

#-------------------------------------------
'''using context manager 'with' handling context'''
# with open('sample_test.txt', 'w') as f:
#     f.wirte('using context manager')
    
#--------------------------------------------
'''context manager class'''

# class Open_file():
    
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
    
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
    
#     def __exit__(self, exc_type, exc_val, traceback):
#         self.file.close()
        

# with Open_file('sample_test.txt', 'w') as f:
#     f.write('Testing')
    
# print(f.closed)

#------------------------------------------------
'''context manager generator tutorial'''

from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f         #'yield generator
    finally:
        f.close()
    
with open_file('sample_test.txt', 'w') as f:
    f.write('Testing decorator contextmanager')
    
print(f.closed)

#------------------------------------------------
'''cd '''

import os

# cwd = os.getcwd()
# os.chdir('sample-dir-one')
# print(os.listdir())
# os.chdir(cwd)

# cwd = os.getcwd()
# os.chdir('sample-dir-two')
# print(os.listdir())
# os.chdir(cwd)

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)
        
with change_dir('sample-dir-one'):
    print(os.listdir())

with change_dir('sample-dir-two'):
    print(os.listdir())
