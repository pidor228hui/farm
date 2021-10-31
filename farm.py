import time
import vk_api
import random

from threading import Thread


def main(tokk):
    while True:
        time.sleep(random.randint(0, 5))
        vk_session = vk_api.VkApi(token=tokk)
        vk = vk_session.get_api()
        user_name = f"{vk_session.method('account.getProfileInfo')['first_name']} {vk_session.method('account.getProfileInfo')['last_name']}"
        while True:
            try:
                cid = vk.wall.createComment(owner_id=-174105461,
                                            post_id=6713149,
                                            message='ферма')['comment_id']
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