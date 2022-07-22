# Run
## Command
`python3 ./example_yield.py`


## Console
```bash
$ python3 ./example_yield.py
==============================
[info] yield_func(): <generator object yield_func at 0x7f68c6db6c10>
==============================
execute step 1
execute result of step 1
execute step 2
execute result of step 2
execute step 3
execute result of step 3
==============================
execute step 1
execute result of step 1
execute step 1
execute result of step 1
execute step 2
execute result of step 2
execute step 2
execute result of step 2
execute step 3
execute result of step 3
execute step 3
execute result of step 3
Traceback (most recent call last):
  File "./example_yield.py", line 38, in <module>
    main()
  File "./example_yield.py", line 29, in main
    print(next(_yield_func0))  # Error, iteration of _yield_func0 is stopped!!!
StopIteration
```
