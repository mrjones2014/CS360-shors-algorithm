#!/usr/bin/env python3

import plotly.offline as py
import plotly.graph_objs as go
import CsvDataWriter
import pprint
import csv
import glob
import os

pp = pprint.PrettyPrinter(indent=4)

def get_most_recent_data_file():
    list_of_files = glob.glob('./benchmark_data/*') # * means all if need specific format then *.csv
    return max(list_of_files, key=os.path.getctime)

def plot(data):
    """Takes a dict in the form {"x": [x axis data], "y": [y axis data]} and generates a plot."""
    trace = go.Scatter(x=data["x"], y=data["y"], mode='lines+markers', name='lines+markers')
    plotData = [trace]
    layout = go.Layout(title="Runtime of Shor's Algorithm", width=800, height=600)
    figure = go.Figure(data=plotData, layout=layout)
    # py.image.save_as(figure, filename="test-plot.png")
    print(py.plot(figure, image_width=800, image_height=600))

def make_plot(filename):
    plot(parse_data(filename))

def transform_data(data):
    x_axis = []
    y_axis = []
    for i in data:
        x_axis.append(i[0])
        y_axis.append(i[len(i) - 1])
    
    plotData = {"x": x_axis, "y": y_axis}
    # print(plotData)
    return plotData

def parse_data(filename):
    x_axis = []
    y_axis = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            x_axis.append(row["input_len"])
            y_axis.append(row["average"])
    data = {"x": x_axis, "y": y_axis}
    pp.pprint(data)
    print()
    print()
    return data
            

if __name__ == "__main__":
    make_plot(get_most_recent_data_file())