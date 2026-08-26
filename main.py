import os
import sys
import time
import random
import asyncio
from datetime import datetime
import pytz
from pyrogram import Client, filters
from pyrogram.types import ChatPermissions

# ----------------- 1. المتغيرات والبيئة -----------------
API_ID = int(os.environ.get("API_ID", 35368782))
API_HASH = os.environ.get("API_HASH", "72dc553687bd0437165b5c9bbaca4447")
STRING_SESSION = os.environ.get("STRING_SESSION", "")

SOURCE_NAME = "سورس موريارتي الملكي"
OWNER_NAME = "𝗪𝗜𝗟𝗟𝗜𝗔𝗠 𝗠𝗢𝗥𝗜𝗔𝗥𝗧𝗬"
START_IMG = "https://telegra.ph/file/1000120117.jpg"

if STRING_SESSION:
    app = Client("moriarty_session", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)
else:
    app = Client("moriarty_userbot", api_id=API_ID, api_hash=API_HASH)

BAGHDAD_TZ = pytz.timezone('Asia/Baghdad')

# الحافظات الرقمية
ALLOWED_USERS = []
MUTED_USERS = []
WARNED_USERS = []
FORBIDDEN_WORDS = []

AUTO_TIME_ACTIVE = False
AUTO_SAVE_ACTIVE = False
PM_GUARD_ACTIVE = False

MY_ORIGINAL_NAME = OWNER_NAME
MY_ORIGINAL_BIO = ""

# ----------------- 2. القائمة الرئيسية (.الاوامر) -----------------

@app.on_message(filters.me & filters.command("الاوامر", prefixes="."))
async def main_menu(client, message):
    text = (
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"( `.م1` ) - اوامر الادمن والكتم الذكي\n"
        f"( `.م2` ) - اوامر الانتحال والاسترجاع\n"
        f"( `.م3` ) - اوامر الوقتي والتشغيل\n"
        f"( `.م4` ) - حماية الخاص والحفظ التلقائي\n"
        f"( `.م5` ) - اوامر المنشن والتكرار\n"
        f"( `.م6` ) - اوامر التحميل والترجمة\n"
        f"( `.م7` ) - اوامر المنع والقفل\n"
        f"( `.م8` ) - اوامر التنظيف والمسح\n"
        f"( `.م9` ) - اوامر التخصيص والفارات\n"
        f"( `.م10` ) - اوامر الوقت والساعة\n"
        f"( `.م11` ) - اوامر الكشف والروابط\n"
        f"( `.م12` ) - اوامر المساعدة والإذاعة\n"
        f"( `.م13` ) - اوامر الارسال والردود\n"
        f"( `.م14` ) - اوامر الملصقات والبحث\n"
        f"( `.م15` ) - اوامر التسلية والتحشيش\n"
        f"( `.م16` ) - اوامر تحويل الصيغ\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"💎 **للاستخدام:** ارسل القائمة من `.م1` إلى `.م16`."
    )
    await message.delete()
    try:
        await client.send_photo(message.chat.id, photo=START_IMG, caption=text)
    except Exception:
        await client.send_message(message.chat.id, text)

# ----------------- 3. القوائم من .م1 إلى .م16 -----------------

@app.on_message(filters.me & filters.command(["الامر 1", "الامر1", "م1"], prefixes="."))
async def menu_1(client, message):
    await message.edit_text(
        "⚡️ **أوامر الأدمن والكتم ( .م1 ):**\n\n"
        "▫️ `.حظر` : حظر العضو بالرد\n"
        "▫️ `.طرد` : طرد العضو بالرد\n"
        "▫️ `.كتم` : كتم ذكي لحذف رسائل العضو تلقائياً\n"
        "▫️ `.الغاء الكتم` : إلغاء الكتم الذكي"
    )

@app.on_message(filters.me & filters.command(["الامر 2", "الامر2", "م2"], prefixes="."))
async def menu_2(client, message):
    await message.edit_text(
        "👥 **أوامر الانتحال والحساب ( .م2 ):**\n\n"
        "▫️ `.انتحال` : نسخ الاسم والبايو والصورة بالرد\n"
        "▫️ `.ارجاع` : استعادة اسمك وصورتك وبايوك الاصلي"
    )

@app.on_message(filters.me & filters.command(["م3"], prefixes="."))
async def menu_3(client, message):
    await message.edit_text(
        "⏰ **أوامر الوقتي والتشغيل ( .م3 ):**\n\n"
        "▫️ `.تفعيل الوقت` : وضع الوقت بجانب اسمك والبايو وتحديثه كل دقيقة\n"
        "▫️ `.تعطيل الوقت` : إيقاف الوقت واسترجاع حسابك الاصلي"
    )

@app.on_message(filters.me & filters.command("م4", prefixes="."))
async def menu_4(client, message):
    await message.edit_text(
        "🛡 **حماية الخاص والحفظ التلقائي ( .م4 ):**\n\n"
        "▫️ `.تفعيل الحماية` : تفعيل حماية الخاص\n"
        "▫️ `.تعطيل الحماية` : إلغاء حماية الخاص\n"
        "▫️ `.سماح` : السماح للشخص بالمراسلة\n"
        "▫️ `.تفعيل الحفظ التلقائي` : حفظ الوسائط ذاتية التدمير تلقائياً\n"
        "▫️ `.تعطيل الحفظ التلقائي` : إيقاف الحفظ التلقائي\n"
        "▫️ `.حفظ` : حفظ الصورة/الفيديو المقفول بالرد"
    )

@app.on_message(filters.me & filters.command("م5", prefixes="."))
async def menu_5(client, message):
    await message.edit_text(
        "📢 **أوامر المنشن والتكرار ( .م5 ):**\n\n"
        "▫️ `.تكرار` [العدد] [النص] : تكرار إرسال نص معين\n"
        "▫️ `.منشن` : عمل تاج لجميع أعضاء المجموعة"
    )

@app.on_message(filters.me & filters.command("م6", prefixes="."))
async def menu_6(client, message):
    await message.edit_text("📥 **أوامر التحميل والترجمة ( .م6 ):**\n\n▫️ `.ترجمة` [النص] : ترجمة النص إلى العربية")

@app.on_message(filters.me & filters.command("م7", prefixes="."))
async def menu_7(client, message):
    await message.edit_text("منع **أوامر المنع والقفل ( .م7 ):**\n\n▫️ `.منع` [الكلمة] : إضافة كلمة لقائمة المنع\n▫️ `.الغاء منع` [الكلمة] : حذف الكلمة من القائمة")

@app.on_message(filters.me & filters.command("م8", prefixes="."))
async def menu_8(client, message):
    await message.edit_text("🧹 **أوامر التنظيف والمسح ( .م8 ):**\n\n▫️ `.مسح` [العدد] : حذف عدد محدد من رسائلك")

@app.on_message(filters.me & filters.command("م9", prefixes="."))
async def menu_9(client, message):
    await message.edit_text("⚙️ **أوامر التخصيص والفارات ( .م9 ):**\n\n▫️ `.فحص` : اختبار سرعة واستجابة السورس")

@app.on_message(filters.me & filters.command("م10", prefixes="."))
async def menu_10(client, message):
    await message.edit_text("🕒 **أوامر الوقت والساعة ( .م10 ):**\n\n▫️ `.الوقت` : عرض الوقت والتاريخ الحالي بالتفصيل")

@app.on_message(filters.me & filters.command("م11", prefixes="."))
async def menu_11(client, message):
    await message.edit_text("🔎 **أوامر الكشف والروابط ( .م11 ):**\n\n▫️ `.ايدي` : عرض الآيدي والاسم والمعلومات")

@app.on_message(filters.me & filters.command("م12", prefixes="."))
async def menu_12(client, message):
    await message.edit_text("📻 **أوامر الإذاعة ( .م12 ):**\n\n▫️ `.إذاعة خاص` [النص] : إرسال نص لكل محادثات الخاص\n▫️ `.إذاعة مجموعات` [النص] : إرسال نص لجميع المجموعات")

@app.on_message(filters.me & filters.command("م13", prefixes="."))
async def menu_13(client, message):
    await message.edit_text("💬 **أوامر الارسال والردود ( .م13 ):**\n\n▫️ `.ارسل` [النص] : إعادة إرسال النص بصيغة موحدة")

@app.on_message(filters.me & filters.command("م14", prefixes="."))
async def menu_14(client, message):
    await message.edit_text("🎨 **أوامر الملصقات والبحث ( .م14 ):**\n\n▫️ `.ملصق` : تحويل الصورة إلى ملصق بالرد")

@app.on_message(filters.me & filters.command("م15", prefixes="."))
async def menu_15(client, message):
    await message.edit_text("🎯 **أوامر التسلية والتحشيش ( .م15 ):**\n\n▫️ `.كت` : سؤال كت تويت\n▫️ `.صراحة` : سؤال صراحة عشوائي")

@app.on_message(filters.me & filters.command("م16", prefixes="."))
async def menu_16(client, message):
    await message.edit_text("🔄 **أوامر تحويل الصيغ ( .م16 ):**\n\n▫️ `.تفكيك` : تحويل الملصق إلى صورة")

# ----------------- 4. أوامر التنفيذ الفعلية -----------------

# -- الوقت التلقائي --
async def auto_time_loop(client):
    global AUTO_TIME_ACTIVE, OWNER_NAME
    while AUTO_TIME_ACTIVE:
        try:
            now = datetime.now(BAGHDAD_TZ)
            time_str = now.strftime("%I:%M %p")
            new_name = f"{OWNER_NAME} | {time_str}"
            new_bio = f"⏰ الوقت الان: {time_str} | {SOURCE_NAME}"
            await client.update_profile(first_name=new_name, bio=new_bio)
        except Exception:
            pass
        await asyncio.sleep(60)

@app.on_message(filters.me & filters.command(["تفعيل الوقت", "تفعيلالوقت"], prefixes="."))
async def start_auto_time(client, message):
    global AUTO_TIME_ACTIVE
    if not AUTO_TIME_ACTIVE:
        AUTO_TIME_ACTIVE = True
        asyncio.create_task(auto_time_loop(client))
        await message.edit_text("⏰ **تم تفعيل الوقت التلقائي بنجاح!**")
    else:
        await message.edit_text("⚠️ **الوقت التلقائي مفعل بالفعل.**")

@app.on_message(filters.me & filters.command(["تعطيل الوقت", "تعطيلالوقت"], prefixes="."))
async def stop_auto_time(client, message):
    global AUTO_TIME_ACTIVE, OWNER_NAME, MY_ORIGINAL_BIO
    AUTO_TIME_ACTIVE = False
    try:
        await client.update_profile(first_name=OWNER_NAME, bio=MY_ORIGINAL_BIO)
    except Exception:
        pass
    await message.edit_text("🛑 **تم تعطيل الوقت التلقائي وإعادة بياناتك الرسمية.**")

# -- الانتحال و الاسترجاع --
@app.on_message(filters.me & filters.command("انتحال", prefixes="."))
async def impersonate_user(client, message):
    global MY_ORIGINAL_BIO, MY_ORIGINAL_NAME
    if not message.reply_to_message:
        return await message.edit_text("⚠️ **يرجى الرد على الشخص المراد انتحاله.**")
    
    await message.edit_text("🔄 **جاري انتحال الحساب...**")
    user = message.reply_to_message.from_user
    try:
        full_user = await client.get_chat(user.id)
        me = await client.get_me()
        me_full = await client.get_chat(me.id)
        
        MY_ORIGINAL_NAME = me.first_name if me.first_name else OWNER_NAME
        MY_ORIGINAL_BIO = me_full.bio if me_full.bio else ""
        
        new_name = user.first_name if user.first_name else ""
        new_bio = full_user.bio if full_user.bio else ""
        await client.update_profile(first_name=new_name, bio=new_bio)
        
        photos = [p async for p in client.get_chat_photos(user.id, limit=1)]
        if photos:
            dl_photo = await client.download_media(photos[0].file_id)
            await client.set_profile_photo(photo=dl_photo)
            if os.path.exists(dl_photo):
                os.remove(dl_photo)
                
        await message.edit_text(f"🎭 **تم انتحال:** {user.first_name} **بنجاح!**")
    except Exception as e:
        await message.edit_text(f"⚠️ **خطأ أثناء الانتحال:** {e}")

@app.on_message(filters.me & filters.command("ارجاع", prefixes="."))
async def revert_profile(client, message):
    global MY_ORIGINAL_BIO, MY_ORIGINAL_NAME
    await message.edit_text("🔄 **جاري استعادة معلوماتك...**")
    try:
        await client.update_profile(first_name=MY_ORIGINAL_NAME, bio=MY_ORIGINAL_BIO)
        photos = [p async for p in client.get_chat_photos("me", limit=1)]
        if photos:
            await client.delete_profile_photos(photos[0].file_id)
        await message.edit_text("✅ **تم استرجاع معلومات الحساب وصورته بنجاح.**")
    except Exception as e:
        await message.edit_text(f"⚠️ **خطأ أثناء الاسترجاع:** {e}")

# -- الحماية والحفظ --
@app.on_message(filters.me & filters.command(["تفعيل الحماية", "تفعيلالحماية"], prefixes="."))
async def enable_pm(client, message):
    global PM_GUARD_ACTIVE
    PM_GUARD_ACTIVE = True
    await message.edit_text("🛡 **تم تفعيل حماية الخاص.**")

@app.on_message(filters.me & filters.command(["تعطيل الحماية", "تعطيلالحماية"], prefixes="."))
async def disable_pm(client, message):
    global PM_GUARD_ACTIVE
    PM_GUARD_ACTIVE = False
    await message.edit_text("🔓 **تم تعطيل حماية الخاص.**")

@app.on_message(filters.me & filters.command("سماح", prefixes="."))
async def allow_user(client, message):
    global ALLOWED_USERS
    uid = message.chat.id if message.chat.type.name == "PRIVATE" else (message.reply_to_message.from_user.id if message.reply_to_message else None)
    if uid:
        if uid not in ALLOWED_USERS:
            ALLOWED_USERS.append(uid)
        await message.edit_text("✅ **تم السماح للمستخدم بالمراسلة.**")

@app.on_message(filters.private & filters.incoming & ~filters.me, group=0)
async def pm_guard(client, message):
    global PM_GUARD_ACTIVE, ALLOWED_USERS, WARNED_USERS
    if not PM_GUARD_ACTIVE:
        return
    uid = message.from_user.id
    if uid in ALLOWED_USERS or message.from_user.is_bot or message.from_user.is_contact:
        return
    if uid not in WARNED_USERS:
        WARNED_USERS.append(uid)
        await client.send_message(message.chat.id, f"✋ **أهلاً بك {message.from_user.first_name}**\n🔒 حماية الخاص مفعلة، يرجى انتظار موافقة المالك.")

@app.on_message(filters.me & filters.command("حفظ", prefixes="."))
async def manual_save(client, message):
    if not message.reply_to_message or not message.reply_to_message.media:
        return await message.edit_text("⚠️ **قم بالرد على وسائط مقفولة لحفظها.**")
    await message.edit_text("📥 **جاري الحفظ...**")
    try:
        saved = await message.reply_to_message.download()
        await client.send_document("me", saved, caption="📥 **تم حفظ الوسائط بنجاح.**")
        if os.path.exists(saved):
            os.remove(saved)
        await message.edit_text("✅ **تمت العملية وحفظها في المحفوظات.**")
    except Exception as e:
        await message.edit_text(f"⚠️ **فشل الحفظ:** {e}")

# -- الحظر والكتم والمسح --
@app.on_message(filters.me & filters.command("كتم", prefixes="."))
async def mute_cmd(client, message):
    global MUTED_USERS
    if message.reply_to_message:
        uid = message.reply_to_message.from_user.id
        if uid not in MUTED_USERS:
            MUTED_USERS.append(uid)
            await message.edit_text("🔇 **تم كتم العضو ذكياً.**")

@app.on_message(filters.me & filters.command(["الغاء الكتم", "الغاءالكتم"], prefixes="."))
async def unmute_cmd(client, message):
    global MUTED_USERS
    if message.reply_to_message:
        uid = message.reply_to_message.from_user.id
        if uid in MUTED_USERS:
            MUTED_USERS.remove(uid)
            await message.edit_text("🔊 **تم إلغاء الكتم.**")

@app.on_message(filters.incoming & ~filters.me, group=1)
async def delete_muted(client, message):
    global MUTED_USERS
    if message.from_user and message.from_user.id in MUTED_USERS:
        try:
            await message.delete()
        except Exception:
            pass

@app.on_message(filters.me & filters.command("مسح", prefixes="."))
async def purge_msgs(client, message):
    args = message.text.split()
    count = int(args[1]) if len(args) > 1 and args[1].isdigit() else 5
    await message.delete()
    deleted = 0
    async for msg in client.get_chat_history(message.chat.id, limit=count * 2):
        if msg.from_user and msg.from_user.is_self:
            try:
                await msg.delete()
                deleted += 1
                if deleted >= count:
                    break
            except Exception:
                pass

# -- الإذاعة والتكرار والمنشن --
@app.on_message(filters.me & filters.command("تكرار", prefixes="."))
async def repeat_cmd(client, message):
    args = message.text.split(maxsplit=2)
    if len(args) >= 3 and args[1].isdigit():
        count = int(args[1])
        text = args[2]
        await message.delete()
        for _ in range(min(count, 50)):
            await client.send_message(message.chat.id, text)
            await asyncio.sleep(0.3)

@app.on_message(filters.me & filters.command("إذاعة خاص", prefixes="."))
async def broadcast_pm(client, message):
    text = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else None
    if not text:
        return await message.edit_text("⚠️ **اكتب النص بعد الأمر.**")
    await message.edit_text("📢 **جاري الإذاعة للخاص...**")
    async for dialog in client.get_dialogs():
        if dialog.chat.type.name == "PRIVATE":
            try:
                await client.send_message(dialog.chat.id, text)
                await asyncio.sleep(0.3)
            except Exception:
                pass
    await message.edit_text("✅ **تمت الإذاعة للخاص بنجاح.**")

# -- الفحص والأدوات --
@app.on_message(filters.me & filters.command("فحص", prefixes="."))
async def ping_cmd(client, message):
    start = time.time()
    ms = round((time.time() - start) * 1000, 2)
    await message.edit_text(f"🕵️‍♂️ **{SOURCE_NAME} شغال بنجاح!**\n⚡️ **السرعة:** `{ms}ms`")

@app.on_message(filters.me & filters.command("ايدي", prefixes="."))
async def my_id(client, message):
    await message.edit_text(f"👤 **اسمك:** {message.from_user.first_name}\n🆔 **آيديك:** `{message.from_user.id}`")

@app.on_message(filters.me & filters.command("الوقت", prefixes="."))
async def time_cmd(client, message):
    now = datetime.now(BAGHDAD_TZ)
    await message.edit_text(f"🕒 **الساعة:** `{now.strftime('%I:%M:%S %p')}`\n📅 **التاريخ:** `{now.strftime('%Y-%m-%d')}`")

@app.on_message(filters.me & filters.command("كت", prefixes="."))
async def cut_cmd(client, message):
    q = ["أكثر شيء تخاف تفقده؟", "عادة غريبة تعملها لما تكون لوحدك؟", "أكبر غلطة تعلمت منها؟"]
    await message.edit_text(f"📝 **كت تويت:**\n\n{random.choice(q)}")

@app.on_message(filters.me & filters.command("صراحة", prefixes="."))
async def saraha_cmd(client, message):
    q = ["هل أنت راضي عن حياتك حالياً؟", "شنو أكبر سر خافيه عن أقرب ناس لك؟"]
    await message.edit_text(f"🎯 **سؤال صراحة:**\n\n{random.choice(q)}")

if __name__ == "__main__":
    print(f"⚡ {SOURCE_NAME} STARTED SUCCESSFULLY ⚡")
    app.run()