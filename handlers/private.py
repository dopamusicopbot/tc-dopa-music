from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_image("https://telegra.ph/file/088455df524bc7d105c44.jpg")
    await message.reply_text(
        f"""**ʜᴇʏ, I'm {bn} 🎵

ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ'ꜱ ᴠᴏɪᴄᴇ ᴄᴀʟʟ. ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [╚⌬•T͜͡ᴄ፨D͜͡ᴏᴘᴀ፨U͜͡sᴇʀ•<A͜͡ғᴋ>•⌬╝](https://t.me/nIkLaUsMiKaElSn).

ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘʟᴀʏ ᴍᴜꜱɪᴄ ꜰʀᴇᴇʟʏ!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🛠", url="https://github.com/Dopamusicbot/tc-dopa-music")
                  ],[
                    InlineKeyboardButton(
                        "💬 Gʀᴏᴜᴘ", url="https://t.me/UNIVERSAL_OP_CHAT"
                    ),
                    InlineKeyboardButton(
                        "✨Sᴏᴜʀᴄᴇ Cᴏᴅᴇ✨", url="https://github.com/Dopamusicbot/tc-dopa-music"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Mᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ᴛᴏ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/nIkLaUsMiKaElSn"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ᴀʀᴇ ʏʀʀ ᴊɪɴᴅᴀ ʜᴏᴏ ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡Sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ⚡", url="https://github.com/Dopamusicbot/tc-dopa-music")
                ]
            ]
        )
   )


