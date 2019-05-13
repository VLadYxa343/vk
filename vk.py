import vk_api
import time

token = "7fd7279a13fbbc09c8fb36170d785bed341f47946bfc8433d14f8ed292b49bcea229ddb0b6e0be435a197"
vk_session = vk_api.VkApi(token=token)

while True:
    vk_session.method("messages.send", {"peer_id": -181018057, "message": "Бонус", "random_id": 0})
    time.sleep(11800)
