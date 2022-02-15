from flask import Flask, render_template, request, session
from numpy import random
import sqlite3 as sql
from bds import *
from datetime import datetime

crear_tablas() # base de datos

app = Flask(__name__)
app.secret_key = 'asdfDF92.,'

juegos = {'Adivina el número': 'adivina_numero'}

@app.route("/", methods = ['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('login.html', juegos = juegos)
    else:
        session['user'] = request.form.get('user')
        return render_template('home.html', nombre = session['user'], juegos = juegos)

@app.route("/adivina_numero", methods = ['GET','POST'])
def adivina_numero():
    if request.method == 'GET':
        msg = 'Adivina un número entre 1 y 100. Yo te diré si es demasiado alto o demasiado bajo.'
        exito = False
        session['num_pc'] = random.randint(1,101) # usamos session para que guarde el valor entre una request y otra
        session['intentos'] = 0
    else:
        session['intentos'] = session['intentos'] + 1
        num = int(request.form.get('guess'))
        if num == session['num_pc']:
            num_intentos = session['intentos']
            msg = f'Acertaste en {num_intentos} intentos.'
            exito = True
            msg_insert = insert_adivina_numero(session['user'], datetime.now().strftime("%Y-%m-%d %H:%M:%S"),num_intentos)
            msg = msg + ' -- ' + msg_insert
        else:
            exito = False
            if num > session['num_pc']:
                msg = 'Demasiado alto'
            else:
                msg = 'Demasiado bajo'
    return render_template('adivina_numero.html', msg = msg, exito = exito)

@app.route("/adivina_numero/estadisticas", methods = ['GET','POST'])
def adivina_numero_estadisticas():
    filas_bd, columnas_bd = fetch_list('adivina_numero')
    return render_template("list.html",mensaje = "Estadísticas del juego 'Adivina el número'",columnas = columnas_bd, filas = filas_bd)

if (__name__ == "__main__"):
    app.run(debug = True)