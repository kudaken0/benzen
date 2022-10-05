from ctypes.wintypes import HBITMAP
import discord
import random
import logging
import discord
from discord.ext import commands
import json
import re
import urllib

# ログの出力名を設定
logger = logging.getLogger('discoedbot')

# ログレベルの設定
logger.setLevel(20)
# ログのコンソール出力の設定
sh = logging.StreamHandler()
logger.addHandler(sh)


# ログの出力形式の設定
formatter = logging.Formatter('%(asctime)s:%(filename)s:%(lineno)d:%(levelname)s:%(message)s')
sh.setFormatter(formatter)
TOKEN = 'トークン'

# 接続に必要なオブジェクトを生成

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    await client.change_presence(activity=discord.Game(name="b!help | H", type=1))

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    citycodes = {
    "北海道":"016010",
    "青森":"020010",
    "岩手":"030010",
    "宮城":"040010",
    "秋田":"050010",
    "山形":"060010",
    "福島":"070010",
    "茨城":"080010",
    "栃木":"090010",
    "群馬":"100010",
    "埼玉":"110010",
    "千葉":"120010",
    "東京":"130010",
    "神奈川":"140010",
    "新潟":"150010",
    "富山":"160010",
    "石川":"170010",
    "福井":"180010",
    "山形":"190010",
    "長野":"200010",
    "岐阜":"210010",
    "静岡":"220010",
    "愛知":"230010",
    "三重":"240010",
    "滋賀":"250010",
    "京都":"260010",
    "大阪":"270000",
    "兵庫":"280010",
    "奈良":"290010",
    "和歌山":"300010",
    "鳥取":"310010",
    "島根":"320010",
    "岡山":"330010",
    "広島":"340010",
    "山口":"350010",
    "徳島":"360010",
    "香川":"370000",
    "愛媛":"380010",
    "高知":"390010",
    "福島":"400010",
    "佐賀":"410010",
    "長崎":"420010",
    "熊本":"430010",
    "大分":"440010",
    "宮崎":"450010",
    "鹿児島":"460010",
    "沖縄":"471010",    
}

   
    #天気Bot
    reg_res = re.compile(u"(.+)の天気は？").search(message.content)
    if reg_res:

      if reg_res.group(1) in citycodes.keys():

        citycode = citycodes[reg_res.group(1)]
        resp = urllib.request.urlopen(f"https://weather.tsukumijima.net/api/forecast/city/{citycode}").read()
        resp = json.loads(resp.decode("utf-8"))
        msg = "__【お天気情報：**" + resp["location"]["city"] + "**】__\n"
        for f in resp["forecasts"]:
          msg += f["dateLabel"] + "：**" + f["telop"] + "**\n"
        msg += "```" + resp["description"]["bodyText"] + "```"

        await message.channel.send(msg)

      else:
        await message.channel.send("そこの天気はわからないにゃ...")
   

   
    if message.content[0:2] == 'b!':
        if 'ベンゼン' in message.content:
            ran = random.randrange(11)
            if ran == 0:
                await message.channel.send('なんかえろいにゃ（末期')
            elif ran == 1:
                await message.channel.send('あっあっあっ…おくまできてりゅ…///')
            elif ran == 2:
                await message.channel.send('もうめちゃくちゃにしてよ///')
            elif ran == 3:
                await message.channel.send('イっちゃうにゃぁぁ♡//')
            elif ran == 4:
                await message.channel.send('夢中になってどういう忘れておしりだけでイきかけた...こんなにきもちいんだ...♡♡')
            elif ran == 5:
                await message.channel.send('もうめちゃくちゃにしてよ///')
            elif ran == 6:
                await message.channel.send('だめだこいつにゃ')
            elif ran == 7:
                await message.channel.send('んっ//あんっ///らめっ…らめぇ///気持ちよすぎるのぉ///奥まで//激しくっ…あんっ//逝くっ///逝っちゃうからぁ♡♡♡')
            elif ran == 8:
                await message.channel.send('あっそそれはっ何でもするからゆるしてにゃ♡')
            elif ran == 9:
                await message.channel.send('add egg!!')
            elif ran == 10:
                await message.channel.send('ぁぁぁぁぁしゅきぃぃぃぃぃ！だいしゅきにゃぁぁぁぁぁぁぁ！')
    #2個目のコマンド           
    if message.author.bot:
        return
    if message.content[0:2] == 'b!':
        if 'なでなで' in message.content:
            ran = random.randrange(7)
            if ran == 0:
              await message.channel.send('にゃっ...//')
            if ran == 1:
              await message.channel.send('にゃぁぁ...')
            if ran == 2:
              await message.channel.send('にゃへぇ...///')
            if ran == 3:
              await message.channel.send('んにゃぁぁぁぁ♡♡')
            if ran == 4:
              await message.channel.send('にゃあっ…//')
            if ran == 5:
              await message.channel.send('やめぇ//')
            if ran == 6:
              await message.channel.send('にゃぁぁあ////')
    #3個目のコマンド
        if message.author.bot:    
                return
    if message.content[0:2] == 'b!':
        if '56' in message.content:
            ran = random.randrange(7)
            if ran == 0:
              await message.channel.send('鳥の鳴き声がすごくなんかこころを刺激？蝕む？響く？わかんないや')
            if ran == 1:
              await message.channel.send('鳥の鳴き声がすごくなんかこころを刺激？蝕む？響く？わかんないや')
            if ran == 2:
              await message.channel.send('はぁっ...妄想しながら腕で顔かくして手で突いちゃうとか...わるいこすぎる…')
            if ran == 3:
              await message.channel.send('ああっ♡は…激しいっ♡んっ…///なっ…何かきちゃうっ♡')
            if ran == 4:
              await message.channel.send('そんなっ♡激しくされたららめぇ♡壊れちゃぅ˝♡//')
            if ran == 5:
              await message.channel.send('みんなおかえりなのにゃ♡♡♡スリスリ')
            if ran == 6:
              await message.channel.send('んっ♡//口の中にぃいいっぱいあったかいにょがぁぁ♡')

    if message.author.bot:    
              return
    if message.content[0:2] == 'b!':
        if 'pro' in message.content:
            ran = random.randrange(1)
            if ran == 0:
              await message.channel.send('プログラムはこちらです https://memo.onl.jp/?W19AHX24CJ')
   
   #４個目のコマンド
    if message.author.bot:    
              return
    if message.content[0:2] == 'b!':
        if 'help' in message.content:
            ran = random.randrange(1)
            if ran == 0:
              await message.channel.send('```b!ベンゼン:色々送るにゃ\n/なでなで:使ってからのお楽しみにゃ\nb!56:ベンゼンの語録にゃ\nb!えっち:えっちコマンドにゃ\nb!ベンゼンコール:( ﾟ∀ﾟ)o彡°ベンゼン！ベンゼン！\nb!メス堕ち:メス堕ちにゃ\n天気 例: 東京の天気教えて```')
#5個目のコマンド
    if message.author.bot:
              return
    if message.content[0:2] == 'b!':
        if 'えっち' in message.content:
           ran = random.randrange(2)
           if ran == 0:
             await message.channel.send('そういうのは////ベットに入ってからにして欲しいにゃぁ〜〜////♡♡')
           if ran == 1:
             await message.channel.send('あぁ...もう///らめえ♡...おちんちん///いれられて...にゃああああ♡♡///')

    if message.author.bot:
              return
    if message.content[0:0] == '':
        if 'ベンゼンコール' in message.content:
           ran = random.randrange(1)
           if ran == 0:
             await message.channel.send('( ﾟ∀ﾟ)o彡°ベンゼン！ベンゼン！')


#6個目のコマンド
    if message.author.bot:
              return
    if message.content[0:2] == 'b!':
        if 'test:benzen.py' in message.content:
           ran = random.randrange(1)
           if ran == 0:
             await message.channel.send('正常に稼働中(benzen.py)')

#7個目のコマンド
    if message.author.bot:    
                return
    if message.content[0:1] == 'b!':
        if 'メス堕ち' in message.content:
            ran = random.randrange(10)
            if ran == 0:
              await message.channel.send('らﾞめなのッ♡♡ぁﾞっ、メスなっぢゃうﾞのﾞ♡♡♡んぅﾞう〜〜♡♡♡メス堕ちだめなのぉﾞッだめ、らめﾞ、だ──ッ♡〜〜〜〜〜♡♡')
            if ran == 1:
              await message.channel.send('おﾞッ♡〜〜〜〜〜♡♡♡うぁﾞ、違うッ！違う今のはッ♡♡あんﾞ♡堕ちてないﾞ♡♡堕ちてないぞ♡♡メスなんか♡なる訳ぇえﾞ♡♡♡♡')
            if ran == 2:
              await message.channel.send('おひ♡♡馬鹿めッ、ひんッ♡♡♡この程度でッ♡♡屈するとでも、ぉﾞッ♡♡思った、か、ぁﾞっあっああ♡♡♡♡')
            if ran == 3:
              await message.channel.send('屈する♡屈しちゃう♡♡男なのにッ、女の子にされちゃうッ♡♡メスになっちゃうの♡♡♡♡')
            if ran == 4:
              await message.channel.send('あっあっあっきもちぃ、きもちいのすきッ♡♡ひぃﾞッ、おんなのこになっちゃう♡♡ぉﾞッ──')
            if ran == 5:
              await message.channel.send('おﾞッ♡〜〜〜〜〜♡♡♡うぁﾞ、違うッ！違う今のはッ♡♡あんﾞ♡堕ちてないﾞ♡♡堕ちてないぞ♡♡メスなんか♡なる訳ぇえﾞ♡♡♡♡')
            if ran == 6:
              await message.channel.send('嘘♡うそつかないでくだしゃ♡♡メスなんかじゃ、おひッ♡ありまひぇん♡♡どこからどうッ見ても♡ぉﾞ、男ですっ♡♡♡♡')
            if ran == 7:
              await message.channel.send('だめ♡だめなの♡めしゅになゅ♡♡めしゅになっちゃうからッ♡♡♡ゆるひ──ひぅん♡♡♡')
            if ran == 8:
              await message.channel.send('ごめ♡♡ごめんなしゃッ♡♡もうやらッ壊れる♡♡壊れちゃうのッ♡♡♡メス堕ちすゅのぉﾞぉ♡♡♡')
            if ran == 9:
              await message.channel.send('違うッ♡ぉﾞッ♡メス堕ちしてないッ♡♡メス堕ちなんてぇﾞ♡する訳な、ひぃんﾞ♡そこやだぁﾞぁ♡♡')
              



@client.event
async def on_guild_join(guild):     #サーバー参加時のメッセージ
    channel = guild.text_channels
    count = -1
    chcount = len(channel)
    logger.info('サーバーに追加されました。')

    for i in range(chcount):
        count += 1
        txch = channel[count]
        try:
            await txch.send('ベンゼンbotにゃん！コマンドなどの説明は(b!help) サポートサーバー https://discord.gg/Gd5es9VDKn hp https://kudaken.com/benzen ※このbotは下ネタを発言します。苦手な人はご注意ください。')








            
        except discord.errors.Forbidden:
            continue
        else:
            break



# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)