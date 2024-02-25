from pyrogram import Client

# تنظیمات API
api_id = 27075414
api_hash = "aca0fe0dc1fae5c69309a8c04f487cde"
phone_number ="+989384245687"

# ایجاد یک نمونه از Client
app = Client("my", api_id=api_id, api_hash=api_hash, phone_number=phone_number)

# تعریف تابع برای دریافت پیام
@app.on_message()
def my_handler(client, message):
    print(message)

# شروع اتصال و اجرای برنامه
with app:
    app.run()
