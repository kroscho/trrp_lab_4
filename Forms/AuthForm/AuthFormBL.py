from tkinter import messagebox as mb
import sys, os
import requests
import webbrowser 
from tkinter import * 

path_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.append(path_dir)

from ClientConfiguration.ClientConfiguration import *
from API.VKUrls import *
from Encryption.Encryption import *

def ShowWarning():
    msg = "Вы не были до этого авторизованы\nВам необходимо авторизоваться!"
    mb.showwarning("Предупреждение", msg)

def CreateAuthorizeUrl():
    session = requests.Session()
    params = {
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URL,
        'scope': 'wall,groups,offline,docs',
        'display': 'page',
        'response_type': 'token',
        'v': VK_API_VERSION,
    }
    prepared_request = session.get(VK_AUTHORIZE_URL, params=params)
    return prepared_request.url

def SetTokenToFile(str):
    WriteToFile(TOKEN_FILE_PATH, str)
    key = LoadKey()
    Encrypt(TOKEN_FILE_PATH, key)

def Auth(event):
    url = CreateAuthorizeUrl()
    webbrowser.open_new(url)