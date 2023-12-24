
# MultiPastingBot

## Overview
This Telegram bot is designed to make it easy to share pieces of text or code. The bot will paste text through various services and generate shareable links.

## Features
1. You can use the corresponding commands to share a snippet of text or code.
    - For example: `/paste <text or reply_file>`.
2. The bot processes the given content with the selected paste service and generates a shareable link.
3. You can take the generated link and share it as you wish.

## Active Bot
Example of MultiPastingBot, founded by [Mert{🐈}](https://t.me/theliec), running as [Paste Code All in One](https://t.me/codepasterobot).
Thank you [Mert](https://github.com/fswair) ❤️

## Usage
1. Sending text or files with the default paste service:
    - `/paste` (spaceb.in)
2. Options to use different pasting services:
    - `/nekobin` (nekobin.com)
    - `/dpaste` (dpaste.org)
    - `/spacebin` (spaceb.in)
    - `/pasty` (pasty.lus.pm)
    - `/centos` (paste.centos.org)
    - `/batbin` (batbin.me)

## Installation
1. Clone the repository: `git clone https://github.com/suphiozturk8/MultiPastingBot.git && cd MultiPastingBot`
2. Install the dependencies: `pip install -r requirements.txt`
3. Set your Telegram bot token in the `config.py` file.
4. Run the bot: `python main.py`

## Licence
This project is licensed under the [MIT Licence](LICENSE).
