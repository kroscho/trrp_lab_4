from requests.api import delete
import requests
from API.VKUrls import *
from ClientConfiguration.ClientConfiguration import *

def GetUserInfo(access_token):
    params = {
        'access_token': access_token,
        'fields': 'photo_200_orig,screen_name',
        'v': VK_API_VERSION
    }
    response = requests.get(VK_API_GET_USER_INFO_URL, params=params)
    if response.status_code == 200:
        return dict(response.json())['response'][0]
    else:
        return {}