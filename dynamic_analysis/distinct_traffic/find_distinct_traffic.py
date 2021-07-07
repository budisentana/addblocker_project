import os
import json
import pandas as pd
import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

first_party_file = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/distinct_traffic/newlist.txt'
har_file_path = '/home/budi/adblocker_project/har_result/baseline.har'
sum_all = '/home/budi/symptom_checker/dynamic_analysis/sum_all.txt'

def find_traffic_on_har (file,har_file_path):
    conn_dict=[]
    with open (har_file_path) as rsf:
        data = rsf.read()
        json_data = json.loads(data)
        json_log = json_data['log']
        for item in json_log:
            json_item = json_log['entries']
            for sub_item in json_item:
                url = sub_item['request']['url']
                if 'http:'in url :
                    http = True
                else:
                    http = False
                if 'https:'in url :
                    https = True
                else:
                    https = False

                item_dict = {'app': file,'url':url,'http':http,'https':https}
                if item_dict not in conn_dict:
                    conn_dict.append(item_dict)
    return conn_dict


def listing_first_party(first_party_path):
    first_party_list =[]
    with open (first_party_path,'r') as fl:
        for line in fl:
            first_party_list.append(line.strip('\n'))
    return(first_party_list)

def remove_first_party_traffic(traffic_list,first_party_list):

    third_party_traffic_list=[]   
    for item in traffic_list:
        url=item['url']
        count = 0
        for keyword in first_party_list:
            if keyword in url:
                count+=1
        if count == 0:
            third_party_traffic_list.append(item)
    return(third_party_traffic_list)

def main():
    har_file = 'co.crystalapp.crystal'
    traffic_list = find_traffic_on_har(har_file,har_file_path)
    # for x,item in enumerate(traffic_list):
    #     print(x,item)

    first_party_list = listing_first_party(first_party_file)
    # for item in first_party_list:
    #     print(item)

    third_party_traffic = remove_first_party_traffic(traffic_list,first_party_list)
    for x,item in enumerate(third_party_traffic):
        print(x,item)

if __name__=='__main__':
    main()