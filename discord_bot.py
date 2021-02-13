import discord
import asyncio
import random
import time
from urllib.request import urlopen, Request
import urllib
import bs4
import youtube_dl



token = ""
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tm = time.localtime(1575142526.500323)



@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('j!도움말')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content == "j!도움말":
        embed = discord.Embed(
            title="도움말", description="1. j!도움말 : 이 걸 보여준다. \n 2. j!트위치 : 트위치 주소 \n 3. j!디스코드 : 디스코드 서버 초대 주소 \n 4. j!랜덤숫자_1~10 , j!랜덤숫자_1~50 , j!랜덤숫자_1~100 \n  범위 안에 있는 수 중 한개 랜덤 발표 \n 5. j!계산기 : 계산기임 \n 6. j!가위바위보 : 봇과 가위바위보를 할 수 있다. \n 7. j!시간 : 시간을 알려준다. \n 8. j!날짜 : 날짜를 알려준다. \n 9. j!날씨 : 날씨를 알려준다. \n 10. j!투표 : 투표기능이다. (막 쓰면 추방 될 수 있으니 주의^^) \n 11. j!업데이트 : 업데이트 내역을 알려준다. \n 12. j!마크시참 : 트위치에서 사용하는 '!마크시참'과 같은 기능이다. \n 13. 음악기능 \n j!입장 : 음성채널에 입장한다. \n j!퇴장 : 음성채널에서 퇴장한다. \n j!재생 {유튜브 링크} : {유튜브 링크}를 재생한다.", color=0x191919)
        await message.channel.send(embed=embed)

    if message.content == "j!안녕":
        await message.channel.send("안녕")

    if message.content == "j!트위치":
        embed = discord.Embed(
            title="트위치", description="https://twitch.tv/0813jake", color=0xA465FD)
        await message.channel.send(embed=embed)

    if message.content == "j!디스코드":
        embed = discord.Embed(
            title="디스코드", description="https://discord.gg/yFcJHm624S", color=0x6B66FF)
        await message.channel.send(embed=embed)

    if message.content == "j!랜덤숫자":
        embed = discord.Embed(
            title="랜덤숫자", description=" 1. j!랜덤숫자_1~10 \n 2. j!랜덤숫자_1~50 \n 3. j!랜덤숫자_1~100")
        await message.channel.send(embed=embed)

    if message.content == "j!랜덤숫자_1~100":
        await message.channel.send(random.randint(1, 100))

    if message.content == "j!랜덤숫자_1~10":
        await message.channel.send(random.randint(1, 10))

    if message.content == "j!랜덤숫자_1~50":
        await message.channel.send(random.randint(1, 50))

    if message.content.startswith("j!계산기"):
        if len(message.content) > 6:
            try:
                evv = eval(message.content[5:])
                if isinstance(evv, int):
                    await message.channel.send(evv)
                elif isinstance(evv, float):
                    await message.channel.send(evv)
            except NameError:
                await message.channel.send("계산식이 이상합니다.")
                print(message.content[5:])
        if len(message.content) < 6:
            await message.channel.send("사용방법 : j!계산기 <수1> <+-/*> <수2>")

    if message.content.startswith('j!가위바위보'):
        rsp = ["가위", "바위", "보"]
        embed = discord.Embed(
            title="가위바위보", description="가위바위보를 합니다 3초내로 (가위/바위/보)를 써주세요!", color=0x00aaaa)
        channel = message.channel
        msg1 = await message.channel.send(embed=embed)

        def check(m):
            return m.author == message.author and m.channel == channel
        try:
            msg2 = await client.wait_for('message', timeout=3.0, check=check)
        except asyncio.TimeoutError:
            await msg1.delete()
            embed = discord.Embed(
                title="가위바위보", description="앗 3초가 지났네요...!", color=0x00aaaa)
            await message.channel.send(embed=embed)
            return
        else:
            await msg1.delete()
            bot_rsp = str(random.choice(rsp))
            user_rsp = str(msg2.content)
            answer = ""
            if bot_rsp == user_rsp:
                answer = "저는 " + bot_rsp + "을 냈고, 당신은 " + \
                    user_rsp + "을 내셨내요.\n" + "아쉽지만 비겼습니다."
            elif (bot_rsp == "가위" and user_rsp == "바위") or (bot_rsp == "보" and user_rsp == "가위") or (bot_rsp == "바위" and user_rsp == "보"):
                answer = "저는 " + bot_rsp + "을 냈고, 당신은 " + \
                    user_rsp + "을 내셨내요.\n" + "아쉽지만 제가 졌습니다."
            elif (bot_rsp == "바위" and user_rsp == "가위") or (bot_rsp == "가위" and user_rsp == "보") or (bot_rsp == "보" and user_rsp == "바위"):
                answer = "저는 " + bot_rsp + "을 냈고, 당신은 " + user_rsp + "을 내셨내요.\n" + "제가 이겼습니다!"
            else:
                embed = discord.Embed(
                    title="가위바위보", description="앗, 가위, 바위, 보 중에서만 내셔야죠...", color=0x00aaaa)
                await message.channel.send(embed=embed)
                return
            embed = discord.Embed(
                title="가위바위보", description=answer, color=0x00aaaa)
            await message.channel.send(embed=embed)
            return

    if message.content == "j!시간":
        await message.channel.send(time.strftime('%p %I:%M'))

    if message.content == "j!날짜":
        await message.channel.send(time.strftime('%Y-%m-%d'))

    if message.content.startswith("j!날씨"):
        if len(message.content) < 5:
            await message.channel.send("사용방법 : j!날씨 <위치>")
        else:
            location = message.content.split()[1]
            enc_location = urllib.parse.quote(location + '+날씨')
            url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location

            req = Request(url)
            page = urlopen(req)
            html = page.read()
            soup = bs4.BeautifulSoup(html,'html.parser')
            await message.channel.send('현재 ' + location + ' 날씨는 ' + soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text + '도 입니다.')

    if message.content.startswith("j!투표"):
        vote = message.content[4:].split("/")
        await message.channel.send("★투표 - " + vote[0])
        for i in range(1, len(vote)):
            choose = await message.channel.send("''" + vote[i] + "''")
            await choose.add_reaction('👍')

    if message.content == "j!업데이트":
        embed = discord.Embed(
            title="업데이트 기록", description="[2021년 2월 이전 업데이트 내역은 제외됩니다.] \n 2021-02-01 : 투표기능 추가 \n 2021-02-02 : 노래 기능 넣을려다가 안되서 안넣음(?) \n 2021-02-12 : j!마크시참 기능 추가(자세한 내용은 'j!도움말' 이용) \n 2021-02-12 : 음악기능 추가(자세한 내용은 'j!도움말' 이용)", color=0xD5D5D5)
        await message.channel.send(embed=embed)

    if message.content == "j!마크시참":
        embed = discord.Embed(
            title="마크시참", description="서버주소 : helly.kro.kr \n 서버버전 : 1.16.5")
        await message.channel.send(embed=embed)

    if message.content.startswith("j!입장"):
        await message.author.voice.channel.connect()
        await message.channel.send("음성채널에 입장합니다.")

    if message.content.startswith("j!퇴장"):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc
        
        await voice.disconnect()
        await message.channel.send("음성채널에서 퇴장합니다.")

    if message.content.startswith("j!재생"):
        await message.channel.send("로딩중입니다. 잠시만 기다려주세요.")

        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc

        url = message.content.split(" ")[1]
        option = {'outtmpl' : "file/"+url.split('=')[1],
        'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '192',}]
        }

        with youtube_dl.YoutubeDL(option) as ydl:
            ydl.download([url])
            info = ydl.extract_info(url,download=False)
            title = info['title']
      
        voice.play(discord.FFmpegPCMAudio("file/"+url.split('=')[1]+".mp3"))
        await message.channel.send(title+"를 재생합니다.")


    
client.run(ODAwMjQ4ODc4NzIwMjIxMjI0.YAPX2A.Y0yX7jiKPhy0k_LqH49HvLg5Eco)
