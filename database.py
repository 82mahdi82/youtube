import sqlite3

def creat_database_tables():
    connect = sqlite3.connect("data.db")
    cur = connect.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS video(video_id VARCHAR(250) PRIMARY KEY,mid int(250))")
    connect.commit()
    connect.close()



def insert_video(video_id,mid):
    connect = sqlite3.connect("data.db")
    cur = connect.cursor()
    cur.execute(f"insert into video (video_id,mid) values ('{video_id}',{mid})")
    connect.commit()
    connect.close()

def use_video(video_id):
    connect = sqlite3.connect("data.db")
    cur = connect.cursor()
    cur.execute(f"select * from video where video_id='{video_id}'")
    dict_info=cur.fetchall()
    connect.commit()
    connect.close()
    return dict_info

creat_database_tables()