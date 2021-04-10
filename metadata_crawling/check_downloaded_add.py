"""This script is use to check the apk downloaded and compare it to the list of 2021"""

import os
import csv

apps_path = '/home/budi/adblocker_project/apps_list/2021'
add_list = '/home/budi/adblocker_project/metadata_crawling/add_list.txt'
failed_to_download = '/home/budi/adblocker_project/metadata_crawling/failed_to_download.txt'
app_not_in = '/home/budi/adblocker_project/metadata_crawling/app_not_in_list.txt'
paid_app='/home/budi/adblocker_project/metadata_crawling/paid_app.csv'

""""This part is use to find apps name based on the file downloaded in folder"""
downloaded_app_list =[]
for root,dirs,files in os.walk(apps_path):
    for i,file in enumerate(files):
        strip_file = file.rstrip('apk')
        strip_file = strip_file.rstrip('.')
        # print(i,strip_file)
        downloaded_app_list.append(strip_file)
# print(downloaded_app_list)


""""This part is used to compare apps in the list to the apps downloaded. The result is writen to failed to downloaded"""
failed_to_download_list =[]
addblocker_list=[]
with open(add_list,'r') as add_file:
    for item in add_file:
        addblocker_list.append(item.strip('\n'))
        if item.strip('\n') not in downloaded_app_list:
            # print(item)
            failed_to_download_list.append(item.strip('\n'))

with open(failed_to_download,'w') as failed_file:
    for item in failed_to_download_list:
        failed_file.write(item)
        # print('Apps failed to download '+item)


"""This part is use to compare number of apps in the list to apps downloaded
    some apps downloaded not in the apps list
"""
app_not_in_list = []
for item in downloaded_app_list:
    if item not in addblocker_list:
        app_not_in_list.append(item.strip('\n'))
        # print('Apps not in the list :'+item)

paid_app_list= []
with open (paid_app,'r') as paid_list:
    csv_data = csv.reader(paid_list,delimiter=';')
    next(csv_data,None)
    for item in csv_data:
        paid_app_list.append(item[1].strip('\n'))
        # print(item[1])

free_app_not_in_list = list(set(failed_to_download_list)-set(paid_app_list))
for item in free_app_not_in_list:
    print(item)

# print(paid_app_list)
# print(failed_to_download_list)
# print(len(failed_to_download_list))
# print(len(free_app_not_in_list))