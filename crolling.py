import requests
from bs4 import BeautifulSoup
import re

url = 'https://your.gg/ko/kr/profile/eko%20bag'

response = requests.get(url)
date_list = []
time_total = 0

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')


    # 날짜
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
        #24시간 이내 플레이한 게임은 '14시간 전' 형태로 표시됨
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
        print(date_list)

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

    print("의 오늘 협곡 플레이타임은",time_total,"분 입니다.")
    
    money = round(time_total / 60, 2)
    book = round(time_total / 89.4,2)
    print(9620 * money,'원을 벌 수 있었네요!')
    print('책',book,'권을 읽을 수 있었네요!')
else: 
    print(response.status_code)