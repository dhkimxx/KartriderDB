from getMatchId import getAllMatchId
from getMatchInfo import getMatchInfo
from getNameId import nicknameToId, idToNickname

start = '2022-02-22 19:00:00'
end = '2022-02-22 20:00:00'
match_id_list = getAllMatchId(start, end)
for match_id in match_id_list:
  getMatchInfo(match_id)

id = 1812254501
nick = 'thisisfine'