import sys
import get_code_info as ci

def function0():
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(1))
    print('print direction:forward,   caller [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(0))
    print('print direction:forward,  current [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)
    function1()

def function1():
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(1))
    print('print direction:forward,   caller [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(0))
    print('print direction:forward,  current [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)
    function2()

def function2():
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(1))
    print('print direction:forward,   caller [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(0))
    print('print direction:forward,  current [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)
