from pathlib import Path

class testedClass():
    def __init__(self):
        pass
    
    def __del__(self):
        pass


def packageFunction(filePath=None):
    if filePath:
        _filePath = filePath
    else:
        _filePath = 'fileIsNeverExist.log'
    print('checking path: ' + _filePath)
    print('checking Path() function: ' + str(Path))
    if Path(_filePath).exists():
        print(_filePath + ' is exist')
    else:
        print(_filePath + ' is not exist!!!')

    print()

def main():
    packageFunction()

if __name__ == '__main__':
    main()
