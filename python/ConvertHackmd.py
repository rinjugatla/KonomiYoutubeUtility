import re, requests
from pprint import pprint
from datetime import datetime

def get_source_web(url: str) -> str:
    response = requests.get(url)
    if response.status_code != 200:
        print(f'{response.status_code} : {response}')
        return None

    return response.text

def get_source_txt(path: str) -> str:
    with open(path, encoding='utf-8') as f:
        lines = f.read()
        return lines

def analyze_live_info(source: str):
    lines = source.split('\n')

    # ### 積木遊び
    music_title_pattern = r'^### (?P<title>.+)$'
    music_title_regex = re.compile(music_title_pattern)

    # [【歌作業枠】ふりーだむな朝もいいよね？【クリスマスイラスト描くよ】](https://www.youtube.com/watch?v=YvRxl5ZD6zs&amp;t=1473) (2022-12-17 12:36:32)
    # - [~~【歌枠】うたうぜー！~~](https://www.youtube.com/watch?v=o3xF08IyM0w&amp;t=351) (2022-02-16 16:16:08) (非公開)
    youtube_pattern = r'\[(?P<title>.+)\]\(https:\/\/www\.youtube\.com\/watch\?v=(?P<id>[\dA-Za-z_\-]+)&amp;t=(?P<time>\d+)\) ?\((?P<date>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\)( ?\((?P<status>.*?)\))?'
    youtube_regex = re.compile(youtube_pattern)

    # key: id, value: youtubeライブ情報
    infos = {}
    music_title: str
    singer_name :str
    need_update_singer_name = False

    for line in lines:
        # 曲名取得
        match_music_title = music_title_regex.search(line)
        if match_music_title:
            music_title = match_music_title.group('title')
            # 曲名の次は必ず歌手名
            need_update_singer_name = True
            continue

        # 歌手名取得
        if need_update_singer_name:
            singer_name = line
            need_update_singer_name = False
            continue

        # ライブ情報取得
        match_youtube = youtube_regex.search(line)
        if match_youtube:
            live_info = match_youtube.groupdict()
            live_title = live_info['title'].replace('~', '')
            live_date = datetime.strptime(live_info['date'], '%Y-%m-%d %H:%M:%S')

            id = live_info['id']
            if id in infos:
                exists_title = music_title in infos[id]['setlist']
                if exists_title:
                    continue

                infos[id]['setlist'][music_title] = {
                    'title': music_title,
                    'singer': singer_name,
                    'time': int(live_info['time'])
                }
            else:
                infos[id] = {
                    'title': live_title,
                    'id': id,
                    'setlist': {
                        music_title : {
                            'title': music_title,
                            'singer': singer_name,
                            'time': int(live_info['time'])
                        }
                    },
                    'date': live_date,
                    'status': live_info['status'] if 'status' in live_info else ''
                }

    return infos

def print_header():
    print('''# このみさんのお歌リスト（歌枠）

:::info
- [このみさんのお歌リスト（歌枠）](https://hackmd.io/@spaghetti/Hkvij39ds)からデータを取得しています。
- 怒られたら消します。
:::''')

def print_format_lives(lives: dict):
    base_url = 'https://www.youtube.com/watch?v=:id:'
    postfix_timesta_url = '&t=:timestamp:s'
    sorted_lives = sorted(lives.items(), key=lambda live: live[1]['date'])
    for live in sorted_lives:
        print()

        live_value = live[1]
        live_url = base_url.replace(':id:', live_value['id'])
        summary = f'[{live_value["title"]}]({live_url})({live_value["date"]})'
        if live_value['status'] is None:
            print(f'## {summary}')
        else:
            print(f'## ~~{summary}~~ {live_value["status"]}')
        print()

        sorted_setlist = sorted(live_value['setlist'].items(), key=lambda live: live[1]['time'])
        for music in sorted_setlist:
            music_value = music[1]
            timestamp_url = f'{live_url}{postfix_timesta_url.replace(":timestamp:", str(music_value["time"]))}'
            print(f'1. [{music_value["title"]}]({timestamp_url})({music_value["singer"]})')

# url = 'https://hackmd.io/@spaghetti/Hkvij39ds'
# 上記URLをchromeの「ソースを表示」から表示し保存したデータに対応
source = get_source_txt('./source/source.txt')
if source is None:
    exit()

lives = analyze_live_info(source)
print_header()
print_format_lives(lives)