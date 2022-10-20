import numpy as np
import pandas as pd
from DrawPath import drawPath

def main():
    weekDF = pd.read_csv("week1.csv")
    drawPath(97, "TB", 13, weekDF)

if __name__ == '__main__':
    main()