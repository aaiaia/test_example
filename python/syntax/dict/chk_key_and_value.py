testDict = {
    'key_0':  'value of key_0',
    'key_1':  'value of key_1',
    'key_2':  'value of key_2',
    'key_3':  'value of key_3',
    'key_4':  'value of key_4',
    'key_5':  'value of key_5',
    'key_6':  'value of key_6',
    'key_7':  'value of key_7',
    'key_8':  'value of key_8',
    'key_9':  'value of key_9'
}

def main():
    print('<<< Check Dictional key and value using range() >>>')
    for _i in range(0, 15):
        _tmpKey = 'key_' + str(_i)
        if _tmpKey in testDict: print('testDict has key: \''+ _tmpKey +'\', value: ' + testDict[_tmpKey])
        else:                   print('testDict not has key: \''+ _tmpKey +'\'')
    print()

    print('<<< Check Dictional key and value using for statements >>>')
    for key, value in testDict.items():
        print('key: ' + key + ', item: ' + value)
    print()

if __name__ == '__main__':
    main()

