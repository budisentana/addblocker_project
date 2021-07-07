"""This script is use to execute activity in Samsung Browser
    This is needed to get the traffic from Samsung Browser adblocker pluggin
"""
import os
# import manifest_extractor as ext
# import execute_activity as exe_act
import subprocess
import time
from subprocess import check_output, STDOUT

samsung_manifest_path = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/samsung_plugin/com.sec.android.app.sbrowser/AndroidManifest.xml'
url_path = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/news_domain.txt'
result_path = '/home/budi/adblocker_project/mitm_result_samsung_pluggin/'

# setup = 'Aggresive'
setup = 'Normal'
pluggin_pacakage = 'com.appsisland.ads.shield.content.blocker'
samsung_package = 'com.sec.android.app.sbrowser'
samsung_main_activity = 'com.sec.android.app.sbrowser.SBrowserMainActivity'

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


def execute_activity(samsung_package,samsung_activity,urls):
    component = samsung_package+'/'+samsung_activity
    action = 'android.intent.action.VIEW'
    for url in urls:
        execute_activity = 'adb shell am start -W -a '+action+' -d '+url+' '+component 
        print(execute_activity)
        try:
            proc = subprocess.call(execute_activity, timeout=3, shell=True)
            time.sleep(10)
        except subprocess.TimeoutExpired:
            pass  

def refresh_browser(samsung_package):
    refresh_cmd = 'adb shell pm clear '+samsung_package
    os.system(refresh_cmd)

def main():

    if 'baselin' in pluggin_pacakage:

        """Activate MITM dump"""
        print ('Activate MITM dump')
        res_path = result_path+'baseline'
        # runmitmdump(res_path.rstrip('.'))

        """Execute Samsung Main Activity"""
        urls = extract_url(url_path)
        execute_activity(samsung_package,samsung_main_activity,urls)

        """Kill MITM dump"""
        kill_mitm()

        """Refresh Browser"""
        refresh_browser(samsung_package)
    else:
        installed = check_installed_apps(pluggin_pacakage)
        if installed ==True:

            """Activate MITM dump"""
            print ('Activate MITM dump')
            if 'Normal' in setup:
                res_path = result_path+'Normal/'+pluggin_pacakage
            elif 'Aggresive' in setup:
                res_path = result_path+'Aggresive/'+pluggin_pacakage
            runmitmdump(res_path.rstrip('.'))

            """Execute app per activity"""
            urls = extract_url(url_path)
            execute_activity(samsung_package,samsung_main_activity,urls)
            """Uninstall apps"""
            uninstall_apk(pluggin_pacakage)

            """Kill MITM dump"""
            kill_mitm()

            """Refresh Browser"""
            refresh_browser(samsung_package)
        else:
            print(pluggin_pacakage+' did not installed. Please proceed to pluggin instalation first')


if __name__ == "__main__":
    main()
