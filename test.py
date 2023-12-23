import asyncio
import unittest
from utils import Paste

class TestPasteServices(unittest.IsolatedAsyncioTestCase):
    async def test_nekobin_paste(self):
        paste = Paste()
        text = "Test text for Nekobin"
        result = await paste.paste_to_nekobin(text)
        self.assertIsNotNone(result)

    async def test_spacebin_paste(self):
        paste = Paste()
        text = "Test text for Spacebin"
        result = await paste.paste_to_spacebin(text)
        self.assertIsNotNone(result)

    async def test_dpaste_paste(self):
        paste = Paste()
        text = "Test text for Dpaste"
        result = await paste.paste_to_dpaste(text)
        self.assertIsNotNone(result)

    async def test_pasty_paste(self):
        paste = Paste()
        text = "Test text for Pasty"
        result = await paste.paste_to_pasty(text)
        self.assertIsNotNone(result)

    async def test_centos_paste(self):
        paste = Paste()
        text = "Test text for Centos"
        result = await paste.paste_to_centos(text)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
    