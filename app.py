from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)

@app.route('/')
def default():
    return render_template('index.html')


@app.route('/rstudio')
def open_rstudio():
    return redirect("http://localhost:8787")

@app.route('/hadoop')
def open_hadoop():
    return redirect("http://localhost:8042/node")

@app.route('/spyder')
def open_spyder():
    return redirect("http://localhost:6080/vnc.html?resize=downscale&autoconnect=1&password=spyder")

@app.route('/spark')
def open_spark():
    return redirect("http://localhost:8081")

@app.route('/ibm')
def open_ibm():
    return redirect("https://welcome.oda.sas.com/login")

@app.route('/tableau')
def open_tableau():
    return redirect("https://sso.online.tableau.com/public/idp/SSO")

@app.route('/git')
def open_git():
    return redirect("http://localhost:3000")

@app.route('/sonar')
def open_sonar():
    return redirect("http://localhost:9001")

@app.route('/jupyter')
def open_jupyter():
    return redirect("http://localhost:8888/?token=jupyter")

@app.route('/tensorflow')
def open_tensorflow():
    return redirect("http://localhost:8888/?token=tensorflow")

@app.route('/orange')
def open_orange():
    return redirect("http://localhost:6901/?password=orange")

@app.route('/markdown')
def open_markdown():
    return redirect("http://localhost:12345")

@app.route('/vscode')
def open_vscode():
    return redirect("http://localhost:8080/?password=vscode")