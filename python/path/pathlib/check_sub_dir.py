from enum import Enum
from pathlib import Path

class SEARCH_TYPE(Enum):
    ALL = 0
    FILE = 1
    DIR = 2

def search(path: str = './', name: str = '', ext: str = '', search_type: SEARCH_TYPE = SEARCH_TYPE.ALL):
    _targetPath = Path(path)
    if _targetPath.exists():
        for _child in _targetPath.iterdir():
            print('\'' + str(type(_child)) + '\', path: \'' + './' + str(_child) + '\'', end='')
            if _child.is_dir():
                print(' is_dir?: ' + str(_child.is_dir()))
            elif _child.is_file():
                print(' is_file?: ' + str(_child.is_file()))
            else:
                print('is unknown')
    else:
        print('\'' + path + '\' is not exist')

def main():
    _testPath = './examples'
    p = Path(_testPath)
    if p.exists():
        for child in p.iterdir():
            print('\'' + str(type(child)) + '\', path: \'' + './' + str(child) + '\'', end='')
            if child.is_dir():
                print(' is_dir?: ' + str(child.is_dir()))
            elif child.is_file():
                print(' is_file?: ' + str(child.is_file()))
            else:
                print(' is unknown')
    else:
        print('error!!! \'' + _testPath + '\' is not exist')

    print('Call search() function')
    search()

if __name__ == '__main__':
    main()
