import numpy as np
import pandas as pd
from DrawPath import drawPath, getPlayerXY

WEEKDF = pd.read_csv("data/week1.csv")
PLAYS = pd.read_csv("data/plays.csv")
PLAYERS = pd.read_csv("data/players.csv")
SCOUTING = pd.read_csv("data/pffScoutingData.csv")
PLAYID = 97 

id = WEEKDF.query("playId == @PLAYID").nflId[0].copy()
play = WEEKDF.query("playId == @PLAYID")
x, y = getPlayerXY(play, id)
gameid = WEEKDF.query("playId == @PLAYID").gameId.unique()[0]

print(WEEKDF.query("playId == @PLAYID").gameId.unique()[0] , PLAYID, id, SCOUTING.query("(playId == @PLAYID) and (nflId == @id)").pff_sack.values[0], 
      SCOUTING.query("(playId == @PLAYID) and (nflId == @id)").pff_hurry.values[0], SCOUTING.query("(playId == @PLAYID) and (nflId == @id)").pff_hit.values[0], 
      x.values[0], y.values[0], PLAYS.query("(playId == @PLAYID) and (gameId == @gameid)").pff_passCoverageType.values[0], 
      PLAYS.query("(playId == @PLAYID) and (gameId == @gameid)").quarter.values[0], SCOUTING.query("(playId == @PLAYID) and (gameId == @gameid) and (nflId == @id)").pff_positionLinedUp.values[0], 
       SCOUTING.query("(playId == @PLAYID) and (gameId == @gameid) and (pff_role == 'Pass')").nflId.values[0], 
       np.average(WEEKDF.query("(playId == @PLAYID) and (gameId == @gameid) and (nflId == @id)").s.values), np.average(WEEKDF.query("(playId == @PLAYID) and (gameId == @gameid) and (nflId == @id)").a.values))