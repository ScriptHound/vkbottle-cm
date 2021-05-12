from typing import Union

from vkbottle.bot import Message, rules


class AdminRule(rules.ABCMessageRule):
    def __init__(self, return_admins: bool = False):
        self.return_admins = return_admins

    async def check(self, message: Message) -> Union[dict, bool]:
        items = (
            await message.ctx_api.messages.get_conversations_by_id(
                peer_ids=message.peer_id)
        ).items

        if items:
            chat_settings = items[0].chat_settings
            admins = [chat_settings.owner_id, *chat_settings.admin_ids]
        else:
            return False

        if message.from_id not in admins:
            await message.answer("У вас нет доступа к этой команде.")
            return False

        if self.return_admins:
            return {"admins": admins}
        return True
