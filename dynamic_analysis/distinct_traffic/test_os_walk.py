import os

test_path = '/home/budi/adblocker_project/har_result/har_result_all_normal'

for roots,dirs,files in os.walk(test_path,topdown=True):
    
    dirs.clear()
    for file in files:
        print(file)
