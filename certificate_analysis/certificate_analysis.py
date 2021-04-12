import os
import json
import pandas as pd

apps_path = '/home/budi/adblocker_project/apps_list/'
certificate_path = '/home/budi/adblocker_project/adblocker_code/certificate_analysis/'
cert_res_path = 'keytool_result/'

folder_list =['2021','2019','2016']
# folder_list =['test']


for item in folder_list:
    folder_path = apps_path+item+'/'
    for root,folder,files in os.walk(folder_path):       
        for file in files:
            apk_name = root+file
            res_name = certificate_path+cert_res_path+item+'/'+file+'.txt'
            print(res_name)
            os.system('keytool -printcert -jarfile '+apk_name+'>'+res_name )


for item in folder_list:
    folder_path = certificate_path+cert_res_path+item+'/'
    cert_peryear=[]
    for root,folder,files in os.walk(folder_path):
        for file in files:
            file_dir = root+file
            print(file_dir) 
            with open(file_dir,'r') as file_name: 
                signature = '' 
                key_length = ''
                for line in file_name:
                    if 'Signature algorithm' in line:
                        signature = line.lstrip('Signature algorithm name ')
                        signature = signature.lstrip(':')
                        signature = signature.replace('with', ' + ').strip('\n')
                    if 'Public Key' in line:
                        key_length = line.lstrip('Subject Public Key Algorithm')
                        key_length = key_length.lstrip(':')
                        # key_length = key_length.replace('-bit RSA key','').strip('\n')
                cert_item_list = {'file_name':file,'signature':signature,'key_length':key_length}
                cert_peryear.append(cert_item_list)

    df_cert = pd.DataFrame(cert_peryear)  
    csv_file = certificate_path+'certificate_'+item+'.csv'
    df_cert.to_csv(csv_file,index=False)    
