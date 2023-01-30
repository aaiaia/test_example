
# for system
import sys
import time
import threading
# for data type
import queue

class testClass:
    def __init__(self, queue_obj:queue.Queue=None):
        self.queue_obj = queue_obj
        print('self.queue_obj: ' + str(self.queue_obj))
        print('constructor')

    def __del__(self):
        print('exit')

    def yield_func(self) -> str:
        if self.queue_obj != None:
            while True:
                queueVal = self.queue_obj.get()
                if queueVal != None:
                    yield queueVal
                else:
                    break
        else:
            raise Exception('class testClass needs queue.Queue Object!')
        return queueVal

    def putQueue(self, data:str=None):
        self.queue_obj.put(data)

def printYieldsUsingFor(textTypeYields):
    __info = sys._getframe(0)
    print(__info.f_code.co_name + ', line# ' + str(__info.f_lineno) + ' start')

    for textTypeYield in textTypeYields:
        print(__info.f_code.co_name + ', line# ' + str(__info.f_lineno) + ' \'for\' statement, start')

        print('textTypeYield in \'for\' statements: ' + str(textTypeYield))
        if textTypeYield == 'exit':
            print('exit \'for\' statements')
            break
        else:
            pass
        time.sleep(0.05)  # protect cpu usagea

        print(__info.f_code.co_name + ', line# ' + str(__info.f_lineno) + ' \'for\' statement, end')

    print(textTypeYields)

    print(__info.f_code.co_name + ', line# ' + str(__info.f_lineno) + ' end')

def main():
    testObj = testClass(queue.Queue())

    textTypeYields = testObj.yield_func()

    threadPrintYields = threading.Thread(target=printYieldsUsingFor, name="printYieldsUsingFor", args=(textTypeYields, ))
    threadPrintYields .start()

    print('insert key in any string, if you want stop, insert \'exit\'')
    while True:
        time.sleep(0.05)  # delaying print time
        print('keyin: ', end = '')
        keyin = sys.stdin.readline().rstrip("\r\n")
        if keyin == 'exit':
            testObj.putQueue(None)
            print('quit keyin')
            break
        elif keyin == '':
            continue
        else:
            testObj.putQueue(keyin)

if __name__ == '__main__':
    main()
