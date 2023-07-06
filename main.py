import requests
import ssl
from random import choice
from data.UserAgent import UserAgent
from urllib3.exceptions import InsecureRequestWarning
from http import cookiejar
from utils import *
from data.Lists import *
import threading



class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
r                                 = requests.Session()

r.cookies.set_policy(BlockCookies())


def sendView(number):
    headers = {
                # All of this needed in order to make the response working!
                'x-tt-token': '03b106dd97f551b67041844163e77c3dd604088157aa674c8d89d291e212d8d786fb64ac1479a0f26f31ed77dc7a2dffe4937371287588968c734cc55a0017cb3cb0f176457fc60aa0f11c886dfb6e9f86a449f3d590e27897418ad35220494198f10-CkBkZjI0ZTE4Njk1ZDliZGRjMzhhM2RiYWQ0NTQ2YTQzM2YzNGVjNDYyZGQyNjhkZDg1ZjhmYjMxNzBiYmQ4NGMx-2.0.0',
                'user-agent': choice(UserAgent),
                'x-ladon': 'mIBAT3HpBPCDI+1zqWZH5LOADV2RoR0v6BsZFCJD+sb7pfAp',
                'x-argus': 'rZW0jsgjdiIDrkkDEPnqaD5JJt4c43cfx6HHR/5fJ8KqwHrKKgqdc0QE94UfbJC5YiB2asEUAXL6Nj/O212qR5wXU7Se+YWajiqJMTPXgmedIvg67bqo57snDDlbUqvNrCO4d2zbFXziLNfBZOQOnfkvEB/c1bJitp/MVLnFxYt1bFB8/mLZdxocBX8CLen9dcA/QhwML3nIQVUQQ84hyFI4zGtBuyhVHvcGVdSeTYBCEz2LrxgwnkBIbdQGgX6TI/hKYULOnO76cXTQP+5taB0HU6ohqiZTO6dzCyluDsa40OxUwwcJ8xuq2LQVybaSZ0iY1tYAYjrgGwbpdK45SqK0BvQ9jJAgfq3NaOQ5zGTnGA+dqDBiyER4OJar66OEDXJGDpNQ1ieIjzOGsNEH0F5+OVh8HDx/Ea9Q1tZU+7a8VbW27rGlEAfPikZPDBjM2a6DMI1FJa+SDyfva1AuXq4acLxQNMbyHRiUmKoEtNA7U9Vr6ep175x829E8XF/9C2UzgerJYD27lLl7X3Z1Zy2fJDYoyqa9ETDFnBCSWjHuCscYJRuV9Z7niiaiApb/3zevKz8+574FrQkUqb5R+3Kbftt6l2g8P0XHexXOSh4El8YyVyevPoTk5YPHiS1oS9M=',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            }

    data = {
        'pre_item_playtime': '242',
        'user_algo_refresh_status': 'true',
        'first_install_time': '1688541685',
        'enter_from': 'general_search',
        f'item_id': {itemID},
        'is_ad': '0',
        'follow_status': '2',
        'sync_origin': 'false',
        'follower_status': '1',
        'action_time': '1688599944',
        'tab_type': '22',
        'pre_hot_sentence': '',
        'play_delta': '1',
        'pre_item_id': '7246762556486978817',
    }
    apiDomain     = choice(ApiDomain)

    try:
        response = requests.post(
        f'https://{apiDomain}/aweme/v1/aweme/stats/?iid=7252230999672751874&device_id=7252227231014520322&ac=wifi&channel=googleplay&aid=1180&app_name=trill&version_code=300203&version_name=30.2.3&device_platform=android&os=android&ab_version=30.2.3&ssmix=a&device_type=ASUS_I001DA&device_brand=asus&language=en&os_api=28&os_version=9&openudid=9ae85fe97adfbf35&manifest_version_code=300203&resolution=1600*900&dpi=240&update_version_code=300203&_rticket=1688599944988&current_region=MY&app_type=normal&sys_region=US&mcc_mnc=50201&timezone_name=Asia%2FKuala_Lumpur&carrier_region_v2=502&residence=MY&app_language=en&carrier_region=MY&ac2=wifi5g&uoo=0&op_region=MY&timezone_offset=28800&build_number=30.2.3&host_abi=arm64-v8a&locale=en&region=US&content_language=en%2Czh-Hant%2C&ts=1688648323&cdid=82ae2e4c-0952-4875-8c22-d25fce126b67',
        headers=headers,
        data=data,
        timeout= 5
    )
        print(f"Request {number}: {response.text}")
    except requests.exceptions.ConnectTimeout as e:
        print(f"Request {number}: Connection Timeout")

def sendShare(number):
    headers = {
                # All of this needed in order to make the response working!
                'x-tt-token': '03b106dd97f551b67041844163e77c3dd604088157aa674c8d89d291e212d8d786fb64ac1479a0f26f31ed77dc7a2dffe4937371287588968c734cc55a0017cb3cb0f176457fc60aa0f11c886dfb6e9f86a449f3d590e27897418ad35220494198f10-CkBkZjI0ZTE4Njk1ZDliZGRjMzhhM2RiYWQ0NTQ2YTQzM2YzNGVjNDYyZGQyNjhkZDg1ZjhmYjMxNzBiYmQ4NGMx-2.0.0',
                'user-agent': choice(UserAgent),
                'x-ladon': 'mIBAT3HpBPCDI+1zqWZH5LOADV2RoR0v6BsZFCJD+sb7pfAp',
                'x-argus': 'rZW0jsgjdiIDrkkDEPnqaD5JJt4c43cfx6HHR/5fJ8KqwHrKKgqdc0QE94UfbJC5YiB2asEUAXL6Nj/O212qR5wXU7Se+YWajiqJMTPXgmedIvg67bqo57snDDlbUqvNrCO4d2zbFXziLNfBZOQOnfkvEB/c1bJitp/MVLnFxYt1bFB8/mLZdxocBX8CLen9dcA/QhwML3nIQVUQQ84hyFI4zGtBuyhVHvcGVdSeTYBCEz2LrxgwnkBIbdQGgX6TI/hKYULOnO76cXTQP+5taB0HU6ohqiZTO6dzCyluDsa40OxUwwcJ8xuq2LQVybaSZ0iY1tYAYjrgGwbpdK45SqK0BvQ9jJAgfq3NaOQ5zGTnGA+dqDBiyER4OJar66OEDXJGDpNQ1ieIjzOGsNEH0F5+OVh8HDx/Ea9Q1tZU+7a8VbW27rGlEAfPikZPDBjM2a6DMI1FJa+SDyfva1AuXq4acLxQNMbyHRiUmKoEtNA7U9Vr6ep175x829E8XF/9C2UzgerJYD27lLl7X3Z1Zy2fJDYoyqa9ETDFnBCSWjHuCscYJRuV9Z7niiaiApb/3zevKz8+574FrQkUqb5R+3Kbftt6l2g8P0XHexXOSh4El8YyVyevPoTk5YPHiS1oS9M=',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            }

    data = {
                # All of this needed in order to make the response working!
                'stats_channel': 'copy',
                'pre_item_playtime': '',
                'user_algo_refresh_status': 'true',
                'first_install_time': '1688541685',
                'enter_from': 'others_homepage',
                f'item_id': {itemID},
                'is_ad': '0',
                'item_type': '1',
                'sync_origin': 'false',
                'share_delta': '1',
                'action_time': '1688582639',
                'pre_hot_sentence': '',
                'request_id': '',
                'aweme_type': '0',
                'order': '',
                'pre_item_id': '',
            }
    apiDomain     = choice(ApiDomain)
    cdid = generate_random_uuid()
    current_timestamp = generate_current_timestamp()
            # All of this needed in order to make the response working!
    URI = f'https://{apiDomain}/aweme/v1/aweme/stats/?iid=7252230999672751874&device_id=7252227231014520322&ac=wifi&channel=googleplay&aid=1180&app_name=trill&version_code=300203&version_name=30.2.3&device_platform=android&os=android&ab_version=30.2.3&ssmix=a&device_type=ASUS_I001DA&device_brand=asus&language=en&os_api=28&os_version=9&openudid=9ae85fe97adfbf35&manifest_version_code=300203&resolution=1600*900&dpi=240&update_version_code=300203&_rticket=1688582639919&current_region=MY&app_type=normal&sys_region=US&mcc_mnc=50201&timezone_name=Asia%2FKuala_Lumpur&carrier_region_v2=502&residence=MY&app_language=en&carrier_region=MY&ac2=wifi5g&uoo=0&op_region=MY&timezone_offset=28800&build_number=30.2.3&host_abi=arm64-v8a&locale=en&region=US&content_language=en%2Czh-Hant%2C&ts={current_timestamp}&cdid={cdid}'

    try:
        response = requests.post(URI, headers=headers, data=data, timeout=5)
        print(f"Request {number}: {response.text}")
    except requests.exceptions.ConnectTimeout as e:
        print(f"Request {number}: Connection Timeout")


if __name__ == "__main__":
    clearConsole();
    VideoURI = input("Enter video link: ")
    amount = int(input("Desired Amount: "))
    sendType = int(input("[0] - Views BOT\n[1] - Shares BOT: \n"))
    itemID = clearURL(VideoURI)

    if sendType == 0:
       sendProcess = sendView
    elif sendType == 1:
       sendProcess = sendShare
    else:
        print(f"Error {sendType}")


    threads = []
    for n in range(amount):
        t = threading.Thread(target=sendProcess, args=(n+1,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()