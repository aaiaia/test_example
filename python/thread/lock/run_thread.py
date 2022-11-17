import sys
import time
import datetime
import threading

from pytz import timezone

__shared_var_non_block = 0
__shared_var_block = 0

def thread_acc_test(thread_number, acc_count:int, thread_lock=None):
    global __shared_var_non_block, __shared_var_block
    _time = time.time()
    _currtime = datetime.datetime.now(timezone('Asia/Seoul'))
    print(str(_currtime) + ', thread_acc_test, thread_number is \'' + str(thread_number) + '\', time: \'' + str(_time) + '\' [start]')

    if thread_lock:
        for _i in range(0, acc_count):
            thread_lock.acquire()

            #there is test codes, thread access
            __shared_var_block += 1

            thread_lock.release()
    else:
        for _i in range(0, acc_count):
            #there is test codes, thread access
            __shared_var_non_block += 1

    print('[INFO]__shared_var_non_block= ' + str(__shared_var_non_block) + ', __shared_var_block= ' + str(__shared_var_block))

    _time = time.time()
    _currtime = datetime.datetime.now(timezone('Asia/Seoul'))
    print(str(_currtime) + ', thread_acc_test, thread_number is \'' + str(thread_number) + '\', time: \'' + str(_time) + '\' [end]')

def main():
    print('thread test program is started')
    _thread_lock        = threading.Lock()

    for _i in range(0,10):
        _thread_acc_test_var    = threading.Thread(target=thread_acc_test, name="thread_acc_test_non_blocking", args=(_i, 100000, None,))
        _thread_acc_test_var.start()

    for _i in range(10,20):
        _thread_acc_test_var    = threading.Thread(target=thread_acc_test, name="thread_acc_test_blocking", args=(_i, 100000, _thread_lock,))
        _thread_acc_test_var.start()

    print('thread test program will be closed')

if __name__ == '__main__':
    main()
