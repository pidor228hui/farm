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
            print('Комментарий написан!')
            pizda = 0
            while pizda == 0:
                try:
                    api.wall.createComment(owner_id = -174105461, post_id = 6713149, message = 'Ферма') #не трогать
                    pizda = pizda + 1
                except Exception as er:
                    pizda = pizda + 1
                    print(er)
                    
        time.sleep(14500)
farm()
           
