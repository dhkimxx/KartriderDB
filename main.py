from getMatchId import getAllMatchId
from getMatchInfo import getMatchInfo
from getNameId import nicknameToId, idToNickname
import datetime
import pandas as pd

DB = pd.DataFrame([])

now = datetime.datetime.now()
start = now + datetime.timedelta(days=-366)
end = start + datetime.timedelta(days = 60)


print("Start Time: ", start)
print("End Time: ", end)
match_id_list = getAllMatchId(start, end)
print("Match counts: ", len(match_id_list))
for match_id in match_id_list:
  df = getMatchInfo(match_id)
  DB = pd.concat([DB, df])

DB = pd.DataFrame(DB)
DB.reset_index()
DB.to_csv('DataBase', index = False)