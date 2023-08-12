class Test:
    def __init__(self):
        self.attr_0 = 'value of attr_0'
        self.attr_1 = 'value of attr_1'
        self.attr_2 = 'value of attr_2'
        self.attr_3 = 'value of attr_3'
        self.attr_4 = 'value of attr_4'
        self.attr_5 = 'value of attr_5'
        self.attr_6 = 'value of attr_6'
        self.attr_7 = 'value of attr_7'
        self.attr_8 = 'value of attr_8'
        self.attr_9 = 'value of attr_9'
        print('constructor')
    def __del__(self):
        print('destructor')
        print('exit')

def main():
    global testClass
    testClass = Test()
    print('')

    print('<<< Attribue check in for statements >>>')
    for _i in range(0, 15):
        _checkAttr = 'attr_' + str(_i)
        if hasattr(testClass, _checkAttr):  print('testClass has attribute \'' + _checkAttr + '\'')
        else:                               print('testClass not has attribute \'' + _checkAttr + '\'')
    print('')

    print('<<< Attribute check manually >>>')
    if hasattr(testClass, 'attr_0'):    print('testClass.attr_0: ' + testClass.attr_0)
    else:                               print('testClass not has attribute \'attr_0\'')
    if hasattr(testClass, 'attr_1'):    print('testClass.attr_1: ' + testClass.attr_1)
    else:                               print('testClass not has attribute \'attr_1\'')
    if hasattr(testClass, 'attr_2'):    print('testClass.attr_2: ' + testClass.attr_2)
    else:                               print('testClass not has attribute \'attr_2\'')
    if hasattr(testClass, 'attr_3'):    print('testClass.attr_3: ' + testClass.attr_3)
    else:                               print('testClass not has attribute \'attr_3\'')
    if hasattr(testClass, 'attr_4'):    print('testClass.attr_4: ' + testClass.attr_4)
    else:                               print('testClass not has attribute \'attr_4\'')
    if hasattr(testClass, 'attr_5'):    print('testClass.attr_5: ' + testClass.attr_5)
    else:                               print('testClass not has attribute \'attr_5\'')
    if hasattr(testClass, 'attr_6'):    print('testClass.attr_6: ' + testClass.attr_6)
    else:                               print('testClass not has attribute \'attr_6\'')
    if hasattr(testClass, 'attr_7'):    print('testClass.attr_7: ' + testClass.attr_7)
    else:                               print('testClass not has attribute \'attr_7\'')
    if hasattr(testClass, 'attr_8'):    print('testClass.attr_8: ' + testClass.attr_8)
    else:                               print('testClass not has attribute \'attr_8\'')
    if hasattr(testClass, 'attr_9'):    print('testClass.attr_9: ' + testClass.attr_9)
    else:                               print('testClass not has attribute \'attr_9\'')
    if hasattr(testClass, 'attr_10'):   print('testClass.attr_10: ' + testClass.attr_10)
    else:                               print('testClass not has attribute \'attr_10\'')
    if hasattr(testClass, 'attr_11'):   print('testClass.attr_11: ' + testClass.attr_11)
    else:                               print('testClass not has attribute \'attr_11\'')
    if hasattr(testClass, 'attr_12'):   print('testClass.attr_12: ' + testClass.attr_12)
    else:                               print('testClass not has attribute \'attr_12\'')
    print('')

if __name__ == '__main__':
    main()

