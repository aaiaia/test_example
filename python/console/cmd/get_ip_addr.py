# for system
import sys
import time
# for run console commands
import subprocess
# for Debugging
import getopt

def parseIpAddr(cmd_msg:str) -> (dict):
    __cmd_list = cmd_msg.split('\n--\n')
    __ipAddr = {}

    for __cmd in __cmd_list:
        print(__cmd)
        __charLoc = __cmd.find(':')
        __eth = __cmd[:__charLoc]

        __charLoc = __cmd.find('inet ') + 5
        __ip = __cmd[__charLoc:]
        __ip = __ip[:__ip.find(' ')]
        print('name:' + __eth + ', ' + 'ip:' + __ip)

        __ipAddr[__eth] = __ip

    print('>> __cmd_list')
    print(__cmd_list)

    return __ipAddr

def dropIp(ipInfo:dict, keys:list = []) -> (dict):
    if keys != []:
        for __key, __value in ipInfo:
            print('key:' + __key)
            print('value:' + __value)
    else:
        pass
    return ipInfo

def getIpAddr(dropEth:list] = []) -> (dict, str):
    __ipInfo = {}
    __cmd_sts = 0
    __cmd_msg = ''

    __cmd_sts, __cmd_msg = subprocess.getstatusoutput('ifconfig | grep -w inet -B 1')
    if __cmd_sts == 0:  # command has no error
        __ipInfo = parseIpAddr(__cmd_msg)
        __ipInfo = dropIp(__ipinfo, ['dummy'])
    else:  # command has error
        __cmd_msg.replace('\n', '; ')
    return __ipInfo, __cmd_msg

def main(argv):
    print(argv)
    HELP_MSG = '--help, --example=[STRING], --test'

    _funcName = sys._getframe(0).f_code.co_name
    print(_funcName + ' in ' + __name__ + ' is start')

    # Define local variables
    __example = ''

    __ipInfo = {}
    __cmdMsg = ''

    try:
        # opts: getopt 옵션에 따라 파싱 ex) [('-i', 'myinstancce1')]
        # etc_args: getopt 옵션 이외에 입력된 일반 Argument
        # argv 첫번째(index:0)는 파일명, 두번째(index:1)부터 Arguments
        opts, etc_args = getopt.getopt(argv[1:], \
            "he:l:", ["help", "example=", "test"])
    except getopt.GetoptError as e: # 옵션지정이 올바르지 않은 경우
        print(e)
        print(HELP_MSG)
        sys.exit(2)

    for opt, arg in opts: # 옵션이 파싱된 경우
        if opt in ("-h", "--help"): # HELP 요청인 경우 사용법 출력
            print(HELP_MSG)
            sys.exit(2)
        elif opt in ("-e", "--example"):
            __example = arg
            print('set __example: ' + __example)
        elif opt in ("-l", "--test"):
            print('--test option is detected!')

    # Implements
    __ipInfo, __cmdMsg = getIpAddr()

    print('>> about ipInfo', end=':')
    print(type(__ipInfo), end=':')
    print(__ipInfo,)

    print('>> debug message')
    print(__cmdMsg)

    print(_funcName + ' in ' + __name__ + ' is end')

if __name__ == '__main__':
    main(sys.argv)

