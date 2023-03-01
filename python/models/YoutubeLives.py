from .YoutubeLive import YoutubeLive

class YoutubeLives():
    def __init__(self, live_data: list) -> None:
        """とりあえず[https://api.mofucloud.com/archive/videos?_sort=date_published]に対応

        Args:
            live_data (list): APIリクエスト結果
        """
        self.__lives = [YoutubeLive(live) for live in live_data]

    def to_markdown(self, prefix_live: str = '', prefix_chapter: str = '') -> str:
        lives_md = [live.to_markdown(prefix_live, prefix_chapter) for live in  self.__lives]

        text = '\n\n'.join(lives_md)
        return text

    def to_html(self) -> str:
        base_block = '''<div class="ui equal width center aligned padded grid">
                            :lives_block:
                        </div>'''

        live_blocks = [live.to_html() for live in  self.__lives]
        lives_block = '\n'.join(live_blocks)

        block = base_block.replace(':lives_block:', lives_block)
        return block