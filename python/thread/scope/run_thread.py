import sys
import time
import datetime
import threading

from pytz import timezone

def thread_test(number, float_time, waittime_sec=1):
    _currtime = datetime.datetime.now(timezone('Asia/Seoul'))
    print(str(_currtime) + ', thread_test, number is \'' + str(number) + '\', time: \'' + str(float_time) + '\' [start]')
    time.sleep(waittime_sec)
    _currtime = datetime.datetime.now(timezone('Asia/Seoul'))
    print(str(_currtime) + ', thread_test, number is \'' + str(number) + '\', time: \'' + str(float_time) + '\' [end]')

def main():
    print('thread test program is started')
    _waittime_sec = 5

    for _i in range(0,10):
        _time               = time.time()
        _thread_test_var    = threading.Thread(target=thread_test, name="thread_test", args=(_i, _time, _waittime_sec, ))
        _thread_test_var.start()
        time.sleep(0.1)

    print('wait ' + str(_waittime_sec) + 's')
    time.sleep(_waittime_sec)

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
