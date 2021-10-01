from flask import Flask, redirect, render_template
import requests

app = Flask(__name__)

def main():
    urlClientes = 'https://sistemalift1.com/lift_ps/api/Clientes'
    urlPedidos = 'https://sistemalift1.com/lift_ps/api/Pedidos'
    urlProdutos = 'https://sistemalift1.com/lift_ps/api/Produtos'
    urlItens = 'https://sistemalift1.com/lift_ps/api/ItensPedido'

    clientes = requests.get(urlClientes).json()
    pedidos = requests.get(urlPedidos).json()
    produtos = requests.get(urlProdutos).json()
    itens = requests.get(urlItens).json()

    listaClientes = [cliente['nome'] for cliente in clientes]
    # print(listaClientes)

    listaPedidos = [pedido['cliente'] for pedido in pedidos]
    # print(listaPedidos)

    listaData = [pedido['data'] for pedido in pedidos]
    # print(listaData)

    listaPedidosFinal = []

    for i in range(len(itens)):
        row = {}
        row['código'] = itens[i]['pedido']
        row['cliente'] = clientes[pedidos[itens[i]['pedido'] - 1]['cliente'] - 1]['nome']
        row['data'] = pedidos[itens[i]['pedido'] - 1]['data']
        row['valor'] = produtos[itens[i]['produto'] - 1]['valor'] * itens[i]['quantidade']
        listaPedidosFinal.append(row)

    return listaPedidosFinal

@app.route('/')
def home():
    tabela = main()
    lista = {'codigo': '1', 'nome': "Sérgio Theo Galvão", "data": "29-01-2000"}
    return render_template("index.html", tabela=tabela)

if __name__ == '__main__':
    app.run()