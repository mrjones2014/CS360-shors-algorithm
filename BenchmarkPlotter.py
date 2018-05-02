import plotly.offline as py
import plotly.graph_objs as go
import CsvDataWriter
import csv

def plot(data):
    """Takes a dict in the form {"x": [x axis data], "y": [y axis data]} and generates a plot."""
    trace = go.Scatter(x=data["x"], y=data["y"])
    plotData = [trace]
    layout = go.Layout(title="Runtime of Shor's Algorithm", width=800, height=600)
    figure = go.Figure(data=plotData, layout=layout)
    # py.image.save_as(figure, filename="test-plot.png")
    py.iplot(figure, image_width=800, image_height=600)

def transform_data(data):
    x_axis = []
    y_axis = []
    for i in data:
        x_axis.append(i[0])
        y_axis.append(i[len(i) - 1])
    
    plotData = {"x": x_axis, "y": y_axis}
    print(plotData)
    return plotData

def parse_data(filename):
    x_axis = []
    y_axis = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            x_axis.append(row["input"])
            y_axis.append(row["average"])
    return {"x": x_axis, "y": y_axis}
            

if __name__ == "__main__":
    filename = CsvDataWriter.test()
    plot_data = parse_data(filename)
    plot(plot_data)