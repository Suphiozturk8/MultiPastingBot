
import re
import json
from httpx import AsyncClient


class Paste:
    def __init__(self) -> None:
        self.nekobin_api = "https://nekobin.com/api/documents"
        self.spacebin_api = "https://spaceb.in/api/v1/documents"
        self.dpaste_api = "https://dpaste.org/api/"
        self.pasty_api = "https://pasty.lus.pm/api/v1/pastes"
        self.centos_api = "https://paste.centos.org/api/create?apikey=5uZ30dTZE1a5V0WYhNwcMddBRDpk6UzuzMu-APKM38iMHacxdA0n4vCqA34avNyt"
        self.batbin_api = "https://batbin.me/api/v2/paste"

        self.nekobin = "https://nekobin.com"
        self.spacebin = "https://spaceb.in"
        self.pasty = "https://pasty.lus.pm"
        self.batbin = "https://batbin.me"

    async def paste_text(self, paste_bin: str, text: str):
        if paste_bin == "spacebin":
            return await self.paste_to_spacebin(text)
        elif paste_bin == "dpaste":
            return await self.paste_to_dpaste(text)
        elif paste_bin == "nekobin":
            return await self.paste_to_nekobin(text)
        elif paste_bin == "pasty":
            return await self.paste_to_pasty(text)
        elif paste_bin == "centos":
            return await self.paste_to_centos(text)
        elif paste_bin == "batbin":
            return await self.paste_to_batbin(text)
        else:
            return "**Invalid paste service selected!**"

    async def check_status(self, resp_status: int, status_code: int):
        if resp_status != status_code:
            return "oh no"
        else:
            return "casper"

    async def paste_to_nekobin(self, text: str):
        async with AsyncClient() as nekoc:
            data = {"content": text}
            resp = await nekoc.post(
                self.nekobin_api,
                json=data
            )
            chck = await self.check_status(
                resp.status_code, 201
            )
            if not chck == "casper":
                return None
            else:
                jsned = resp.json()
                return f"{self.nekobin}/{jsned['result']['key']}"

    async def paste_to_spacebin(self, text: str):
        async with AsyncClient() as spacbc:
            data = {
                "content": text,
                "extension": "md"
            }
            resp = await spacbc.post(
                self.spacebin_api,
                data=data
            )
            chck = await self.check_status(
                resp.status_code, 201
            )
            if not chck == "casper":
                return None
            else:
                jsned = resp.json()
                return f"{self.spacebin}/{jsned['payload']['id']}"

    async def paste_to_dpaste(self, text: str):
        async with AsyncClient() as dpc:
            data = {"content": text}
            resp = await dpc.post(
                self.dpaste_api,
                data=data
            )
            chck = await self.check_status(
                resp.status_code, 200
            )
            if not chck == "casper":
                return None
            else:
                return resp.text.replace('"', "")

    async def paste_to_pasty(self, text: str):
        async with AsyncClient() as pstyc:
            data = {"content": text}
            resp = await pstyc.post(
                self.pasty_api,
                data=json.dumps(data)
            )
            chck = await self.check_status(
                resp.status_code, 200
            )
            if not chck == "casper":
                return None
            else:
                jsned = resp.json()
                return f"{self.pasty}/{jsned['id']}"

    async def paste_to_centos(self, text: str):
        async with AsyncClient() as cntsc:
            data = {"text": text}
            resp = await cntsc.post(
                self.centos_api,
                data=data
            )
            chck = await self.check_status(
                resp.status_code, 200
            )
            if not chck == "casper":
                return None
            else:
                return resp.text.replace("\n", "")

    async def paste_to_batbin(self, text: str):
        async with AsyncClient() as btbnc:
            create_config = {
                "headers": {
                    "Content-Type": "text/plain;charset=utf-8"
                }
            }
            resp = await btbnc.post(
                self.batbin_api,
                content=text,
                **create_config
            )
            chck = await self.check_status(
                resp.status_code, 200
            )
            if not chck == "casper":
                return None
            else:
                jsned = resp.json()
                return f"{self.batbin}/{jsned['message']}"


def get_arg(message: str):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


async def pastebin_service(text: str):
    if re.search(r'\bdpaste\b', text):
        pastebin = "dpaste"
    elif re.search(r'\bspacebin\b', text):
        pastebin = "spacebin"
    elif re.search(r'\bnekobin\b', text):
        pastebin = "nekobin"
    elif re.search(r'\bpasty\b', text):
        pastebin = "pasty"
    elif re.search(r'\bcentos\b', text):
        pastebin = "centos"
    elif re.search(r'\bbatbin\b', text):
        pastebin = "batbin"
    else:
        pastebin = "spacebin"
    return pastebin
