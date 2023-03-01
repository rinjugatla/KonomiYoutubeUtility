from .Chapter import Chapter

class Chapters():
    def __init__(self, id: str, chapters: list[dict]) -> None:
        # 開始秒数に並んでいる前提なのでソートはしない
        self.__chapters = [Chapter(id, chapter) for chapter in chapters]

    @property
    def first(self) -> Chapter:
        return self.__chapters[0]

    @property
    def last(self) -> Chapter:
        return self.__chapters[-1]

    @property
    def musics(self) -> list[Chapter]:
        chapters = [chapter for chapter in self.__chapters if chapter.is_music]
        return chapters

    @property
    def not_musics(self) -> list[Chapter]:
        chapters = [chapter for chapter in self.__chapters if not chapter.is_music]
        return chapters

    @property
    def count(self) -> int:
        result = len(self.__chapters)
        return result

    def to_markdown(self, prefix: str = '') -> str:
        lines = [chapter.to_markdown(prefix) for chapter in self.__chapters]
        text = '\n'.join(lines)
        return text

    def to_html(self) -> str:
        base_block = '''<div class="ui segment">
                            <div class="ui relaxed divided list">
                                :chapters_block:
                            </div>
                        </div>'''
        
        chapter_blocks = [chapter.to_html() for chapter in self.__chapters]
        chapters_block = '\n'.join(chapter_blocks)

        block = base_block.replace(':chapters_block:', chapters_block)
        return block
