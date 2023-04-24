import vk_api


def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция. """

    # Код двухфакторной аутентификации,
    # который присылается по смс или уведомлением в мобильное приложение
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device


def uploader(vk: vk_api.vk_api.VkApiMethod):
    upload = vk_api.VkUpload(vk)
    upload.photo(photos=['static/img/1552120.jpg', 'static/img/istockphoto-909990952-612x612.jpg',
                         'static/img/proekt-chto-takoe.jpg', ],
                 album_id=int(input()),
                 group_id=int(input()))


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()
    uploader(vk)


if __name__ == "__main__":
    main()
