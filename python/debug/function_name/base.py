import sys
import imported_code0 as lib0, imported_code1 as lib1

def function_in_base():
    lib1.function0()

def main():
    print('-> call from main() function')
    lib0.function0()
    print('-> call from function_in_base() function')
    function_in_base()

if __name__ == '__main__':
    main()
