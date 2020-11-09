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
