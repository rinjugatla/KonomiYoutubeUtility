from models.YoutubeLives import YoutubeLives

def __markdown_header() -> str:
    header = '''# このみさんのお歌リスト（歌枠）

:::info
- [このみさんのお歌リスト（歌枠）](https://hackmd.io/@spaghetti/Hkvij39ds)からデータを取得しています。
- 怒られたら消します。
:::'''

    return header

def to_markdown(youtube_lives: YoutubeLives) -> str:
    header = __markdown_header()
    lives_md = youtube_lives.to_markdown('##', '1.')

    markdown = f'{header}\n\n{lives_md}'
    return markdown

def to_html(youtube_lives: YoutubeLives) -> str:
    base_block = '''<html>

                    <head>
                        <script src="https://code.jquery.com/jquery-3.6.2.slim.min.js"
                            integrity="sha256-E3P3OaTZH+HlEM7f1gdAT3lHAn4nWBZXuYe89DFg2d0=" crossorigin="anonymous"></script>
                        <script src="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.5.0/semantic.min.js"
                            integrity="sha512-Xo0Jh8MsOn72LGV8kU5LsclG7SUzJsWGhXbWcYs2MAmChkQzwiW/yTQwdJ8w6UA9C6EVG18GHb/TrYpYCjyAQw=="
                            crossorigin="anonymous" referrerpolicy="no-referrer"></script>
                        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.5.0/semantic.min.css"
                            integrity="sha512-KXol4x3sVoO+8ZsWPFI/r5KBVB/ssCGB5tsv2nVOKwLg33wTFP3fmnXa47FdSVIshVTgsYk/1734xSk9aFIa4A=="
                            crossorigin="anonymous" referrerpolicy="no-referrer" />
                        <script>
                            $(document).ready(function () { $('.ui.dropdown').dropdown(); });
                        </script>
                    </head>

                    <body>
                        <header></header>
                        <main>
                            :live_block:
                        </main>
                        <footer></footer>
                    </body>

                    </html>'''

    live_block = youtube_lives.to_html()
    html = base_block.replace(':live_block:', live_block)

    return html