import sys
import get_code_info as ci

def function0():
    function1()
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(0))
    print('print direction:backward, current [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(1))
    print('print direction:backward,  caller [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)

def function1():
    function2()
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(0))
    print('print direction:backward, current [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(1))
    print('print direction:backward,  caller [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)

def function2():
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(0))
    print('print direction:backward, current [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(1))
    print('print direction:backward,  caller [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)
