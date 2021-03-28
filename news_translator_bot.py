#リプライ機能あり
import tweepy
import os
from os.path import join, dirname
from dotenv import load_dotenv

from newsapi import NewsApiClient

import requests
import pprint

import json


load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

api_url = "https://script.google.com/macros/s/AKfycbw1LNap_3dkdCQv-lmT__r_4ZCicSo5vNNQJ4Ly_h1Yag2twD2m3jKppr7GuV6BjyGkpw/exec"

class Translator:
    def __init__(self, api_url, source_language = "en", target_language = "ja"):
        self.api_url = api_url
        self.source = source_language
        self.target = target_language

    def translate(self, input_text):
        params = {
        'text': input_text,
        'source': self.source,
        'target': self.target
        }
        result_dir = {}

        r_post = requests.post(api_url, data=params)

        translated_text = json.loads(r_post.text)["text"]
        # print(a["text"])

        return translated_text





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

translator = Translator(api_url)

#- News Net関係  ----------------------------------------------------
Newsnet_api_key = os.environ.get("Newsnet_api_key")

# クライアントを初期化
newsapi = NewsApiClient(api_key=Newsnet_api_key)

# sourcesで指定したニュースサイトからトップニュースを取得
# headlines = newsapi.get_top_headlines(sources='techcrunch')
headlines = newsapi.get_top_headlines(category='technology',language='en')

site_title = headlines['articles'][0]["title"] #タイトル
translated_title = translator.translate(site_title) #タイトルの翻訳

site_publishedAt = headlines['articles'][0]["publishedAt"][:10] #日付
site_url = headlines['articles'][0]["url"] #URL

tweet_main = "タイトル:「" + translated_title + "」\nこのニュースの日付:" + site_publishedAt + "\nリンク↓" + site_url

tweet_original_title = "元タイトル:「" + site_title + "」"

site_content = headlines['articles'][0]["content"] #内容
translated_site_content = translator.translate(site_content) #内容の翻訳
tweet_content = "内容:" + translated_site_content

# 140字以内の文字数に分割
tweet_content_list = []

count_reply = 0
#mainについて分割処理
if len(tweet_main) <= 140:
    tweet_content_list.append(tweet_main)
else:
    tweet_main = "タイトル:「" + translated_title + "」\nこのニュースの日付:" + site_publishedAt #URLを除いた2つで考える
    while True:
        tweet_main_i = tweet_main[count_reply*140:count_reply*140+140]
        len_main = len(tweet_main_i)
        tweet_content_list.append(tweet_main_i)
        if len_main < 140:
            break
        count_reply += 1
    tweet_content_list.append("リンク↓" + site_url)


count_reply = 0
#元タイトルについて分割処理
if len(tweet_original_title) <= 140:
    tweet_content_list.append(tweet_original_title)
else:
    while True:
        tweet_original_title_i = tweet_original_title[count_reply*140:count_reply*140+140]
        len_tweet_original_title_i = len(tweet_original_title_i)
        tweet_content_list.append(tweet_original_title_i)
        if len_tweet_original_title_i < 140:
            break
        count_reply += 1


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
my_status = api.update_status("＊Google翻訳で翻訳しています。＊\n" + tweet_content_list.pop(0))
for mes in tweet_content_list:
    my_status = api.update_status(mes,in_reply_to_status_id = my_status.id)
