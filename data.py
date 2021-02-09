import plotly.figure_factory as pf
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()
fig = pf.create_distplot([data], ["Reading Time"], show_hist = False)
fig.show()

print("Population Mean ", statistics.mean(data))

def randomSetOfMeans(counter):
    dataSet = []

    for i in range(0, counter):
        randomIndex = random.randint(0, len(data))
        value = data[randomIndex]
        dataSet.append(value)

    mean = statistics.mean(dataSet)
    return mean

def showFig(meanList):
    df = meanList
    fig = pf.create_distplot([df], ["Reading Time"], show_hist = False)
    fig.show()

def main():
    meanlist = []

    for i in range(0,100):
        setOfMeans = randomSetOfMeans(10)
        meanlist.append(setOfMeans)
    showFig(meanlist)
    print("Sampling Mean: ", statistics.mean(meanlist))

main()