import time
import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()


client = Client(os.getenv('account_sid'), os.getenv('auth_token'))

def get_status(user_id):
    url = 'https://api.vk.com/method/users.get'
    params = {
        'user_ids': f'{user_id}',
        'v': 5.92,
        'access_token': os.getenv('token'),
        'fields': 'online'
    }
    response = requests.post(url, params=params)
    return response.json()['response'][0]['online']  # Верните статус пользователя в ВК


def sms_sender(sms_text):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    message = client.messages \
        .create(
        body="hi!!",
        from_=os.getenv('NUMBER_FROM'),
        to=os.getenv('NUMBER_TO')
    )

    return message.sid  # Верните sid отправленного сообщения из Twilio


if __name__ == "__main__":
    vk_id = input("user_id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
