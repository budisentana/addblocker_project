import os
import manifest_extractor as ext
import execute_activity as exe_act
import subprocess
import time
from subprocess import check_output, STDOUT


apk_path = '/home/budi/adblocker_project/apps_list/2021'
# apk_path = '/home/budi/adblocker_project/apps_list/2019'
# apk_path = '/home/budi/adblocker_project/apps_list/2016'
extracted_apk_path = '/home/budi/adblocker_project/extracted_apk/2021'
# extracted_apk_path = '/home/budi/adblocker_project/extracted_apk/2019'
# extracted_apk_path = '/home/budi/adblocker_project/extracted_apk/2016'
injected_apk_path = '/home/budi/adblocker_project/injected_apk/2021/'
# injected_apk_path = '/home/budi/adblocker_project/injected_apk/2019/'
# injected_apk_path = '/home/budi/adblocker_project/injected_apk/2016/'
trafic_capture_path = '/home/budi/adblocker_project/mitm_result/2021/'
# trafic_capture_path = '/home/budi/adblocker_project/mitm_result/2019/'
# trafic_capture_path = '/home/budi/adblocker_project/mitm_result/2016/'
url_path = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/news_domain.txt'
injector_path = '/home/budi/adblocker_project/AddSecurityExceptionAndroid/'

def install_apk(apkName):
  print("Installing "+apkName)
  os.system('adb install '+apkName)

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
    print ('Kill MITM dump').rstrip('apk')
    cmd = 'pkill mitmdump'
    os.system(cmd)

def add_exeption(app,injector_path,apk_path,injected_apk_path):
    os.chdir(injector_path)
    cmd = './addSecurityExceptions.sh '+apk_path
    os.system(cmd)
    new_file = app+'_new.apk'
    mv_cmd = 'mv '+new_file+' '+injected_apk_path
    try:
        # os.system(mv_cmd)
        cmd_stdout = check_output(mv_cmd, stderr=STDOUT, shell=True).decode()
        new_file_path = injected_apk_path+new_file
    except Exception as e:
        new_file_path = apk_path
    return (new_file_path)

def runmitmdump(res_path):
  print("Running mitmdump on Terminal")
  arg = 'mitmdump -w '+res_path
  subprocess.Popen(arg,shell=True)

def check_result():
    global trafic_capture_path
    result_list=[]
    for rt, drs, fls in os.walk(trafic_capture_path):
        for file in fls:
            if file not in result_list:
                result_list.append(file)
    return result_list

def main():
    global apk_path, extracted_apk_path
    
    result_list = check_result()
    # print(result_list)

    for rt,drs,fls in os.walk(apk_path):
        for file in fls:
            package = file.rstrip('apk')
            # print (package)
            if package.rstrip('.') not in result_list:
                apk_path = rt+'/'+file
                print(apk_path)
                """Extracting apk using apktool"""
                extract_apk(apk_path,extracted_apk_path)
                
                """Find manifest"""
                app = file.rstrip('apk')
                manifest_path = extracted_apk_path+'/'+app.rstrip('.')+'/AndroidManifest.xml'
                package_name = ext.package_name_ex(manifest_path)

                """Inject security exeption to apps"""
                new_file_path = add_exeption(app.rstrip('.'),injector_path,apk_path,injected_apk_path)

                """Installing apk"""
                install_apk(new_file_path)

                """Activate MITM dump"""
                res_path = trafic_capture_path+file.rstrip('apk')
                runmitmdump(res_path.rstrip('.'))

                """Execute app per activity"""
                urls = extract_url(url_path)
                exe_act.execute_intent(manifest_path,urls)

                """Uninstall apps"""
                uninstall_apk(package_name)

                """Kill MITM dump"""
                kill_mitm()

                time.sleep(3)

if __name__ == "__main__":
    main()
