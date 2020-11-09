from flask import Flask, Markup, render_template, redirect, url_for
import json
import datetime

app = Flask(__name__)

@app.after_request
def add_header(response):
    expiry_time = datetime.datetime.utcnow() + datetime.timedelta(0.1)
    response.headers['Cache-Control'] = 'public, max-age=360'
    response.headers["Expires"] = expiry_time.strftime("%a, %d %b %Y %H:%M:%S GMT")
    return response

def read_api(table):
    labels = []
    cases = []
    data = {}
    import urllib, json
    import urllib.request
    apiurl = "http://api:4006/api/v1/corona/" + table
    response = urllib.request.urlopen(apiurl)
    data = json.loads(response.read())
    for label in data['cases']:
        labels.append(label['name'])
        cases.append(label['val'])
    return (labels, cases)

def read_api_month(table,month):
    labels = []
    cases = []
    data = {}
    import urllib, json
    import urllib.request
    apiurl = "http://api:4006/api/v1/corona/" + table + "/month/" + month
    response = urllib.request.urlopen(apiurl)
    data = json.loads(response.read())
    for label in data['cases']:
        labels.append(label['name'])
        cases.append(label['val'])
    return (labels, cases)

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
    apiurl = "http://api:4006/api/v1/corona/config/" + key
    response = urllib.request.urlopen(apiurl)
    data = json.loads(response.read())
    return data

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/')
def index():
    return redirect(url_for('linecharts'))
    # table = 'cases'
    # labels, values = read_api(table)
    # line_labels=labels
    # line_values=values
    # return render_template('line_chart.html', pageuri=table, title='Corona ' + table, max=read_config(table), labels=line_labels, values=line_values)

@app.route('/view/charts')
def linecharts():
    labels_current, values_current = read_api("current")
    labels_average, values_average = read_api("average")
    labels_cases, values_cases = read_api("cases")
    labels_probes, values_probes = read_api("probes")
    return render_template('charts_line.html',
            labels_current=labels_current, values_current=values_current,
            labels_average=labels_average, values_average=values_average,
            labels_cases=labels_cases,     values_cases=values_cases,
            labels_probes=labels_probes,   values_probes=values_probes
        )

@app.route('/view/charts/<table>')
def linechart(table):
    labels, values = read_api(table)
    return render_template('chart_line.html', text=table, labels=labels, values=values )

@app.route('/klopapier')
def klopapier():
    labels, values = read_klopapier()
    return render_template('chart_line.html', text='Klopapier DM-Drogerie Essen Borbeck',
        labels=labels, values=values)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

# @app.route('/<table>')
# def line(table):
#     labels, values = read_api(table)
#     line_labels=labels
#     line_values=values
#     return render_template('line_chart.html', pageuri=table, title='Corona ' + table, max=read_config(table), labels=line_labels, values=line_values)
#
# @app.route('/<table>/<id>')
# def probes_x(table,id):
#     id = int(id)
#     probelabels, probevalues = read_api(table)
#     line_labels=probelabels[-id:]
#     line_values=probevalues[-id:]
#     return render_template('line_chart.html', pageuri=table, title='Corona ' + table, max=read_config(table), labels=line_labels, values=line_values)
#
# @app.route('/<table>/month/<id>')
# def dataByMonth(table,id):
#     id = str(id)
#     probelabels, probevalues = read_api_month(table,id)
#     line_labels=probelabels
#     line_values=probevalues
#     return render_template('line_chart.html', pageuri=table, title='Corona ' + table, max=read_config(table), labels=line_labels, values=line_values)
#
#
# @app.route('/klopapier')
# def klopapier():
#     klopapierlabels, klopapiervalues = read_klopapier()
#     line_labels=klopapierlabels
#     line_values=klopapiervalues
#     return render_template('line_klopapier.html', title='Klopapier DM-Drogerie Essen Borbeck', max=read_config("klopapier"), labels=line_labels, values=line_values)
#
# @app.route('/klopapier/<id>')
# def klopapier_x(id):
#     id = int(id)
#     klopapierlabels, klopapiervalues = read_klopapier()
#     line_labels=klopapierlabels[-id:]
#     line_values=klopapiervalues[-id:]
#     return render_template('line_klopapier.html', title='Klopapier DM-Drogerie Essen Borbeck', max=read_config("klopapier"), labels=line_labels, values=line_values)

# def read_markedplace():
#     name = []
#     value = []
#     data = {}
#     import urllib, json
#     import urllib.request
#     apiurl = "http://api:4006/api/v1/markplace"
#     response = urllib.request.urlopen(apiurl)
#     data = json.loads(response.read())
#     return data
#
# def read_markedplaceById(id):
#     name = []
#     value = []
#     data = {}
#     import urllib, json
#     import urllib.request
#     apiurl = "http://api:4006/api/v1/markplace/" + id
#     response = urllib.request.urlopen(apiurl)
#     data = json.loads(response.read())
#     return data

# def read_cases():
#     clabels = []
#     ccases = []
#     data = {}
#     import urllib, json
#     import urllib.request
#     apiurl = "http://api:4006/api/v1/corona/cases"
#     response = urllib.request.urlopen(apiurl)
#     data = json.loads(response.read())
#     for label in data['cases']:
#         clabels.append(label['name'])
#         ccases.append(label['val'])
#     return (clabels, ccases)
#
# def read_average():
#     clabels = []
#     ccases = []
#     data = {}
#     import urllib, json
#     import urllib.request
#     apiurl = "http://api:4006/api/v1/corona/average"
#     response = urllib.request.urlopen(apiurl)
#     data = json.loads(response.read())
#     for label in data['cases']:
#         clabels.append(label['name'])
#         ccases.append(label['val'])
#     return (clabels, ccases)
#
# def read_probes():
#     clabels = []
#     ccases = []
#     data = {}
#     import urllib, json
#     import urllib.request
#     apiurl = "http://api:4006/api/v1/corona/probes"
#     response = urllib.request.urlopen(apiurl)
#     data = json.loads(response.read())
#     for label in data['cases']:
#         clabels.append(label['name'])
#         ccases.append(label['val'])
#     return (clabels, ccases)
#
# def read_current():
#     clabels = []
#     ccases = []
#     data = {}
#     import urllib, json
#     import urllib.request
#     apiurl = "http://api:4006/api/v1/corona/current"
#     response = urllib.request.urlopen(apiurl)
#     data = json.loads(response.read())
#     for label in data['cases']:
#         clabels.append(label['name'])
#         ccases.append(label['val'])
#     return (clabels, ccases)

# @app.route('/probes')
# def probes():
#     probelabels, probevalues = read_probes()
#     line_labels=probelabels
#     line_values=probevalues
#     return render_template('line_chart.html',pageuri='probes',  title='Corona Probes', max=read_config("probes"), labels=line_labels, values=line_values)

# @app.route('/probes/<id>')
# def probes_x(id):
#     id = int(id)
#     probelabels, probevalues = read_probes()
#     line_labels=probelabels[-id:]
#     line_values=probevalues[-id:]
#     return render_template('line_chart.html', pageuri='probes', title='Corona Probes', max=read_config("probes"), labels=line_labels, values=line_values)

# @app.route('/line')
# def line():
#     labels, values = read_cases()
#     line_labels=labels
#     line_values=values
#     return render_template('line_chart.html', pageuri='line', title='Corona Fallzahlen', max=read_config("cases"), labels=line_labels, values=line_values)

# @app.route('/bar')
# def bar():
#     labels, values = read_cases()
#     bar_labels=labels
#     bar_values=values
#     return render_template('bar_chart.html', title='Corona Fallzahlen', max=read_config("cases"), labels=bar_labels, values=bar_values)
#
# @app.route('/bar/<id>')
# def bar_x(id):
#     id = int(id)
#     labels, values = read_cases()
#     bar_labels=labels[-id:]
#     bar_values=values[-id:]
#     return render_template('bar_chart.html', title='Corona Fallzahlen', max=read_config("cases"), labels=bar_labels, values=bar_values)

# @app.route('/averagebar')
# def averagebar():
#     averagelabels, averagevalues = read_average()
#     bar_labels=averagelabels
#     bar_values=averagevalues
#     return render_template('averagebar_chart.html', title='Corona 7-Tage Durchschnitt ', max=read_config("average"), labels=bar_labels, values=bar_values)

# @app.route('/averagebar/<id>')
# def averagebar_x(id):
#     id = int(id)
#     averagelabels, averagevalues = read_average()
#     bar_labels=averagelabels[-id:]
#     bar_values=averagevalues[-id:]
#     return render_template('averagebar_chart.html', pageuri='averageline', title='Corona 7-Tage Durchschnitt ', max=read_config("average"), labels=bar_labels, values=bar_values)

# @app.route('/pie')
# def pie():
#     pie_labels = labels
#     pie_values = values
#     return render_template('pie_chart.html', title='Corona Fallzahlen', max=read_config("cases"), set=zip(values, labels, colors))

# @app.route('/line/<id>')
# def line_x(id):
#     id = int(id)
#     labels, values = read_cases()
#     line_labels=labels[-id:]
#     line_values=values[-id:]
#     return render_template('line_chart.html', pageuri='line', title='Corona Fallzahlen', max=read_config("cases"), labels=line_labels, values=line_values)
#
# @app.route('/averageline')
# def averageline():
#     averagelabels, averagevalues = read_average()
#     line_labels=averagelabels
#     line_values=averagevalues
#     return render_template('line_chart.html', pageuri='averageline', title='Corona 7-Tage Durchschnitt', max=read_config("average"), labels=line_labels, values=line_values)
#
# @app.route('/averageline/<id>')
# def averageline_x(id):
#     id = int(id)
#     averagelabels, averagevalues = read_average()
#     line_labels=averagelabels[-id:]
#     line_values=averagevalues[-id:]
#     return render_template('line_chart.html', pageuri='averageline', title='Corona 7-Tage Durchschnitt', max=read_config("average"), labels=line_labels, values=line_values)
#
# @app.route('/current')
# def current():
#     currentlabels, currentvalues = read_current()
#     line_labels=currentlabels
#     line_values=currentvalues
#     return render_template('line_chart.html', pageuri='current', title='Aktuelle Fallzahlen', max=read_config("current"), labels=line_labels, values=line_values)
#
# @app.route('/current/<id>')
# def current(id):
#     id = int(id)
#     currentlabels, currentvalues = read_current()
#     line_labels=currentlabels[-id:]
#     line_values=currentvalues[-id:]
#     return render_template('line_chart.html', pageuri='current', title='Aktuelle Fallzahlen', max=read_config("current"), labels=line_labels, values=line_values)
