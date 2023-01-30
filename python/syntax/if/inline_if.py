import sys
import time

def main():
    while True:
        _tempString = ''
        _tempInteger = 0

        time.sleep(0.05)  # delaying print time

        print('_keyin: ', end = '')
        _keyin = sys.stdin.readline().rstrip("\r\n")
        if _keyin == 'exit':
            print('quit _keyin')
            break
        elif _keyin == '':
            continue
        else:
            _tempString = _keyin if not _keyin.isdecimal( ) else 'value is decimal'
            _tempInteger = int(_keyin) if _keyin.isdecimal() else -1

            print('_tempString: ', end='')
            print(_tempString)
            print('_tempInteger=', end='')
            print(_tempInteger)

if __name__ == '__main__':
    main()
