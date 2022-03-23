from tkinter import *
import webbrowser
from API.UserApi import *
from API.GroupsApi import *
import vk_api, json, requests, traceback
from vk_api.bot_longpoll import VkBotEventType

def MainForm(event, payload):

    def Callback(event):
        url = "https://vk.com/" + userInfo['screen_name']
        webbrowser.open_new(url)

    def Callback2(event):
        vk_session = vk_api.VkApi(token=payload['access_token'])
        vk = vk_session.get_api()
        #longpoll = vk_api.bot_longpoll.VkBotLongPoll(vk_session, id, wait=25)

        result = json.loads(requests.post(vk.docs.getMessagesUploadServer(type='doc', peer_id=userInfo['id'])['upload_url'],
                                        files={'file': open(TOKEN_FILE_PATH, 'rb')}).text)
        #jsonAnswer = vk.docs.save(file=result['file'], title='title', tags=[])
        print("FILE:   " + result['file'])
        LoadFile(payload['access_token'], result['file'], "test_title", "test_tag")
        print("ДОбавили")
        #vk.messages.send(
        #    peer_id=userInfo['id'],
        #    random_id=0,
        #    attachment=f"doc{jsonAnswer['doc']['owner_id']}_{jsonAnswer['doc']['id']}"
        #)
    
    userInfo = GetUserInfo(payload['access_token'])
    print(payload['access_token'])

    #groupsList = GetAllGroups(payload['access_token'], userInfo['id'])
    #print(groupsList)

    window = Tk()  
    window.title("Добро пожаловать в приложение VK_API")  
    window.geometry('900x500')   

    link1 = Label(window, text="Привет, " + userInfo['first_name'], fg="blue", cursor="hand2")
    link1.bind("<Button-1>", Callback)
    link1.pack()

    link1 = Label(window, text="ГОО", fg="blue", cursor="hand2")
    link1.bind("<Button-1>", Callback2)
    link1.pack()

    window.mainloop()