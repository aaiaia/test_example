# Command
## run unittest

`python3 -m unittest callfunc.py`

log
```bash
$ python3 -m unittest callfunc.py
<class 'callfunc.changePath'> __init__
<class 'callfunc.dummyClass'> __init__
<class 'callfunc.changePath'> __del__
<class 'callfunc.dummyClass'> __del__
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

## run unittest with detail log
`python3 -m unittest -v callfunc.py`

log
```bash
$ python3 -m unittest -v callfunc.py
test_function1 (callfunc.UnitTest_testModule1) ... <class 'callfunc.changePath'> __init__
<class 'callfunc.dummyClass'> __init__
<class 'callfunc.changePath'> __del__
<class 'callfunc.dummyClass'> __del__
ok
test_function2 (callfunc.UnitTest_testModule1) ... ok
test_function1 (callfunc.UnitTest_testModule2) ... ok
test_function2 (callfunc.UnitTest_testModule2) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```
