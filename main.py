import os
from pyrogram import Client

# المعلومات مثبتة هنا مباشرة حتى تشتغل بدون أي مشاكل
API_ID = 35368782
API_HASH = "72dc553687bd0437165b5c9bbaca4447"
STRING_SESSION = os.getenv("STRING_SESSION")

# إعداد عميل بايروگرام
app = Client(
    "moriarty_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION
)

if __name__ == "__main__":
    print("Starting bot session...")
    app.run()
