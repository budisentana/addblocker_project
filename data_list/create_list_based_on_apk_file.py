"""Create apk list based on the apk downloaded per year"""

import os



app_path = '/home/budi/adblocker_project/apps_list/'
dest_path = '/home/budi/adblocker_project/adblocker_code/data_list/'


for root,dirs,files in os.walk(app_path):
    for dir in dirs:
        print(dir)
        dir_path = app_path+dir
        file_name = dir+'_list.txt'
        file_path = dest_path+file_name
        apk_list=[]
        for rt,dr,fl in os.walk(dir_path):           
            for item_file in fl:
                apk_list.append(item_file)
        
        with open(file_path,'w') as apk_file:
            for item in apk_list:
                apk_file.write(item+'\n')
