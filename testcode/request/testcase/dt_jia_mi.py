# -*- encoding: utf-8 -*-
# @ModuleName: dt_jia_mi
# @Author: SZQ
# @Time: 2023/5/1 17:46
import base64
import time
import hashlib
import pyDes
import binascii

import requests
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA





def test_test():
    appId = "202005191337190001"
    userId = "481184942747947008"
    appType = "ZFB_H5"
    appSecret = "c217ab0e74decdb5f0eccf2a59ae574a"
    version = "V1"
    signType = "RSA"
    businessDataEncryptType = "DES"
    public_key = "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCIb5xttvFD3D+9d/DthIvbwnsneNydfIS1Cs1uFRnNHRYamA0W8uXuC1i7k4ARCnW49Zzgo9cJ5CejLJ1ngYiQeXWiX16imc22yPHMguvfoOv6XoBFXmqa2JEfIbOY6xPmWUzYI9OULrlHJQiWdasbx4HNKkj9MLEdljDFWiwzvwIDAQAB\n-----END PUBLIC KEY-----"

    # 第一步：使用MD5对（appSecret + appSecret）进行加密，得到3DES加密的key
    app_secret = 'c217ab0e74decdb5f0eccf2a59ae574ac217ab0e74decdb5f0eccf2a59ae574a'
    md5 = hashlib.md5()
    md5.update(app_secret.encode('utf-8'))
    # 3DES加密的key
    des_key = md5.hexdigest()
    print(des_key)

    # 转换成16位
    result = []
    s = ""
    for i in range(len(des_key)):
        s += des_key[i]
        if i % 2 != 0:
            int_hex = int(s, 16)
            result.append(int_hex)
            s = ""
    print(f'result======{result}')


    # 第二步：使用3DES对businessData进行加密，得到加密后的businessData

    businessData_str = '{"latitude":30.29231494846645,"longitude":120.0992418015297,"locationCode":"0H","channelCode":"1","currentRecord":"0","recordCount":"10","context":{"versionCode":"5016","os":"ios"}}'
    k = pyDes.triple_des(key=result, padmode=pyDes.PAD_PKCS5)
    en = k.encrypt(businessData_str)
    businessData = binascii.hexlify(en).decode()
    print(f'businessData是{businessData}')




    timestamp = time.time()

    signStr = f'appId={appId}&appSecret={appSecret}&appType={appType}&businessData={businessData}&businessDataEncryptType={businessDataEncryptType}&timestamp={timestamp}&userId={userId}&version={version}'


    # 3、对签名数据进行MD5加密，得到签名
    md5.update(signStr.encode('utf-8'))
    # MD5加密的key
    des_key = md5.hexdigest()

    # 转换成16位
    sign_str_encrypt = []
    s1 = ""
    for i in range(len(des_key)):
        s1 += des_key[i]
        if i % 2 != 0:
            int_hex = int(s1, 16)
            sign_str_encrypt.append(int_hex)
            s1 = ""
    print(f'des_key======{des_key}')
    print(f'sign_str_encrypt======{sign_str_encrypt}')


    # 第四步、使用RSA算法对签名进行加密，使用公钥，得到最终签名
    cipher_public = PKCS1_v1_5.new(RSA.importKey(public_key))
    text_encrypted = cipher_public.encrypt(des_key.encode('utf-8'))
    print(f'text_encrypted------{text_encrypted}')
    text_encrypted_base64 = base64.b64encode(text_encrypted).decode()
    print(f'text_encrypted_base64------{text_encrypted_base64}')

    # 发送请求
    url = 'https://test.api.my-dt.com/gas/shop/getSimpleShopList'
    request_data = {
        "appId": "202005191337190001",
        "userId": "481184942747947008",
        "appType": "ZFB_H5",
        # "appSecret": "c217ab0e74decdb5f0eccf2a59ae574a",
        "version": "V1",''
        "timestamp": time.time(),
        "businessData": businessData,
        "sign": text_encrypted_base64,
        "signType": "RSA",
        "businessDataEncryptType": "DES",
        # "publicKey": "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCIb5xttvFD3D+9d/DthIvbwnsneNydfIS1Cs1uFRnNHRYamA0W8uXuC1i7k4ARCnW49Zzgo9cJ5CejLJ1ngYiQeXWiX16imc22yPHMguvfoOv6XoBFXmqa2JEfIbOY6xPmWUzYI9OULrlHJQiWdasbx4HNKkj9MLEdljDFWiwzvwIDAQAB"
    }
    r = requests.post(url, json=request_data)
    print(f'返回json---------{r.json()}')
    print(f'返回text----------{r.text}')
