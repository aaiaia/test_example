import sys
import time
import datetime
import threading

from pytz import timezone

def thread_test(number, float_time):
    _currtime = datetime.datetime.now(timezone('Asia/Seoul'))
    print(str(_currtime) + ', thread_test, number is \'' + str(number) + '\', time: \'' + str(float_time) + '\' [start]')
    time.sleep(5)
    _currtime = datetime.datetime.now(timezone('Asia/Seoul'))
    print(str(_currtime) + ', thread_test, number is \'' + str(number) + '\', time: \'' + str(float_time) + '\' [end]')

def main():
    print('thread test program is started')

    for _i in range(0,10):
        _time               = time.time()
        _thread_test_var    = threading.Thread(target=thread_test, name="thread_test", args=(_i, _time, ))
        _thread_test_var.start()
        time.sleep(0.1)

    while True:
        print('To exit, insert \'q\'')
        input = sys.stdin.readline().rstrip("\r\n")
        if input == 'q':
            break
        else:
            continue

    print('thread test program will be closed')

if __name__ == '__main__':
    main()
