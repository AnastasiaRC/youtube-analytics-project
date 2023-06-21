import datetime
import isodate
from googleapiclient import discovery


class PlayList:
    DEVELOPER_KEY = "AIzaSyBl82uN0RmBB8DDeThFJQLrc9Aa6zYGQQE"

    def __init__(self, playlist_id: str):
        self.__playlist_id = playlist_id
        self.youtube = discovery.build("youtube", "v3", developerKey=self.DEVELOPER_KEY)
        self.playlists = self.youtube.playlistItems().list(playlistId=self.__playlist_id,
                                               part='contentDetails,snippet', maxResults=50,).execute()
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlists['items']]
        self.video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(self.video_ids)).execute()
        self.title = self.playlists['items'][0]['snippet']['title'][:-13]
        self.url = f'https://www.youtube.com/playlist?list={self.__playlist_id}'

    @property
    def total_duration(self):
        list_duration_video = []
        for video in self.video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']# YouTube video duration is in ISO 8601 format
            duration = isodate.parse_duration(iso_8601_duration)
            list_duration_video.append(duration)
        duration_playlist = sum(list_duration_video, datetime.timedelta())
        return duration_playlist

    def show_best_video(self):
        likes = 0
        popular_video = 0
        for video in self.video_response['items']:
            if int(video['statistics']['likeCount']) > likes:
                likes = int(video['statistics']['likeCount'])
                popular_video = video['id']
        return f'https://youtu.be/{popular_video}'
