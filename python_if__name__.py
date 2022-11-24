print(__name__)

def main():
    print('first modules name: {}'.format(__name__))

if __name__ == '__main__':
    # check 'is this file directly run' 
    main()
else:
    print('run from import')