class Test:
    def __init__(self):
        print('constructor')
    def __del__(self):
        print('exit')

def main():
    testClass = Test()

if __name__ == '__main__':
    main()
