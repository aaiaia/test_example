import os
import sys
import threading
import time
import datetime

def thread_test(number, float_time, thread_cond, timeout_100ms=10):
    print('Thread#' + str(number) + ' is started!!!')

    thread_cond.acquire()
    while True:
        if thread_cond.wait(timeout=1):
            _time_s = time.time()

            _sum = 0
            for _i in range(number,number+10000000):
                _sum += _i

            _time_e = time.time()
            _time_d = _time_e = _time_s
            print('Thread#: ' + str(number) + ', _sum result: ' + str(_sum) + ', dt=' + str(_time_d))
        else:
            pass

    thread_cond.release()

    print('Thread#' + str(number) + ' is ended!!!')

def main():
    _thread_list    = []
    _thread_cond    = threading.Condition()

    for _i in range(0,10):
        _time   = time.time()

        _thread_new = threading.Thread(target=thread_test, name='thread_test', args=(_i, _time, _thread_cond, ))
        _thread_new.start()

    while True:
        print('To exit, insert \'q\', notify \'n\', notify_all \'a\'')
        input = sys.stdin.readline().rstrip("\r\n")
        if input == 'q':
            break
        elif input == 'n':
            with _thread_cond:
                print('insert thread numbrt wakeup: ')
                input = sys.stdin.readline().rstrip("\r\n")
                try:
                    _thread_wakeup_num = int(input)
                    print('wakeup thread num: ' + str(_thread_wakeup_num))
                    _thread_cond.notify(n=_thread_wakeup_num)
                except:
                    print('wakeup just one thread')
                    _thread_cond.notify()
        elif input == 'a':
            with _thread_cond:
                _thread_cond.notify_all()
        else:
            continue

if __name__ == '__main__':
    main()
