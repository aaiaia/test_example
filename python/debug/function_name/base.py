import sys
import imported_0, imported_1

def function_in_base():
    imported_1.example_function_1_0()

def main():
    print('-> call from main() function')
    imported_0.example_function_0_0()
    print('-> call from function_in_base() function')
    function_in_base()

if __name__ == '__main__':
    main()
