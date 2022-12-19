import requests
from pprint import pprint
from models.YoutubeLives import YoutubeLives

def get_api(url: str) -> str:
    response = requests.get(url)
    if response.status_code != 200:
        print(f'{response.status_code} : {response}')
        return None

    return response.json()

def create_header_text() -> str:
    header = '''# このみさんのお歌リスト（歌枠）

:::info
- [このみさんのお歌リスト（歌枠）](https://hackmd.io/@spaghetti/Hkvij39ds)からデータを取得しています。
- 怒られたら消します。
:::'''

    return header

def save_to_markdown(youtube_lives: YoutubeLives):
    header = create_header_text()
    lives_md = youtube_lives.to_markdown('##', '1.')

    with open('live_md.md', 'w', encoding='utf-8') as f:
        f.write(header)
        f.write('\n\n')
        f.write(lives_md)

api_url = 'https://api.mofucloud.com/archive/videos?_sort=date_published'
live_data = get_api(api_url)
if live_data is None:
    exit()

youtube_lives = YoutubeLives(live_data)
save_to_markdown(youtube_lives)