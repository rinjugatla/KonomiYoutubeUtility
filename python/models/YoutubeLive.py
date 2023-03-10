from datetime import datetime
from .Chapters import Chapters

class YoutubeLive():

    def __init__(self, live: dict) -> None:
        self.__id: str = live['video_id']
        self.__title : str = live['title']
        self.parse_date(live['date_published'])

        self.__is_private: bool = live['is_private']
        self.__is_unplayable: bool = live['is_unplayable']
        self.__is_unlisted: bool = live['is_unlisted']

        self.__chapters = Chapters(live['video_id'], live['chapters'])

    def parse_date(self, date_text: str):
        # YYYY-MM-DD形式かYYYY-MM-DD HH:MM:SS形式しかないので簡易判定
        if len(date_text) == 10:
            self.__date = datetime.strptime(date_text, '%Y-%m-%d')
        else:
            self.__date = datetime.strptime(date_text, '%Y-%m-%d %H:%M:%S')

    @property
    def id(self) -> str:
        return self.__id

    @property
    def url(self) -> str:
        return f'https://www.youtube.com/watch?v={self.id}'

    @property
    def title(self) -> str:
        return self.__title

    @property
    def date(self) -> datetime:
        return self.__date

    def format_date(self, format: str = '%Y-%m-%d') -> str:
        return self.__date.strftime(format)

    @property
    def thumbnail(self) -> str:
        return f'https://i.ytimg.com/vi/{self.id}/mqdefault.jpg'

    @property
    def can_play(self) -> bool:
        can_play = not (self.__is_private or self.__is_unplayable)
        return can_play

    def is_unlisted(self) -> bool:
        return self.__is_unlisted

    @property
    def chapters(self) -> Chapters:
        return self.__chapters

    def to_markdown(self, prefix_live: str = '', prefix_chapter: str = '') -> str:
        summary = f'[{self.title}]({self.url}) ({self.format_date()})'
        if not self.can_play:
            summary = f'~~{summary}~~ (再生不可)'

        if prefix_live != '':
            summary = f'{prefix_live} {summary}'
        
        chapters = self.__chapters.to_markdown(prefix_chapter)
        
        text = f'{summary}\n\n{chapters}'
        return text

    def to_html(self) -> str:
        base_block = '''<div class="ui center aligned" style="margin-top:4em;">
                            <div class="ui card">
                                <div class="image">
                                    <img src=":thumbnail_url:">
                                </div>
                                <div class="content">
                                    <a class="header" href=":url:" target="_blank" rel="noopener noreferrer">:title:</a>
                                    <div class="meta">
                                        <span class="date">:date:</span>
                                    </div>
                                    <div class="description">
                                        :chapters_block:
                                    </div>
                                </div>
                                <div class="extra content">
                                    <i class="music icon"></i>
                                    :chapter_count: Chapters
                                </div>
                            </div>
                        </div>'''

        chapters_block = self.__chapters.to_html()
        block = base_block.replace(':thumbnail_url:', self.thumbnail).\
                           replace(':url:', self.url).\
                           replace(':title:', self.title).\
                           replace(':date:', self.format_date()).\
                           replace(':chapters_block:', chapters_block).\
                           replace(':chapter_count:', str(self.__chapters.count))
        
        return block

