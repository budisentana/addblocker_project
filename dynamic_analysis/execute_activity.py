import manifest_extractor as ext
import re, sys, os, string,csv, subprocess
import collections
import time
import subprocess
# from com.dtmilano.android.viewclient import ViewClient


class OrderedSet(collections.Set):
    def __init__(self, iterable=()):
        self.d = collections.OrderedDict.fromkeys(iterable)

    def __len__(self):
        return len(self.d)

    def __contains__(self, element):
        return element in self.d

    def __iter__(self):
        return iter(self.d)

# base_path = '/home/budi/crypto_project/sandbox/trx.org.freewallet.app/AndroidManifest.xml'
# base_path = '/home/budi/crypto_project/sandbox/adblocker.lite.browser/AndroidManifest.xml'
base_path = '/home/budi/crypto_project/sandbox/com.apusapps.browser/AndroidManifest.xml'
# base_path = '/home/budi/crypto_project/sandbox/com.blocking.sites/AndroidManifest.xml'

def execute_intent(manifest_path,urls):
    # main_activity = ext.main_activity_ex(manifest_path)
    package_name = ext.package_name_ex(manifest_path)
    intent_action = ext.intent_action_ex(manifest_path)

    for item in intent_action:
        activity,action = item['activity'],item['action']
        # parse_act = activity.split('.')
        # parse_pack = package_name.split('.')
        # diff = np.subtract (set(parse_main), set(parse_package))
        # diff = OrderedSet(parse_act)-OrderedSet(parse_pack)
        # res_activity = str('.'.join(diff))
        # print(res_activity)
        # component = package_name+'/.'+res_activity
        if action == 'android.intent.action.VIEW':
            # print (activity,action)
            component = package_name+'/'+activity
            for url in urls:
                    execute_activity = 'adb shell am start -W -a '+action+' -d '+url+' '+component 
                    print(execute_activity)
                    try:
                    # execute_task = os.system(execute_activity)
                        proc = subprocess.call(execute_activity, timeout=3, shell=True)
                        time.sleep(2)
                    except subprocess.TimeoutExpired:
                        pass  


def main():
    urls = ['detik.com','nytimes.com']
    execute_intent(base_path,urls)

if __name__ == "__main__":
    main()
