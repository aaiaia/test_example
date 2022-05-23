import sys
import time
import datetime
import threading

from pytz import timezone

def thread_test(number, float_time, thread_evt, timeout_100ms=10):
    _currtime = datetime.datetime.now(timezone('Asia/Seoul'))
    print(str(_currtime) + ', thread_test, number is \'' + str(number) + '\', time: \'' + str(float_time) + '\' [start]')
    for _i in range(0, timeout_100ms):
        time.sleep(0.1)
    thread_evt.clear()
    _currtime = datetime.datetime.now(timezone('Asia/Seoul'))
    print(str(_currtime) + ', thread_test, number is \'' + str(number) + '\', time: \'' + str(float_time) + '\' [end]')

def main():
    print('thread test program is started')
    _thread_evt_list    = []
    _thread_locked      = True 

    for _i in range(0,10):
        _thread_evt               = threading.Event()
        _time               = time.time()

        _thread_evt_list.append(_thread_evt)
        _thread_evt.set()

        _thread_test_var    = threading.Thread(target=thread_test, name="thread_test", args=(_i, _time, _thread_evt, ))
        _thread_test_var.start()

        time.sleep(0.05)

    while _thread_locked:
        _thread_locked_or_acc   = False
        for _i, _thread_evt in enumerate(_thread_evt_list):
            _fr = _thread_evt.wait(0.1)
            _thread_locked_or_acc      |= _fr  # if one or more threads are released, it has True
            _currtime = datetime.datetime.now(timezone('Asia/Seoul'))
            if _fr:
                print(str(_currtime) + ', wait result: ' + str(_fr) + ', ' + str(_i) + ' is locked')
            else:
                print(str(_currtime) + ', wait result: ' + str(_fr) + ', ' + str(_i) + ' is released')
        _thread_locked  = _thread_locked_or_acc
        if not _thread_locked:
            print('_thread_locked: ' + str(_thread_locked))

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
