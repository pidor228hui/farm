import vk_api, traceback, random as r
import time
import random
import re
from vk_api.longpoll import VkLongPoll, VkEventType
from termcolor import colored
from random import randint

tokenakka = []

def farm():
    with open('tokens.txt') as file1:
        tokenakka = [row.strip() for row in file1]
    while True:
        for result in tokenakka:
            vk_session = vk_api.VkApi(token=result)
            api = vk_session.get_api()
            print(result)
            pizda = 0
            while pizda == 0:
                try:
                    api.wall.createComment(owner_id = -174105461, post_id = 35135, message = 'Ферма') #не трогать
                    time.sleep(3)
                    api.messages.send(user_id = Сюда айди осн акк, где бот будет писать что отправил смс, message = 'Готово', random_id = r.randint(1,2048)) #Eсли отправка смс не нужна, можно удалить эту строку с time.sleep
                    pizda = pizda + 1
                except Exception as er:
                    pizda = pizda + 1
                    print(er)
                    
        time.sleep(14500)
farm()
           
