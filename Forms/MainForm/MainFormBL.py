from tkinter import messagebox as mb
import sys, os
import webbrowser 
from tkinter import * 

path_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.append(path_dir)

from ClientConfiguration.ClientConfiguration import *
from API.VKUrls import *
from Encryption.Encryption import *

def Callback1(event, screenName):
    url = "https://vk.com/" + screenName
    webbrowser.open_new(url)