import os
import json
import pandas as pd

apps_path =  '/home/budi/adblocker_project/apps_list/'
file_size_path = '/home/budi/adblocker_project/adblocker_code/malware_analysis/'
result_path = '/home/budi/adblocker_project/adblocker_code/mobsf_analysis/mobsf_result/'

"""Check file size"""

folder_list =['2021','2019','2016']
# folder_list =['test']

app_to_analyze=[]
for item in folder_list:
    folder_path = apps_path+item+'/'
    for root,dirs,files in os.walk(folder_path):
        oversize_list=[]
        for file in files:
            file_path = root+file
            # print(file_path)
            file_size = os.path.getsize(file_path)
            if file_size >  33554432:
                item_list = {'file_name':file,'file_size':file_size}
                oversize_list.append(item_list)
            else:
                file_path = result_path+item+'/'+file+'.json' 
                with open (file_path,'r') as fp:
                    try:
                        data = fp.read()
                        json_data = json.loads(data)
                        json_VT = json_data['virus_total']
                        if json_VT is None or 'Scan not performed' in str(json_VT) or 'Scan request successfully queued' in str(json_VT):
                            item_list = {'path':folder_path+file,'dir':item,'file':file}
                            print(item_list)
                            app_to_analyze.append(item_list)
                            print(len(app_to_analyze))
                    except:
                        print('virus total error --------------------------------'+file)
                        item_list = {'path':folder_path+file,'dir':item,'file':file}
                        app_to_analyze.append(item_list)
                        pass

    df_size = pd.DataFrame(oversize_list)  
    csv_file = file_size_path+'oversize_file_'+item+'.csv'
    df_size.to_csv(csv_file,index=False)

app_to_analyze_path = file_size_path+'app_to_analyze.csv'
# with open (app_to_analyze_path,'w') as fl:
#     for item in app_to_analyze:
#         fl.write(item+'\n')
df_to_analyze = pd.DataFrame(app_to_analyze)
df_to_analyze.to_csv(app_to_analyze_path,index=False)