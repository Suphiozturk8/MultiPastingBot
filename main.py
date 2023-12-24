
import os
import logging
import tempfile
from telethon import TelegramClient, events, Button

from utils import Paste, pastebin_service, get_arg
from config import (
    NAME,
    API_ID,
    API_HASH,
    BOT_TOKEN,
    HELP_MESSAGE,
    START_MESSAGE,
)

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(asctime)s - %(message)s"
)
log = logging.getLogger("TelethonSnippets")

log.info("Bot Connecting...")
try:
    client = TelegramClient(
        NAME,
        api_id=API_ID,
        api_hash=API_HASH
    ).start(bot_token=BOT_TOKEN)
except BaseException as e:
    log.warning(e)
    exit(1)


@client.on(
    events.NewMessage(
        pattern=r"^[.?!/₺#@](paste|nekobin|dpaste|spacebin|pasty|centos|batbin)"
    )
)
async def paste_(event):
    p_service = await pastebin_service(event.raw_text.split(" ")[0])
    paste_msg = await event.client.send_message(
        event.chat_id,
        f"**Pasting into {p_service.capitalize()} service...**"
    )
    replied_msg = await event.get_reply_message()
    txt = get_arg(event)
    message = txt
    if not txt:
        if not replied_msg:
            return await paste_msg.edit(
                "**Please reply to a text or file.**"
            )
        if replied_msg.file:
            temp_dir = tempfile.mkdtemp()
            file_path = os.path.join(
                temp_dir,
                replied_msg.file.name
            )
            await replied_msg.download_media(file_path)
            with open(file_path, "r") as file:
                message = file.read()
            os.remove(file_path)
        elif replied_msg.text:
            message = replied_msg.text

    paste_cls = Paste()
    pasted = await paste_cls.paste_text(
        p_service,
        message
    )
    if not pasted:
        return await paste_msg.edit(
            """
**Paste failed!**
**Please try changing the paste service.**
            """
        )
    await paste_msg.edit(
        f"""
**Pasted to {p_service.capitalize()} service!**

**Url:** `{pasted}`
        """,
        buttons=p_buttons(p_service, pasted),
        link_preview=True
    )
    log.info(pasted)


def p_buttons(p_service, pasted):
    return [
        [
            Button.url(
                f"{p_service.capitalize()}",
                url=f"{pasted}"
            )
        ],
        [
            Button.url(
                "Share",
                url=f"https://telegram.me/share/url?url={pasted}"
            )
        ]
    ]


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
    mention = f"[{event.sender.first_name}](tg://user?id={event.sender.id})"
    await event.reply(
        START_MESSAGE.format(mention),
        link_preview=False
    )


@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
    await event.reply(
        HELP_MESSAGE,
        link_preview=False
    )


log.info("Bot Active ✓")
client.run_until_disconnected()
