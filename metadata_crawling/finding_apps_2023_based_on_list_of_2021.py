"""""This part is use to crawled the metadata based on the apps list of 2021
    The result return the list that still available in 2023 and 
    the list that already remove from google play store in 2023
"""
from distutils.log import error
import os
import json
import pandas as pd
import csv
import time

npm_path = '/home/budi/adblocker_project/adblocker_code/metadata_crawling/'
app_list_2021 = '/home/budi/adblocker_project/adblocker_code/data_list/2021_list.txt'
metadata_2023 = '/home/budi/adblocker_project/adblocker_code/metadata_crawling/metadata_2023_based_on_2021/'
list_metadata = '/home/budi/adblocker_project/adblocker_code/metadata_crawling/metadata_2023_based_on_2021_list.csv'
list_failed_to_scrap = '/home/budi/adblocker_project/adblocker_code/metadata_crawling/failed_to_scrap_in_2023_based_on_2021_list.csv'
managed_to_scrap_list=[]
failed_to_scrap_list=[]

with open(app_list_2021,'r') as app_id:
    for item in app_id:
        item_id = item.rstrip('apk\n')
        item_id = item_id.rstrip('.')
        result_path = metadata_2023+item_id
        try:
            print('Scraping apps metadata Per Id : '+item_id )
            os.system('node '+npm_path+'metadata_scraper_per_id_update.js '+item_id+ ' ' + result_path)
            managed_to_scrap_list.append(item_id)
        except error as e:
            print('app id not found')
            failed_to_scrap_list.append(item_id)

print('Done for web scrapping')
time.sleep(5)

"""Read JSON reasult from the scrape result folder"""
metadata = []
for item in managed_to_scrap_list:
    app_path = metadata_2023+item+'.txt'
    print(app_path)
    try:
        with open(app_path,'r') as app_metadata:
            data=app_metadata.read()
            json_data = json.loads(data)
            item_dict = {'appId':json_data['appId'],'install':json_data['installs'],#'score': json_data['score'],
            'genre':json_data['genre'],'price':json_data['price'],
            'currency':json_data['currency'],'free':json_data['free'],'title':json_data['title'],'summary':json_data['summary']}
            metadata.append(item_dict)
    except IOError:
        print(IOError)        

failed_to_scrap_df = pd.DataFrame(failed_to_scrap_list)
failed_to_scrap_df.to_csv(list_failed_to_scrap,sep=';')
metadata_df = pd.DataFrame(metadata)
metadata_df.to_csv(list_metadata,sep=';')
