from cryptography.fernet import Fernet
import sys, os

path_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path_dir)

from ClientConfiguration.ClientConfiguration import *

def WriteKey():
# Создаем ключ и сохраняем его в файл
    key = Fernet.generate_key()
    with open(CRYPTO_KEY_PATH, 'wb') as key_file:
        key_file.write(key)

def LoadKey():
# Загружаем ключ 'crypto.key' из текущего каталога
    return open(CRYPTO_KEY_PATH, 'rb').read()

def Encrypt(filename, key):
# Зашифруем файл и записываем его
    f = Fernet(key)
    with open(filename, 'rb') as file:
        # прочитать все данные файла
        file_data = file.read()
    # Зашифровать данные
    encrypted_data = f.encrypt(file_data)
    # записать зашифрованный файл
    with open(filename, 'wb') as file:
        file.write(encrypted_data)
    
def Decrypt(filename, key):
# Расшифруем файл и записываем его
    f = Fernet(key)
    with open(filename, 'rb') as file:
        # читать зашифрованные данные
        encrypted_data = file.read()
    # расшифровать данные
    decrypted_data = f.decrypt(encrypted_data)
    # записать оригинальный файл
    with open(filename, 'wb') as file:
        file.write(decrypted_data)

# запись в файл
def WriteToFile(filename, str):
    f = open(filename, 'w+')
    f.seek(0)
    f.write(str)
    f.close()

# чтение с файла
def ReadFromFile(filename):
    f = open(filename, 'r')
    str = f.read()
    f.close()
    return str