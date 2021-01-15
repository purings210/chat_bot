import requests
import random
from bs4 import BeautifulSoup

token = '1534222164:AAGYO1KCBfjQ_A80hDXIKX4sw-ojgBIWFzU'
url = f'https://api.telegram.org/bot{token}/sendMessage'
chat_id = 1315531202

# 로또 번호 뽑기
# numbers = range(1, 46)
# pick = random.sample(numbers, 6)
# text = pick

# 코스피 정보 가져오기
kospi_url = 'https://finance.naver.com/sise/'
res = requests.get(kospi_url).text
soup = BeautifulSoup(res, 'html.parser')
text = '현재 코스피 가격 : ' + soup.select_one('#KOSPI_now').text

message_url = f'{url}?chat_id={chat_id}&text={text}'
# print(f'{url}?chat_id={chat_id}&text=안녕하세요')

requests.get(message_url)

