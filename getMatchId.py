import os
import requests

KEY = os.environ['_API_KEY']
HEADERS = {'Authorization': KEY}

def getAllMatchId(start_date, end_date, offset = 0, limit = 100):
  _API_URL = f'https://api.nexon.co.kr/kart/v1.0/matches/all?start_date={start_date}&end_date={end_date}&offset={offset}&limit={limit}'
  res = requests.get(_API_URL, headers = HEADERS)
  res_json = res.json()
  matches_data = res_json['matches'][0]
  match_id = matches_data['matches']
  return match_id