"""Create baseline traffic using Google Chrome"""
import os
import subprocess
import time
from subprocess import check_output, STDOUT


baseline_path = '/home/budi/adblocker_project/mitm_result/baseline30'
# baseline_path = '/home/budi/adblocker_project/mitm_result/baseline10'
url_path = '/home/budi/adblocker_project/adblocker_code/dynamic_analysis/news_domain.txt'

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

def main():
    """Activate MITM dump"""
    runmitmdump(baseline_path)

    """Execute main activity with intent action in Google Chrome"""
    urls = extract_url(url_path)
    for url in urls:
        cmd = 'adb shell am start -n com.android.chrome/com.google.android.apps.chrome.Main -a android.intent.action.VIEW -d '+url
        os.system(cmd)
        time.sleep(30)

    """Kill MITM dump"""
    kill_mitm()

    time.sleep(5)

if __name__ == "__main__":
    main()
