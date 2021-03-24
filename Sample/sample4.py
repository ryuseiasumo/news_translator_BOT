from newsapi import NewsApiClient
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

Newsnet_api_key = os.environ.get("Newsnet_api_key")

newsapi = NewsApiClient(api_key=Newsnet_api_key)
all_articles = newsapi.get_everything(q='google', sources='techcrunch', from_param="2021-03-01", to="2021-03-11")

if( all_articles['totalResults'] > 0 ):
    print("ニュース件数： {}".format(all_articles['totalResults']))
    print(all_articles['articles'][0])
else:
    print("条件に合致したニュースはありません。")
