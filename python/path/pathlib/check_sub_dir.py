from pathlib import Path

def main():
    _testPath = './examples'
    p = Path(_testPath )
    if p.exists():
        for child in p.iterdir():
            print('\'' + str(type(child)) + '\', path: \'' + './' + str(child) + '\'', end='')
            if child.is_dir():
                print('is_dir?: ' + str(child.is_dir()))
            elif child.is_file():
                print('is_file?: ' + str(child.is_file()))
            else:
                print('is unknown')
    else:
        print('error!!! \'' + _testPath + '\' is not exist')

if __name__ == '__main__':
    main()
