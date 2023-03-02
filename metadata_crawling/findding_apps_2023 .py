"""
   Crawling apps metadata containing a certain keywords
   parsing parameter to metadata_scraper.js
    This is for 2023 apps
"""

import os
import json
import pandas as pd
import csv
import time
# import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt

res_path = '/home/budi/adblocker_project/adblocker_code/metadata_crawling/res_by_keyword_2023/'
csv_path = '/home/budi/adblocker_project/adblocker_code/metadata_crawling/add_metadata_2023.csv'
keyword = ['adblock','adsblock',"'ad block'","'ads block'"]
npm_path = '/home/budi/adblocker_project/adblocker_code/metadata_crawling/'

# for item in keyword:
#     print('Scraping apps metadata using keyword : '+item)
#     os.system('node '+ npm_path+'metadata_scraper.js'+' '+item +' '+res_path)

#     """"Read the first scrap result to find the similar apps"""
#     item = item.strip("''")
#     target_file_path = res_path+item+'.txt'
#     with open(target_file_path) as target:
#         target_data = target.read()
#         target_json = json.loads(target_data)
#         for target_item in target_json:
#             target_app_id = target_item['appId']
#             print ('Finding the similar apps to '+target_app_id)
#             os.system('node '+npm_path+'scrap_similar_app.js '+target_app_id+' '+res_path)

#     time.sleep(5)
"""Read JSON reasult from the scraper
    This part is use to created a raw list of 2023 apps based on keyword search as well as the similar apps
    The list resulted need to be manually filtered

"""
ad_dict=[]
for root, dirs, files in os.walk(res_path):
    for file in files:
        with open(res_path+file) as source_file:
            data= source_file.read()
            json_data = json.loads(data)
            for item in json_data:
                # print(item['appId'])
                item_dict = {'appId':item['appId'],'title':item['title'],'summary':item['summary']}
                if item_dict not in ad_dict:
                    ad_dict.append(item_dict)

# pd_res = pd.DataFrame(ad_dict)
for item in ad_dict:
    print(item['appId'],item['summary'])

csv_columns = ['appId','title','summary']
try:
    with open(csv_path, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in ad_dict:
            writer.writerow(data)
except IOError:
    print("I/O error")

