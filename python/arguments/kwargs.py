def target_func(
        arg_a,
        arg_b=None,
        arg_c=None,
        arg_d=None,
        arg_e=None,
        arg_f=None,
        arg_g=None
        ):
    print('<<< inserted arguments >>>')
    print('arg_a: ' + str(arg_a))
    print('arg_b: ' + str(arg_b))
    print('arg_c: ' + str(arg_c))
    print('arg_d: ' + str(arg_d))
    print('arg_e: ' + str(arg_e))
    print('arg_f: ' + str(arg_f))
    print('arg_g: ' + str(arg_g))

    #arg_a: essential_args
    arg_b = '' if arg_b is None else arg_b
    arg_c = '' if arg_c is None else arg_c
    arg_d = '' if arg_d is None else arg_d
    arg_e = '' if arg_e is None else arg_e
    arg_f = '' if arg_f is None else arg_f
    arg_g = '' if arg_g is None else arg_g

    print('<<< initialized arguments >>>')
    print('arg_a: ' + str(arg_a))
    print('arg_b: ' + str(arg_b))
    print('arg_c: ' + str(arg_c))
    print('arg_d: ' + str(arg_d))
    print('arg_e: ' + str(arg_e))
    print('arg_f: ' + str(arg_f))
    print('arg_g: ' + str(arg_g))

def wraper_func(arg_a, **kwargs):
    for keyword in kwargs:
        print('keyword: \'' + str(keyword) + '\', value: \'' + str(kwargs[keyword]) + '\'')

    target_func(arg_a, **kwargs)

def main():
    wraper_func(
        arg_a='123',
        arg_b=None,
        arg_c='456',
        arg_d=None,
        arg_e=None,
        arg_f='789',
        arg_g=None
            )

if __name__ == '__main__':
    main()
