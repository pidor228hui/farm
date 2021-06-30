import time
import vk_api
import random

from threading import Thread

nb = '🍻алкаши🍻'
#   Вводишь нужное название беседы


def main(tokk):
    while True:
        time.sleep(random.randint(0, 5))
        vk_session = vk_api.VkApi(token=tokk)
        vk = vk_session.get_api()
        while True:
            try:
                sm = vk.messages.searchConversations(q=f'{nb}')['items'][0]['peer']['id']
                time.sleep(random.randint(0, 5))
                cid = vk.wall.createComment(owner_id=-174105461,
                                            post_id=6713149,
                                            message='ферма')['comment_id']
                print('Комментарий оставлен')
                rt = vk.wall.getComments(owner_id=-174105461,
                                         post_id=6713149,
                                         comment_id=cid)['items'][0]['text']
                print(f'Ответ ириса: {rt}')
                if rt[:1] == '✅':
                    coin = rt.split()[3][1:]
                    try:
                        vk.messages.send(peer_id=sm,
                                         random_id=0,
                                         message=f'бкоин {coin}')
                        print('Сообщение в беседу доставлено\nЗасыпаю.')
                    except Exception as er_mg:
                        print(f'Произошла ошибка {er_mg}\nВероятно, данного аккаунта нету в нужной беседе.')
                else:
                    print('НЕЗАЧЁТ!!!')
            except Exception as er:
                print(er)
            time.sleep(14500)


tokens = len(open('tokens.txt').readlines())
f = open('tokens.txt')
c = 0
data = f.read()
while c != tokens:
    tok = data.split('\n')[c]
    c = c + 1
    try:
        w = Thread(target=main, args=(tok,))
        w.start()
    except:
        time.sleep(1)