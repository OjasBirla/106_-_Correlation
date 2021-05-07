import csv
import numpy as np
import pandas as pd
import plotly.express as px

def getDataSource():
    with open("Student Marks vs Days Present.csv") as f:
        reader = csv.DictReader(f)

        marks = []
        daysPresent = []

        for i in list(reader):
            marks.append(float(i["Marks In Percentage"]))
            print(marks)
            daysPresent.append(float(i["Days Present"]))
        
        return {"x": marks, "y": daysPresent}

def findCorrelation(dataSoucre):
    correlation = np.corrcoef(dataSoucre["x"], dataSoucre["y"])
    return correlation

def plotFigure(data_path):
    df = pd.read_csv(data_path)

    graph = px.scatter(df, y="Marks In Percentage", x="Days Present")
    graph.show()

def setup():
    dataSoucre = getDataSource()
    correlation = findCorrelation(dataSoucre)
    print(correlation[0, 1])

    plotFigure("Student Marks vs Days Present.csv")

setup()