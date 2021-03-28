# news_translator_BOT
英語のニュースのタイトル、及び内容をgoogle翻訳で日本語に訳した文章、ニュースの日付、元記事のURLを自動でツイートするTwitterBOTです。  

ただし、定期的にツイートするにはcronなどの設定をする必要があります。  
例としてcronについてのやり方を載せます。  
1：端末で $ crontab -e と叩く(macとかだと、vimかnamoあたりが開く？)  
2：crontabに以下のように情報を記載する  
   (分)(時)(日)(月)(曜日) 実行するコマンドのパス  
   (毎日12時に実行される例： 0 12 * * * pythonのパス 実行ファイルのパス)  
   pythonのパスは、$ which python で出力されたものを記述すればいいと思います。  
3：cronにファイルのアクセス権を付与する  
以下のサイトを参考にしました。  
https://fremilli.com/mac-cron-python/
