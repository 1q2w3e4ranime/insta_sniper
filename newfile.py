import requests
import random
import string
import time

# بياناتك
session_id = "72080029639%3A8rH0VdbmfiXLae%3A27%3AAYdV-Cz8I9gWVo1pXNCynT8UbgNKqXMF4jtxdXJYiQ"
bot_token = "8027799848:AAGOPCIFUgN4kTETXKfE0MolV9ImRzTD09U"
chat_id = "975437008"

# إعدادات الطلب
headers = {
    "cookie": f"sessionid={session_id}",
    "user-agent": "Mozilla/5.0"
}

# توليد يوزر عشوائي
def generate_username(length):
    chars = string.ascii_lowercase + string.digits + "._"
    return ''.join(random.choices(chars, k=length))

# التحقق من توفر اليوزر
def check_username(username):
    url = f"https://www.instagram.com/{username}/?__a=1&__d=dis"
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        print(f"\n[متاح] ==> {username}")
        return True
    else:
        print(f"[محجوز] ==> {username}")
        return False

# إرسال إلى تليغرام
def send_to_telegram(username):
    message = f"تم العثور على يوزر متاح: @{username}"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    requests.post(url, data=data)

# بدء البحث
def start_search(length):
    while True:
        user = generate_username(length)
        if check_username(user):
            send_to_telegram(user)
            print(f"\n====> اليوزر المتاح: {user} تم إرساله إلى تليغرام")
            break
        time.sleep(1)

# التشغيل
if __name__ == "__main__":
    print("اختر نوع اليوزر:\n1. ثلاثي\n2. رباعي")
    choice = input("ادخل رقم الاختيار: ")
    if choice == "1":
        start_search(3)
    elif choice == "2":
        start_search(4)
    else:
        print("اختيار غير صحيح.")