import manifest_extractor as ext
import re, sys, os, string,csv, subprocess
import collections
import time
import subprocess

# base_path = '/home/budi/crypto_project/sandbox/trx.org.freewallet.app/AndroidManifest.xml'
# base_path = '/home/budi/crypto_project/sandbox/adblocker.lite.browser/AndroidManifest.xml'
base_path = '/home/budi/crypto_project/sandbox/com.apusapps.browser/AndroidManifest.xml'
# base_path = '/home/budi/crypto_project/sandbox/com.blocking.sites/AndroidManifest.xml'


package_name = ext.package_name_ex(base_path)
intent_action = ext.intent_action_ex(base_path)

for item in intent_action:
    activity,action = item['activity'],item['action']
    print(item)

# cmd ='mv dfg.txt hggg'

# from subprocess import check_output, STDOUT
# # cmd = "Your Command goes here"
# try:
#     cmd_stdout = check_output(cmd, stderr=STDOUT, shell=True).decode()
# except Exception as e:
#     print('errrrrr')