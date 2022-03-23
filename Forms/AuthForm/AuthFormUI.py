from tkinter import *
from AuthFormBL import *

path_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path_dir)

from MainForm.MainFormUI import MainForm

def GetTokenFromFile(event):
    str = ReadFromFile(TOKEN_FILE_PATH)
    if str != "":
        key = LoadKey()
        Decrypt(TOKEN_FILE_PATH, key)
        str = ReadFromFile(TOKEN_FILE_PATH)
        print(str)
        if str != "":
            txt1.delete('1.0', END)
            txt1.insert('1.0', str)
            Encrypt(TOKEN_FILE_PATH, key)
        else:
            ShowWarning()
    else:
        ShowWarning()

def RedirectToMainForm(event):
    str = txt1.get(1.0, END).replace('\n', "")
    SetTokenToFile(str)
    if str.find("access_token") != -1 and str.find("expires_in") != -1 and str.find("user_id") != -1:
        str = str.replace("=","&").split("&")
        access_token = str[1]
        expires_in = str[3]
        user_id = str[5]
        print("acces_token=" + access_token + "expires_in=" + expires_in, "user_id=" + user_id)
        payload = {
            'access_token': access_token,
            'expires_in': expires_in,
            'user_id': user_id,
        }
    else:
        mb.showinfo('Ошибка', 'Неправильная ссылка!\nПосле успешной авторизации скопируйте ссылку сюда!')
    return MainForm(event, payload)

window = Tk()  
window.title("Добро пожаловать в приложение VK_API")  
window.geometry('900x250')

lbl3 = Label(window, text="Если вы уже входили через это приложение, нажмите: ")  
lbl3.pack()

link3 = Label(window, text="Получить токен", fg="blue", cursor="hand2")
link3.bind("<Button-1>", GetTokenFromFile)
link3.pack()


lbl1 = Label(window, text="Для получения Acces токена перейди по ссылке,\n авторизуйтесь и скопируйте ссылку на которую вас перенаправит после авторизации:")  
lbl1.pack()

link1 = Label(window, text="Авторизоваться", fg="blue", cursor="hand2")
link1.bind("<Button-1>", Auth)
link1.pack()

lbl2 = Label(window, text="Скопируйте ссылку на которую вас направило после успешной авторизации сюда:")  
lbl2.pack()

txt1 = Text(window,width=50, height=5)
txt1.pack()

link2 = Label(window, text="Перейти на сайт для работы с api вк", fg="blue", cursor="hand2")
link2.bind("<Button-1>", RedirectToMainForm)
link2.pack()


window.mainloop()