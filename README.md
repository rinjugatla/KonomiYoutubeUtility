# KonomiYoutubeUtility

- [古槻このみ](https://www.youtube.com/@hrtk_knm/featured)さんのお歌枠をまとめるツール
- [配信一覧ページ](https://rinjugatla.github.io/KonomiYoutubeUtility/)

## 環境構築

### Svelte版(自動更新)

1. cd svelte
2. npm install
3. npm run dev または npm run build

### Python版

1. cd python
2. python -m venv venv
3. venv/Script/active
4. pip install -r requirements.txt

#### 曲リストの更新(手動更新)

python/outputにMarkdown, HTMLが出力されます。

1. python ConvertApi.py
