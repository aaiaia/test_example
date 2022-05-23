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
    thread_evt.set()    # event set to True
    _currtime = datetime.datetime.now(timezone('Asia/Seoul'))
    print(str(_currtime) + ', thread_test, number is \'' + str(number) + '\', time: \'' + str(float_time) + '\' [end]')

def main():
    print('thread test program is started')
    _thread_evt_list    = []
    _thread_unlocked    = False

    for _i in range(0,10):
        _thread_evt         = threading.Event()
        _time               = time.time()

        _thread_evt_list.append(_thread_evt)
        _thread_evt.clear() # event set to False

        _thread_test_var    = threading.Thread(target=thread_test, name="thread_test", args=(_i, _time, _thread_evt, ))
        _thread_test_var.start()

        time.sleep(0.05)

    _wait_sec = 0.01
    while not _thread_unlocked:
        _thread_unlocked_and_acc   = True
        for _i, _item_thread_evt in enumerate(_thread_evt_list):
            _fr                         = _item_thread_evt.wait(_wait_sec)
            _thread_unlocked_and_acc    &= _fr  # if one or more threads are released, it has True
            _currtime = datetime.datetime.now(timezone('Asia/Seoul'))
            if _fr:
                print(str(_currtime) + ', wait result: ' + str(_fr) + ', ' + str(_i) + ' is released')
            else:
                print(str(_currtime) + ', wait result: ' + str(_fr) + ', ' + str(_i) + ' is locked, wait: ' + str(_wait_sec) + 's')

        _thread_unlocked = _thread_unlocked_and_acc
        if _thread_unlocked_and_acc:
            _thread_unlocked    = True
            _currtime = datetime.datetime.now(timezone('Asia/Seoul'))
            print(str(_currtime) + ', _thread_unlocked: ' + str(_thread_unlocked))

    for _i, _item_thread_evt in enumerate(_thread_evt_list):
        _fr = _item_thread_evt.wait(0.01)
        _currtime = datetime.datetime.now(timezone('Asia/Seoul'))
        if _fr:
            print(str(_currtime) + ', [' + str(_i) + '] Checking thread is unlocked: ' + str(_fr ) + '(=event set())')
        else:
            print(str(_currtime) + ', [' + str(_i) + '] Checking thread is locked: ' + str(_fr ) + '(event clear())')

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
