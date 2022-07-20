# Command
## run
`python3 -m unittest swap_func.py`

```bash
$ python3 -m unittest swap_func.py
<class 'swap_func.Test_changeFunction0'> test_0000_PathLibMockingUsingPatch_notExist
checking path: fileIsNeverExist.log
checking Path() function: <MagicMock name='Path' id='139636934424848'>
fileIsNeverExist.log is not exist!!!

.<class 'swap_func.Test_changeFunction0'> test_0001_PathLibMockingUsingPatch_exist
checking path: mockingFileLoc.log
checking Path() function: <MagicMock name='Path' id='139636934516640'>
mockingFileLoc.log is exist

.<class 'swap_func.Test_changeFunction1'> test_0000_PathLibMockingUsingPatch_notExist
checking path: fileIsNeverExist.log
checking Path() function: <MagicMock name='Path' id='139636934547536'>
fileIsNeverExist.log is not exist!!!

.<class 'swap_func.Test_changeFunction1'> test_0001_PathLibMockingUsingPatch_exist
checking path: mockingFileLoc.log
checking Path() function: <MagicMock name='Path' id='139636934579584'>
mockingFileLoc.log is exist

.
----------------------------------------------------------------------
Ran 4 tests in 0.003s

OK
```
