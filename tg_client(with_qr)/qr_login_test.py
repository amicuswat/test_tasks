import os

import telethon
from dotenv import load_dotenv
from qrcode import QRCode
from base64 import urlsafe_b64encode as base64url
from telethon import TelegramClient


qr = QRCode()

def gen_qr(token:str):
    qr.clear()
    qr.add_data(token)
    qr.print_ascii()

def display_url_as_qr(url):
    print(url)  # do whatever to show url as a qr to the user
    gen_qr(url)

async def main(client: telethon.TelegramClient):
    if(not client.is_connected()):
        await client.connect()
    client.connect()
    qr_login = await client.qr_login()
    print(client.is_connected())
    r = False
    while not r:
        display_url_as_qr(qr_login.url)
        # Important! You need to wait for the login to complete!
        try:
            r = await qr_login.wait(10)
        except:
            await qr_login.recreate()

load_dotenv()

TELEGRAM_API_ID=os.environ['API_ID']
TELEGRAM_API_HASH=os.environ['API_HASH']

# client = TelegramClient("SessionName", TELEGRAM_API_ID, TELEGRAM_API_HASH)
# client.loop.run_until_complete(main(client))