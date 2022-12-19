class Chapter():
    def __init__(self, id: str, chapter: dict) -> None:
        self.__id: str = id
        self.__title: str = chapter['title']
        self.__artists: str = chapter['artists']
        self.__featured_artists: str = chapter['featured_artists']
        self.__start = int(chapter['start']) # timestamp 
        self.__is_music: bool = chapter['is_music']

    @property
    def id(self) -> str:
        return self.__id

    @property
    def title(self) -> str:
        return self.__title

    @property
    def artists(self) -> str:
        return self.__artists

    @property
    def featured_artists(self) -> str:
        return self.__featured_artists

    @property
    def start(self) -> int:
        return self.__start

    @property
    def timestamp(self) -> int:
        return self.__start

    @property
    def is_music(self) -> bool:
        return self.__is_music

    @property
    def timestamp_url_param(self) -> str:
        return f't={self.timestamp}s'

    @property
    def url(self) -> str:
        return f'https://www.youtube.com/watch?v={self.id}&{self.timestamp_url_param}'

    @property
    def __str__(self) -> str:
        if self.artists is None:
            text = f'{self.title} {self.url}'
        else:
            text = f'{self.title} {self.artists} {self.url}'
        return text

    def to_markdown(self, prefix: str = '') -> str:
        if self.artists is None:
            text = f'[{self.title}]({self.url})'
        else:
            text = f'[{self.title}]({self.url}) {self.artists}'

        if prefix != '':
            text = f'{prefix} {text}'

        return text


    def to_html(self) -> str:
        base_block = '''<div class="item">
                            <div class="content">
                                <a href=":url:" target="_blank">
                                    <div class="header">:title:</div>
                                </a>
                                :artists:
                            </div>
                        </div>'''

        block = base_block.replace(':url:', self.url).\
                           replace(':title:', self.title).\
                           replace(':artists:', self.artists if self.is_music else '')
        return block

        