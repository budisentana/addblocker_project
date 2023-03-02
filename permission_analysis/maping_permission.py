from unittest import result
from api_specific_resources import load_permissions
import json


def permission_mapping(api_level,permission_name):

    function_type = 'permissions'
    result = load_permissions(api_level,function_type)
    return result

def main():
    api_level = 30
    permission_name = 'android.permission.RECEIVE_BOOT_COMPLETED'
    result = permission_mapping(api_level,permission_name)
    print(result[permission_name]['protectionLevel'])
if __name__=='__main__':
    main()