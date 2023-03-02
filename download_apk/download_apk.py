"""This script is used to leveraging apk pull to download the apps to device and then pull it to the computer
    For this case is use to download the adblock apk in 2023
"""

import os 
import pandas as pd


download_path = '/home/budi/adblocker_project/apps_list/2023_raw_apk/'
app_list_path = '/home/budi/adblocker_project/adblocker_code/data_list/2023_list_manual.csv'


def check_download(app_id,download_path):
    for roots,folders,files in os.walk(download_path):
        for folder in folders:
            if app_id in folder:
                # print(app_id,folder)
                return True
                break
            else:
                return False

def apk_pull(app_id,download_path):
    pull_command = 'curl -sL bit.ly/apkpull | bash -s -- ' + app_id + ' -d '+download_path +' --uninstall'
    print(pull_command)
    os.system(pull_command)

def main():
    app_df = pd.read_csv(app_list_path)
    for index,item in app_df.iterrows():
        app_id =item[1]
        status = check_download(app_id,download_path)
        print(index,app_id)

        # if status == False:
            # apk_pull(app_id,download_path)
            # print(index,app_id)

if __name__=='__main__':
    main()