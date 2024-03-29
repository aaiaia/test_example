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

    print('>> parsing process')
    for __cmd in __cmd_list:
        __charLoc = __cmd.find(':')
        __eth = __cmd[:__charLoc]

        __charLoc = __cmd.find('inet ') + 5
        __ip = __cmd[__charLoc:]
        __ip = __ip[:__ip.find(' ')]
        print('eth:' + __eth + ', ' + 'ip:' + __ip)

        __ipAddr[__eth] = __ip

    return __ipAddr

def dropIpUsingSimilarKeys(ipInfo:dict, targetKeys:list = []) -> (dict):
    __foundKeys = []
    if targetKeys != []:
        for __targetKey in targetKeys:
            for __ipInfoKey in ipInfo.keys():
                if __targetKey in __ipInfoKey:
                    print('\'' + __ipInfoKey + '\' is similar with \'' + __targetKey + '\'')
                    __foundKeys.append(__ipInfoKey)
    else:
        print('keys is blank list!!!')

    for __foundKey in __foundKeys:
        print('removed key:' + __foundKey + ' and value:' + ipInfo[__foundKey])
        del ipInfo[__foundKey]
    return ipInfo

def getIpAddr(dropEthKeyList:list = []) -> (dict, str):
    __cmd_run = 'ifconfig | grep -w inet -B 1'

    __ipInfo = {}
    __cmd_sts = 0
    __cmd_msg = ''

    __cmd_sts, __cmd_msg = subprocess.getstatusoutput(__cmd_run)
    print('>> run command: \'' + __cmd_run + '\'')
    print(__cmd_msg)
    if __cmd_sts == 0:  # command has no error
        __ipInfo = parseIpAddr(__cmd_msg)
        print('>> parsed command message')
        print(__ipInfo)
        __ipInfo = dropIpUsingSimilarKeys(__ipInfo, dropEthKeyList)
        print('>> dropped ips')
        print(__ipInfo)
    else:  # command has error
        __cmd_msg.replace('\n', '; ')
    return __ipInfo, __cmd_msg

def main(argv):
    print(argv)
    HELP_MSG = '--help, --eliminates=[STRING,STRING,...STRING], --test'

    _funcName = sys._getframe(0).f_code.co_name
    print(_funcName + ' in ' + __name__ + ' is start')

    # Define local variables
    __elimenates = ''

    __ipInfo = {}
    __cmdMsg = ''
    __dropEthKeyList = ['lo', 'docker', 'vpn']

    try:
        # opts: getopt 옵션에 따라 파싱 ex) [('-i', 'myinstancce1')]
        # etc_args: getopt 옵션 이외에 입력된 일반 Argument
        # argv 첫번째(index:0)는 파일명, 두번째(index:1)부터 Arguments
        opts, etc_args = getopt.getopt(argv[1:], \
            "he:l:", ["help", "eliminates=", "test"])
    except getopt.GetoptError as e: # 옵션지정이 올바르지 않은 경우
        print(e)
        print(HELP_MSG)
        sys.exit(2)

    for opt, arg in opts: # 옵션이 파싱된 경우
        if opt in ("-h", "--help"): # HELP 요청인 경우 사용법 출력
            print(HELP_MSG)
            sys.exit(2)
        elif opt in ("-e", "--eliminates"):
            __elimenates = arg
            print('set __elimenates: ' + __elimenates)
        elif opt in ("-l", "--test"):
            print('--test option is detected!')

    # option settings
    if __elimenates != '':
        __dropEthKeyList = __elimenates.split(',')
        print('set __dropEthKeyList:' + str(__dropEthKeyList))

    # Implements
    __ipInfo, __cmdMsg = getIpAddr(__dropEthKeyList)

    print('>> about ipInfo', end=':')
    print(type(__ipInfo), end=':')
    print(__ipInfo)

    print('>> command message')
    print(__cmdMsg)

    print(_funcName + ' in ' + __name__ + ' is end')

if __name__ == '__main__':
    main(sys.argv)

