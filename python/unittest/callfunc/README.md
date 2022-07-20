# Command
## run unittest

`python3 -m unittest callfunc.py`

log
```bash
$ python3 -m unittest callfunc.py
<class 'callfunc.UnitTest_testModule1'> setUp
<class 'callfunc.UnitTest_testModule1'> test_function1
<class 'callfunc.changePath'> __init__
<class 'callfunc.dummyClass'> __init__
<class 'callfunc.changePath'> __del__
<class 'callfunc.dummyClass'> __del__
<class 'callfunc.UnitTest_testModule1'> tearDown
.<class 'callfunc.UnitTest_testModule1'> setUp
<class 'callfunc.UnitTest_testModule1'> test_function2
<class 'callfunc.UnitTest_testModule1'> tearDown
.<class 'callfunc.UnitTest_testModule2'> setUpClass
<class 'callfunc.UnitTest_testModule2'> setUp
<class 'callfunc.UnitTest_testModule2'> test_function1
<class 'callfunc.UnitTest_testModule2'> tearDown
.<class 'callfunc.UnitTest_testModule2'> setUp
<class 'callfunc.UnitTest_testModule2'> test_function2
<class 'callfunc.UnitTest_testModule2'> tearDown
.<class 'callfunc.UnitTest_testModule2'> tearDownClass

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

## run unittest with detail log
`python3 -m unittest -v callfunc.py`

log
```bash
$ python3 -m unittest -v callfunc.py
test_function1 (callfunc.UnitTest_testModule1) ... <class 'callfunc.UnitTest_testModule1'> setUp
<class 'callfunc.UnitTest_testModule1'> test_function1
<class 'callfunc.changePath'> __init__
<class 'callfunc.dummyClass'> __init__
<class 'callfunc.changePath'> __del__
<class 'callfunc.dummyClass'> __del__
<class 'callfunc.UnitTest_testModule1'> tearDown
ok
test_function2 (callfunc.UnitTest_testModule1) ... <class 'callfunc.UnitTest_testModule1'> setUp
<class 'callfunc.UnitTest_testModule1'> test_function2
<class 'callfunc.UnitTest_testModule1'> tearDown
ok
<class 'callfunc.UnitTest_testModule2'> setUpClass
test_function1 (callfunc.UnitTest_testModule2) ... <class 'callfunc.UnitTest_testModule2'> setUp
<class 'callfunc.UnitTest_testModule2'> test_function1
<class 'callfunc.UnitTest_testModule2'> tearDown
ok
test_function2 (callfunc.UnitTest_testModule2) ... <class 'callfunc.UnitTest_testModule2'> setUp
<class 'callfunc.UnitTest_testModule2'> test_function2
<class 'callfunc.UnitTest_testModule2'> tearDown
ok
<class 'callfunc.UnitTest_testModule2'> tearDownClass

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```
