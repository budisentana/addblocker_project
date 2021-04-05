import os

data_path = '/home/budi/adblocker_project/adblocker_code/data_list/'
file_2021 = data_path+'2021_list.txt'
file_2019 = data_path+'2019_list.txt'
diff_file = '/home/budi/adblocker_project/adblocker_code/metadata_crawling/diff_2019_2021.txt'

list_2021=[]
with open(file_2021,"r") as file_2021_x:
    for item in file_2021_x:
        list_2021.append(item.strip('\n'))
        # print(item)
list_2019=[]
with open(file_2019,"r") as file_2019_x:
    for item in file_2019_x:
        list_2019.append(item.strip('\n'))
        # print(item)

diff = list(set(list_2019)-set(list_2021))
with open(diff_file,'w') as diff_file:
    for item in diff:
        item_strip = item.strip('apk')
        diff_file.write(item_strip.strip('.')+'\n')

"""Calculate the apps in additional list with the apk manage to downloaded"""
additional_path = '/home/budi/adblocker_project/apps_list/additional_app_2021/'
diff_additional_file =  '/home/budi/adblocker_project/adblocker_code/metadata_crawling/diff_failed_to_download.txt'

downloaded_file=[]
for root,dirs,files in os.walk(additional_path):
    for file in files:
        downloaded_file.append(file)

app_failed_to_download = list(set(diff)-set(downloaded_file))
with open(diff_additional_file,'w') as diff_file_failed:
    for item in app_failed_to_download:
        item_strip = item.rstrip('apk')
        diff_file_failed.write(item_strip.strip('.')+'\n')
        # diff_file_failed.write(item+'\n')
