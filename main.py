import vk_api
import random
import datetime
import time


#для того чтобы получить token cоздаёшь своё приложения переходишь по ссылке, не забывая после client_id указать id приложения, указывая необходимые права (тут лишние)
#https://oauth.vk.com/authorize?client_id=1&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,photos,video,audio,groups,wall,messages&response_type=token&v=5.92&state=123456
#разрешаешь доступ и тебя перекидывать на страницу где в ссылке на страницу есть access_token который тебе и нужен

file = open('pablics.txt')
res = open('results.txt', 'a')
res.write(datetime.datetime.now().isoformat() + '\n')
rand = random.randint(0, 2000000)
pause = random.randint(2, 10)
vk = vk_api.VkApi(login=your_login, password=your_password, token=your_token)
for owner_id in file:
    try:
        owner_id = '-' + owner_id
        time.sleep(pause)
        vk.method('wall.post', {'owner_id': int(owner_id), 'from_group': '1', 'message': "your_message"})
    except Exception as e:
        res.write(owner_id.strip() + str(e) + '\n')
    else:
        res.write(owner_id.strip() + '\n')
res.write('\n')
res.close()
