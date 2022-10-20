def drawPath(play, list):
# Plot path 
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
    fig = plt.figure()
    movement = fig.add_axes([0,0,1,1])
    movement.plot(a,b)
    movement.plot(c,d)
    movement.plot(e,f)
    movement.plot(g,h)
    movement.plot(i,j)
    movement.plot(k,l)
    movement.plot(m,n)
    movement.plot(o,p)
    movement.plot(q,r)
    movement.plot(s,t)
    movement.plot(u,v)
    movement.set_ylim(0,53.3) # Height of football field 
    movement.set_xlim(0,120) # Width of football field 
    plt.grid(True, color="black", axis="x")
    plt.show()

def getPlayerXY(play, player):
    pPath = play.query("jerseyNumber == @player")
    x = pPath.x
    y = pPath.y

    return x,y
