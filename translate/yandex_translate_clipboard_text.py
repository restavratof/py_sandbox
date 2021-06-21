import argparse
import os
import pyperclip
import requests
import subprocess


def send_message(message):
    subprocess.Popen(['notify-send', message])
    return


def read_key_from_file(file_path:str):
    # print(f'read_key_from_file - IN: {file_path}')
    result = ''
    if os.path.exists(file_path):
        f = open(file_path, "r")
        result = f.read()
    # print(f'read_key_from_file - OUT: {result}')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--lang',
                        help='translate destination language code')
    args = parser.parse_args()
    lang = args.lang
else:
    lang = os.environ.get('YANDEX_TRANSLATE_DEST_LANG') or 'ru'
print(f'lang={lang}')

key_file = os.environ.get('YANDEX_TRANSLATE_KEY_FILE') or ''
key = read_key_from_file(key_file)

if key:
    text = pyperclip.paste()
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    payload = {'key': key, 'text': text, 'lang': lang}
    r = requests.get(url, params=payload)
    result_code = r.status_code
    print(f'result_code: {result_code}')
    result = r.json()
    send_message(result['message'])

else:
    print('ERROR: YANDEX_TRANSLATE_KEY_FILE env variable was not defined!')