import os
import requests

KEY = os.environ['_API_KEY']
HEADERS = {'Authorization': KEY}

def getMatchInfo(match_id):
  _API_URL = f'https://api.nexon.co.kr/kart/v1.0/matches/{match_id}'
  res = requests.get(_API_URL, headers = HEADERS)
  res_json = res.json()
  matchId = res_json['matchId']
  matchType = res_json['matchType']
  matchResult = res_json['matchResult']
  gameSpeed = res_json['gameSpeed']
  startTime = res_json['startTime']
  endTime = res_json['endTime']
  playTime = res_json['playTime']
  channelName = res_json['channelName']
  trackId = res_json['trackId']
  
  res_json_keys = list(res_json.keys())
  for key in res_json_keys[:-1]:
    print(key, ': ', res_json[key])
  
  if 'Team' in channelName:
    teams = res_json['teams']
    for team in teams:
      teamId = team['teamId']
      players = team['players']
      for player in players:
        character = player['character']
        kart = player['kart']
        pet = player['pet']
        flyingPet = player['flyingPet']
        partsEngine = player['partsEngine']
        partsHandle = player['partsHandle']
        partsWheel = player['partsWheel']
        partsKit = player['partsKit']
        rankinggrade2 = player['rankinggrade2']
        matchRank = player['matchRank']
        matchRetired = player['matchRetired']
        matchWin = player['matchWin']
        matchTime = player['matchTime']
        
        player_keys = list(player.keys())
        print("{")
        for key in player_keys:
          print('\t', key, ': ', player[key])
        print('}')
  else:
    players = res_json['players']
    for player in players:
      character = player['character']
      kart = player['kart']
      pet = player['pet']
      flyingPet = player['flyingPet']
      partsEngine = player['partsEngine']
      partsHandle = player['partsHandle']
      partsWheel = player['partsWheel']
      partsKit = player['partsKit']
      rankinggrade2 = player['rankinggrade2']
      matchRank = player['matchRank']
      matchRetired = player['matchRetired']
      matchWin = player['matchWin']
      matchTime = player['matchTime']
      
      player_keys = list(player.keys())
      print("{")
      for key in player_keys:
        print('\t',key, ': ', player[key])
      print("}")
      
  return
