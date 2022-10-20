def drawPath(play, total, people, list):
# Plot path 
    gId = play.gameId.unique()[0]
    pId = play.playId.unique()[0]
    total = total.query("gameId == @gId")
    total = total.query("playId == @pId")
    desc = total.playDescription.unique()    
    
    a,b = getPlayerXY(play, list[0])
    c,d = getPlayerXY(play, list[1])
    e,f = getPlayerXY(play, list[2])
    g,h = getPlayerXY(play, list[3])
    i,j = getPlayerXY(play, list[4])
    k,l = getPlayerXY(play, list[5])
    m,n = getPlayerXY(play, list[6])
    o,p = getPlayerXY(play, list[7])
    q,r = getPlayerXY(play, list[8])
    s,t = getPlayerXY(play, list[9])
    u,v = getPlayerXY(play, list[10])
    
    import matplotlib.pyplot as plt 
    # fig = plt.figure()
    # movement = fig.add_axes([0,0,1,1])
    plt.plot(a,b, label=people.query("nflId == @list[0]").displayName.unique()[0])
    plt.plot(c,d, label=people.query("nflId == @list[1]").displayName.unique()[0])
    plt.plot(e,f, label=people.query("nflId == @list[2]").displayName.unique()[0])
    plt.plot(g,h, label=people.query("nflId == @list[3]").displayName.unique()[0])
    plt.plot(i,j, label=people.query("nflId == @list[4]").displayName.unique()[0])
    plt.plot(k,l, label=people.query("nflId == @list[5]").displayName.unique()[0])
    plt.plot(m,n, label=people.query("nflId == @list[6]").displayName.unique()[0])
    plt.plot(o,p, label=people.query("nflId == @list[7]").displayName.unique()[0])
    plt.plot(q,r, label=people.query("nflId == @list[8]").displayName.unique()[0])
    plt.plot(s,t, label=people.query("nflId == @list[9]").displayName.unique()[0])
    plt.plot(u,v, label=people.query("nflId == @list[10]").displayName.unique()[0])
    # movement.set_ylim(0,53.3) # Height of football field 
    # movement.set_xlim(0,120) # Width of football field 
    plt.grid(True, color="black", axis="x")
    plt.title(desc[0], fontsize=8)
    plt.legend()
    plt.show()

def getPlayerXY(play, player):
    pPath = play.query("nflId == @player")
    x = pPath.x
    y = pPath.y

    return x,y
