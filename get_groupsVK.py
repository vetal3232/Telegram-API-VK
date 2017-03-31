import vk
from vk_main import MyVkData
session = vk.AuthSession(app_id=MyVkData.APP_ID,user_login=MyVkData.LOGIN   ,user_password=MyVkData.PASSWORD)
vkapi = vk.API(session)

groups = vkapi.groups.get(user_id=MyVkData.MY_USER_ID, extended=1)
print(groups)
groups_count = groups[0]
print ('Колличество групп пользователя: {0}'.format(groups_count))
groups=groups[1:]
[print (group) for group in groups]