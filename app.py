from ensurepip import bootstrap
from multiprocessing import context
from flask import Flask, redirect,request,make_response,render_template,url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

items = ["Tenis", "Zapatillas", "Sandalias"]

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', e=e), 404

@app.route('/index')
def index():
    ip_usuario = request.remote_addr
    response = make_response(redirect("/informacion"))
    response.set_cookie('ip_usuario', ip_usuario)
    return response 

@app.route('/informacion')
def informacion():
    ip_usuario = request.cookies.get('ip_usuario')
    context = {
        "ip_usuario": ip_usuario,
        "items": items
    }
    return render_template("informacion.html", **context)

app.run(debug=True)