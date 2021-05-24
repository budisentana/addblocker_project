"""Create apk list based on the apk downloaded per year"""

import os



app_path = '/home/budi/adblocker_project/apps_list/'
dest_path = '/home/budi/adblocker_project/adblocker_code/data_list/'


for root,dirs,files in os.walk(app_path):
    for dir in dirs:
        print(dir)
        dir_path = app_path+dir
        file_name = dir+'_list.txt'
        file_name_manual = dir+'_list_manual.csv'
        file_path = dest_path+file_name
        file_path_manual = dest_path+file_name_manual
        apk_list=[]
        for rt,dr,fl in os.walk(dir_path):           
            for item_file in fl:
                apk_list.append(item_file)
        
        with open(file_path,'w') as apk_file:
            for item in apk_list:
                apk_file.write(item+'\n')

        """ This part is use to create csv file that will be modified manually 
            to define the category of each apps into browser or vpn
        """
        with open(file_path_manual,'w') as manual_file:
            for item in apk_list:
                manual_file.write(item+'\n')



all_year_list=[]
year_list=['2016','2019','2021']
for item in year_list:
    file_path = dest_path+item+'_list.txt'
    list_per_year=[]
    with open(file_path,'r') as fl:
        for line in fl:
            list_per_year.append(line.strip('\n'))
    all_year_list.append(list_per_year)

common_app=set.intersection(*[set(x) for x in all_year_list])

common_dest_path = dest_path+'common_list.txt'
with open (common_dest_path,'w') as cfl:
    for item in common_app:
        cfl.write(item+'\n')