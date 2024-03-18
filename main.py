import telebot
import s1
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import time
import do
import subprocess
import sys
import database

database.creat_database_tables()

TOKEN ='6317356905:AAGQ2p8Lo0Kc4mkChTmE7ZbI2p1bzw9cIO8'
# channel_id=-1001818196521 
channel_id= -1001996341847

dict_cid_qualiry_url={}#cid{quality:url}
list_cid_serch={}
userStep = {}   # {cid:step}
def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        userStep[uid] = 0
        return 0


def list_of(list,num=0):
    if num==0:
        return list[num:num+5]
    else:
        return list[num*5:num*5+5]

def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        cid = m.chat.id
        if m.content_type == 'text':
            print(str(m.chat.first_name) +
                  " [" + str(m.chat.id) + "]: " + m.text)
        elif m.content_type == 'photo':
            print(str(m.chat.first_name) +
                  " [" + str(m.chat.id) + "]: " + "New photo recieved")
        elif m.content_type == 'document':
            print(str(m.chat.first_name) +
                  " [" + str(m.chat.id) + "]: " + 'New Document recieved')

bot = telebot.TeleBot(TOKEN,)
bot.set_update_listener(listener)


@bot.callback_query_handler(func=lambda call: call.data.startswith('download_q'))
def handler_serch(call):
    cid=call.message.chat.id
    mid=call.message.message_id
    url=call.data.split("_")[2]
    video_id=call.data.split("_")[-1]
    list_check=database.use_video(video_id)
    if len(list_check)>0:
        bot.forward_message(cid,channel_id,list_check[0][1])
    elif len(list_check)==0:
        bot.send_message(cid,"درحال دانلود")
        local_filename=do.download_file(dict_cid_qualiry_url[cid][url],f"{video_id}.mp4")
        bot.send_message(cid,"درحال ارسال")
        # result=subprocess.run([sys.executable, "testpro.py", local_filename], capture_output=True, text=True)
        # print("Output:", result.stdout)
        # print("Errors:", result.stderr)
        # message_id_video=int(result.stdout)
        with open(local_filename, 'rb') as video:
            messag=bot.send_video(cid, video)
        message_id_video=messag.me
        database.insert_video(video_id,message_id_video)
        bot.forward_message(cid,channel_id,message_id_video)
        # # with open(local_filename, 'rb') as video:
        # #     bot.send_video(cid, video)
        # dict_cid_qualiry_url.pop(cid)
@bot.callback_query_handler(func=lambda call: call.data.startswith('downld'))
def handler_serch(call):
    cid=call.message.chat.id
    mid=call.message.message_id
    video_id=call.data.split("_")[1]
    link=call.data.split("_")[2]
    print(video_id)
    print(link)
    list_g=do.download_video(link)
    
    print(list_g)
    markup=InlineKeyboardMarkup()
    dict_cid_qualiry_url.setdefault(cid,{})
    for i in list_g:
        dict_cid_qualiry_url[cid].setdefault(i['qualityLabel'],i["url"])
        markup.add(InlineKeyboardButton(f"کیفیت {i['qualityLabel']}",callback_data=f"download_q_{i['qualityLabel']}_{video_id}"))
    bot.edit_message_reply_markup(cid,mid,reply_markup=markup)

    

@bot.callback_query_handler(func=lambda call: call.data== 'serch')
def handler_serch(call):
    cid=call.message.chat.id
    name=call.message.chat.first_name
    bot.send_message(cid,"سرچ کنید...")
    userStep[cid]=1

@bot.callback_query_handler(func=lambda call: call.data.startswith("page"))
def handler_serch(call):
    cid=call.message.chat.id
    page=call.data.split("_")[1]
    list_res_page=list_of(list_cid_serch[cid],int(page)-1)
    if len(list_res_page)==0:
        bot.a
    for video in list_res_page:
        try:
            # print(video)
            # print(video["url_jpeg"])
            markup=InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("دانلود",callback_data=f"downld_{video['video_id']}_{video['link']}"))
            bot.send_photo(cid, video["url_jpeg"],caption=f"""{video["title"]}
زمان: {video["time"]}
اسم چنل: {video["chanlel"]}
""",reply_markup=markup)
            time.sleep(0.5)
        except:
            markup=InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("دانلود",callback_data=f"downld_{video['video_id']}_{video['link']}"))
            bot.send_message(cid,video["title"],reply_markup=markup)
    markup=InlineKeyboardMarkup()
    if int(page)==1:
        markup.add(InlineKeyboardButton("صفحه بعد",callback_data=f"page_{int(page)+1}"))
    else:
        markup.add(InlineKeyboardButton("صفحه بعد",callback_data=f"page_{int(page)+1}"),InlineKeyboardButton("صفحه قبل",callback_data=f"page_{int(page)-1}"))
    bot.send_message(cid,f"صفحه {page}",reply_markup=markup)


@bot.message_handler(commands=['start'])
def command_start(m):
    cid=m.chat.id
    name=m.chat.first_name
    # bot.send_photo(cid,"https://i.ytimg.com/vi/kg2s5OMx16Y/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDvEV3sTc4lfM8dFf4t-TUlvyE8XQ")
    markup=InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("سرچ در یوتیوب",callback_data="serch"))
    # markup.add(InlineKeyboardButton("دانلود کلیپ با لینک",callback_data="download"))
    bot.send_message(cid,f"""
سلام {name}
برای استفاده از ربات از دکمه های زیر استفاده کنید                    
""",reply_markup=markup)
    userStep[cid]=0
    


@bot.message_handler(func=lambda m: get_user_step(m.chat.id)==1)
def handler_serch_message(m):
    cid=m.chat.id
    list_res_serch=list_of(s1.search_youtube(m.text))
    list_cid_serch.setdefault(cid,s1.search_youtube(m.text))
    for video in list_res_serch:
        try:
            # print(video)
            # print(video["url_jpeg"])
            markup=InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("دانلود",callback_data=f"downld_{video['video_id']}_{video['link']}"))
            bot.send_photo(cid, video["url_jpeg"],caption=f"""{video["title"]}
زمان: {video["time"]}
ویو:{video["viewCount"]}
مدت انتشار:{video["publishedTime"]}
اسم چنل: {video["chanlel"]}
""",reply_markup=markup)
            time.sleep(0.5)
        except:
            markup=InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("دانلود",callback_data=f"downld_{video['video_id']}_{video['link']}"))
            bot.send_message(cid,video["title"],reply_markup=markup)

    markup=InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("صفحه بعد",callback_data=f"page_{2}"))
    bot.send_message(cid,"صفحه 1",reply_markup=markup)

bot.infinity_polling()
