import os
from pyrogram import Client

API_ID = 35368782
API_HASH = "72dc553687bd0437165b5c9bbaca4447"
STRING_SESSION = os.getenv("STRING_SESSION")

if not STRING_SESSION:
    raise ValueError("STRING_SESSION is missing from GitHub Secrets.")

app = Client(
    "moriarty_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION
)

def main():
    print("Bot is starting...")
    app.run()

if __name__ == "__main__":
    main()
