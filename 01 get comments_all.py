import csv
from googleapiclient.discovery import build

api_key = "AIzaSyD5DYqhfZbFf4rNv0mKUXeulzXyUjHZeRI"

channels_all = [
    {"channelId": "UCRhUp6SYaJ7zme4Bjwt28DQ", "title": "David Langer"},
    {"channelId": "UCig0KhrB5NClMvX9QrbXcrw", "title": "Global Health with Greg Martin"}
]
channels_search = [
    {"channelId": "UCWN3xxRkmTPmbKwht9FuE5A", "title": "Siraj Raval"},
    {"channelId": "UC79Gv3mYp6zKiSwYemEik9A", "title": "DataCamp"},
    {"channelId": "UCsvqVGtbbyHaMoevxPAq9Fg", "title": "Simplilearn"},
    {"channelId": "UCsT0YIqwnpJCM-mx7-gSA4Q", "title": "TEDx Talks"}
]

youtube = build('youtube', 'v3', developerKey=api_key)


def fetch_all_videos(channel_id):
    playlist = youtube.channels().list(
        id=channel_id,
        part='contentDetails'
    ).execute()
    result = youtube.playlistItems().list(
        playlistId=playlist['items'][0]['contentDetails']['relatedPlaylists']['uploads'],
        maxResults=50,
        part='snippet'
    ).execute()
    return result


def search_videos(search_keyword, channel_id):
    result = youtube.search().list(
        part='snippet',
        q=search_keyword,
        channelId=channel_id,
        type='video',
        order='viewCount',
        maxResults=50
    ).execute()
    return result


def get_comments(video_id):
    result = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        textFormat="plainText",
        maxResults=100
    ).execute()
    return result


if __name__ == '__main__':
    result_list_1 = []
    for channel in channels_all:
        res_1 = fetch_all_videos(channel['channelId'])
        channelId = channel['channelId']
        channelTitle = channel['title']
        for item in res_1['items']:
            lst_1 = get_comments(item['snippet']['resourceId']['videoId'])
            videoTitle = item['snippet']['title']
            videoPublishedAt = item["snippet"]["publishedAt"].encode("ascii", "ignore")
            for temp in lst_1["items"]:
                cemp = {}
                cemp.setdefault("channelId", channelId)
                cemp.setdefault("channelTitle", channelTitle)
                cemp.setdefault('videoId', temp['snippet']['topLevelComment']['snippet']['videoId'])
                cemp.setdefault('videoTitle', videoTitle)
                cemp.setdefault("videoPublishedAt", videoPublishedAt)
                cemp.setdefault('commentId', temp['snippet']['topLevelComment']['id'])
                cemp.setdefault('author', temp['snippet']['topLevelComment']['snippet']['authorDisplayName'])
                cemp.setdefault("text", temp['snippet']['topLevelComment']['snippet']['textDisplay'])
                cemp.setdefault('replies', temp["snippet"]["totalReplyCount"])
                cemp.setdefault('likes', temp['snippet']['topLevelComment']['snippet']["likeCount"])
                result_list_1.append(cemp)

    result_list_2 = []
    res_2 = search_videos("healthcare|medicine|biomedical|Python|Neural|Machine Learning",
                          channels_search[0]['channelId'])
    channelId = channels_search[0]['channelId']
    channelTitle = channels_search[0]['title']
    for item in res_2['items']:
        lst_2 = get_comments(item['id']['videoId'])
        videoTitle = item['snippet']['title']
        videoPublishedAt = item["snippet"]["publishedAt"].encode("ascii", "ignore")
        for temp in lst_2["items"]:
            cemp = {}
            cemp.setdefault("channelId", channelId)
            cemp.setdefault("channelTitle", channelTitle)
            cemp.setdefault('videoId', temp['snippet']['topLevelComment']['snippet']['videoId'])
            cemp.setdefault('videoTitle', videoTitle)
            cemp.setdefault("videoPublishedAt", videoPublishedAt)
            cemp.setdefault('commentId', temp['snippet']['topLevelComment']['id'])
            cemp.setdefault('author', temp['snippet']['topLevelComment']['snippet']['authorDisplayName'])
            cemp.setdefault("text", temp['snippet']['topLevelComment']['snippet']['textDisplay'])
            cemp.setdefault('replies', temp["snippet"]["totalReplyCount"])
            cemp.setdefault('likes', temp['snippet']['topLevelComment']['snippet']["likeCount"])
            result_list_2.append(cemp)

    result_list_3 = []
    res_3 = search_videos("R|Python", channels_search[1]['channelId'])
    channelId = channels_search[1]['channelId']
    channelTitle = channels_search[1]['title']
    for item in res_3['items']:
        lst_3 = get_comments(item['id']['videoId'])
        videoTitle = item['snippet']['title']
        videoPublishedAt = item["snippet"]["publishedAt"].encode("ascii", "ignore")
        for temp in lst_3["items"]:
            cemp = {}
            cemp.setdefault("channelId", channelId)
            cemp.setdefault("channelTitle", channelTitle)
            cemp.setdefault('videoId', temp['snippet']['topLevelComment']['snippet']['videoId'])
            cemp.setdefault('videoTitle', videoTitle)
            cemp.setdefault("videoPublishedAt", videoPublishedAt)
            cemp.setdefault('commentId', temp['snippet']['topLevelComment']['id'])
            cemp.setdefault('author', temp['snippet']['topLevelComment']['snippet']['authorDisplayName'])
            cemp.setdefault("text", temp['snippet']['topLevelComment']['snippet']['textDisplay'])
            cemp.setdefault('replies', temp["snippet"]["totalReplyCount"])
            cemp.setdefault('likes', temp['snippet']['topLevelComment']['snippet']["likeCount"])
            result_list_3.append(cemp)

    result_list_4 = []
    res_4 = search_videos("R|Machine Learning|Tableau", channels_search[2]['channelId'])
    channelId = channels_search[2]['channelId']
    channelTitle = channels_search[2]['title']
    for item in res_4['items']:
        lst_4 = get_comments(item['id']['videoId'])
        videoTitle = item['snippet']['title']
        videoPublishedAt = item["snippet"]["publishedAt"].encode("ascii", "ignore")
        for temp in lst_4["items"]:
            cemp = {}
            cemp.setdefault("channelId", channelId)
            cemp.setdefault("channelTitle", channelTitle)
            cemp.setdefault('videoId', temp['snippet']['topLevelComment']['snippet']['videoId'])
            cemp.setdefault('videoTitle', videoTitle)
            cemp.setdefault("videoPublishedAt", videoPublishedAt)
            cemp.setdefault('commentId', temp['snippet']['topLevelComment']['id'])
            cemp.setdefault('author', temp['snippet']['topLevelComment']['snippet']['authorDisplayName'])
            cemp.setdefault("text", temp['snippet']['topLevelComment']['snippet']['textDisplay'])
            cemp.setdefault('replies', temp["snippet"]["totalReplyCount"])
            cemp.setdefault('likes', temp['snippet']['topLevelComment']['snippet']["likeCount"])
            result_list_4.append(cemp)

    result_list_5 = []
    res_5 = search_videos("health data|Big Data", channels_search[3]['channelId'])
    channelId = channels_search[3]['channelId']
    channelTitle = channels_search[3]['title']
    for item in res_5['items']:
        lst_5 = get_comments(item['id']['videoId'])
        videoTitle = item['snippet']['title']
        videoPublishedAt = item["snippet"]["publishedAt"].encode("ascii", "ignore")
        for temp in lst_5["items"]:
            cemp = {}
            cemp.setdefault("channelId", channelId)
            cemp.setdefault("channelTitle", channelTitle)
            cemp.setdefault('videoId', temp['snippet']['topLevelComment']['snippet']['videoId'])
            cemp.setdefault('videoTitle', videoTitle)
            cemp.setdefault("videoPublishedAt", videoPublishedAt)
            cemp.setdefault('commentId', temp['snippet']['topLevelComment']['id'])
            cemp.setdefault('author', temp['snippet']['topLevelComment']['snippet']['authorDisplayName'])
            cemp.setdefault("text", temp['snippet']['topLevelComment']['snippet']['textDisplay'])
            cemp.setdefault('replies', temp["snippet"]["totalReplyCount"])
            cemp.setdefault('likes', temp['snippet']['topLevelComment']['snippet']["likeCount"])
            result_list_5.append(cemp)

    final_result_list = []
    final_result_list.extend(result_list_1)
    final_result_list.extend(result_list_2)
    final_result_list.extend(result_list_3)
    final_result_list.extend(result_list_4)
    final_result_list.extend(result_list_5)

    with open("YouTube_comments_all.csv", "w", newline='', encoding='utf-8') as comment_file:
        comment_writer = csv.writer(comment_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        comment_writer.writerows([["channelId", "channelTitle", "videoId", "videoTitle", "videoPublishedAt",
                                   "commentId", "author", "text", "replies", "likes"]])
        for item in final_result_list:
            comment_writer.writerows([[item["channelId"],
                                       item["channelTitle"],
                                       item["videoId"],
                                       item["videoTitle"],
                                       item["videoPublishedAt"],
                                       item["commentId"],
                                       item["author"],
                                       item["text"],
                                       item["replies"],
                                       item["likes"]
                                       ]])
