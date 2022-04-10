import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


session = vk_api.VkApi(token = '25065c5f99d3dc440d69d76db77c0555b8054d9175074679aa7b5e8355eddf6ad8866c869e51c4515dd52')
LPoll = VkLongPoll(session)

def send_response(id, text):
    session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0})

for event in LPoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
        	if event.from_chat:
        		msg = event.text.lower()
        		id = event.chat_id

        		if msg in ["Привет", "привет"]:
        			send_response(id, "Привет вездекодерам!")