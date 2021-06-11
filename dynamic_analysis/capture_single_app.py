"""This script is use to execute activity from a given apps"""
import os
import manifest_extractor as ext
import execute_activity as exe_act
import subprocess
import time
from subprocess import check_output, STDOUT

apk_path = '/home/budi/adblocker_project/apps_list/2021/com.seven.adclear.fsb.apk'
url_path = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/news_domain.txt'
extracted_apk_path = '/home/budi/adblocker_project/extracted_apk/2021/'
trafic_capture_path = '/home/budi/adblocker_project/mitm_result/2021/'
result_path = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/result_setting.csv'


def uninstall_apk(package):
  print("Uninstalling "+package)
  os.system('adb uninstall '+package)
  
def extract_apk(apk_path,destination_path):
    print ('Extracting '+apk_path)
    apktool_ex = 'apktool d '+apk_path
    os.chdir(destination_path)
    os.system(apktool_ex)

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
def check_manifest(extracted_apk_path,package_name):
    dr_list = next(os.walk(extracted_apk_path))[1]
    # print(dr_list)
    if package_name in dr_list:
        print('Extracted apk found')
        return True
    else:
        print('No extracted apk found')
        return False

def add_to_result(result_path,apk_name):
    with open (result_path,'a') as fl:
        fl.write(apk_name)

def main():
    global apk_path, extracted_apk_path
    package_name = find_package_name(apk_path)

    """Add to result"""
    add_to_result(result_path,package_name)

    # print(package_name)
    """Check existing extracted apk"""
    installed = check_installed_apps(package_name)
    if installed == True:
        manifest_check = check_manifest(extracted_apk_path,package_name)
        if manifest_check == True:
            manifest_path = extracted_apk_path+package_name+'/AndroidManifest.xml'
        else:
            print('manifest not found --> Do apk extraction')           
            extract_apk(apk_path,extracted_apk_path)
            manifest_path = extracted_apk_path+package_name+'/AndroidManifest.xml'

        """Activate MITM dump"""
        print ('Activate MITM dump')
        res_path = trafic_capture_path+package_name
        runmitmdump(res_path.rstrip('.'))

        """Execute app per activity"""
        urls = extract_url(url_path)
        exe_act.execute_intent(manifest_path,urls)

        """Uninstall apps"""
        uninstall_apk(package_name)

        """Kill MITM dump"""
        kill_mitm()


    else:
        print('Apps '+package_name+ '  is not installed --> Please proceed to instalation first')



if __name__ == "__main__":
    main()
