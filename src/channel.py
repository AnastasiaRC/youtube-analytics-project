import json
from googleapiclient import discovery


class Channel:
    """Класс для ютуб-канала"""
    DEVELOPER_KEY ="AIzaSyBl82uN0RmBB8DDeThFJQLrc9Aa6zYGQQE"
    api_service_name = "youtube"
    api_version = "v3"

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.youtube = discovery.build(self.api_service_name, self.api_version, developerKey=self.DEVELOPER_KEY)
        self.__channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.channel_description = self.channel['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.count_subscribers = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.total_count_views = self.channel['items'][0]['statistics']['viewCount']

    def print_info(self):
        """Выводит словарь в json-подобном удобном формате с отступами"""
        dict_to_print = (json.dumps(self.channel, indent=2, ensure_ascii=False))
        return dict_to_print

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        """Kласс-метод, возвращающий объект для работы с YouTube API"""
        cls.youtube = discovery.build(cls.api_service_name, cls.api_version, developerKey=cls.DEVELOPER_KEY)
        return cls.youtube

    def to_json(self, file):
        """Mетод сохраняющий в файл значения атрибутов экземпляра Channel"""
        with open(file, 'w', encoding='cp1251') as f:
            data = {
                'title': self.title,
                'channel_description': self.channel_description,
                'url': self.url,
                'count_subscribers': self.count_subscribers,
                'video_count': self.video_count,
                'total_count_views': self.total_count_views,
                'channel_id': self.__channel_id
            }
            json.dump(data, f, indent='\t')

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value

