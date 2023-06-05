from googleapiclient import discovery


class Channel:
    """Класс для ютуб-канала"""
    DEVELOPER_KEY ="AIzaSyBl82uN0RmBB8DDeThFJQLrc9Aa6zYGQQE"
    api_service_name = "youtube"
    api_version = "v3"

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        youtube = discovery.build(self.api_service_name, self.api_version, developerKey=self.DEVELOPER_KEY)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        for playlist in channel['items']:
            if playlist['id'] == self.channel_id:
                print(playlist)

