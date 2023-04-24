import vk_api
from datetime import datetime


def main():
    login, password = '89091575553', 'Maxim500'
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    response = vk.wall.get(count=5, offset=1)

    if response['items']:
        for i in range(len(response['items'])):
            print(response['items'][i]['text'])
            print(datetime.utcfromtimestamp(response['items'][i]['date']).strftime('date: %Y-%m-%d; time: %H:%M:%S'))


if __name__ == '__main__':
    main()
