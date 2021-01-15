from flask import Flask, request
import requests
import random
from bs4 import BeautifulSoup
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello')
def hello():
    return '하이'

@app.route('/telegram', methods=['POST'])
def telegram():
    #######
    # print(request.get_json())
    user_msg = request.get_json().get('message').get('text')
    user_id = request.get_json().get('message').get('from').get('id')
    
    token = '1534222164:AAGYO1KCBfjQ_A80hDXIKX4sw-ojgBIWFzU'
    url = f'https://api.telegram.org/bot{token}/sendMessage'

    # 사용자가 무슨말을 했는지?
    if user_msg == '로또':
        # 로또번호 추천
        numbers = range(1, 46)
        lotto = random.sample(numbers, 6)

        result = sorted(lotto)
    elif user_msg == '코로나 확진자':
        YEAR = str(datetime.today().year)
        MONTH = str(datetime.today().month)
        DAY = str(datetime.today().day)
        today = '[' + YEAR + '년 ' + MONTH + '월 ' + DAY + '일]'
        
        COVID_19_url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90&oquery=%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90&tqi=hsaablp0Jy0ssKYHMtRssssstt8-215023'
        COVID_19_res = requests.get(COVID_19_url).text
        COVID_19_soup = BeautifulSoup(COVID_19_res, 'html.parser')

        result = today + '\n'      
        result += '확진자 수 : ' + COVID_19_soup.select_one('#_cs_production_type > div > div:nth-child(7) > div.status_info > ul > li.info_01 > em').text + '\n'
        result += '누적 확진자 수 : ' + COVID_19_soup.select_one('#_cs_production_type > div > div:nth-child(7) > div.status_info > ul > li.info_01 > p').text + '\n'
        result += '코로나에 걸리지 않도록 손을 깨끗히 씻어주세요!'
    else: 
        result = '로또\n코로나 확진자\n기능만 사용 가능합니다.'

    message_url = f'{url}?chat_id={user_id}&text={result}'
    requests.get(message_url)
    return '', 200

# 내용이 변경되었을 때 자동으로 서버 재시작해주는 코드
if __name__ == '__main__':
    app.run(debug=True)
# FLASK_ENV=development flask run