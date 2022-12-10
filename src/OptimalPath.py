# Imports 
import numpy as np 
from DrawPath import getPlayerXY
import matplotlib.pyplot as plt 

# Function optimalPath:
# this function takes in 5 parameters: the week dataframe, the plays dataframe, the players dataframe, the scouting dataframe,
# and the play id (numeric)
# this function plots the 'optimal pass rush path' and gets the equation of the line 
# 
# 
def optimalPath(weekDF, total, people, scouting, playid):
    
    # sets for the 'pass rushers' and 'qb' 
    defLine = []
    qb = []
    
    # query week-x data to the play, query Scouting data to the play, 
    # get players who are only pass rushers or the qb for paths 
    play = weekDF.query("playId == @playid")
    scouting = scouting.query("playId == @playid")
    scouting = scouting.query("gameId == @play.gameId.unique()[0]")
    scouting = scouting.query("(pff_role == 'Pass Rush') or (pff_role == 'Pass')")
    
    # fill sets with playerId 
    for player in play.nflId.unique():
        if(scouting.query("pff_role == 'Pass Rush'").nflId.values.__contains__(player)):
            defLine.append(player)
        if(scouting.query("pff_role == 'Pass'").nflId.values.__contains__(player)):
            qb.append(player)

    # get player movement points for each set
    for i in qb:
        qbX, qbY = getPlayerXY(play, i)
    for j in defLine:
        dlX, dlY = getPlayerXY(play, j)
    
    # plot values   
        if(people.query("nflId == @j").nflId.values.__contains__(j)):
            plt.plot([qbX.values[0] - 3, dlX.values[0]], [qbY.values[0], dlY.values[0]], marker='<')
            print()
            # getFunction(qbX.values[0] - 3, dlX.values[0], qbY.values[0], dlY.values[0], True)
            getFunction(qbX.values[0] - 3, dlX.values[0], qbY.values[0], dlY.values[0])
            print()
    
# simple y=mx+b equation    
def getFunction(x1, x2, y1, y2): 
    # if(isOptimal == True):
        m = (y2-y1) / (x2-x1)
        b = y1 - m*x1
        print(np.array([m,b]))
        return np.array([m,b])
    # if(isOptimal == False):
    #     # Implement getFunc method for curved lines
    #     print(np.polyfit(x2,y2,5))
    #     return np.polyfit(x2,y2,5)
            
    
