"""This script is use to execute activity in Chrome Browser for general-type pluggin
    This is needed to get the traffic from Chrome Browser before and after the general-type pluggin adblocker installed
    This is needed the adblocker apps to be installed before this script can be run
"""
import os
import manifest_extractor as ext
import execute_activity as exe_act
import subprocess
import time
from subprocess import check_output, STDOUT

url_path = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/news_domain.txt'
result_path = '/home/budi/adblocker_project/mitm_result_general_pluggin/'
url_test = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/test_domain.txt'
note_path = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/general_pluggin/general_pluggin_note.csv'

setup = 'Aggresive'
# setup = 'Normal'
# pluggin_pacakage = 'baseline'
pluggin_pacakage = 'to.freedom.android2'
general_package = 'com.android.chrome'
general_main_activity = 'com.google.android.apps.chrome.Main'

def uninstall_apk(package):
  print("Uninstalling "+package)
  os.system('adb uninstall '+package)
  
def extract_url(url_path):
    print('Extracting URL list')
    url_list =[]
    with open (url_path,'r') as fl:
        for line in fl:
            url_list.append(line.strip())
    return url_list

def kill_mitm():
    print ('Kill MITM dump')
    cmd = 'pkill mitmdump'
    os.system(cmd)

def runmitmdump(res_path):
  print("Running mitmdump on Terminal")
  arg = 'mitmdump -w '+res_path
  subprocess.Popen(arg,shell=True)

def find_package_name(apk_path):
    split_app = apk_path.split('/')
    package_name = split_app[-1].replace('.apk','')
    return(package_name)

def check_installed_apps(package_name):
    installed_check = 'adb shell pm list packages -f | grep '+package_name
    try:
        cmd_stdout = check_output(installed_check, stderr=STDOUT, shell=True).decode()
        return True
    except:
        return False

def add_to_result(result_path,apk_name):
    with open (result_path,'a') as fl:
        fl.write(apk_name)


def execute_activity(general_package,general_activity,urls):
    component = general_package+'/'+general_activity
    action = 'android.intent.action.VIEW'
    for url in urls:
        execute_activity = 'adb shell am start -W -a '+action+' -d '+url+' '+component 
        print(execute_activity)
        try:
            proc = subprocess.call(execute_activity, timeout=3, shell=True)
            time.sleep(10)
        except subprocess.TimeoutExpired:
            pass  

def refresh_browser(general_package):
    refresh_cmd = 'adb shell pm clear '+general_package
    os.system(refresh_cmd)

def find_browsable_activity(general_manifest_path,url_test):
    url_list = extract_url(url_test)
    exe_act.execute_intent(general_manifest_path,url_list)

def main():
  
    installed = check_installed_apps(pluggin_pacakage)
    if installed ==True:
        # """Add note for each general pluggin"""
        # add_to_result(note_path,pluggin_pacakage)

        """Activate MITM dump"""
        print ('Activate MITM dump')
        if 'Normal' in setup:
            res_path = result_path+'Normal/'+pluggin_pacakage
        elif 'Aggresive' in setup:
            res_path = result_path+'Aggresive/'+pluggin_pacakage
        runmitmdump(res_path.rstrip('.'))

        """Execute app per activity"""
        urls = extract_url(url_path)
        execute_activity(general_package,general_main_activity,urls)
        """Uninstall apps"""
        uninstall_apk(pluggin_pacakage)

        """Kill MITM dump"""
        kill_mitm()

        """Refresh Browser"""
        refresh_browser(general_package)
    else:
        print(pluggin_pacakage+' did not installed. Please proceed to pluggin instalation first')


if __name__ == "__main__":
    main()
