import os
import requests

key = os.environ['_API_KEY']
headers = {'Authorization': key}

def nicknameToId(nickname):
  _API_URL = f'https://api.nexon.co.kr/kart/v1.0/users/nickname/{nickname}'
  res = requests.get(_API_URL, headers = headers)
  res_json = res.json()
  name = res_json['name']
  accessId = res_json['accessId']
  level = res_json['level']
  return name, accessId, level

def idToNickname(access_id):
  _API_URL = f'https://api.nexon.co.kr/kart/v1.0/users/{access_id}'
  res = requests.get(_API_URL, headers = headers)
  res_json = res.json()
  name = res_json['name']
  accessId = res_json['accessId']
  level = res_json['level']
  return name, accessId, level