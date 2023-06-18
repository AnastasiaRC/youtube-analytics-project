from googleapiclient import discovery


class Video:
    DEVELOPER_KEY = "AIzaSyBl82uN0RmBB8DDeThFJQLrc9Aa6zYGQQE"

    def __init__(self, video_id: str):
        self.__video_id = video_id
        self.youtube = discovery.build("youtube", "v3", developerKey=self.DEVELOPER_KEY)
        self.videos = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                 id=self.__video_id).execute()
        self.title = self.videos['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/watch?v=/{self.__video_id}'
        self.count_views = self.videos['items'][0]['statistics']['viewCount']
        self.count_likes = self.videos['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
