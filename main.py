import discord
from datetime import datetime
import asyncio
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import re

# # command_prefix 안에는 원하는 접두사를 넣어주면 된다.
# # ex) !, / ....
intents = discord.Intents.all()
# # client = discord.Client(command_prefix='!', intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

# @bot.event
# async def on_ready():
#     print('Loggend in Bot: ', bot.user.name)
#     print('Bot id: ', bot.user.id)
#     print('connection was succesful!')
#     print('=' * 30)
#     # 위 코드는 =라는 문자를 30개 출력하라는 뜻이다.

# bot.run('MTA4NjUxOTc3ODY2NTA1NDIxOA.G5CMaE.CVg1nWZ4jdCrYIvnI_lrYy1u675YqvlqAYvEDs')


TOKEN = 'MTA4NjUxOTc3ODY2NTA1NDIxOA.G5CMaE.CVg1nWZ4jdCrYIvnI_lrYy1u675YqvlqAYvEDs'
CHANNEL_ID = '1086501479701041313'
 
 
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await self.change_presence(status=discord.Status.online, activity=discord.Game("준혁이랑 같이 React 공부"))
 
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content[0] != '!':
            return
        else:
            message.content = message.content[1:]
 
        if message.content == 'ping':
            await message.channel.send('pong {0.author.mention}'.format(message))
        else:
            answer = self.get_answer(message.content)
            await message.channel.send(answer)
 
    def get_day_of_week(self):
        weekday_list = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
 
        weekday = weekday_list[datetime.today().weekday()]
        date = datetime.today().strftime("%Y년 %m월 %d일")
        result = '{}({})'.format(date, weekday)
        return result
 
    def get_time(self):
        return datetime.today().strftime("%H시 %M분 %S초")

    def work_time(self):
        return datetime.today().strftime("32-%H시 60-%M분 60-%S초")

    def summoner_time(self):
        url = 'https://your.gg/ko/kr/profile/eko%20bag'

        response = requests.get(url)
        date_list = []
        time_total = 0

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')


        # 날짜
        #24시간 이내 플레이한 게임은 '14시간 전' 형태로 표시됨
        playDate1 = soup.select_one('#__next > div > main > div.sc-7e8eaz-4.aoCmH > div > div > div:nth-child(2) > div > div.d490eh-1.gkciwT > span.buiiz7-0.d490eh-3.hNWwqN.cfnrzw')
        for i in playDate1:
            playDate1 = (i.get_text()[3:5])
        if(str(type(playDate1)) == "<class 'str'>"):
            date_list.append(1)
        else:
            date_list.append(playDate1)
    
        playDate2 = soup.select_one('#__next > div > main > div.sc-7e8eaz-4.aoCmH > div > div > div:nth-child(3) > div > div.d490eh-1.gkciwT > span.buiiz7-0.d490eh-3.hNWwqN.cfnrzw')
        for i in playDate2:
            playDate2 = (i.get_text()[3:5])
        if(str(type(playDate2)) == "<class 'str'>"):
            date_list.append(1)
        else:
            if int(playDate1) == int(playDate2):
                date_list.append(playDate2)
        
        playDate3 = soup.select_one('#__next > div > main > div.sc-7e8eaz-4.aoCmH > div > div > div:nth-child(4) > div > div.d490eh-1.gkciwT > span.buiiz7-0.d490eh-3.hNWwqN.cfnrzw')
        for i in playDate3:
            playDate3 = (i.get_text()[3:5])
        if(str(type(playDate3)) == "<class 'str'>"):
            date_list.append(1)
        else:
            if int(playDate2) == int(playDate3):
                date_list.append(playDate3)

        playDate4 = soup.select_one('#__next > div > main > div.sc-7e8eaz-4.aoCmH > div > div > div:nth-child(5) > div > div.d490eh-1.gkciwT > span.buiiz7-0.d490eh-3.hNWwqN.cfnrzw')
        for i in playDate4:
            playDate4 = (i.get_text()[3:5])
        if(str(type(playDate4)) == "<class 'str'>"):
            date_list.append(1)
        else:
            if int(playDate3) == int(playDate4):
                date_list.append(playDate4)
    
        playDate5 = soup.select_one('#__next > div > main > div.sc-7e8eaz-4.aoCmH > div > div > div:nth-child(6) > div > div.d490eh-1.gkciwT > span.buiiz7-0.d490eh-3.hNWwqN.cfnrzw')
        for i in playDate5:
            playDate5 = (i.get_text()[3:5])
        if(str(type(playDate5)) == "<class 'str'>"):
            date_list.append(1)
        else:
            if int(playDate4) == int(playDate5):
                date_list.append(playDate5)
    
        playDate6 = soup.select_one('#__next > div > main > div.sc-7e8eaz-4.aoCmH > div > div > div:nth-child(7) > div > div.d490eh-1.gkciwT > span.buiiz7-0.d490eh-3.hNWwqN.cfnrzw')
        for i in playDate6:
            playDate6 = (i.get_text()[3:5])
        if(str(type(playDate6)) == "<class 'str'>"):
            date_list.append(1)
        else:
            if int(playDate5) == int(playDate6):
                date_list.append(playDate6)
            # print(date_list)

    # 플레이시간
        playTime1 = soup.select_one('#__next > div > main > div.sc-7e8eaz-4.aoCmH > div > div > div:nth-child(2) > div > div.d490eh-1.gkciwT > span.buiiz7-0.d490eh-5.hNWwqN')
        playTime2 = soup.select_one('#__next > div > main > div.sc-7e8eaz-4.aoCmH > div > div > div:nth-child(3) > div > div.d490eh-1.gkciwT > span.buiiz7-0.d490eh-5.hNWwqN')
        playTime3 = soup.select_one('#__next > div > main > div.sc-7e8eaz-4.aoCmH > div > div > div:nth-child(4) > div > div.d490eh-1.gkciwT > span.buiiz7-0.d490eh-5.hNWwqN')
        playTime4 = soup.select_one('#__next > div > main > div.sc-7e8eaz-4.aoCmH > div > div > div:nth-child(5) > div > div.d490eh-1.gkciwT > span.buiiz7-0.d490eh-5.hNWwqN')
        playTime5 = soup.select_one('#__next > div > main > div.sc-7e8eaz-4.aoCmH > div > div > div:nth-child(6) > div > div.d490eh-1.gkciwT > span.buiiz7-0.d490eh-5.hNWwqN')
        playTime6 = soup.select_one('#__next > div > main > div.sc-7e8eaz-4.aoCmH > div > div > div:nth-child(7) > div > div.d490eh-1.gkciwT > span.buiiz7-0.d490eh-5.hNWwqN')
    
    # 00:00 형식에서 minutes 만 추출
        for i in playTime1:
            time1 = (i.get_text()[:2])
        for i in playTime2:
            time2 = (i.get_text()[:2])
        for i in playTime3:
            time3 = (i.get_text()[:2])
        for i in playTime4:
            time4 = (i.get_text()[:2])
        for i in playTime5:
            time5 = (i.get_text()[:2])
        for i in playTime6:
            time6 = (i.get_text()[:2])
        # print(time1)
        # print(type(time1))
        #플레이타임 합계 계산
        if len(date_list) == 1:
            time_total = int(time1)
        elif len(date_list) == 2:
            time_total = (int(time1) + int(time2))
        elif len(date_list) == 3:
            time_total = (int(time1) + int(time2) + int(time3))
        elif len(date_list) == 4:
            time_total = (int(time1) + int(time2) + int(time3) + int(time4))
        elif len(date_list) == 5:
            time_total = (int(time1) + int(time2) + int(time3) + int(time4) + int(time5))
        elif len(date_list) == 6:
            time_total = (int(time1) + int(time2) + int(time3) + int(time4) + int(time5) + int(time6))

        #출력문 만들기
        money = round(time_total / 60, 2)
        book = round(time_total / 89.4,2)
        return f'오늘 협곡 플레이타임은 {time_total}분 입니다.\n최저시급 기준 {money * 9620}원을 벌 수 있었으며,\n책을 읽었더라면 {book}권 읽을 수 있었습니다.'
        # print(9620 * money,'원을 벌 수 있었네요!')
        # print('책',book,'권을 읽을 수 있었네요!')

 
    def get_answer(self, text):
        trim_text = text.replace(" ", "")
 
        answer_dict = {
            '안녕': '안녕하세요. 이준헌 입니다.',
            '요일': ':calendar: 오늘은 {}입니다'.format(self.get_day_of_week()),
            '시간': ':clock9: 현재 시간은 {}입니다.'.format(self.get_time()),
            '세형': '세형이 코딩하니?',
            '준혁': '베추 ㄱ?',
            '준헌': '아 기타사고싶다~',
            '롤': '그대의 {}'.format(self.summoner_time()),
            '민구': '아 학교가기 싫다 인천 너무너무 좋아~~'
        }
 
        if trim_text == '' or None:
            return "알 수 없는 질의입니다. 답변을 드릴 수 없습니다."
        elif trim_text in answer_dict.keys():
            return answer_dict[trim_text]
        else:
            for key in answer_dict.keys():
                if key.find(trim_text) != -1:
                    return "연관 단어 [" + key + "]에 대한 답변입니다.\n" + answer_dict[key]
 
            for key in answer_dict.keys():
                if answer_dict[key].find(text[1:]) != -1:
                    return "질문과 가장 유사한 질문 [" + key + "]에 대한 답변이에요.\n" + answer_dict[key]
 
        return text + "은(는) 없는 질문입니다."
 
 
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)
