# test
import numpy as np
import pandas as pd
from DrawPath import drawPath

WEEKDF = pd.read_csv("data/week1.csv")
PLAYS = pd.read_csv("data/plays.csv")
PLAYERS = pd.read_csv("data/players.csv")
SCOUTING = pd.read_csv("data/pffScoutingData.csv")
PLAYID = 1687  
  
def main():
    # Run drawPath - Expected output picture    
    drawPath(WEEKDF, PLAYS, PLAYERS, SCOUTING, PLAYID)
    
if __name__ == '__main__':
    main()
