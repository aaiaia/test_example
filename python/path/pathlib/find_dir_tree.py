# for system
import sys
from enum import Enum
from pathlib import Path

class SEARCH_TYPE(Enum):
    ALL = 0
    FILE = 1
    DIR = 2

def search(path: str = './', name: str = '', search_type: SEARCH_TYPE = SEARCH_TYPE.ALL):
    _targetPath = Path(path)
    if _targetPath.exists():
        for _child in _targetPath.iterdir():
            print('\'' + str(type(_child)) + '\', path: \'' + './' + str(_child) + '\'')
            if _child.is_dir():
                print('search directory into: ' + str(_child))
                search(str(_child))
            elif _child.is_file():
                pass
            else:
                print('is unknown')
    else:
        print('\'' + path + '\' is not exist')

def test(path: str = './', name: str = '', search_type: SEARCH_TYPE = SEARCH_TYPE.ALL):
    _targetPath = Path(path)
    if _targetPath.exists():
        for _child in _targetPath.iterdir():
            print('\'' + str(type(_child)) + '\', \'' + './' + str(_child) + '\'', end='')
            if _child.is_dir():
                print(' is_directory', end='')
                print(' name: ' + _child.name)
                print('search directory into: ' + str(_child))
                test(str(_child))
            elif _child.is_file():
                print(' is_file', end='')
                print(' name: ' + _child.name)
            else:
                print('is unknown')
    else:
        print('\'' + path + '\' is not exist')

def main(argv):
    print(argv)
    HELP_MSG = 'python3 [SOURCE_FILE] [PATH] [NAME]'

    if len(argv) == 3:
        _path = argv[1]
        _name = argv[2]

        print('Call search() function')
        search(_path, _name)

        print('Call test() function')
        test(_path, _name)
    else:
        print('arguments are invalid')
        print(HELP_MSG)
        return

if __name__ == '__main__':
    main(sys.argv)
