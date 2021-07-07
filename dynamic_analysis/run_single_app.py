"""This script is use to inject security exception and install apps to the device"""
"""Don't forget to activate aggresive settings"""
import os
import subprocess
import time
from subprocess import check_output, STDOUT


apk_path = '/home/budi/adblocker_project/apps_list/2021/to.freedom.android2.apk'
injected_apk_path = '/home/budi/adblocker_project/injected_apk/2021/'
injector_path = '/home/budi/adblocker_project/AddSecurityExceptionAndroid/'


def install_apk(apkName):
  print("Installing "+apkName)
  os.system('adb install '+apkName)


def add_exeption(apk_name,injector_path,apk_path,injected_apk_path):
    app = apk_name.rstrip('apk')
    app = app.rstrip('.')
    # print(app)
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

def check_injected_app (apk_name, injected_apk_path):
    # print(apk_name)
    new_apk = apk_name.replace('.apk','_new.apk')
    injeceted_list =[]
    for rt,drs,fls in os.walk(injected_apk_path):
        for file in fls:
            injeceted_list.append(file)

    if new_apk in injeceted_list:
        print('Injected apps found --> proceed to instalation')
        return True
    else:
        print('No injected apps found -->  Add Security exemption')
        return False        

def main():
    global apk_path

    """Find app name from path"""
    split_apk = apk_path.split('/')
    apk_name = split_apk[-1]
    # print(apk_name)

    """Inject security exeption to apps"""
    check_injected = check_injected_app(apk_name,injected_apk_path)
    if check_injected is True:
        new_file_path = injected_apk_path+apk_name.replace('.apk','_new.apk')
        # print(new_file_path)
    else:
    #    print('false')
        new_file_path = add_exeption(apk_name,injector_path,apk_path,injected_apk_path)

    """Installing apk"""
    install_apk(new_file_path)


if __name__ == "__main__":
    main()
