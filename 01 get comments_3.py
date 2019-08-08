import csv
from googleapiclient.discovery import build

api_key = "AIzaSyD5DYqhfZbFf4rNv0mKUXeulzXyUjHZeRI"

channels_search = [
    {"channelId": "UCWN3xxRkmTPmbKwht9FuE5A", "title": "Siraj Raval"},
    {"channelId": "UC79Gv3mYp6zKiSwYemEik9A", "title": "DataCamp"},
    {"channelId": "UCsvqVGtbbyHaMoevxPAq9Fg", "title": "Simplilearn"},
    {"channelId": "UCsT0YIqwnpJCM-mx7-gSA4Q", "title": "TEDx Talks"}
]

youtube = build('youtube', 'v3', developerKey=api_key)


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

    with open("YouTube_comments_3.csv", "w", newline='', encoding='utf-8') as comment_file:
        comment_writer = csv.writer(comment_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        comment_writer.writerows([["channelId", "channelTitle", "videoId", "videoTitle", "videoPublishedAt",
                                   "commentId", "author", "text", "replies", "likes"]])
        for item in result_list_3:
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
