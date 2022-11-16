import sys
import time
import datetime
import threading

from pytz import timezone

def thread_test(thread_number, float_time, thread_lock, timeout_100ms=1):
    _currtime = datetime.datetime.now(timezone('Asia/Seoul'))
    print(str(_currtime) + ', thread_test, thread_number is \'' + str(thread_number) + '\', time: \'' + str(float_time) + '\' [start]')

    _currtime = datetime.datetime.now(timezone('Asia/Seoul'))
    print(str(_currtime) + ', ' + str(thread_number) + '-th thread wait until lock is acquired')
    while not thread_lock.locked():
        pass
    _currtime = datetime.datetime.now(timezone('Asia/Seoul'))
    print(str(_currtime) + ', ' + str(thread_number) + '-th thread detect lock is acquired')

    for _i in range(0, timeout_100ms):
        time.sleep(0.1)

    _currtime = datetime.datetime.now(timezone('Asia/Seoul'))
    print(str(_currtime) + ', ' + str(thread_number) + '-th thread lock is released')
    thread_lock.release()

    _currtime = datetime.datetime.now(timezone('Asia/Seoul'))
    print(str(_currtime) + ', thread_test, thread_number is \'' + str(thread_number) + '\', time: \'' + str(float_time) + '\' [end]')

def main():
    print('thread test program is started')
    _thread_lock_list   = []
    _thread_is_done     = False

    for _i in range(0,10):
        _thread_lock        = threading.Lock()
        _time               = time.time()

        _thread_lock_list.append(_thread_lock)

        _thread_test_var    = threading.Thread(target=thread_test, name="thread_test", args=(_i, _time, _thread_lock, 5,))
        _thread_test_var.start()
       
        time.sleep(0.100)
        _currtime = datetime.datetime.now(timezone('Asia/Seoul'))
        print(str(_currtime) + ', ' + __name__+ ', ' + str(_i) + '-th thread is aquired')
        _thread_lock.acquire(True)
        _currtime = datetime.datetime.now(timezone('Asia/Seoul'))
        print(str(_currtime) + ', ' + __name__+ ', ' + str(_i) + '-th thread escape aquire()')

    while not _thread_is_done:
        _thread_lock_or_acc = False
        for _i, _thread_lock in enumerate(_thread_lock_list):
            _fr = _thread_lock.locked()
            _thread_lock_or_acc |= _fr
            print(__name__ + ', ' + str(_i) + '-th thread is locked?: ' + str(_fr))

        if not _thread_lock_or_acc:
            _thread_is_done = True
        else:
            time.sleep(0.05)

    for _i, _thread_lock in enumerate(_thread_lock_list):
        print(str(_currtime) + ', ' + __name__+ ', check ' + str(_i) + '-th thread lock: ' + str(_thread_lock.locked()))

    print('thread test program will be closed')

if __name__ == '__main__':
    main()
