class TestClassExample1:
    def __init__(self):
        print('constructor')
    def __del__(self):
        print('exit')

class TestClassExample2:
    def __init__(self):
        print('constructor')
    def __del__(self):
        print('exit')

def main():
    print('start program')
    testClass = TestClassExample1()
    print(testClass.__class__)
    print('isinstance(testClass, TestClassExample1): ' + str(isinstance(testClass, TestClassExample1)))
    print('isinstance(testClass, TestClassExample2): ' + str(isinstance(testClass, TestClassExample2)))
    
    print('end program')

if __name__ == '__main__':
    main()
