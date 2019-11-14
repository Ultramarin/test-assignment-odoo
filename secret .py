TOKEN = ""
CHAT_ID = ""
def get_secret_token(decrypt:lambda message,key:[message,key], key):
    """
    отримання токену розшифровка токену з файлу
    :param decrypt: функція розшифровки
    :param key: ключ розшифровки
    :return: токен бота
    """
    with open('token', 'r') as f:
        token_crypt = f.read()
    TOKEN = decrypt(token_crypt, key)
    return TOKEN
