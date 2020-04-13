import discord 
from discord import utils

import helptest 
class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))
	
	async def on_raw_reaction_add(self, paylood):
		channel = self.get_channel(paylood.channel_id) # получаем обЪект канала 
     	message = await channel.fetch_message(paylood.message_id) # получаем объект сообщения
     	member = utils.get(message.guild.members, id=paylood.user_id ) # 
    
    try:
    	emoji = str(paylood.emoji) # эмоджик который выбрал юзер
    	role = utils.get(message.guild.roles, id=helptest.ROLES[emoji]) # объект выбранной роли (если есть)
    	
    	if(len(i for i in member.roles if i.id not in helptest.EXCROLES ) <= helptest.MAX_ROLES_PER_USER):
          	await member.add_roles(role)
          	print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
        else:
        	await message.remove_reaction(paylood.emoji, member)
        	print('[SUCCESS] Too many rales for user {0.display_name} has been granted with role {1.name}'.format(member, role))

    except KeyError as e:
    	print('[ERROR] KeyError, no role found for ' + emoji)
    except Exception as e:
    	print(repr(e))

    async def on_raw_reaction_remove(self, paylood):
		pass

		
# RUN
client = MyClient()
client.run(helptest.TOKEN)