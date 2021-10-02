from flask import Flask, redirect, render_template, request
import requests
from api import *

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

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
    cliente = get_info_clientes()
    pedido = teste[pedidos]
    lista = get_lista_pedidos()
    itens = get_items()
    clientes = get_clientes()
    pedi = get_pedidos()
    pessoa = clientes[pedi[itens[pedidos]['pedido'] - 1]['cliente'] - 1]
    pessoa['data'] = pedi[itens[pedidos]['pedido'] - 1]['data']
    return render_template("pedidos.html", pedido=pedido, cliente=pessoa)

    

if __name__ == '__main__':
    app.run()