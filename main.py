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

def save_api_domain(api_domain):
    with open('API_LATEST.txt', 'a') as file:
        file.write(api_domain + '\n')


def sendView(number):
    headers = {
        'x-ss-stub': '314E244CD08E27C8027EC7C950A1F9A5',
        'x-tt-multi-sids': '7030568591091254274%3Afce62dcd599ac161f768f3135034cfea',
        'sdk-version': '2',
        'x-bd-kmsv': '0',
        'x-tt-token': '03fce62dcd599ac161f768f3135034cfea055a4bd421eda9c9ca4b23c07e44f65cad571a15519f3ae0398fc0a772c410c0619680a33580e55300a96ce34d5ec44fe17ead05220977c787021d35b37aebca5e0cfe4874aaca1e9849e351e9920abe48f-CkBiZTEzMzc2YTA1Mjc0ZmFjYzE3M2FkMzc3YzE0NTY4ZjAxNTQ1NjZhOWFjZmIxY2Y1Y2Q3YzU1MTljMGE0M2Zj-2.0.0',
        'x-ss-req-ticket': '1689081331327',
        'x-bd-client-key': '#HUgX+TXdb81tRNHaX0thUm5Jb3YrObbDbWi6y8v5rIlyROSRVmKyBip/8nvCbYeOs8JedIbiT0WHpZsG',
        'multi_login': '1',
        'passport-sdk-version': '19',
        'x-tt-dm-status': 'login=1;ct=1;rt=1',
        'x-vc-bdturing-sdk-version': '2.3.2.i18n',
        'x-tt-store-region': 'my',
        'x-tt-store-region-src': 'uid',
        'user-agent': 'com.ss.android.ugc.trill/300304 (Linux; U; Android 9; en_US; SM-A908N; Build/PQ3B.190801.06281541;tt-ok/3.12.13.1)',
        'x-ladon': '2WkdH9tGZF3iviqrmciB/7BNih05Hj46hCC0B2HKsLUTQko8',
        'x-khronos': '1689081330',
        'x-argus': '6aFEsGy4IIE8WMtWYnLED7NRxxltCVnhSuzFozwyDOJOkI7y38G7uJHrmKz6HDVLERwV8TtzgVvfAXKVMUR7C9xSN17a4tCEe+rMhYtAkSsVtpTVZpRcUHmll2WRjXcbj3qZTcXT+6aUFnWK7IsibvVPNrnU2crcs8iA24wagl/z7qKXia6/ykXCdXqDpAkt1Gc2GSyMk6Q16Js/HYnNfK33tF6Z1szgYgnspkLMGg/ksOZxoKqvPlVBckc7GlROuwh2UqKCTGtByQ3yrrJbatf4laZNMW6n0HdYxh/nsL2G/7WaGI35cEfVR8ySbfoqIOkp+7HOTRW2QatvE8qyT/MJo6oxlfI6V2ViYoe23772guB/Eh9PZpCPVX+r0Ducf7/kBAPlnMw729xs/uMIvX8xH8pucUAWCHYvOd7TIrSbNY3pqf+nuHRtUlkKdyEVUZRtSCfSNbxm9/pdb3DEcSqg4LENvkJpIsLkhBDUn7TGSMb53rTZbuDOhWf+WL6GPRcVD+bo22KlB59Tn2Wutj5mllQNjxebhTi3nH7dhQCfwpGfZcmOTlnM7OB6WnYQKzlac8GBtK1hjvyJ2rDUQFGidQvVLbPEgCDAb5oKoPGCXg==',
        'x-gorgon': '8404e04a00050bccbd03360613d86a8ddb4b0d3888879aee5d77',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'store-country-code=my; install_id=7254523177588524805; ttreq=1$c23d4bf2ff5bed061801f2383f714ffd7e99193e; passport_csrf_token=73e074fc3e023177463e2cebdc5376a4; passport_csrf_token_default=73e074fc3e023177463e2cebdc5376a4; store-idc=alisg; tt-target-idc=alisg; multi_sids=7030568591091254274%3Afce62dcd599ac161f768f3135034cfea; odin_tt=a954cf72021ff2efa2cfd5ae6967b5ad3439ac2a45bd1aee079e39f3c885abedf220332ae980fe2134c0030a9f38997c0cf8a55c952baeb5eb12f7835835273d0ae280f4d4bb166903c6a69edf525b52; cmpl_token=AgQQAPO0F-RP_bGvdkXZMZ07_syke0fd_4c_YM4VLA; d_ticket=41570132b7d0d6032f8f3a9dc26e3a33a581e; sid_guard=fce62dcd599ac161f768f3135034cfea%7C1689075369%7C15551999%7CSun%2C+07-Jan-2024+11%3A36%3A08+GMT; uid_tt=d8265d7c94a2e502fd5dd30b63107b744202c487d4b3b6111b4ae0ce25046562; uid_tt_ss=d8265d7c94a2e502fd5dd30b63107b744202c487d4b3b6111b4ae0ce25046562; sid_tt=fce62dcd599ac161f768f3135034cfea; sessionid=fce62dcd599ac161f768f3135034cfea; sessionid_ss=fce62dcd599ac161f768f3135034cfea; store-country-code-src=uid; tt-target-idc-sign=Gs7IhYNrRUE545q8n8axlAPvnjHp86rqmNxVdzDMBSlho621veTIVDkmVpGno9b0rp_oFg_Y7DeHM8wyDGz0xCRQqxvVI_g95Ou8-85kr1VKZJ53leDnmj7KaNlYNGHCHX-lM-HwIRag8Fq2Tdf-1KrCHbPURv34YL1G_foQ69YlyPwAv-ONAh3oBg6egmv9RP9voxioJaZZipcOOLzINrNu89RU-xwhslctYvl6hh_Vigt7chYFCNqEuvpAeKj8X7kGZClT6xBibFM6UxeIr38Tjct8Jbb5KSUqzg9vw55qXZ3SuGpFUirI9ltIv_jTazgW6KYEEyUiXMqkpW0xvT709W1Z_r31_t8-8q5qBgrHDONfxu4SqAIwwieCvK5X0WerxneL6hfoDZrB-SoAbYPD-ghlyiZMUHhxd8M9cO6pnhtUNPy2EPLdCWLgjXxAax3X1aIt-n74qK8koLCFhyVP4Njp-MBSXnGNTvqZf3e4B9v791jK0WuHWZkuh1Vk; msToken=d2HWwVXFHS4Y6X_zTw8OniekUjCUKDZM8kRoU3yLMKMlhznQQS5HS-j8DeV8PoVLUVJDMBjjR927t5oQyG3rqO1I3BRdtWjVab4ZYHFm7jAAScT9QuZaFInBtw==',
    }
    data = {
        'pre_item_playtime': '1556',
        'user_algo_refresh_status': 'false',
        'first_install_time': '1689075327',
        'enter_from': 'others_homepage',
        f'item_id': {itemID},
        'is_ad': '0',
        'follow_status': '1',
        'sync_origin': 'false',
        'follower_status': '0',
        'action_time': '1689081331',
        'tab_type': '3',
        'pre_hot_sentence': '',
        'play_delta': '1',
        'request_id': '',
        'aweme_type': '0',
        'order': '',
        'pre_item_id': '7253698396685389058',
    }
    apiDomain     = choice(ApiDomain)

    try:
        response = requests.post(
            'https://api22-core-c-alisg.tiktokv.com/aweme/v1/aweme/stats/?iid=7254523177588524805&device_id=7254521958107366917&ac=wifi&channel=googleplay&aid=1180&app_name=trill&version_code=300304&version_name=30.3.4&device_platform=android&os=android&ab_version=30.3.4&ssmix=a&device_type=SM-A908N&device_brand=samsung&language=en&os_api=28&os_version=9&openudid=d4bcfda1bbdad09e&manifest_version_code=300304&resolution=1280*720&dpi=240&update_version_code=300304&_rticket=1689081331326&current_region=MY&app_type=normal&sys_region=US&mcc_mnc=50201&timezone_name=Asia%2FKuala_Lumpur&carrier_region_v2=502&residence=MY&app_language=en&carrier_region=MY&ac2=wifi5g&uoo=0&op_region=MY&timezone_offset=28800&build_number=30.3.4&host_abi=arm64-v8a&locale=en&region=US&ts=1689081332&cdid=1894fddb-6132-4c11-9d1d-d7fec0c24a7d',
            timeout=5,
            headers=headers,
            data=data,
        )
        print(f"Request {number}: {response.text} And URI : {apiDomain}")
        if response.text and response.status_code == 200:
            save_api_domain(apiDomain)  # Save the apiDomain in a file
    except requests.exceptions.ConnectTimeout as e:
        print(f"Request {number}: Connection Timeout")

def sendShare(number):
    headers = {
                # All of this needed in order to make the response working!
                #'x-tt-token': '03b106dd97f551b67041844163e77c3dd604088157aa674c8d89d291e212d8d786fb64ac1479a0f26f31ed77dc7a2dffe4937371287588968c734cc55a0017cb3cb0f176457fc60aa0f11c886dfb6e9f86a449f3d590e27897418ad35220494198f10-CkBkZjI0ZTE4Njk1ZDliZGRjMzhhM2RiYWQ0NTQ2YTQzM2YzNGVjNDYyZGQyNjhkZDg1ZjhmYjMxNzBiYmQ4NGMx-2.0.0',
                'user-agent': choice(UserAgent),
               # 'x-ladon': 'mIBAT3HpBPCDI+1zqWZH5LOADV2RoR0v6BsZFCJD+sb7pfAp',
                #'x-argus': 'rZW0jsgjdiIDrkkDEPnqaD5JJt4c43cfx6HHR/5fJ8KqwHrKKgqdc0QE94UfbJC5YiB2asEUAXL6Nj/O212qR5wXU7Se+YWajiqJMTPXgmedIvg67bqo57snDDlbUqvNrCO4d2zbFXziLNfBZOQOnfkvEB/c1bJitp/MVLnFxYt1bFB8/mLZdxocBX8CLen9dcA/QhwML3nIQVUQQ84hyFI4zGtBuyhVHvcGVdSeTYBCEz2LrxgwnkBIbdQGgX6TI/hKYULOnO76cXTQP+5taB0HU6ohqiZTO6dzCyluDsa40OxUwwcJ8xuq2LQVybaSZ0iY1tYAYjrgGwbpdK45SqK0BvQ9jJAgfq3NaOQ5zGTnGA+dqDBiyER4OJar66OEDXJGDpNQ1ieIjzOGsNEH0F5+OVh8HDx/Ea9Q1tZU+7a8VbW27rGlEAfPikZPDBjM2a6DMI1FJa+SDyfva1AuXq4acLxQNMbyHRiUmKoEtNA7U9Vr6ep175x829E8XF/9C2UzgerJYD27lLl7X3Z1Zy2fJDYoyqa9ETDFnBCSWjHuCscYJRuV9Z7niiaiApb/3zevKz8+574FrQkUqb5R+3Kbftt6l2g8P0XHexXOSh4El8YyVyevPoTk5YPHiS1oS9M=',
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
        print(f"Request {number}: {response.text} URI : {URI}")
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
