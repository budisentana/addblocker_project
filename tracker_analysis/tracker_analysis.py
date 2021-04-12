import os
import json
import pandas as pd

result_path = '/home/budi/adblocker_project/adblocker_code/mobsf_analysis/mobsf_result/'
tracker_path = '/home/budi/adblocker_project/adblocker_code/tracker_analysis/'

folder_list =['2021','2019','2016']
# folder_list =['test']

for item in folder_list:
    folder_path = result_path+item+'/'
    for root,dirs,files in os.walk(folder_path):
        tracker_peryear=[]
        for file in files:
            file_path = root+file
            with open (file_path,'r') as tf:
                tracker_file = tf.read()
                json_data = json.loads(tracker_file)
                json_tracker = json_data['trackers']['trackers']
                for i,line in enumerate(json_tracker):
                    for key,value in line.items():
                        provider = key
                        reference = value
                        track_item = {'file_name':file,'tracker_name':provider,'reference':reference}
                        tracker_peryear.append(track_item)
    
    df_tracker = pd.DataFrame(tracker_peryear)  
    csv_file = tracker_path+'tracker_'+item+'.csv'
    df_tracker.to_csv(csv_file,index=False)