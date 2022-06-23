from getMatchId import getAllMatchId
from getMatchInfo import getMatchInfo
from getNameId import nicknameToId, idToNickname

start = '2021-08-23 20:00:00'
end = '2021-08-23 21:00:00'
match_id_list = getAllMatchId(start, end)
for match_id in match_id_list:
  getMatchInfo(match_id)

id = 1812254501
nick = 'thisisfine'
