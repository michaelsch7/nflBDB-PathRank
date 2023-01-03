import numpy as np
import pandas as pd
from DrawPath import drawPath, getPlayerXY
import math 

WEEKDF = pd.read_csv("data/week1.csv")
PLAYS = pd.read_csv("data/plays.csv")
PLAYERS = pd.read_csv("data/players.csv")
SCOUTING = pd.read_csv("data/pffScoutingData.csv")
PLAYID = 97 

# gameid = WEEKDF.gameId.unique()
gameid = 2021090900
plays = WEEKDF.playId.unique().copy()

df = pd.DataFrame(columns=['gameId','playId', 'playerId', 'sack', 'hurry', 'hit', 'xVal', 'yVal', 'coverage', 'q', 'pos', 'qb', 'avgSpeed', 'avgAcc'])

count = 0 
for p in plays: 
    PLAYID = p
    idBlock = WEEKDF.query("(playId == @PLAYID) and (gameId == @gameid)").nflId.unique().copy()
    play = WEEKDF.query("(playId == @PLAYID) and (gameId == @gameid)").copy()
    
    for id in idBlock:
        if math.isnan(id) == False:
            x, y = getPlayerXY(play, id)
            newRow = { 'gameId':gameid , 'playId':PLAYID, 'playerId':id, 'sack':SCOUTING.query("(playId == @PLAYID) and (nflId == @id) and (gameId == @gameid)").pff_sack.values[0], 
                'hurry':SCOUTING.query("(playId == @PLAYID) and (nflId == @id) and (gameId == @gameid)").pff_hurry.values[0], 'hit':SCOUTING.query("(playId == @PLAYID) and (nflId == @id) and (gameId == @gameid)").pff_hit.values[0], 
                'xVal':x.values[0], 'yVal':y.values[0], 'coverage':PLAYS.query("(playId == @PLAYID) and (gameId == @gameid)").pff_passCoverageType.values[0], 
                'q':PLAYS.query("(playId == @PLAYID) and (gameId == @gameid)").quarter.values[0], 'pos':SCOUTING.query("(playId == @PLAYID) and (gameId == @gameid) and (nflId == @id)").pff_positionLinedUp.values[0], 
                'qb':SCOUTING.query("(playId == @PLAYID) and (gameId == @gameid) and (pff_role == 'Pass')").nflId.values[0], 
                'avgSpeed':np.average(WEEKDF.query("(playId == @PLAYID) and (gameId == @gameid) and (nflId == @id)").s.values),
                'avgAcc':np.average(WEEKDF.query("(playId == @PLAYID) and (gameId == @gameid) and (nflId == @id)").a.values)}
            df = df.append(newRow, ignore_index=True)
            
print(df)

    