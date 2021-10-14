import numpy as np
import csv
from plotly import plot
import plotly.express as px

def getDataSource(data_path):
    marks_in_percentage=[]
    days_present=[]
    with open(data_path) as csv_file:
        raeder = csv.DictReader(csv_file)
        for row in raeder:
            marks_in_percentage.append(float(row['Marks In Percentage']))
            days_present.append(float(row['Days Present']))
        return{"x":marks_in_percentage,"y":days_present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between marks in percentage and days preset is:--" , correlation[0,1])

def plotFigure(data_path):
    with open(data_path) as f:
        df= csv.DictReader(f)
        fig= px.scatter(df,x="Days Present",y="Marks In Percentage")
        fig.show()


def setup():
    data_path= "c-160.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()

