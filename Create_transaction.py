import json
from datetime import time

import rsa as rsa

# Создание и подписание транзакции в блокчейне.
def generate_transaction(user, weight, group, sender, recipient, number):
    global key
    transaction = {"additional": {"number": number, "time": time.time(), "weight": weight, "group": group},
                   "user": {"public_key": key[0], "address": user["address"], "post_code": user["post_code"]},
                   "content": {'sender': sender, "recipient": recipient}}
    return transaction

#Подписание транзакции
def sing_transaction(transaction):
    global key
    signature = rsa.sign(message=str(transaction).encode(), priv_key=key[1], hash_method='SHA-256')
    return signature

#Нужно сохранять/получать ключи из файлов, для этого также пешим две функции, для генерации и записи
def save_key(key, fp):
    pubkey, privkey = key[0], key[1]
    pubkey_pem = pubkey.save_pkcs1(format='PEM')  #  (format='PEM')
    privkey_pem = privkey.save_pkcs1(format='PEM')
    print(pubkey_pem)
    print(privkey_pem)
    with open(fp + 'PublicKey', 'w') as file:
        file.write(pubkey_pem.decode())
    with open(fp + 'PrivateKey', 'w') as file:
        file.write(privkey_pem.decode())

    # для чтения из файла
    def get_key(fp):
        global key
        puk = fp + 'PublicKey'
        prk = fp + 'PrivateKey'
        with open(puk, 'r') as file:
            key.append(rsa.PublicKey.load_pkcs1(file.read().encode(), 'PEM'))
        with open(prk, 'r') as file:
            key.append(rsa.PrivateKey.load_pkcs1(file.read().encode(), 'PEM'))


# Проверка подписи транзакции
def verify(transaction, signature):
    key = transaction['user']['public_key']
    print(str(transaction).encode())
    print(signature)
    return rsa.verify(message=str(transaction).encode(), signature=signature, pub_key=key)

#Запись транзакции в файл python
#Вы можете заметить, что транзакции прошлось хранить в виде байт-кода в отдельных файлах, формата .dat.

def write_transaction(transaction, signature, fp):
    number = transaction["additional"]["number"]
    fp_transaction = fp + 'transaction' + str(number) + '.json'
    fp_signature = fp + 'signatue' + str(number) + '.dat'
    transaction['user']['public_key'] = [transaction['user']['public_key']['n'], transaction['user']['public_key']['e']]
    with open(fp_transaction, 'w', encoding='UTF8') as file:
        json.dump(transaction, file, indent=4)
    with open(fp_signature, 'wb') as file:
        file.write(signature)