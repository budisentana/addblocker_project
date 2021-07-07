from mitmproxy.io import FlowReader
from mitmproxy import http
import time
import os

# dump_path = '/home/budi/adblocker_project/mitm_result/baseline'
# parser_path = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/har_dump.py'
# har_path = '/home/budi/adblocker_project/har_result/baseline.har'

# dump_path = '/home/budi/adblocker_project/mitm_result/'
# parser_path = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/har_dump.py'
# har_path = '/home/budi/adblocker_project/har_result/'

# dump_path = '/home/budi/adblocker_project/mitm_result_aggresive/'
# parser_path = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/har_dump.py'
# har_path = '/home/budi/adblocker_project/har_result_aggresive/'

# dump_path = '/home/budi/adblocker_project/mitm_result_samsung_pluggin/'
# parser_path = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/har_dump.py'
# har_path = '/home/budi/adblocker_project/har_result_samsung_pluggin/'

# dump_path = '/home/budi/adblocker_project/mitm_result_general_pluggin/'
# parser_path = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/har_dump.py'
# har_path = '/home/budi/adblocker_project/har_result_general_pluggin/'

# dump_path = '/home/budi/adblocker_project/mitm_result_dolphin_pluggin/'
# parser_path = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/har_dump.py'
# har_path = '/home/budi/adblocker_project/mitm_result_dolphin_pluggin/'


dump_path = '/home/budi/adblocker_project/mitm_result/baseline'
parser_path = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/har_dump.py'
har_path = '/home/budi/adblocker_project/har_result/baseline'


def har_parser(dump_path,parser_path,har_path):
    parse_cmd = 'mitmdump -n -r '+dump_path+ ' -s ' +parser_path +' --set hardump='+har_path
    os.system(parse_cmd)


def main():
    # # har_parser(dump_path,parser_path,har_path)
    # har_parser(dump_path,parser_path,har_path)
    global har_path
    for root,dirs,files in os.walk(dump_path):
        for dir in dirs:
            dir_dump_path = root+dir
            dir_har_path = har_path+dir
            # print(dir_har_path)
            # print(dir_dump_path)
            for rt,dr,fls in os.walk(dir_dump_path):
                for fl in fls:
                    file_har_path = dir_har_path+'/'+fl
                    file_dump_path = dir_dump_path+'/'+fl
                    # print(file_har_path)
                    # print(file_dump_path)
                    har_parser(file_dump_path,parser_path,file_har_path)
                    print (file_har_path+ ' >>>>> Converstion Finish ------------------------------------------')
                    time.sleep(3)

if __name__ == '__main__':
    main()

