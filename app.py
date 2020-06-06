from flask import Flask, Markup, render_template
import json

app = Flask(__name__)

# labels = [
#     'JAN', 'FEB', 'MAR', 'APR',
#     'MAY', 'JUN', 'JUL', 'AUG',
#     'SEP', 'OCT', 'NOV', 'DEC'
# ]

def read_cases():
    clabels = []
    ccases = []
    data = json.loads(open('cases.json','r').read())
    for label in data['cases'][0]:
        clabels.append(label)
        ccases.append(data['cases'][0][label])
        # print ("Label: ", clabels, " cases: ", ccases)
    return (clabels, ccases)

def read_average():
    clabels = []
    ccases = []
    data = json.loads(open('average.json','r').read())
    for label in data['cases'][0]:
        clabels.append(label)
        ccases.append(data['cases'][0][label])
        # print ("Label: ", clabels, " cases: ", ccases)
    return (clabels, ccases)


labels, values = read_cases()
averagelabels, averagevalues = read_average()
# values = [
#     967.67, 1190.89, 1079.75, 1349.19,
#     2328.91, 2504.28, 2873.83, 4764.87,
#     4349.29, 6458.30, 9907, 16297
# ]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/bar')
def bar():
    bar_labels=labels
    bar_values=values
    return render_template('bar_chart.html', title='Corona Fallzahlen', max=900, labels=bar_labels, values=bar_values)

# average
@app.route('/averagebar')
def averagebar():
    bar_labels=averagelabels
    bar_values=averagevalues
    return render_template('averagebar_chart.html', title='Corona 7-Tage Durchschnitt ', max=10, labels=bar_labels, values=bar_values)


@app.route('/line')
def line():
    line_labels=labels
    line_values=values
    return render_template('line_chart.html', title='Corona Fallzahlen', max=900, labels=line_labels, values=line_values)

@app.route('/averageline')
def averageline():
    line_labels=averagelabels
    line_values=averagevalues
    return render_template('line_chart.html', title='Corona 7-Tage Durchschnitt', max=10, labels=line_labels, values=line_values)


@app.route('/pie')
def pie():
    pie_labels = labels
    pie_values = values
    return render_template('pie_chart.html', title='Corona Fallzahlen', max=900, set=zip(values, labels, colors))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
