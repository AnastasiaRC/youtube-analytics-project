import json
from googleapiclient import discovery


class Channel:
    """Класс для ютуб-канала"""
    DEVELOPER_KEY = "AIzaSyBl82uN0RmBB8DDeThFJQLrc9Aa6zYGQQE"

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.youtube = discovery.build("youtube", "v3", developerKey=self.DEVELOPER_KEY)
        self.__channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.channel_description = self.channel['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.count_subscribers = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.total_count_views = self.channel['items'][0]['statistics']['viewCount']

    def __str__(self):
        """Возвращает Заголовок канала с его ссылкой"""
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        """ Возвращает True или False при сложении экземпляров класса"""
        return int(self.count_subscribers) + int(other.count_subscribers)

    def __sub__(self, other):
        """ Возвращает True или False при вычетании экземпляров класса"""
        return int(self.count_subscribers) - int(other.count_subscribers)

    def __gt__(self, other):
        """ Возвращает True или False при сравнении (>) экземпляров класса"""
        return int(self.count_subscribers) > int(other.count_subscribers)

    def __ge__(self, other):
        """ Возвращает True или False при сравнении (>=) экземпляров класса"""
        return int(self.count_subscribers) >= int(other.count_subscribers)

    def __lt__(self, other):
        """ Возвращает True или False при сравнении (<) экземпляров класса"""
        return int(self.count_subscribers) < int(other.count_subscribers)

    def __le__(self, other):
        """ Возвращает True или False при сравнении (<=) экземпляров класса"""
        return int(self.count_subscribers) <= int(other.count_subscribers)

    def __eq__(self, other):
        """ Возвращает True или False при сравнении (==) экземпляров класса"""
        return int(self.count_subscribers) == int(other.count_subscribers)

    def print_info(self):
        """Выводит словарь в json-подобном удобном формате с отступами"""
        dict_to_print = (json.dumps(self.channel, indent=2, ensure_ascii=False))
        return dict_to_print

    @property
    def channel_id(self):
        return self.__channel_id


    @channel_id.setter
    def channel_id(self, value):
        self.__channel_id = value

    @classmethod
    def get_service(cls):
        """Kласс-метод, возвращающий объект для работы с YouTube API"""
        cls.youtube = discovery.build("youtube", "v3", developerKey=cls.DEVELOPER_KEY)
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



