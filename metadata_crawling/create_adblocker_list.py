import os
import pandas as pd
import csv

scrap_path = '/home/budi/adblocker_project/metadata_crawling/filtered2_add_metadata.csv'
add_list = '/home/budi/adblocker_project/metadata_crawling/add_list.txt'

pd_data = pd.read_csv(scrap_path,usecols=['appId'])
print(pd_data)

pd_data.to_csv(add_list,header=None, index=None)