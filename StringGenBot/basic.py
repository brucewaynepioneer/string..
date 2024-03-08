from data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

gif = "start.mp4"
# Start Message
@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    user = await bot.get_me()
    mention = user.mention
    await bot.send_animation(
        msg.chat.id,
        animation=gif,
        caption=f"""Welcome to String Bot!""",
        reply_markup=InlineKeyboardMarkup(Data.buttons)
    )
