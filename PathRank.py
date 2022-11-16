import numpy as np
import pandas as pd
from DrawPath import drawPath

def main():
    # Data
    weekDF = pd.read_csv("data/week1.csv")
    people = pd.read_csv("data/players.csv")
    total = pd.read_csv("data/plays.csv")
    scouting = pd.read_csv("data/pffScoutingData.csv")
    
    # Run drawPath - Expected output picture    
    drawPath(weekDF, total, people, scouting, 2298)
    
if __name__ == '__main__':
    main()
