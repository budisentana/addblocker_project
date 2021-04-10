"""This script is use to find anti analysis technique from the result of MOBSF
"""

import os 
import json
import pandas as pd
import csv

result_path = '/home/budi/adblocker_project/adblocker_code/mobsf_analysis/mobsf_result/'
package_path = '/home/budi/adblocker_project/adblocker_code/package_analysis/'

for root,dirs,files in os.walk(result_path):
    for dir in dirs:
        package_peryear=[]
        subfolder_path = root+dir+'/'
        print(subfolder_path)
        for rt,drs,fls in os.walk(subfolder_path):
            for file in fls:
                file_path = rt+file
                print(file_path)
                file_name = file.rstrip('.json')
                with open(file_path,'r') as pkg_file:
                    pkg_data = pkg_file.read()
                    json_data = json.loads(pkg_data)
                    pkg_key =  json_data['apkid']
                    try:
                        for line in pkg_key:
                            # print(line) 
                            for item in json_data['apkid'][line]:
                                class_name = line
                                pkg_comp = item
                                detail = json_data['apkid'][line][item]
                                # print(file_name,line,item,json_data['apkid'][line][item])                       
                                package_item = {'file_name':file_name,'class_name':class_name,'package_component':pkg_comp,'detail':detail}
                                package_peryear.append(package_item)
                    except:
                        pass

            pkg_df = pd.DataFrame(package_peryear)
            print(pkg_df)
            csv_file = package_path+'package_'+dir+'.csv'
            pkg_df.to_csv(csv_file,index=False)

# """
#     This part is use to find the percentage of exported component
# """
# def zeroHandler():
#     return 0

# csv_result = ['2021','2019']
# for item in csv_result:
#     csv_file_peryear = exported_path+'exported_component_'+item+'.csv'
#     percentage_peryear_path = exported_path+'percentage_exp_comp_'+item+'.csv'
#     percentage_list=[]
#     with open (csv_file_peryear,'r') as file_peryear:
#         csv_reader = csv.reader(file_peryear)
#         next(csv_reader,None)
#         for line in csv_reader:    
#             try:
#                 act_perc = round(((int(line[2])/int(line[1]))*100),2)
#                 serv_perc = round(((int(line[4])/int(line[3]))*100),2)
#                 rec_perc = round(((int(line[6])/int(line[5]))*100),2)
#                 prov_perc = round(((int(line[8])/int(line[7]))*100),2)
#             except ZeroDivisionError:
#                 zeroHandler()
#             percentage={'file_name':line[0],'activity_perc':act_perc,'service_perc':serv_perc,'receiver_perc':rec_perc,'provider_per':prov_perc}
#             percentage_list.append(percentage)
#     df_perc = pd.DataFrame(percentage_list)
#     df_perc.to_csv(percentage_peryear_path,index=False)
#     print(df_perc)