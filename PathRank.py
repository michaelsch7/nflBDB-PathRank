import numpy as np
import pandas as pd
from DrawPath import drawPath, getPlayerXY

def main():
    weekDF = pd.read_csv("week1.csv")
    # drawPath(97, "TB", 13, 12, weekDF)
    play = weekDF.query("playId == 4287")
    play = play.query("team == 'TB'")

    list = []
    for player in play.jerseyNumber.unique():
        list.append(player)
    
    drawPath(play, list)

if __name__ == '__main__':
    main()