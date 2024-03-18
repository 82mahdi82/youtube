from youtubesearchpython import VideosSearch

def search_youtube(query, max_results=100):
    """
    انجام جستجو در یوتیوب
    :param query: عبارتی که می‌خواهید جستجو کنید
    :param max_results: حداکثر تعداد نتایج
    """

    videos_search = VideosSearch(query, limit=max_results)
    results = videos_search.result()['result']
    videos = []
    t=0
    for video in results:
        print(video)
        if len(video['thumbnails'])>1:
            videos.append({'title': video['title'],
                           'video_id': video['id'],
                           "url_jpeg": video['thumbnails'][len(video['thumbnails'])-1]['url'],
                           "time":video['duration'],
                           "chanlel":video['channel']['name'],
                           "viewCount":video["viewCount"]["short"],
                           "publishedTime":video["publishedTime"]})
        else:
            videos.append({'title': video['title'],
                           'video_id': video['id'],
                           "url_jpeg": video['thumbnails'][0]['url'],
                           "time":video['duration'],
                           "chanlel":video['channel']['name'],
                           "viewCount":video["viewCount"]["short"],
                           "publishedTime":video["publishedTime"]})    
        
        t+=1
    return videos


