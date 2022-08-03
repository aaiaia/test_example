import sys
import get_code_info as ci

def example_function_0_0():
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(0))
    print('print direction:forward,  current [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(1))
    print('print direction:forward,   caller [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)
    example_function_0_1()

def example_function_0_1():
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(0))
    print('print direction:forward,  current [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(1))
    print('print direction:forward,   caller [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)
    example_function_0_2()

def example_function_0_2():
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(0))
    print('print direction:forward,  current [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)
    _filename, _funcname, _codeline = ci.get_code_info(sys._getframe(1))
    print('print direction:forward,   caller [file:function:line] -> ' + _filename + ':' + _funcname + ':' + _codeline)
