

# try:
#     f = open(r'C:\Users\bokseon hwang\Documents\gitsinbook\Peach\test.txt')
#     # var = bad_var
    
try: 
    f = open(r'C:\Users\bokseon hwang\Documents\gitsinbook\Peach\test.txt')
    if f.name == 'test.txt':
        raise Exception
except FileExistsError:     # specific except error first
    print('sorry, this file dose not exist')
except Exception as e:      # general except error last
    print('sorry something went wrong : {}'.format(e))
    
else:
    print(f.read())
    f.close()
finally:    # something need to do whether it is error or not
    print("executing filnally....") 
