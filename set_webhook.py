import requests

token = '1534222164:AAGYO1KCBfjQ_A80hDXIKX4sw-ojgBIWFzU'
url = f'https://api.telegram.org/bot{token}/setWebhook'
ngrok_url = 'https://4d0e11b6402d.ngrok.io/telegram'

webhook_url = f'{url}?url={ngrok_url}'
print(webhook_url)
