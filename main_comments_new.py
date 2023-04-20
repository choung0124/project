import re
import emoji
import unicodedata

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

api_key = 'AIzaSyAhe0mLJS2PYbJQAJ2jI1edRIiuOubZUNw'
youtube = build('youtube', 'v3', developerKey=api_key)

channel_id = 'UCkinYTS9IHqOEwR1Sze2JTw'

channels_response = youtube.channels().list(
    part='contentDetails',
    id=channel_id
).execute()

uploads_playlist_id = channels_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

playlist_items_response = youtube.playlistItems().list(
    part='contentDetails',
    playlistId=uploads_playlist_id,
    maxResults=50
).execute()

video_ids = [item['contentDetails']['videoId'] for item in playlist_items_response['items']]

for video_id in video_ids:
    video_response = youtube.videos().list(
        part='snippet,statistics',
        id=video_id
    ).execute()

    comment_count = int(video_response['items'][0]['statistics']['commentCount'])
    if comment_count == 0:
        continue

    comments_response = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=100
    ).execute()

    for comment in comments_response['items']:
        exporting_comments = []
        new_comment = comment['snippet']['topLevelComment']['snippet']['textDisplay']
        #print(new_comment)
        with open("temp.txt", "a", encoding="utf-8") as file:
            file.write(new_comment + "\n")

        if 'replies' in comment:
            for reply in comment['replies']['comments']:
                new_reply = reply['snippet']['textDisplay']
                #print(new_reply)
                with open("temp.txt", "a", encoding="utf-8") as file:
                    file.write(new_reply + "\n")

text_file = open("temp.txt", "r", encoding="utf-8")
data = text_file.read()
data_into_list = data.replace('\n', '').split(".")
pattern = '[a-zA-Z]+'
korean_words = []
filtered_korean_words = []

for string in data_into_list:
    korean_string = re.sub(pattern, '', string)
    korean_words.append(korean_string)


def remove_emojis(korean_string):
    return emoji.get_emoji_regexp().sub(u'', korean_string)


filtered_korean_words = [remove_emojis(korean_string)for korean_string in korean_words]

#print(Kkma.morphs(u"f{filtered_korean_words}"))

print(filtered_korean_words)
korean_text = "\n".join(filtered_korean_words)
#pre_korean_text = unicodedata.normalize('NFKD', korean_text).encode('cp949', 'ignore')

with open("extracted_text_korean_only.txt", "w", encoding="utf-8") as file:
    file.write(korean_text)

print(len(filtered_korean_words))