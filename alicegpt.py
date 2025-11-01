from .. import loader, utils
from telethon.tl.types import Message
from telethon import functions
from telethon import events
from datetime import timedelta
import random
version = (1, 0, 0)


bot1 = ["@alice_ya_bot", 8310045254]


@loader.tds
class AliceGPT(loader.Module):
    """ALICE GPT"""

    strings = {
        "name": "AliceGPT",
    }

    @loader.command()
    async def alice(self, message):
        """<текст> - запрос к Алисе"""
        chat = bot1[1]
        reply = await message.get_reply_message()
        text = reply.raw_text if reply else message.text[5:]
        if len(text) < 3:
         await utils.answer(message, "🤦🏼‍♀️ <b>Кошмар!\nСлишком короткий запрос.</b>")
         return
        await utils.answer(message, "💅🏻 <b>Алиса думает...</b>")
        async with message.client.conversation(bot1[1]) as conv:

            response = await conv.send_message(text)

            response1 = await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))

            if "Начинаю творить, вернусь через несколько секунд" in response1.text:
             response2 = await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
             await utils.answer(message, f" 🤷🏼‍♀️ <b>твой вопрос:</b> \n{text}\n\n💅🏻 <b>ответ Алисы:</b>\n{response2.photo}")
    await self._client.forward_messages(chat, {response2}, me)
    await response.delete()
    await response1.delete()
    await response2.delete()
             return
            elif "Рисую, через несколько секунд будет готово" in response1.text:
             response2 = await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
             await utils.answer(message, f" 🤷🏼‍♀️ <b>твой вопрос:</b> \n{text}\n\n💅🏻 <b>ответ Алисы:</b>\n{response2.photo}")
             await self._client.forward_messages(chat, {response2}, me)
             await response.delete()
             await response1.delete()
             await response2.delete()
             return
            elif "Дайте мне несколько секунд" in response1.text:
                response2 = await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
                await utils.answer(message, f" 🤷🏼‍♀️ <b>твой вопрос:</b> \n{text}\n\n💅🏻 <b>ответ Алисы:</b>\n{response2.photo}")
                await self._client.forward_messages(chat, {response2}, me)
                await response.delete()
                await response1.delete()
                await response2.delete()
                return
            else:
             await utils.answer(message, f" 🤷🏼‍♀️ <b>твой вопрос:</b> \n{text}\n\n💅🏻 <b>ответ Алисы:</b>\n{response1.text}")
             await response.delete()
             await response1.delete()

    @loader.command()
    async def aliceclear(self, message):
        """- очищает историю переписки с Алисой (контекст)"""
        chat = bot1[1]
        text = "🧹 Новый диалог"
        async with message.client.conversation(bot1[0]) as conv:
            response = await conv.send_message(text)
            response1 = await conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
            await utils.answer(message, "✅<b>Контекст успешно сброшен!</b>")
            await response.delete()
            await response1.delete()