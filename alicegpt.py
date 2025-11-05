version = (1, 0, 0)

# meta developer: 

import random
from datetime import timedelta
from telethon import events
from telethon import functions
from telethon.tl.types import Message
from .. import loader, utils

bot1 = ["@alice_ya_bot", 8310045254]
@loader.tds
class AliceGPT(loader.Module):
    """Нейросеть Алиса"""

    strings = {
        "name": "AliceGPT",
    }
           
    @loader.command()
    async def alice(self, message):
        """<текст> - спросить Алису"""
        chat = bot1[1]
        reply = await message.get_reply_message()
        text = reply.raw_text if reply else message.text[5:]
        if len(text) < 3:
         await utils.answer(message, "🙅🏻‍♀️<b>Ошибка!\nСлишком короткий запрос.</b>")
         return
        await utils.answer(message, "🤷🏻‍♀️<b>Алиса думает...</b>")
        async with message.client.conversation(bot1[0]) as conv:
            
            response = await conv.send_message(text)
            
            response1 = await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
            
            photo = await message.client.send_file(message.to_id, response2.media)
            
            if "Рисую, через несколько секунд будет готово" in response1.text:
             response2 = await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
             await utils.answer(message, {photo})
             await response.delete()
             await response1.delete()
             await response2.delete()
             return
            elif "Дайте мне несколько секунд" in response1.text:
             response2 = await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
             await utils.answer(message, {photo})
             await response.delete()
             await response1.delete()
             await response2.delete()
             return   
            elif "Начинаю творить, вернусь через несколько секунд" in response1.text:
             response2 = await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
             await utils.answer(message, {photo})
             await response.delete()
             await response1.delete()
             await response2.delete()
             return    
            else:
             await utils.answer(message, f"💁🏻‍♀️ <b>Ответ Алисы:</b>\n{response1.text}")
             await response.delete()
             await response1.delete()


            	
    @loader.command()
    async def aliceclear(self, message):
        """- очищает историю переписки с Алисой (контекст)"""
        chat = bot1[1]
        text = "/clear"
        async with message.client.conversation(bot1[0]) as conv:
            response = await conv.send_message(text)
            response1 = await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
            await utils.answer(message, "🙎🏻‍♀️<b>Контекст успешно очищен!</b>")
            await response.delete()
            await response1.delete()
