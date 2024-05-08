import logging 
from os import environ
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
SESSION = environ.get("SESSION")
TIME = int(environ.get("TIME", "60"))
CHANNEL_ID = int(environ.get("CHANNEL_ID", "-1001815790599"))
PORT = environ.get("PORT", "8080")
WEBHOOK = environ.get("WEBHOOK", True)


if SESSION is not None:
    session = StringSession(str(SESSION))
else:
    session = "pyrobot"

try:
    client = TelegramClient(
        session=session,
        api_id=API_ID,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged
    )

async def start(self):
    await app.start()
    await app.send_message(chat_id=int(LOG_CHANNEL), text="Restarted 🤒")
    appe = web.AppRunner(await web_server())
    await appe.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(appe, bind_address, PORT).start()        
    idle()
    
except Exception as e:
    print(e)

if __name__ == '__main__':
    bot = Bot()
    bot.run()
