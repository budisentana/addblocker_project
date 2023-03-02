import os
import json
import pandas as pd
import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from tld import get_fld,get_tld

"""Baseline traffic"""
# first_party_file = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/distinct_traffic/newlist.txt'
# third_party_traffic_file = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/distinct_traffic/All_apps/baseline.csv'
har_file_path = '/home/budi/adblocker_project/har_result/har_result_all_normal/baseline/baseline10'

"""Pluggin Browser --> Samsung"""
# first_party_file = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/distinct_traffic/newlist.txt'
# third_party_traffic_path = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/distinct_traffic/plugin/plugin_browser/plugin_browser_samsung/'
# har_file_path = '/home/budi/adblocker_project/har_result/har_result_samsung_pluggin'

har_path = '/home/budi/adblocker_project/har_result'
# har_path = '/home/budi/adblocker_project/har_result/har_result_samsung_pluggin'
domain_path = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/distinct_traffic'
first_party_file = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/distinct_traffic/newlist.txt'

def find_traffic_on_har (har_file_path):
    fld_list=[]
    netloc_list=[]
    with open (har_file_path) as rsf:
        data = rsf.read()
        json_data = json.loads(data)
        json_log = json_data['log']
        for item in json_log:
            json_item = json_log['entries']
            for sub_item in json_item:
                url_ori = sub_item['request']['url']
                try:
                    res_tld = get_tld(url_ori,as_object=True)
                    # fld_item = {'app_id':file,'first_level_domain':res_tld.fld}
                    # netloc_item = {'app_id':file,'first_level_domain':res_tld.parsed_url.netloc}
                    fld_item = res_tld.fld
                    netloc_item = res_tld.parsed_url.netloc

                    if fld_item not in fld_list:
                        fld_list.append(fld_item)
                    if netloc_item not in netloc_list:
                        netloc_list.append(netloc_item)
                except:
                    pass
    return fld_list,netloc_list


def listing_first_party(first_party_path):
    first_party_list =[]
    with open (first_party_path,'r') as fl:
        for line in fl:
            first_party_list.append(line.strip())
    return(first_party_list)

def remove_first_party_traffic(fld,netloc,first_party_list):

    third_party_fld_list=[]
    third_party_netloc_list=[]   
    for item in fld:
        # url=item['first_level_domain']
        url=item
        count=0
        for keyword in first_party_list:
            
            if keyword.strip() in url:
                count+=1
        if count==0 and url not in third_party_fld_list:
            third_party_fld_list.append(url)

    for item in netloc:
        # url=item['first_level_domain']
        url=item
        count=0
        for keyword in first_party_list:
            
            if keyword.strip() in url:
                count+=1
        if count==0 and url not in third_party_netloc_list:
            third_party_netloc_list.append(url)

    return third_party_fld_list,third_party_netloc_list

def write_traffic_to_file(file_name,new_dir,fld,netloc):
    fld_list=[]
    netloc_list=[]
    write_fld = new_dir+'/'+file_name+'_fld.csv'
    write_netloc =  new_dir+'/'+file_name+'_netloc.csv'
    print(write_netloc)
    for item in fld:
        fld_list.append({'app_id':file_name,'first_level_domain':item})
    
    for item in netloc:
        netloc_list.append({'app_id':file_name,'netloc':item})
    
    df_fld = pd.DataFrame(fld_list)           
    df_fld.to_csv(write_fld)

    df_netloc = pd.DataFrame(netloc_list)           
    df_netloc.to_csv(write_netloc)
 
def dir_creator(har_path, dir_path,new_parent_path):
    new_path = dir_path.replace(har_path,new_parent_path)
    new_path = new_path.replace('har','domain')
    print(new_path)
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    return new_path

def main():
    first_party_list = listing_first_party(first_party_file)

    for roots,dirs,files in os.walk(har_path):
        for dir in dirs:
            # print(roots+'/'+dir)
            dir_path = roots+'/'+dir
            new_dir = dir_creator(har_path,dir_path,domain_path)
            for rt,drs,fls in os.walk(dir_path,topdown=True):
                drs.clear()
                for fl in fls:
                    har_file_path=rt+'/'+fl
                    # print(har_file_path)
                    fld_list,netloc_list = find_traffic_on_har(har_file_path)
                    third_party_fld,third_party_netloc = remove_first_party_traffic(fld_list,netloc_list,first_party_list)
                    write_traffic_to_file(fl,new_dir,third_party_fld,third_party_netloc)

        # for fl in files:
        #     print(roots+'/'+fl)

    # har_file = 'baseline'
    # fld_list,netloc_list = find_traffic_on_har(har_file_path)
    # # print(netloc_list)
    # print(len(netloc_list))
    # first_party_list = listing_first_party(first_party_file)
    # # for item in first_party_list:
    # #     print(item)

    # third_party_fld,third_party_netloc = remove_first_party_traffic(fld_list,netloc_list,first_party_list)
    
    # for x,item in enumerate(third_party_fld):
    #     print(x,item)

    # # for x,item in enumerate(traffic_list):
    # #     print(x,item)

    # first_party_list = listing_first_party(first_party_file)
    # # for item in first_party_list:
    # #     print(item)

    # third_party_traffic = remove_first_party_traffic(traffic_list,first_party_list)
    # # for x,item in enumerate(third_party_traffic):
    # #     print(x,item)
    # write_traffic_to_file(third_party_traffic,third_party_traffic_file)

if __name__=='__main__':
    main()