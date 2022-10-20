import numpy as np
import pandas as pd
from DrawPath import drawPath, getPlayerXY

def main():
    weekDF = pd.read_csv("week1.csv")
    people = pd.read_csv("players.csv")
    total = pd.read_csv("plays.csv")
    play = weekDF.query("playId == 4287")
    play = play.query("team == 'DAL'")

    list = []
    for player in play.nflId.unique():
        list.append(player)
    
    drawPath(play, total, people, list)

if __name__ == '__main__':
    main()