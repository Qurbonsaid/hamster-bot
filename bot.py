'''HamsterBot clicker'''
import sys
from time import sleep, time
from random import randint
from requests import post
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from telethon.sync import TelegramClient, functions
from telethon.sessions import StringSession
from config import API_ID, API_HASH, SESSION


def get_url():
    '''Url getter'''
    client = TelegramClient(StringSession(SESSION), API_ID, API_HASH).start()
    if not SESSION:
        client.send_message('me', f'{client.session.save()}')
        print(
            'Session was sent to your saved messages, please add it to the config.py file'
        )
        return None
    result = client(functions.messages.RequestWebViewRequest(
        'hamster_kombat_bot',
        'hamster_kombat_bot',
        'android',
        False,
        False,
        'https://hamsterkombat.io/clicker'
    ))
    return result.url


def generate_headers(auth_token):
    '''Headers generator'''
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f'Bearer {auth_token}',
        "Origin": "https://hamsterkombat.io",
        "Referer": "https://hamsterkombat.io/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent":
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 \
          like Mac OS X) AppleWebKit/605.1.15 \
            (KHTML, like Gecko) Version/16.6 \
              Mobile/15E148 Safari/604.1",
    }


def get_token(app_url):
    '''token getter'''
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options)
    driver.get(app_url)
    sleep(5)
    return driver.execute_script('return window.localStorage.authToken;')


def get_taps(auth_token):
    '''get taps'''
    sync = post(
        'https://api.hamsterkombatgame.io/clicker/sync',
        headers=generate_headers(auth_token),
        timeout=60
    ).json()
    return sync['clickerUser']['availableTaps'], sync['clickerUser']['maxTaps']


def click(auth_token, available_taps, maximum_taps):
    '''clicker function'''
    count = randint(10, 20)
    tap = post(
        'https://api.hamsterkombatgame.io/clicker/tap',
        headers=generate_headers(auth_token),
        json={
            'availableTaps': available_taps,
            'count': count,
            'timestamp': round(time() * 1000)
        },
        timeout=60
    ).json()
    sleep(count / 100)
    print(
        f'{count} taps simulated. {tap["clickerUser"]["availableTaps"]} available taps left...')
    if tap['clickerUser']['availableTaps'] > 0:
        return click(auth_token, tap['clickerUser']['availableTaps'], maximum_taps)
    print(
        f'All taps are used, waiting for new taps for {maximum_taps // 3} seconds...')
    sleep(maximum_taps // 3)
    print('Enery is restored, starting clicking again...')
    return click(auth_token, *get_taps(auth_token))


if __name__ == '__main__':
    print('Getting web app url...')
    url = get_url()
    if not url:
        sys.exit(0)
    print('Getting authToken...')
    token = get_token(url)
    print('Getting available taps count...')
    taps, max_taps = get_taps(token)
    print(f'Available taps: {taps}\nMax taps: {max_taps}')
    print('Starting clicker...')
    click(token, taps, max_taps)
