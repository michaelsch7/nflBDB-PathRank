def drawPath(x,y):
# Plot path 
    import matplotlib.pyplot as plt 
    fig = plt.figure()
    movement = fig.add_axes([0,0,1,1])
    movement.plot(x,y)
    movement.set_ylim(0,53.3) # Height of football field 
    movement.set_xlim(0,120) # Width of football field 
    plt.grid(True, color="black", axis="x")
    plt.show()

def getPlayerXY(play, player):
    pPath = play.query("jerseyNumber == @player")
    x = pPath.x
    y = pPath.y

    return x,y
