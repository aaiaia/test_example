# for system
import sys
from pathlib import Path
# for data type
from enum import Enum
# for debugging
import getopt

class DEF_TYPE(Enum):
    ALL = 0
    FILE = 1
    DIR = 2

def search(path: str = './', name: str = '', search_type: DEF_TYPE = DEF_TYPE.ALL):
    _ret_result = False
    _ret_path = ''
    if name != '':
        _targetPath = Path(path)
        if _targetPath.exists():
            for _child in _targetPath.iterdir():
                """ determinant match with target, has 1st priority """
                if _child.name == name:
                    if search_type == DEF_TYPE.ALL:
                        _ret_result = True
                    elif search_type == DEF_TYPE.DIR and _child.is_dir():
                        _ret_result = True
                    elif search_type == DEF_TYPE.FILE and _child.is_file():
                        _ret_result = True
                    else:
                        _ret_result = False
                else:
                    _ret_result = False

                """ set target path info, has 2nd priority """
                if _ret_result:
                    _ret_path = str(_child)
                    print('target is found: ', end='')
                    print(str(_ret_path))

                """ if not match with target and _child is directory, go into it, has 3rd priority """
                if not _ret_result and _child.is_dir():
                    print('search directory into: ' + str(_child))
                    _ret_result, _ret_path = search(str(_child), name, search_type)
                else:
                    pass

                """ if target is found, just break for statement, has lowest priority """
                if _ret_result:
                    break

        else:
            print('\'' + path + '\' is not exist')
    else:
        print('name is blank, end search')

    return _ret_result, _ret_path

def test(path: str = './', name: str = ''):
    _targetPath = Path(path)
    if _targetPath.exists():
        for _child in _targetPath.iterdir():
            print(str(type(_child)) + ', ' + './' + str(_child) + '', end='')
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

    _test = False
    _path = ''
    _name = ''
    _type = DEF_TYPE.ALL

    try:
        # opts: getopt 옵션에 따라 파싱 ex) [('-i', 'myinstancce1')]
        # etc_args: getopt 옵션 이외에 입력된 일반 Argument
        # argv 첫번째(index:0)는 파일명, 두번째(index:1)부터 Arguments
        etc_args = []
        opts, etc_args = getopt.getopt(argv[1:], \
            "h:tp:n:e:", ["help", "test", "path=", "name=", "type="])
        if etc_args != []:
            opts, etc_args = getopt.getopt(argv[3:], \
                "h:te:", ["help", "test", "type="])

    except getopt.GetoptError: # 옵션지정이 올바르지 않은 경우
        print(HELP_MSG)
        sys.exit(2)

    for opt, arg in opts: # 옵션이 파싱된 경우
        if opt in ("-h", "--help"): # HELP 요청인 경우 사용법 출력
            print(HELP_MSG)
            sys.exit(2)
        elif opt in ("-t", "--test"):
            _test = True
            print('set test mode')
        elif opt in ("-p", "--path"):
            _path = arg
            print('set path: ' + _path)
        elif opt in ("-n", "--name"):
            _name = arg
            print('set name: ' + _name)
        elif opt in ("-e", "--type"):
            _type = arg
            if _type == 'file' or _type == 'FILE':
                _type = DEF_TYPE.FILE
            elif  _type == 'dir' or _type == 'DIR':
                _type = DEF_TYPE.DIR
            elif  _type == 'all' or _type == 'ALL':
                _type = DEF_TYPE.ALL
            print('set type: ' + str(_type))

    if not _test:
        if len(argv) >= 3:
            if _path == '': _path = argv[1]
            if _name == '': _name = argv[2]
            print('search path: ' + _path)
            print('search name: ' + _name)

            print('Call search() function')
            _found_result, _found_path = search(_path, _name, _type)
            if _found_result:
                print('search() path: ' + _found_path)
            else:
                print('search() failed: ' + _name)
        else:
            print('arguments are invalid')
            print(HELP_MSG)
    else:
        print('Call test() function')
        test(_path, _name)

if __name__ == '__main__':
    main(sys.argv)
