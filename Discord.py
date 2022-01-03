import discord
from discord import voice_client
from discord.ext import commands
from youtube_dl import YoutubeDL
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord import FFmpegPCMAudio
import asyncio
import time
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import json
import time
import os
import random

bot = commands.Bot(command_prefix='>')
client = discord.Client()


user = []
musictitle = []
song_queue = []
musicnow = []

def title(msg):
    global music

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    dirver = load_chrome_driver()
    driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
    source = driver.page_source
    bs = bs4.BeautifulSoup(source, 'lxml')
    entire = bs.find_all('a', {'id': 'video-title'})
    entireNum = entire[0]
    music = entireNum.text.strip()
    
    musictitle.append(music)
    musicnow.append(music)
    test1 = entireNum.get('href')
    url = 'https://www.youtube.com'+test1
    with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
    URL = info['formats'][0]['url']

    driver.quit()
    
    return music, URL

def play(ctx):
    global vc
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    URL = song_queue[0]
    del user[0]
    del musictitle[0]
    del song_queue[0]
    vc = get(bot.voice_clients, guild=ctx.guild)
    if not vc.is_playing():
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda e: play_next(ctx)) 

def play_next(ctx):
    if len(musicnow) - len(user) >= 2:
        for i in range(len(musicnow) - len(user) - 1):
            del musicnow[0]
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    if len(user) >= 1:
        if not vc.is_playing():
            del musicnow[0]
            URL = song_queue[0]
            del user[0]
            del musictitle[0]
            del song_queue[0]
            vc.play(discord.FFmpegPCMAudio(URL,**FFMPEG_OPTIONS), after=lambda e: play_next(ctx))

        else:
            if not vc.is_playing():
                client.loop.create_task(vc.disconnet())
                
def load_chrome_driver():
      
    options = webdriver.ChromeOptions()

    options.binary_location = os.getenv('GOOGLE_CHROME_BIN')

    options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    return webdriver.Chrome(executable_path=str(os.environ.get('CHROME_EXECUTABLE_PATH')), chrome_options=options)

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(">명령어"))
    
    if not discord.opus.is_loaded():
        discord.opus.load_opus('opus')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("그런 명령어는 없어용")

@bot.command()
async def 코(ctx):
    await ctx.send("큰 @정우렁")
    
@bot.command()
async def 도구년(ctx):
    await ctx.send("???: 음식 맛이 어떠세요? 우마이!!!")
    await ctx.send("???: 저 죽었어요. 화이팅 화이팅!")

@bot.command()
async def 랄(ctx):
    embed = discord.Embed(title="솜주먹")
    embed.set_image(url="https://cdn.discordapp.com/attachments/647860626592497674/927653196623667210/1577089726860.jpg")
    await ctx.send(embed=embed)
    
@bot.command()
async def 민정환(ctx):
    embed = discord.Embed(title="@고인")
    embed.set_image(url="https://cdn.discordapp.com/attachments/647860626592497674/927655639830917120/o0698040013797061164.jpg")
    await ctx.send(embed=embed)
    
@bot.command()
async def LiteArc(ctx):
    embed = discord.Embed(title="탈출")
    embed.set_image(url="https://cdn.discordapp.com/attachments/647860626592497674/927656771475099648/d1f1c32425418469cba7e0d77849cd77.png")
    await ctx.send(embed=embed)    

@bot.command()
async def 실압고(ctx):
    embed = discord.Embed(title="김 실장님")
    embed.set_image(url=https://cdn.discordapp.com/attachments/647860626592497674/927658427021406289/download.jpg")
    await ctx.send(embed=embed)  
    
@bot.command()
async def 영바(ctx):
    await ctx.send("보")
    
@bot.command()
async def 점(ctx):
    await ctx.send("토 수류탄")
    
@bot.command()
async def 유랑단(ctx):
    await ctx.send("길드원분들 모두 사랑합니다 :)")
 

@bot.command()
async def 들어와(ctx):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send("채널에 사람이 없네용")

@bot.command()
async def 나가(ctx):
    try:
        await ctx.send("넹")
        await vc.disconnect()
    except:
        await ctx.send("이미 그 채널에 없어용")
    
@bot.command()
async def URL재생(ctx, *, url):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send("채널에 사람이 없네용")

    YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "지금 " + url + "을(를) 재생하고 있습니다", color = 0x00ff00))
    else:
        user.append(msg)
        result, URLTEST = title(msg)
        song_queue.append(URLTEST)
        await ctx.send("이미 노래가 재생중이라 " + result +"을(를) 대기열로 추가시켰어요!")

@bot.command()
async def 재생(ctx, *, msg):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send("채널에 사람이 없네용")

    if not vc.is_playing():

        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            
        driver = load_chrome_driver()
        driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl 

        driver.quit()
        
        musicnow.insert(0, entireText)
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "지금 " + musicnow[0] + "을(를) 재생하고 있습니다.", color = 0x00ff00))
        vc.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS),after=lambda e: play_next(ctx))
    else:
        user.append(msg)
        result, URLTEST = title(msg)
        song_queue.append(URLTEST)
        await ctx.send("이미 노래가 재생중이라 " + result +"을(를) 대기열로 추가시켰어요!")

@bot.command()
async def 일시정지(ctx):
    if vc.is_playing():
        vc.pause()
        await ctx.send(embed = discord.Embed(title= "일시정지", description = musicnow[0] + "을(를) 일시정지 했습니다.", color = 0x00ff00))
    else:
        await ctx.send("지금 노래가 재생되고 있지 않아용.")

@bot.command()
async def 다시재생(ctx):
    try:
        vc.resume()
    except:
         await ctx.send("지금 노래가 재생되고 있지 않아용.")
    else:
         await ctx.send(embed = discord.Embed(title= "다시재생", description = entireText  + "을(를) 다시 재생했습니다.", color = 0x00ff00))

@bot.command()
async def 노래끄기(ctx):
    if vc.is_playing():
        vc.stop()
        await ctx.send(embed = discord.Embed(title= "노래끄기", description = entireText  + "을(를) 종료했습니다.", color = 0x00ff00))
    else:
        await ctx.send("지금 노래가 재생되고 있지 않아용.")

@bot.command()
async def 지금노래(ctx):
    if not vc.is_playing():
        await ctx.send("지금은 노래가 재생되지 않네용")
    else:
        await ctx.send(embed = discord.Embed(title = "지금노래", description = "지금 " + musicnow[0] + "을(를) 재생하고 있습니다.", color = 0x00ff00))

@bot.command()
async def 멜론차트(ctx):
    if not vc.is_playing():
        
        options = webdriver.ChromeOptions()
        options.add_argument("headless")

        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            
        driver = load_chrome_driver()
        driver.get("https://www.youtube.com/results?search_query=멜론차트")
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl 

        driver.quit()

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + musicnow[0] + "을(를) 재생하고 있습니다.", color = 0x00ff00))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    else:
        await ctx.send("이미 노래가 재생 중이라 노래를 재생할 수 없어용")

@bot.command()
async def 재생추가(ctx, *, msg):
    user.append(msg)
    result, URLTEST = title(msg)
    song_queue.append(URLTEST)
    await ctx.send(result + "를 재생목록에 추가했어요!")

@bot.command()
async def 재생삭제(ctx, *, number):
    try:
        ex = len(musicnow) - len(user)
        del user[int(number) - 1]
        del musictitle[int(number) - 1]
        del song_queue[int(number)-1]
        del musicnow[int(number)-1+ex]
            
        await ctx.send("대기열이 정상적으로 삭제되었습니다.")
    except:
        if len(list) == 0:
            await ctx.send("대기열에 노래가 없어 삭제할 수 없어요!")
        else:
            if len(list) < int(number):
                await ctx.send("숫자의 범위가 목록개수를 벗어났습니다!")
            else:
                await ctx.send("숫자를 입력해주세요!")

@bot.command()
async def 재생목록(ctx):
    if len(musictitle) == 0:
        await ctx.send("아직 아무노래도 등록하지 않았어용.")
    else:
        global Text
        Text = ""
        for i in range(len(musictitle)):
            Text = Text + "\n" + str(i + 1) + ". " + str(musictitle[i])
            
        await ctx.send(embed = discord.Embed(title= "노래목록", description = Text.strip(), color = 0x00ff00))

@bot.command()
async def 재생목록초기화(ctx):
    try:
        ex = len(musicnow) - len(user)
        del user[:]
        del musictitle[:]
        del song_queue[:]
        while True:
            try:
                del musicnow[ex]
            except:
                break
        await ctx.send(embed = discord.Embed(title= "목록초기화", description = """목록이 정상적으로 초기화되었습니다.""", color = 0x00ff00))
    except:
        await ctx.send("아직 아무노래도 등록하지 않았어용.")

@bot.command()
async def 재생목록재생(ctx):

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    
    if len(user) == 0:
        await ctx.send("아직 아무노래도 등록하지 않았어용.")
    else:
        if len(musicnow) - len(user) >= 1:
            for i in range(len(musicnow) - len(user)):
                del musicnow[0]
        if not vc.is_playing():
            play(ctx)
        else:
            await ctx.send("노래가 이미 재생되고 있어용")
            
@bot.command()
async def 가위바위보(ctx, user: str):  # user:str로 !game 다음에 나오는 메시지를 받아줌
    rps_table = ['가위', '바위', '보']
    bot = random.choice(rps_table)
    result = rps_table.index(user) - rps_table.index(bot)  # 인덱스 비교로 결과 결정
    if result == 0:
        await ctx.send("누가 이겼을까요?")
        embed = discord.Embed(title="가위바위보 결과", description=f"{user} vs {bot}  \n비겼습니다.")
        embed.set_image(url="https://cdn.discordapp.com/attachments/704638702500184087/891942246709075998/IMG_0508.jpg")
        await ctx.send(embed=embed)
    elif result == 1 or result == -2:
        await ctx.send("누가 이겼을까요?")
        embed = discord.Embed(title="가위바위보 결과", description=f"{user} vs {bot} \n유저가 이겼습니다.")
        embed.set_image(url="https://cdn.discordapp.com/attachments/704638702500184087/891941823277310002/a82c203715c643e0b61f6091ee20afaf.jpg")
        await ctx.send(embed=embed)
    else:
        await ctx.send("누가 이겼을까요?")
        embed = discord.Embed(title="가위바위보 결과", description=f"{user} vs {bot}  \n제가 이겼습니다.")
        embed.set_image(url="https://cdn.discordapp.com/attachments/704638702500184087/891941815404593152/575123b7ed92e9b97e54c8a11f3104c9.jpg")
        await ctx.send(embed=embed)
        
player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@bot.command()
async def 틱택토(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("<@" + str(player1.id) + ">'의 차례입니다.")
        elif num == 2:
            turn = player2
            await ctx.send("<@" + str(player2.id) + ">'의 차례입니다.")
    else:
        await ctx.send("게임이 진행중입니다! 끝나고 다시 만드세용")

@bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " 이겼어요!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("Tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("1~9 자리에 놓으세요.")
        else:
            await ctx.send("당신의 차례가 아닙니다.")
    else:
        await ctx.send("새로운 틱택토 게임을 만드세요.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@틱택토.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("2명의 플레이어를 멘션하세요.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("표시할 위치를 입력하세요")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("정수를 입력하세요.")
        
@bot.command()
async def 명령어(ctx):
    await ctx.send(embed = discord.Embed(title='명령어',description="""
\n>명령어 -> 제리봇의 모든 명령어를 볼 수 있습니다.
\n>들어와 -> 제리봇을 자신이 속한 채널로 부릅니다.
\n>나가 -> 제리봇을 자신이 속한 채널에서 내보냅니다.
\n>URL재생 [노래링크] -> 유튜브URL를 입력하면 제리봇이 노래를 틀어줍니다.
(목록재생에서는 사용할 수 없습니다.)
\n>재생 [노래이름] -> 제리봇이 노래를 검색해 틀어줍니다.
\n>노래끄기 -> 현재 재생중인 노래를 끕니다.
>일시정지 -> 현재 재생중인 노래를 일시정지시킵니다.
>다시재생 -> 일시정지시킨 노래를 다시 재생합니다.
\n>지금노래 -> 지금 재생되고 있는 노래의 제목을 알려줍니다.
\n>멜론차트 -> 최신 멜론차트를 재생합니다.
\n>재생목록 -> 이어서 재생할 노래목록을 보여줍니다.
>재생목록재생 -> 목록에 추가된 노래를 재생합니다.
>재생목록초기화 -> 목록에 추가된 모든 노래를 지웁니다.
\n>재생추가 [노래] -> 노래를 대기열에 추가합니다.
>재생삭제 [숫자] -> 대기열에서 입력한 숫자에 해당하는 노래를 지웁니다.
\n>가위바위보 [입력] -> 제리와 가위바위보를 합니다.
>틱택토 @username @username -> 틱택토 판을 생성합니다.
>이스터에그 ex) >command
>place 1~9 -> 판에 O,X를 놓습니다.""", color = 0x00ff00)) 

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
