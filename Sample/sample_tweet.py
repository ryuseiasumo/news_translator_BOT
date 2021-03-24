#リプライ機能あり
import tweepy
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#-  Twitter API関係  -----------------------------------------------
#Twitter APIを使用するためのConsumerキー、アクセストークン設定
API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

# tweepyの設定（認証情報を設定）
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# tweepyの設定（APIインスタンスの作成）
api = tweepy.API(auth)
#-------------------------------------------------------------------


#- News Net関係  ----------------------------------------------------
from newsapi import NewsApiClient
Newsnet_api_key = os.environ.get("Newsnet_api_key")

# クライアントを初期化
newsapi = NewsApiClient(api_key=Newsnet_api_key)

# sourcesで指定したニュースサイトからトップニュースを取得
# headlines = newsapi.get_top_headlines(sources='techcrunch')
headlines = newsapi.get_top_headlines(category='technology',language='en')

site_title = headlines['articles'][0]["title"]
site_publishedAt = headlines['articles'][0]["publishedAt"][:10]
site_url = headlines['articles'][0]["url"]
tweet_main = "タイトル:" + site_title + "\n日付:" + site_publishedAt + "\nURL:" + site_url


site_content = headlines['articles'][0]["content"]
tweet_content = "内容:" + site_content

# 140字以内の文字数に分割
tweet_content_list = []

count_reply = 0
#mainについて分割処理
if len(tweet_main) <= 140:
    tweet_content_list.append(tweet_main)
else:
    tweet_main = "タイトル:" + site_title + "\n日付:" + site_publishedAt #URLを除いた2つで考える
    while True:
        tweet_main_i = tweet_main[count_reply*140:count_reply*140+140]
        len_main = len(tweet_main_i)
        tweet_content_list.append(tweet_main_i)
        if len_main < 140:
            break
        count_reply += 1
    tweet_content_list.append("URL:" + site_url)


count_reply = 0
while True:
    tweet_content_i = tweet_content[count_reply*140:count_reply*140+140]
    len_content = len(tweet_content_i)
    tweet_content_list.append(tweet_content_i)
    if len_content < 140:
        break
    count_reply += 1

print(tweet_content_list)
# 取得したトップニュースの１件を表示
# print(headlines['articles'][0])
#-------------------------------------------------------------------


#ツイッター投稿
# api.update_status("テスト\n" + tweet_main)
my_status = api.update_status("テスト\n" + tweet_content_list.pop(0))
for mes in tweet_content_list:
    my_status = api.update_status(mes,in_reply_to_status_id = my_status.id)
