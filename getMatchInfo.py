import os
import requests
import pandas as pd

KEY = os.environ['_API_KEY']
HEADERS = {'Authorization': KEY}

def getMatchInfo(match_id):
  _API_URL = f'https://api.nexon.co.kr/kart/v1.0/matches/{match_id}'
  res = requests.get(_API_URL, headers = HEADERS)
  res_json = res.json()

  data = []
  data_cols = ['matchId', 'matchType', 'matchResult', 'gameSpeed', 'startTime', 'endTime', 'playTime', 'channelName', 'trackId', 'teamId', 'character', 'kart', 'pet', 'flyingPet', 'partsEngine', 'partsHandle', 'partsWheel', 'partsKit', 'rankinggrade2', 'matchRank', 'matchRetired', 'matchWin', 'matchTime']
 
  matchId = res_json['matchId']
  matchType = res_json['matchType']
  matchResult = res_json['matchResult']
  gameSpeed = res_json['gameSpeed']
  startTime = res_json['startTime']
  endTime = res_json['endTime']
  playTime = res_json['playTime']
  channelName = res_json['channelName']
  trackId = res_json['trackId']
 
  if 'Team' in channelName or 'club' in channelName:
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
        data.append([matchId, matchType, matchResult, gameSpeed, startTime, endTime, playTime, channelName, trackId, teamId, character, kart, pet, flyingPet, partsEngine, partsHandle, partsWheel, partsKit, rankinggrade2, matchRank, matchRetired, matchWin, matchTime])
        
  else:
    teamId = None
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
      data.append([matchId, matchType, matchResult, gameSpeed, startTime, endTime, playTime, channelName, trackId, teamId, character, kart, pet, flyingPet, partsEngine, partsHandle, partsWheel, partsKit, rankinggrade2, matchRank, matchRetired, matchWin, matchTime])

  df = pd.DataFrame(data, columns = data_cols)
  return df
