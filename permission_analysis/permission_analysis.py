"""this script is use to get permission from MobSF result"""
import os
import json
import pandas as pd

result_path = '/home/budi/adblocker_project/adblocker_code/mobsf_analysis/mobsf_result/'
permission_path = '/home/budi/adblocker_project/adblocker_code/permission_analysis/'

folder_list =['2021','2019','2016']
# folder_list =['test']

for item in folder_list:
    folder_path = result_path+item+'/'
    for root,dirs,files in os.walk(folder_path):
        permission_peryear=[]
        for file in files:
            file_path = root+file
            with open (file_path,'r') as pf:
                perm_file = pf.read()
                json_data = json.loads(perm_file)
                json_perm = json_data['permissions']
                for line in json_perm:
                    status = json_perm[line]['status']
                    info = json_perm[line]['info']
                    perm_item = {'file_name':file,'permission':line,'status':status,'info':info}
                    permission_peryear.append(perm_item)
    
    df_perm = pd.DataFrame(permission_peryear)  
    csv_file = permission_path+'permission_'+item+'.csv'
    df_perm.to_csv(csv_file,index=False)