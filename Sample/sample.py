from newsapi import NewsApiClient
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

Newsnet_api_key = os.environ.get("Newsnet_api_key")

# クライアントを初期化
newsapi = NewsApiClient(api_key=Newsnet_api_key)

# sourcesで指定したニュースサイトからトップニュースを取得
headlines = newsapi.get_top_headlines(sources='techcrunch')

# 取得したトップニュースの１件を表示
print(headlines['articles'][0])
