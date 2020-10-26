from flask import Flask, Markup, render_template
import json

app = Flask(__name__)

def read_cases():
    clabels = []
    ccases = []
    data = {}
    import urllib, json
    import urllib.request
    apiurl = "http://api:4006/api/v1/corona/cases"
    response = urllib.request.urlopen(apiurl)
    data = json.loads(response.read())
    for label in data['cases']:
        clabels.append(label['name'])
        ccases.append(label['val'])
    return (clabels, ccases)

def read_average():
    clabels = []
    ccases = []
    data = {}
    import urllib, json
    import urllib.request
    apiurl = "http://api:4006/api/v1/corona/average"
    response = urllib.request.urlopen(apiurl)
    data = json.loads(response.read())
    for label in data['cases']:
        clabels.append(label['name'])
        ccases.append(label['val'])
    return (clabels, ccases)

def read_probes():
    clabels = []
    ccases = []
    data = {}
    import urllib, json
    import urllib.request
    apiurl = "http://api:4006/api/v1/corona/probes"
    response = urllib.request.urlopen(apiurl)
    data = json.loads(response.read())
    for label in data['cases']:
        clabels.append(label['name'])
        ccases.append(label['val'])
    return (clabels, ccases)

def read_current():
    clabels = []
    ccases = []
    data = {}
    import urllib, json
    import urllib.request
    apiurl = "http://api:4006/api/v1/corona/current"
    response = urllib.request.urlopen(apiurl)
    data = json.loads(response.read())
    for label in data['cases']:
        clabels.append(label['name'])
        ccases.append(label['val'])
    return (clabels, ccases)

def read_klopapier():
    clabels = []
    ccases = []
    data = {}
    import urllib, json
    import urllib.request
    apiurl = "http://api:4006/api/v1/klopapier"
    response = urllib.request.urlopen(apiurl)
    data = json.loads(response.read())
    for label in data['cases']:
        clabels.append(label['date'])
        ccases.append(label['val'])
    return (clabels, ccases)

def read_config(key):
    name = []
    value = []
    data = {}
    import urllib, json
    import urllib.request
    # /api/v1/corona/config/
    apiurl = "http://api:4006/api/v1/corona/config/" + key
    response = urllib.request.urlopen(apiurl)
    data = json.loads(response.read())
    return data

# max_average = 150
# max_cases = 3700
# max_probes = 44000
# max_current = 1000
max_klopapier = 2000

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/')
def index():
    labels, values = read_cases()
    bar_labels=labels
    bar_values=values
    return render_template('index.html', title='Corona Fallzahlen')

@app.route('/bar')
def bar():
    labels, values = read_cases()
    bar_labels=labels
    bar_values=values
    return render_template('bar_chart.html', title='Corona Fallzahlen', max=read_config("cases"), labels=bar_labels, values=bar_values)

@app.route('/bar/<id>')
def bar_x(id):
    id = int(id)
    labels, values = read_cases()
    bar_labels=labels[-id:]
    bar_values=values[-id:]
    return render_template('bar_chart.html', title='Corona Fallzahlen', max=read_config("cases"), labels=bar_labels, values=bar_values)

@app.route('/probes')
def probes():
    probelabels, probevalues = read_probes()
    line_labels=probelabels
    line_values=probevalues
    return render_template('probes_line_chart.html', title='Corona Probes', max=read_config("probes"), labels=line_labels, values=line_values)

@app.route('/probes/<id>')
def probes_x(id):
    id = int(id)
    probelabels, probevalues = read_probes()
    line_labels=probelabels[-id:]
    line_values=probevalues[-id:]
    return render_template('probes_line_chart.html', title='Corona Probes', max=read_config("probes"), labels=line_labels, values=line_values)

@app.route('/line')
def line():
    labels, values = read_cases()
    line_labels=labels
    line_values=values
    return render_template('line_chart.html', title='Corona Fallzahlen', max=read_config("cases"), labels=line_labels, values=line_values)

@app.route('/line/<id>')
def line_x(id):
    id = int(id)
    labels, values = read_cases()
    line_labels=labels[-id:]
    line_values=values[-id:]
    return render_template('line_chart.html', title='Corona Fallzahlen', max=read_config("cases"), labels=line_labels, values=line_values)


@app.route('/averagebar')
def averagebar():
    averagelabels, averagevalues = read_average()
    bar_labels=averagelabels
    bar_values=averagevalues
    return render_template('averagebar_chart.html', title='Corona 7-Tage Durchschnitt ', max=read_config("average"), labels=bar_labels, values=bar_values)

@app.route('/averageline')
def averageline():
    averagelabels, averagevalues = read_average()
    line_labels=averagelabels
    line_values=averagevalues
    return render_template('average_line_chart.html', title='Corona 7-Tage Durchschnitt', max=read_config("average"), labels=line_labels, values=line_values)

@app.route('/averagebar/<id>')
def averagebar_x(id):
    id = int(id)
    averagelabels, averagevalues = read_average()
    bar_labels=averagelabels[-id:]
    bar_values=averagevalues[-id:]
    return render_template('averagebar_chart.html', title='Corona 7-Tage Durchschnitt ', max=read_config("average"), labels=bar_labels, values=bar_values)

@app.route('/averageline/<id>')
def averageline_x(id):
    id = int(id)
    averagelabels, averagevalues = read_average()
    line_labels=averagelabels[-id:]
    line_values=averagevalues[-id:]
    return render_template('average_line_chart.html', title='Corona 7-Tage Durchschnitt', max=read_config("average"), labels=line_labels, values=line_values)

@app.route('/current')
def current():
    currentlabels, currentvalues = read_current()
    line_labels=currentlabels
    line_values=currentvalues
    return render_template('line_chart.html', title='Aktuelle Fallzahlen', max=read_config("current"), labels=line_labels, values=line_values)

@app.route('/pie')
def pie():
    pie_labels = labels
    pie_values = values
    return render_template('pie_chart.html', title='Corona Fallzahlen', max=read_config("cases"), set=zip(values, labels, colors))

@app.route('/klopapier')
def klopapier():
    klopapierlabels, klopapiervalues = read_klopapier()
    line_labels=klopapierlabels
    line_values=klopapiervalues
    return render_template('line_klopapier.html', title='Klopapier DM-Drogerie Essen Borbeck', max=read_config("klopapier"), labels=line_labels, values=line_values)

@app.route('/klopapier/<id>')
def klopapier_x(id):
    id = int(id)
    klopapierlabels, klopapiervalues = read_klopapier()
    line_labels=klopapierlabels[-id:]
    line_values=klopapiervalues[-id:]
    return render_template('line_klopapier.html', title='Klopapier DM-Drogerie Essen Borbeck', max=read_config("klopapier"), labels=line_labels, values=line_values)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
