import numpy as np 
from DrawPath import getPlayerXY
import matplotlib.pyplot as plt 

def optimalPath(weekDF, total, people, scouting, playid):
    
    defLine = []
    qb = []
    
    play = weekDF.query("playId == @playid")
    scouting = scouting.query("playId == @playid")
    scouting = scouting.query("gameId == @play.gameId.unique()[0]")
    scouting = scouting.query("(pff_role == 'Pass Rush') or (pff_role == 'Pass')")
    
    for player in play.nflId.unique():
        if(scouting.query("pff_role == 'Pass Rush'").nflId.values.__contains__(player)):
            defLine.append(player)
        if(scouting.query("pff_role == 'Pass'").nflId.values.__contains__(player)):
            qb.append(player)

    for i in qb:
        qbX, qbY = getPlayerXY(play, i)
    
    for j in defLine: 
        dlX, dlY = getPlayerXY(play, j)
        if(people.query("(nflId == @j) and (officialPosition == 'NT')").nflId.values.__contains__(j)):
            plt.plot([qbX.values[0], dlX.values[0]], [qbY.values[0], dlY.values[0]], marker='<')
            
    
