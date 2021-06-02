from mitmproxy.io import FlowReader
from mitmproxy import http


# filename = '/home/budi/adblocker_project/mitm_result/baseline'
filename = '/home/budi/adblocker_project/mitm_result/2021/com.androidbull.incognito.browser'

# with open(filename, 'rb') as fp:
#     reader = FlowReader(fp)
#     http_reader = http.HTTPRequest(fp)
    
#     flows = reader.stream()
#     print(len(flows))
#     # for flow in flows:
#     #     print(flow[0]) 
       
#     for item in http_reader:
#         print(item)    

import os

dump_path = '/home/budi/adblocker_project/mitm_result/baseline'
parser_path = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/har_dump.py'
har_path = '/home/budi/adblocker_project/har_result/baseline.har'

def har_parser(dump_path,parser_path,har_path):
    parse_cmd = 'mitmdump -n -r '+dump_path+ ' -s ' +parser_path +' --set hardump='+har_path
    os.system(parse_cmd)


def main():
    # har_parser(dump_path,parser_path,har_path)
    har_parser(dump_path,parser_path,har_path)

if __name__ == '__main__':
    main()

