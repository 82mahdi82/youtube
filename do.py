from pytube import YouTube
# from pyrogram import Client
from pprint import pprint
api_id = 28242333
api_hash ="c378fdf42012175e6376208019f4bb14"
def download_video(video_id):
    """
    دانلود ویدئو با استفاده از شناسه ویدئو
    :param video_id: شناسه ویدئو
    :param save_path: مسیر ذخیره سازی فایل
    """
    yt = YouTube(f"https://www.youtube.com/shorts/{video_id}")
    test=yt.streaming_data["formats"]
    print(test)
    return test

# print(download_video())

import requests

def download_file(url, local_filename):
    # ارسال درخواست GET به URL برای دریافت محتوا
    with requests.get(url, stream=True) as r:
        # بررسی وضعیت درخواست
        r.raise_for_status()
        
        # باز کردن فایل محلی برای نوشتن محتوای دریافتی
        with open(local_filename, 'wb') as f:
            # دریافت و ذخیره محتوای دریافتی به عنوان یک فایل محلی
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
                
    return local_filename

# URL فایل مورد نظر و مسیر محلی برای ذخیره فایل

local_filename = "file_name.mp4"

# دانلود فایل
# with Client("my_account", api_id=api_id, api_hash=api_hash) as app:
#   app.send_video(748626808,file_url , caption="این ویدیو را ببینید:")