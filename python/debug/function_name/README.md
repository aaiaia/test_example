# Example, get filename, function name and codeline
```bash
$ python3 base.py
-> call from main() function
print direction:forward,   caller [file:function:line] -> base.py:main:9
print direction:forward,  current [file:function:line] -> [IMPORTED_FILE_PATH]/imported_code0.py:function0:7
print direction:forward,   caller [file:function:line] -> [IMPORTED_FILE_PATH]/imported_code0.py:function0:9
print direction:forward,  current [file:function:line] -> [IMPORTED_FILE_PATH]/imported_code0.py:function1:14
print direction:forward,   caller [file:function:line] -> [IMPORTED_FILE_PATH]/imported_code0.py:function1:16
print direction:forward,  current [file:function:line] -> [IMPORTED_FILE_PATH]/imported_code0.py:function2:21
-> call from function_in_base() function
print direction:backward, current [file:function:line] -> [IMPORTED_FILE_PATH]/imported_code1.py:function2:19
print direction:backward,  caller [file:function:line] -> [IMPORTED_FILE_PATH]/imported_code1.py:function1:12
print direction:backward, current [file:function:line] -> [IMPORTED_FILE_PATH]/imported_code1.py:function1:13
print direction:backward,  caller [file:function:line] -> [IMPORTED_FILE_PATH]/imported_code1.py:function0:5
print direction:backward, current [file:function:line] -> [IMPORTED_FILE_PATH]/imported_code1.py:function0:6
print direction:backward,  caller [file:function:line] -> base.py:function_in_base:5
```
