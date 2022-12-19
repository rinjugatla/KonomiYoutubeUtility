import requests
from pprint import pprint
from models.YoutubeLives import YoutubeLives

def get_api(url: str) -> str:
    response = requests.get(url)
    if response.status_code != 200:
        print(f'{response.status_code} : {response}')
        return None

    return response.json()

def create_markdown_header_text() -> str:
    header = '''# このみさんのお歌リスト（歌枠）

:::info
- [このみさんのお歌リスト（歌枠）](https://hackmd.io/@spaghetti/Hkvij39ds)からデータを取得しています。
- 怒られたら消します。
:::'''

    return header

def save_to_markdown(youtube_lives: YoutubeLives):
    header = create_markdown_header_text()
    lives_md = youtube_lives.to_markdown('##', '1.')

    with open('output/live_md.md', 'w', encoding='utf-8') as f:
        f.write(header)
        f.write('\n\n')
        f.write(lives_md)

def save_to_html(youtube_lives: YoutubeLives):
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

    with open('output/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

api_url = 'https://api.mofucloud.com/archive/videos?_sort=date_published'
live_data = get_api(api_url)
if live_data is None:
    exit()

youtube_lives = YoutubeLives(live_data)
save_to_markdown(youtube_lives)
save_to_html(youtube_lives)