#Sweet☆Home公式Bot(プロトタイプ)
import tweepy
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#-----------------------------------------------------------------------------
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


print("------------------------------------------------------------------")
print("秋鐘の最新ツイートをリツイート")
akikane = api.user_timeline(screen_name="SweetHo84497180",count=50)    #秋鐘のタイムラインを取得し、akikaneに格納

for status1 in akikane:                #countの回数だけ繰り返し実行。タイムラインから繰り返しstatusを取得する。
    def if_in1(a):                     #関数if_in1を定義。文中に特定の文字列があった場合の分岐処理
        if '@' in a:                   #aに代入する文中に@があった場合
            print('skip retweet1.tweetに@が含まれていたため除外処理')    #コマンドプロンプトに skip retweet .とプリントし、twitterでは何も実行しない
        else:                          #それ以外の場合
            try:                       #とりあえずapi.retweetを試してみる
                api.retweet(status1.id)              #retweet済みエラーが出なければリツイートする
                api.create_favorite(status1.id)      #いいねを付ける
                print('success retweet1.')           #ログ
            except tweepy.error.TweepError:                    #retweet済みエラーが出た場合は以下を実行する
                print('skip error1. You have already retweeted this Tweet.')    #コマンドプロンプトに skip error1.をプリントし、次のtweet検索に進む

    if_in1(status1.text)               #status1に格納したtweetをaに代入して関数if_in1を実行


print("------------------------------------------------------------------")
print("琉偉の最新ツイートをリツイート")
rui = api.user_timeline(screen_name="SweetHo21619667",count=50)

for status2 in rui:
    def if_in2(b):
        if '@' in b:
            print('skip retweet2.tweetに@が含まれていたため除外処理')
        else:
            try:
               api.retweet(status2.id)
               api.create_favorite(status2.id)
               print('success retweet2.')
            except tweepy.error.TweepError:
               print('skip error2. You have already retweeted this Tweet.')

    if_in2(status2.text)
