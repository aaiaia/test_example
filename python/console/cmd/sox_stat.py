# for system
import sys
import time
# for run console commands
import subprocess
# for Debugging
import getopt

def parseSoX_stat(cmd_msg:str) -> (float, int):
    _cmd_list = cmd_msg.split('\n')
    _rms_amplitude = 0.0
    _rough_frequency = 0
    """ just test codes start """
    """
    for __i, __cmd in enumerate(_cmd_list):
        __charLoc = -1
        print('line#' + str(__i) + ':' + __cmd, end='->')
        if('\r' in __cmd):
            print('it has return char!!!')
        elif('\n' in __cmd):
            print('it has line feed char!!!')
        elif('\t' in __cmd):
            print('it has tab sapce char!!!')
        else:
            print('it not has any special char!!!')
    """
    """ just test codes end """
    __s_time = time.time()
    for __cmd in _cmd_list:
        __charLoc = __cmd.rfind(' ') + 1
        if('RMS' in __cmd and 'amplitude' in __cmd):
            print(__cmd + ' => ' + __cmd[__charLoc:])
            _rms_amplitude = float(__cmd[__charLoc:])
            continue
        elif('Rough' in __cmd and 'frequency' in __cmd):
            _rough_frequency = int(__cmd[__charLoc:])
            print(__cmd + ' => ' + __cmd[__charLoc:])
            continue
    __e_time = time.time()
    print('time: ' + str((__e_time - __s_time) * 1000) + 'ms')
    """
    print(_rms_amplitude)
    print(_rough_frequency)
    """

    return _rms_amplitude, _rough_frequency

def main(argv):
    print(argv)
    HELP_MSG = '--help, --file=[STRING], --test'

    _funcName = sys._getframe(0).f_code.co_name
    print(_funcName + ' in ' + __name__ + ' is start')

    # Define local variables
    __file = ''

    # Define hidden variables
    __rms_amplitude = 0.0
    __rough_frequency = 0

    try:
        # opts: getopt 옵션에 따라 파싱 ex) [('-i', 'myinstancce1')]
        # etc_args: getopt 옵션 이외에 입력된 일반 Argument
        # argv 첫번째(index:0)는 파일명, 두번째(index:1)부터 Arguments
        opts, etc_args = getopt.getopt(argv[1:], \
            "hf:l:", ["help", "file=", "test"])
    except getopt.GetoptError as e: # 옵션지정이 올바르지 않은 경우
        print(e)
        print(HELP_MSG)
        sys.exit(2)

    for opt, arg in opts: # 옵션이 파싱된 경우
        if opt in ("-h", "--help"): # HELP 요청인 경우 사용법 출력
            print(HELP_MSG)
            sys.exit(2)
        elif opt in ("-f", "--file"):
            __file = arg
            print('set __file: ' + __file)
        elif opt in ("-l", "--test"):
            print('--test option is detected!')

    # Implements
    if __file != '':
        print('__file: ' + __file)
    else:
        print('__file is blank!')

    _cmd_sts, _cmd_msg = subprocess.getstatusoutput('sox ' + __file + ' -n stat')
    if _cmd_sts == 0:  # command has no error
        print(_cmd_msg)
        __rms_amplitude, __rough_frequency = parseSoX_stat(_cmd_msg)
    else:  # command has error
        print('command return: ' + str(_cmd_sts))
        print(_cmd_msg.replace('\n', '; '))

    print('aboud rms_amplitude', end=':')
    print(type(__rms_amplitude), end=':')
    print(__rms_amplitude)

    print('aboud rough_frequency: ', end=':')
    print(type(__rough_frequency), end=':')
    print(__rough_frequency)

    print(_funcName + ' in ' + __name__ + ' is end')

if __name__ == '__main__':
    main(sys.argv)

