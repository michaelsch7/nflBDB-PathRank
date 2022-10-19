# Imports 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

# Get Data 
playData = pd.read_csv('data/plays.csv')
gameData = pd.read_csv('data/games.csv')
playerData = pd.read_csv('data/players.csv')
pffData = pd.read_csv('data/pffScoutingData.csv')
week1Data = pd.read_csv('data/week1.csv')

def drawPath(playid, team, jersey):
# Query to get desired play, player
    Play = week1Data.query("playId == @playid")
    Team = Play.query("team == @team")
    playerPath = Team.query("jerseyNumber == @jersey")

# Movement path
    x = playerPath.x
    y = playerPath.y

# Plot path 
    fig = plt.figure()
    movement = fig.add_axes([0,0,1,1])
    movement.plot(x,y)
    movement.set_ylim(0,53.3) # Height of football field 
    movement.set_xlim(0,120) # Width of football field 
    plt.grid(True, color="black", axis="x")
    plt.show()