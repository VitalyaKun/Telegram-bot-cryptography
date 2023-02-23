import telebot
from telebot import types
import math

import random
import string
import re

bot = telebot.TeleBot('')

#Клавиатура ввыбора языка
leng = types.ReplyKeyboardMarkup(resize_keyboard=True)
leng_en = types.KeyboardButton('English language🇺🇸')
leng_ru = types.KeyboardButton('Русский язык🇷🇺')
leng.add(leng_en)
leng.add(leng_ru)

#Клавиатура выбора способа шифрования на английском языке
cipher_en = types.ReplyKeyboardMarkup(resize_keyboard=True)
simple_replacement = types.KeyboardButton('Simple replacement cipher')
vigenere = types.KeyboardButton('Vigenère cipher')
spc_en  = types.KeyboardButton('Simple permutation cipher')
aphine_en = types.KeyboardButton ('Affine cipher')
back_en = types.KeyboardButton('Back')
cipher_en.add(simple_replacement)
cipher_en.add(vigenere)
cipher_en.add(spc_en)
cipher_en.add(aphine_en)
cipher_en.add(back_en)

#Клавиатура выбора способа шифрования на русском языке
cipher_ru = types.ReplyKeyboardMarkup(resize_keyboard=True)
simple_replacement_ru = types.KeyboardButton('Шифр простой замены')
vigenere_ru = types.KeyboardButton('Шифр Виженера')
spc_ru  = types.KeyboardButton('Шифр простой перестановки')
aphine_ru = types.KeyboardButton ('Афинный шифр')
back_ru = types.KeyboardButton('Назад')
cipher_ru.add(simple_replacement_ru)
cipher_ru.add(vigenere_ru)
cipher_ru.add(spc_ru)
cipher_ru.add(aphine_ru)
cipher_ru.add(back_ru)

#Клавиатура выбора шифровки/дешифровки для шифра простой замены EN
sr_en = types.ReplyKeyboardMarkup(resize_keyboard=True)
encrypt_sr_en = types.KeyboardButton('Simple replacement encryption❤️')
decrypt_sr_en = types.KeyboardButton('Decryption by simple replacement💜')
back_to_method_en = types.KeyboardButton('Back to choosing the encryption method')
sr_en.add(encrypt_sr_en)
sr_en.add(decrypt_sr_en)
sr_en.add(back_to_method_en)

#Клавиатура выбора шифровки/дешифровки для шифра простой замены RU
sr_ru = types.ReplyKeyboardMarkup(resize_keyboard=True)
encrypt_sr_ru = types.KeyboardButton('Шифрование простой заменой❤️')
decrypt_sr_ru = types.KeyboardButton('Дешифрование простой заменой💜')
back_to_method_ru = types.KeyboardButton('Вернутся к выбору способа шифрования') 
sr_ru.add(encrypt_sr_ru)
sr_ru.add(decrypt_sr_ru)
sr_ru.add(back_to_method_ru)

#Клавиатура выбора шифровки/дешифровки для шифра Виженера EN
vig_en = types.ReplyKeyboardMarkup(resize_keyboard=True)
encrypt_vig_en = types.KeyboardButton('Encryption by Vigenère❤️')
decrypt_vig_en = types.KeyboardButton('Decryption by Vigenère💜')
back_to_method_en_for_vig = types.KeyboardButton('Back to list')
vig_en.add(encrypt_vig_en)
vig_en.add(decrypt_vig_en)
vig_en.add(back_to_method_en_for_vig)

#Клавиатура выбора шифровки/дешифровки для шифра Виженера RU
vig_ru = types.ReplyKeyboardMarkup(resize_keyboard=True)
encrypt_vig_ru = types.KeyboardButton('Шифрование Виженером❤️')
decrypt_vig_ru = types.KeyboardButton('Дешифрование Виженером💜')
back_to_method_ru_for_vig = types.KeyboardButton('Вернутся назад') 
vig_ru.add(encrypt_vig_ru)
vig_ru.add(decrypt_vig_ru)
vig_ru.add(back_to_method_ru_for_vig)

#Клавиатура выбора шифровки/дешифровки для шифра Виженера EN
per_en = types.ReplyKeyboardMarkup(resize_keyboard=True)
encrypt_per_en = types.KeyboardButton('Encryption📕')
decrypt_per_en = types.KeyboardButton('Decryption📗')
back_to_method_en_for_per = types.KeyboardButton('Back to list🚪')
per_en.add(encrypt_per_en)
per_en.add(decrypt_per_en)
per_en.add(back_to_method_en_for_per)

#Клавиатура выбора шифровки/дешифровки для шифра Виженера RU
per_ru = types.ReplyKeyboardMarkup(resize_keyboard=True)
encrypt_per_ru = types.KeyboardButton('Шифрование📕')
decrypt_per_ru = types.KeyboardButton('Дешифрование📗')
back_to_method_ru_for_per = types.KeyboardButton('Вернутся назад🚪') 
per_ru.add(encrypt_per_ru)
per_ru.add(decrypt_per_ru)
per_ru.add(back_to_method_ru_for_per)

#Клавиатура выбора шифровки/дешифровки для Афинного шифра EN
aphine_en = types.ReplyKeyboardMarkup(resize_keyboard=True)
encrypt_aphine_en = types.KeyboardButton('Encryption🐶')
decrypt_aphine_en = types.KeyboardButton('Decryption🦊')
back_to_method_en_for_aphine = types.KeyboardButton('Back to list👈🏻')
aphine_en.add(encrypt_aphine_en)
aphine_en.add(decrypt_aphine_en)
aphine_en.add(back_to_method_en_for_aphine)

#Клавиатура выбора шифровки/дешифровки для Афинного шифра RU
aphine_ru = types.ReplyKeyboardMarkup(resize_keyboard=True)
encrypt_aphine_ru = types.KeyboardButton('Шифрование🐶')
decrypt_aphine_ru = types.KeyboardButton('Дешифрование🦊')
back_to_method_ru_for_aphine = types.KeyboardButton('Вернутся назад👈🏻') 
aphine_ru.add(encrypt_aphine_ru)
aphine_ru.add(decrypt_aphine_ru)
aphine_ru.add(back_to_method_ru_for_aphine)

@bot.message_handler(commands=['start'])  
def start_command(message):
	chat_id = message.chat.id
	bot.send_message(chat_id, f"💁🏻‍♀️ Привет, *{message.from_user.first_name}*!\n\nРады тебя видеть в нашем боте!"
		+ "Тут ты сможешь шифровать и дешифровать свои секреты😱\nКак на английском🇺🇸 так и на русском языке🇷🇺.\nПриятного пользования❤️!",
		parse_mode="Markdown", reply_markup=leng)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    text = message.text
    if message.text == 'Русский язык🇷🇺':
        bot.send_message(message.chat.id, 'Вы перешли в интерфейс для русского языка', reply_markup=cipher_ru)
        
    elif message.text == 'English language🇺🇸':
        bot.send_message(message.chat.id, 'You have entered the English language interface', reply_markup=cipher_en)
        
    elif message.text == 'Назад':
        bot.send_message(message.chat.id, 'Вы вернулись в меню выбора языка', reply_markup=leng)
    
    elif message.text == 'Back':
        bot.send_message(message.chat.id, 'You are returned to the language selection menu', reply_markup=leng)
        
    #Шифр протой замены
    elif text == 'Simple replacement cipher':
        bot.send_message(message.chat.id, '💁🏻‍♀️ Would you like to Encrypt or Decrypt?', reply_markup=sr_en)
        
    elif message.text == 'Simple replacement encryption❤️':
        msg = bot.send_message(message.chat.id, 'Enter the text you want to\nEncrypt✅', parse_mode="Markdown")
        bot.register_next_step_handler(msg, sreen)
        
    elif message.text == 'Decryption by simple replacement💜':
        msg = bot.send_message(message.chat.id, 'Enter the text you want to\nDecrypt✅')
        bot.register_next_step_handler(msg, srden)
        
    elif message.text == 'Back to choosing the encryption method':
        bot.send_message(message.chat.id, 'You are back to choosing the encryption method✅', reply_markup=cipher_en)
        
    elif text == 'Шифр простой замены':
        bot.send_message(message.chat.id, '💁🏻‍♀️ Чего бы ты хотел? Зашифровать или расшифровать?', reply_markup=sr_ru)
        
    elif message.text == 'Шифрование простой заменой❤️':
        msg = bot.send_message(message.chat.id, 'Введите текст который хотите\nШифровать✅')
        bot.register_next_step_handler(msg, sreru)
        
    elif message.text == 'Дешифрование простой заменой💜':
        msg = bot.send_message(message.chat.id, 'Введите текст который хотите\nДешифровать✅')
        bot.register_next_step_handler(msg, srdru)
        
    elif message.text == 'Вернутся к выбору способа шифрования':
        bot.send_message(message.chat.id, 'Вы вернулись к выбору метода шифрования✅', reply_markup=cipher_ru)
    
    #Шифр Виженера
    elif text == 'Vigenère cipher':
        bot.send_message(message.chat.id, '💁🏻‍♀️ Would you like to Encrypt or\nDecrypt?', reply_markup=vig_en)
        
    elif message.text == 'Encryption by Vigenère❤️':
        msg = bot.send_message(message.chat.id, 'Enter the text you want to\nEncrypt✅', parse_mode="Markdown")
        bot.register_next_step_handler(msg, vigeen)
        
    elif message.text == 'Decryption by Vigenère💜':
        msg = bot.send_message(message.chat.id, 'Enter the text you want to\nDecrypt✅')
        bot.register_next_step_handler(msg, vigden)
        
    elif message.text == 'Back to list':
        bot.send_message(message.chat.id, 'You are back to choosing the encryption method✅', reply_markup=cipher_en)
        
    elif text == 'Шифр Виженера':
        bot.send_message(message.chat.id, '💁🏻‍♀️ Чего бы ты хотел? Зашифровать или расшифровать?', reply_markup=vig_ru)
        
    elif message.text == 'Шифрование Виженером❤️':
        msg = bot.send_message(message.chat.id, 'Введите текст который хотите\nШифровать✅')
        bot.register_next_step_handler(msg, vigeru)
        
    elif message.text == 'Дешифрование Виженером💜':
        msg = bot.send_message(message.chat.id, 'Введите текст который хотите\nДешифровать✅')
        bot.register_next_step_handler(msg, vigdru)
        
    elif message.text == 'Вернутся назад':
        bot.send_message(message.chat.id, 'Вы вернулись к выбору метода шифрования✅', reply_markup=cipher_ru)
        
    #Шифр простой перестановки
    elif text == 'Simple permutation cipher':
        bot.send_message(message.chat.id, '💁🏻‍♀️ Would you like to Encrypt or\nDecrypt?', reply_markup=per_en)
        
    elif message.text == 'Encryption📕':
        msg = bot.send_message(message.chat.id, 'Enter the text you want to\nEncrypt✅', parse_mode="Markdown")
        bot.register_next_step_handler(msg, pereen)
        
    elif message.text == 'Decryption📗':
        msg = bot.send_message(message.chat.id, 'Enter the text you want to\nDecrypt✅')
        bot.register_next_step_handler(msg, perden)
        
    elif message.text == 'Back to list🚪':
        bot.send_message(message.chat.id, 'You are back to choosing the encryption method✅', reply_markup=cipher_en)
        
    elif text == 'Шифр простой перестановки':
        bot.send_message(message.chat.id, '💁🏻‍♀️ Чего бы ты хотел? Зашифровать или расшифровать?', reply_markup=per_ru)
        
    elif message.text == 'Шифрование📕':
        msg = bot.send_message(message.chat.id, 'Введите текст который хотите\nШифровать✅')
        bot.register_next_step_handler(msg, pereru)
        
    elif message.text == 'Дешифрование📗':
        msg = bot.send_message(message.chat.id, 'Введите текст который хотите\nДешифровать✅')
        bot.register_next_step_handler(msg, perdru)
        
    elif message.text == 'Вернутся назад🚪':
        bot.send_message(message.chat.id, 'Вы вернулись к выбору метода шифрования✅', reply_markup=cipher_ru)
#Для шифра простой замены
def sreen(message):
    text = message.text
    if message.text:
        bot.send_message(message.chat.id, encrypt(message.text))

def srden(message):
    text = message.text
    if message.text:
        bot.send_message(message.chat.id, decrypt(message.text))

def sreru(message):
    text = message.text
    if message.text:
        bot.send_message(message.chat.id, ruencrypt(message.text))

def srdru(message):
    text = message.text
    if message.text:
        bot.send_message(message.chat.id, rudecrypt(message.text))

#Для шифра Виженера
def vigeen(message):
    text = message.text
    if message.text:
        bot.send_message(message.chat.id, vigener_en(message.text))

def vigden(message):
    text = message.text
    if message.text:
        bot.send_message(message.chat.id, vig_decrypt_en(message.text))

def vigeru(message):
    text = message.text
    if message.text:
        bot.send_message(message.chat.id, vigener_ru(message.text))

def vigdru(message):
    text = message.text
    if message.text:
        bot.send_message(message.chat.id, vig_decrypt_ru(message.text))
        
#Для шифра простой замены
def pereen(message):
    text = message.text
    if message.text:
        bot.send_message(message.chat.id, encrypt_per_en(message.text))

def perden(message):
    text = message.text
    if message.text:
        bot.send_message(message.chat.id, decrypt_per_en(message.text))

def pereru(message):
    text = message.text
    if message.text:
        bot.send_message(message.chat.id, encrypt_per_ru(message.text))

def perdru(message):
    text = message.text
    if message.text:
        bot.send_message(message.chat.id, decrypt_per_ru(message.text))

#Для шифра простой замены
def encrypt(text):
    text = text.upper()
    reg = re.compile('[^A-Z]')
    text = reg.sub('', text)
    alphabet = 'CDEFGHIJKLMNOPQRSTUVWXYZAB'
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    textEncrypted = ""
    for i in text:
        textEncrypted += alphabet[alp.index(i)]
    return textEncrypted

def decrypt(text):
    text = text.upper()
    reg = re.compile('[^A-Z]')
    text = reg.sub('', text)
    alphabet = 'CDEFGHIJKLMNOPQRSTUVWXYZAB'
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    textDecrypted = ""
    for i in text:
        textDecrypted += alp[alphabet.index(i)]
    return textDecrypted
    
def ruencrypt(text):
    text = text.upper()
    reg = re.compile('[^А-Я]')
    text = reg.sub('', text)
    alphabet = 'ЛМЗАИЕУКХЭНВЧРЬГПЫДОЩЯЁФЖЮЙБТЪСШЦ'
    alp = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    RUtextEncrypted = ""
    for i in text:
        RUtextEncrypted += alphabet[alp.index(i)]
    return RUtextEncrypted

def rudecrypt(text):
    text = text.upper()
    reg = re.compile('[^А-Я]')
    text = reg.sub('', text)
    alphabet = 'ЛМЗАИЕУКХЭНВЧРЬГПЫДОЩЯЁФЖЮЙБТЪСШЦ'
    alp = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    RUtextDecrypted = ""
    for i in text:
        RUtextDecrypted += alp[alphabet.index(i)]
    return RUtextDecrypted
    
#Для шифра Виженера
def vigener_en(text):
    text = text.upper()
    reg = re.compile('[^A-Z]')
    text = reg.sub('', text)
    key = 'MOLOKO'
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key *= len(text) // len(key) + 1
    Encrypt = ''
    for i, j in enumerate(text):
        gg = alphabet.index(j) + alphabet.index(key[i])
        Encrypt += alphabet[gg % 26]
    return Encrypt
    
def vig_decrypt_en(text):
    text = text.upper()
    reg = re.compile('[^A-Z]')
    text = reg.sub('', text)
    key = 'MOLOKO'
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key *= len(text) // len(key) + 1
    Decrypted = '' 
    for i, j in enumerate(text):
        gg = alphabet.index(j) - alphabet.index(key[i])
        Decrypted += alphabet[gg % 26]
    return Decrypted
    
def vigener_ru(text):
    text = text.upper()
    reg = re.compile('[^А-Я]')
    text = reg.sub('', text)
    key = 'МОЛОКО'
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    key *= len(text) // len(key) + 1
    Encrypt = ''
    for i, j in enumerate(text):
        gg = alphabet.index(j) + alphabet.index(key[i])
        Encrypt += alphabet[gg % 33]
    return Encrypt
    
def vig_decrypt_ru(text):
    text = text.upper()
    reg = re.compile('[^А-Я]')
    text = reg.sub('', text)
    key = 'МОЛОКО'
    key *= len(text) // len(key) + 1
    Decrypted = ''
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    for i, j in enumerate(text):
        gg = alphabet.index(j) - alphabet.index(key[i])
        Decrypted += alphabet[gg % 33]
    return Decrypted
    
#Функция шифрования текстом с помощью перестановки
def encrypt_per_en(message):
    message = message.upper()
    reg = re.compile('[^A-Z]')
    message = reg.sub('', message)
    key = "CODE"
    cipher = ""
    k_indx = 0
    msg_len = float(len(message))
    msg_lst = list(message)
    key_lst = sorted(list(key))
    col = len(key)
    row = int(math.ceil(msg_len / col))
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
    matrix = [msg_lst[i: i + col]
              for i in range(0, len(msg_lst), col)]
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx]
                           for row in matrix])
        k_indx += 1

    return cipher


#Функция дешифрования кода с помощью перестановки
def decrypt_per_en(message):
    message = message.upper()
    reg = re.compile('[^A-Z]')
    message = reg.sub('', message)
    key = "CODE"    
    msg = ""
    k_indx = 0
    msg_indx = 0
    msg_len = float(len(message))
    msg_lst = list(message)
    col = len(key)
    row = int(math.ceil(msg_len / col))
    key_lst = sorted(list(key))
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])

        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        return "Простите, но мы не можем обработать повторения 😔"
    null_count = msg.count('_')
    if null_count > 0:
        return msg[: -null_count]

    return msg


def encrypt_per_ru(message):
    message = message.upper()
    reg = re.compile('[^А-Я]')
    message = reg.sub('', message)
    key = "КОДА"
    cipher = ""
    k_indx = 0
    msg_len = float(len(message))
    msg_lst = list(message)
    key_lst = sorted(list(key))
    col = len(key)
    row = int(math.ceil(msg_len / col))
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
    matrix = [msg_lst[i: i + col]
              for i in range(0, len(msg_lst), col)]
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx]
                           for row in matrix])
        k_indx += 1

    return cipher

#Функция дешифрования кода с помощью перестановки
def decrypt_per_ru(message):
    message = message.upper()
    reg = re.compile('[^А-Я]')
    message = reg.sub('', message)
    key = "КОДА"
    msg = ""
    k_indx = 0
    msg_indx = 0
    msg_len = float(len(message))
    msg_lst = list(message)
    col = len(key)
    row = int(math.ceil(msg_len / col))
    key_lst = sorted(list(key))
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])

        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        return "Простите, но мы не можем обработать повторения 😔"
    null_count = msg.count('_')
    if null_count > 0:
        return msg[: -null_count]

    return msg

if __name__ == '__main__':
    bot.polling(none_stop=True)