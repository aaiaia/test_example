def yield_func():
    print('execute step 1')
    yield 'execute result of step 1'
    print('execute step 2')
    yield 'execute result of step 2'
    print('execute step 3')
    yield 'execute result of step 3'

def main():
    print('==============================')
    print('[info] yield_func(): ', end='')
    print(yield_func())

    print('==============================')
    for _yield in yield_func():
        print(_yield)

    print('==============================')
    _yield_func0 = yield_func()
    _yield_func1 = yield_func()

    print(next(_yield_func0))
    print(next(_yield_func1))
    print(next(_yield_func0))
    print(next(_yield_func1))
    print(next(_yield_func0))
    print(next(_yield_func1))
    # StopIteration
    print(next(_yield_func0))  # Error, iteration of _yield_func0 is stopped!!!
    print(next(_yield_func1))  # Error, iteration of _yield_func1 is stopped!!!
    print(next(_yield_func0))
    print(next(_yield_func1))
    print(next(_yield_func0))
    print(next(_yield_func1))
    print('==============================')

if __name__ == '__main__':
    main()
