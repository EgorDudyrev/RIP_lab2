#from lab_classes import *
import vk_api

api = vk_api.VkApi().get_api()

print(api.users.get(user_ids='egordudyrev'))


#response = vk_api.VkApi().method(method='users.get',values={'user_ids': 'egordudyrev'})
#print(response)
