from API.VKUrls import *
import requests

# получить группы пользователя
def GetAllGroups(accessToken, userId):
    payload = {
        'access_token': accessToken,
        'user_id': userId,
        'extended': 1,
        'v': VK_API_VERSION
    }
    response = requests.get(VK_API_GET_GROUPS_URL, params=payload)
    if response.status_code == 200:
        group = dict(response.json()).get('response').get('items')
        print(group)
        return group
    else:
        return []

# получить группы пользователя
def LoadFile(accessToken, file, title, tag):
    payload = {
        'access_token': accessToken,
        'file': file,
        'title': title,
        'tags': tag,
        'v': VK_API_VERSION
    }
    response = requests.get(VK_API_SAVE_DOC_URL, params=payload)
    if response.status_code == 200:
        print("Файл добавлен")
        return True
    else:
        return False