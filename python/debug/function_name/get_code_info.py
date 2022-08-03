import sys

def get_code_info(frame):
    _filename = 'UnknownFile'
    _funcname = 'UnknwonFunction'
    _codeline = '?'
    if frame != None:
        _filename = str(frame.f_code.co_filename)
        _funcname = str(frame.f_code.co_name)
        _codeline = str(frame.f_lineno)
    else:
        pass

    return _filename, _funcname, _codeline
