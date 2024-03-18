from pytube import YouTube
# from pyrogram import Client
from pprint import pprint

def download_video(video_id):
    """
    دانلود ویدئو با استفاده از شناسه ویدئو
    :param video_id: شناسه ویدئو
    :param save_path: مسیر ذخیره سازی فایل
    """

    yt = YouTube(video_id)
    test=yt.streaming_data["formats"]
    # print(test)
    return test

# print(download_video("video_id"))

import requests

def download_file(url, local_filename):
    # ارسال درخواست GET به URL برای دریافت محتوا
    with requests.get(url, stream=True) as r:
        # بررسی وضعیت درخواست
        r.raise_for_status()
        
        # باز کردن فایل محلی برای نوشتن محتوای دریافتی
        with open(local_filename, 'wb') as f:
            # دریافت و ذخیره محتوای دریافتی به عنوان یک فایل محلی
            for chunk in r.iter_content(chunk_size=101340):
                f.write(chunk)
                
    return local_filename
