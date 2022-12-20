import requests
from pprint import pprint
from models.YoutubeLives import YoutubeLives
import utilities.DataConverter as dc
import utilities.FileIO as io

def get_api(url: str) -> str:
    response = requests.get(url)
    if response.status_code != 200:
        print(f'{response.status_code} : {response}')
        return None

    return response.json()

api_url = 'https://api.mofucloud.com/archive/videos?_sort=date_published'
live_data = get_api(api_url)
if live_data is None:
    exit()

youtube_lives = YoutubeLives(live_data)

md = dc.to_markdown(youtube_lives)
io.save_text('output/live_md.md' , md)

html = dc.to_html(youtube_lives)
io.save_text('output/index.html' , html)