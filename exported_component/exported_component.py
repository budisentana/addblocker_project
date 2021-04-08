"""This script is use to find exported component from the result of MOBSF
    It shows the number of component as well as the number of exported component
"""

import os 
import json
import pandas as pd
import csv

result_path = '/home/budi/adblocker_project/adblocker_code/mobsf_analysis/mobsf_result/'
exported_path = '/home/budi/adblocker_project/adblocker_code/exported_component/'

# for root,dirs,files in os.walk(result_path):
#     for dir in dirs:
#         exported_component=[]
#         subfolder_path = root+dir+'/'
#         print(subfolder_path)
#         for rt,drs,fls in os.walk(subfolder_path):
#             for file in fls:
#                 file_path = rt+file
#                 # print(file_path)
#                 file_name = file.rstrip('.json')
#                 try:
#                     with open(file_path,'r') as ex_file:
#                         ex_data = ex_file.read()
#                         json_data = json.loads(ex_data)
#                         # file_name = json_data['file_name']        
#                         act = len(json_data['activities'])
#                         ex_act = json_data['exported_count']['exported_activities']
#                         serv = len(json_data['services'])
#                         ex_serv = json_data['exported_count']['exported_services']
#                         rec = len(json_data['receivers'])
#                         ex_rec = json_data['exported_count']['exported_receivers']
#                         prov = len(json_data['providers'])
#                         ex_prov = json_data['exported_count']['exported_providers']
#                         exp_count = {'file_name':file_name,'activities':act,'exp_act':ex_act,'services':serv,'exp_serv':ex_serv,\
#                             'receivers':rec,'exp_rec':ex_rec,'providers':prov,'exp_prov':ex_prov}
#                         # print(exp_count)
#                 except:
#                         exp_count = {'file_name':file_name,'activities':0,'exp_act':0,'services':0,'exp_serv':0,\
#                             'receivers':0,'exp_rec':0,'providers':0,'exp_prov':0}
#                 exported_component.append(exp_count)
#             exp_df = pd.DataFrame(exported_component)
#             print(exp_df)
#             csv_file = exported_path+'exported_component_'+dir+'.csv'
#             exp_df.to_csv(csv_file,index=False)

"""
    This part is use to find the percentage of exported component
"""
def zeroHandler():
    return 0

csv_result = ['2021','2019']
for item in csv_result:
    csv_file_peryear = exported_path+'exported_component_'+item+'.csv'
    percentage_peryear_path = exported_path+'percentage_exp_comp_'+item+'.csv'
    percentage_list=[]
    with open (csv_file_peryear,'r') as file_peryear:
        csv_reader = csv.reader(file_peryear)
        next(csv_reader,None)
        for line in csv_reader:    
            try:
                act_perc = round(((int(line[2])/int(line[1]))*100),2)
                serv_perc = round(((int(line[4])/int(line[3]))*100),2)
                rec_perc = round(((int(line[6])/int(line[5]))*100),2)
                prov_perc = round(((int(line[8])/int(line[7]))*100),2)
            except ZeroDivisionError:
                zeroHandler()
            percentage={'file_name':line[0],'activity_perc':act_perc,'service_perc':serv_perc,'receiver_perc':rec_perc,'provider_per':prov_perc}
            percentage_list.append(percentage)
    df_perc = pd.DataFrame(percentage_list)
    df_perc.to_csv(percentage_peryear_path,index=False)
    print(df_perc)