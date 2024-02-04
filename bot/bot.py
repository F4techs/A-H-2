from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.enums import ParseMode

import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.MARKDOWN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_respond(message: Message) -> None:
    """
    Handler for '/start' commands.
    Sends START_PLACEHOLDER message
    :param message: message object
    :return: None
    """
    await message.answer(config.START_PLACEHOLDER)

@dp.message(Command('delete_context'))
async def clear_context(message: Message) -> None:
    """
    Handler for '/delete_context' command.
    Deletes the context of the conversation with the user
    :param message: message object
    :return: None
    """
    await message.answer(config.CLEAR_CONTEXT_ANSWER)

@dp.message(Command('follow'))
async def follow_command(message: Message) -> None:
    """
    Handler for '/follow' command.
    Sends a custom reply message for the follow command.
    :param message: message object
    :return: None
    """
    await message.answer("Thank you for following! We appreciate your support.")

async def main() -> None:
    """
    Run the polling
    :return: None
    """
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
