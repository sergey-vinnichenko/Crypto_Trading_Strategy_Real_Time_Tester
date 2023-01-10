import requests


# This file sends messages via telegram


# Fill in your bot token here
TOKEN = 'хххххх'
apiURL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

# This function sends messages with notifications
def tg_message(chat_id, message):
    try:
        response = requests.post(apiURL, json={'chat_id': chat_id,
                                               'text': message})
    except Exception:
        print('Telegram message error')

# This function sends messages without notifications
def tg_silent_message(chat_id, message):
    try:
        response = requests.post(apiURL, json={'chat_id': chat_id,
                                               'text': message,
                                               'disable_notification': True})
    except Exception:
        print('Telegram message error')
