from flask import Flask, redirect, render_template, request
import requests
from api import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        lista = get_lista_pedidos()
        pedidos = get_info_pedidos()
        return render_template("index.html", lista=lista, pedidos=pedidos)
    else:
        return redirect(f"/{request.form['submit_button']}")


teste = get_info_pedidos()

@app.route('/<int:pedidos>', methods=['GET', 'POST'])
def pedidos(pedidos):
    pedido = teste[pedidos]
    return render_template("teste.html", pedido=pedido)

if __name__ == '__main__':
    app.run()