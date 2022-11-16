def drawPath(weekDF, total, people, scouting, playid):
        # Plot path 
        import matplotlib.pyplot as plt 
        
        play = weekDF.query("playId == @playid")
        list = []
        scouting = scouting.query("playId == @playid")
        scouting = scouting.query("gameId == @play.gameId.unique()[0]")
        scouting = scouting.query("(pff_role == 'Pass Rush') or (pff_role == 'Pass')")
        for player in play.nflId.unique():
            if(scouting.nflId.values.__contains__(player)):
                list.append(player)
        
        desc = total.playDescription.unique()   
    
        for i in list:
            x,y = getPlayerXY(play, i)
            plt.plot(x,y, label=people.query("nflId == @i").displayName.unique()[0], marker = '<', linestyle = 'None')
        
        plt.grid(True, color="black", axis="x")
        plt.title("Pass Rush", fontsize=8)
        plt.legend()
        plt.show()

def getPlayerXY(play, player):
        pPath = play.query("nflId == @player")
        x = pPath.x
        y = pPath.y

        return x,y

