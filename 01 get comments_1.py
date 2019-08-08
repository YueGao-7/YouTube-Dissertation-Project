import csv
from googleapiclient.discovery import build

api_key = "AIzaSyD5DYqhfZbFf4rNv0mKUXeulzXyUjHZeRI"

channels_all = [
    {"channelId": "UCRhUp6SYaJ7zme4Bjwt28DQ", "title": "David Langer"},
    {"channelId": "UCig0KhrB5NClMvX9QrbXcrw", "title": "Global Health with Greg Martin"}
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

    with open("YouTube_comments_1.csv", "w", newline='', encoding='utf-8') as comment_file:
        comment_writer = csv.writer(comment_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        comment_writer.writerows([["channelId", "channelTitle", "videoId", "videoTitle", "videoPublishedAt",
                                   "commentId", "author", "text", "replies", "likes"]])
        for item in result_list_1:
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
