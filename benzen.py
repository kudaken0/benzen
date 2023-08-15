import discord
import random
import logging
from discord import app_commands
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
TOKEN = 'xxxxxxxx'

# 接続に必要なオブジェクトを生成

intents = discord.Intents.default()#適当に。
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print("起動完了")
    await tree.sync()#スラッシュコマンドを同期
    await client.change_presence(activity=discord.Game(name="/help | えっち", type=1))

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
 
   

@tree.command(name="ベンゼン",description="色んなメッセージを送ります")
async def test_command(interaction: discord.Interaction):
    ran = random.randrange(15)
    if ran == 0: 
        await interaction.response.send_message("なんかえろいにゃ（末期")
    if ran == 1:
        await interaction.response.send_message("あっあっあっ…おくまできてりゅ…///")
    if ran == 2:
        await interaction.response.send_message("もうめちゃくちゃにしてよ///")
    if ran == 3:
        await interaction.response.send_message("イっちゃうにゃぁぁ♡//")
    if ran == 4:
        await interaction.response.send_message("夢中になってどういう忘れておしりだけでイきかけた...こんなにきもちいんだ...♡♡")
    if ran == 5:
        await interaction.response.send_message("もうめちゃくちゃにしてよ///")
    if ran == 6:
        await interaction.response.send_message("だめだこいつにゃ")
    if ran == 7:
        await interaction.response.send_message("んっ//あんっ///らめっ…らめぇ///気持ちよすぎるのぉ///奥まで//激しくっ…あんっ//逝くっ///逝っちゃうからぁ♡♡♡")
    if ran == 8:
        await interaction.response.send_message("あっそそれはっ何でもするからゆるしてにゃ♡")
    if ran == 9:
        await interaction.response.send_message("add egg!!")
    if ran == 10:
        await interaction.response.send_message("ぁぁぁぁぁしゅきぃぃぃぃぃ！だいしゅきにゃぁぁぁぁぁぁぁ！")
    if ran == 11:
        await interaction.response.send_message("ご主人様ご主人様！えへへ…//なんでもないのにゃ!")
    if ran == 12:
        await interaction.response.send_message("今日の夜…だめにゃ？")
    if ran == 13:
        await interaction.response.send_message("もー！お兄ちゃん靴下片付けてって言ったじゃ〜ん!")
    if ran == 14:
        await interaction.response.send_message("ご主人様！見て見て〜！にゃんにゃんっ…♡♡えへ…////")


@tree.command(name="help",description="ヘルプコマンドです")
async def test_command(interaction: discord.Interaction):
    ran = random.randrange(1)
    if ran == 0: 
        await interaction.response.send_message("```/ベンゼン: 色んなメッセージを送ります\n/なでなで: 使ってからのお楽しみです\n/56: ベンゼンの語録\n/ベンゼンコール\n/えっち: エッチコマンドです\n/メス堕ち: メス堕ちです```",ephemeral=True)


@tree.command(name="なでなで",description="使ってからのお楽しみです。")
async def test_command(interaction: discord.Interaction):
    ran = random.randrange(7)
    if ran == 0:
        await interaction.response.send_message("にゃっ...//")
    if ran == 1:
        await interaction.response.send_message("にゃぁぁ...")
    if ran == 2:
        await interaction.response.send_message("にゃへぇ...///")
    if ran == 3:
        await interaction.response.send_message("んにゃぁぁぁぁ♡♡")
    if ran == 4:
        await interaction.response.send_message("にゃあっ…//")
    if ran == 5:
        await interaction.response.send_message("やめぇ//")
    if ran == 6:
        await interaction.response.send_message("にゃぁぁあ////")


@tree.command(name="56",description="色んなメッセージを送ります")
async def test_command(interaction: discord.Interaction):
    ran = random.randrange(6)
    if ran == 0:
        await interaction.response.send_message("はぁっ...妄想しながら腕で顔かくして手で突いちゃうとか...わるいこすぎる…")
    if ran == 1:
        await interaction.response.send_message("ああっ♡は…激しいっ♡んっ…///なっ…何かきちゃうっ♡")
    if ran == 3:
        await interaction.response.send_message("そんなっ♡激しくされたららめぇ♡壊れちゃぅ˝♡//")
    if ran == 4:
        await interaction.response.send_message("みんなおかえりなのにゃ♡♡♡スリスリ")
    if ran == 5:
        await interaction.response.send_message("んっ♡//口の中にぃいいっぱいあったかいにょがぁぁ♡")


@tree.command(name="えっち",description="エッチコマンドです")
async def test_command(interaction: discord.Interaction):
    ran = random.randrange(3)
    if ran == 0:
        await interaction.response.send_message("そういうのは////ベットに入ってからにして欲しいにゃぁ〜〜////♡♡")
    if ran == 1:
        await interaction.response.send_message("あぁ...もう///らめえ♡...おちんちん///いれられて...にゃああああ♡♡///")
    if ran == 2:
        await interaction.response.send_message("まだ僕で遊んでるのにゃ？そんなんだから童貞なのにゃよ？ぶふッあーはははっははっははははははっはー")


@tree.command(name="ベンゼンコール",description="ベンゼンコールです")
async def test_command(interaction: discord.Interaction):
    ran = random.randrange(1)
    if ran == 0:
        await interaction.response.send_message("( ﾟ∀ﾟ)o彡°ベンゼン！ベンゼン！")
  


@tree.command(name="メス堕ち",description="メス堕ちです")
async def test_command(interaction: discord.Interaction):
    ran = random.randrange(10)
    if ran == 0: 
        await interaction.response.send_message("らﾞめなのッ♡♡ぁﾞっ、メスなっぢゃうﾞのﾞ♡♡♡んぅﾞう〜〜♡♡♡メス堕ちだめなのぉﾞッだめ、らめﾞ、だ──ッ♡〜〜〜〜〜♡♡")
    if ran == 1:
        await interaction.response.send_message("おﾞッ♡〜〜〜〜〜♡♡♡うぁﾞ、違うッ！違う今のはッ♡♡あんﾞ♡堕ちてないﾞ♡♡堕ちてないぞ♡♡メスなんか♡なる訳ぇえﾞ♡♡♡♡")
    if ran == 2:
        await interaction.response.send_message("おひ♡♡馬鹿めッ、ひんッ♡♡♡この程度でッ♡♡屈するとでも、ぉﾞッ♡♡思った、か、ぁﾞっあっああ♡♡♡♡")
    if ran == 3:
        await interaction.response.send_message("屈する♡屈しちゃう♡♡男なのにッ、女の子にされちゃうッ♡♡メスになっちゃうの♡♡♡♡")
    if ran == 4:
        await interaction.response.send_message("あっあっあっきもちぃ、きもちいのすきッ♡♡ひぃﾞッ、おんなのこになっちゃう♡♡ぉﾞッ──")
    if ran == 5:
        await interaction.response.send_message("おﾞッ♡〜〜〜〜〜♡♡♡うぁﾞ、違うッ！違う今のはッ♡♡あんﾞ♡堕ちてないﾞ♡♡堕ちてないぞ♡♡メスなんか♡なる訳ぇえﾞ♡♡♡♡")
    if ran == 6:
        await interaction.response.send_message("嘘♡うそつかないでくだしゃ♡♡メスなんかじゃ、おひッ♡ありまひぇん♡♡どこからどうッ見ても♡ぉﾞ、男ですっ♡♡♡♡")
    if ran == 7:
        await interaction.response.send_message("だめ♡だめなの♡めしゅになゅ♡♡めしゅになっちゃうからッ♡♡♡ゆるひ──ひぅん♡♡♡")
    if ran == 8:
        await interaction.response.send_message("ごめ♡♡ごめんなしゃッ♡♡もうやらッ壊れる♡♡壊れちゃうのッ♡♡♡メス堕ちすゅのぉﾞぉ♡♡♡")
    if ran == 9:
        await interaction.response.send_message("違うッ♡ぉﾞッ♡メス堕ちしてないッ♡♡メス堕ちなんてぇﾞ♡する訳な、ひぃんﾞ♡そこやだぁﾞぁ♡♡")


@tree.command(name="教育",description="ビ〇グモーター副社長")
async def test_command(interaction: discord.Interaction):
    ran = random.randrange(1)
    if ran == 0: 
        await interaction.response.send_message("教育教育教育教育教育教育教育教育教育教育教育教育教育教育教育教育死刑死刑死刑死刑死刑死刑死刑死刑死刑死刑死刑教育教育教育教育教育教育教育教育教育教育教育教育教育教育教育")











            
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
            await txch.send('ベンゼンbotにゃん！このbotは元ネタ『ベンゼン』の許可の上作成しました。発言することは大半はTwitterのツイートからもらいました。コマンドなどの説明は(b!help)\nサポートサーバー https://discord.gg/Gd5es9VDKn\nhp https://benzen.kudaken.com\n説明 https://benzen.kudaken.com\n※このbotは下ネタを発言します。苦手な人はご注意ください。')








            
        except discord.errors.Forbidden:
            continue
        else:
            break



# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)