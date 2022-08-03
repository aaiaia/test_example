import sys
import get_code_info as ci

def example_function_1_0():
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(0))
    print('current [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(1))
    print(' caller [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)

def example_function_1_1():
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(0))
    print('current [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(1))
    print(' caller [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)

def example_function_1_2():
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(0))
    print('current [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(1))
    print(' caller [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)
