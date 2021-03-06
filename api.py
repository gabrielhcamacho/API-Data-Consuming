import requests

urlClientes = 'https://sistemalift1.com/lift_ps/api/Clientes'
urlPedidos = 'https://sistemalift1.com/lift_ps/api/Pedidos'
urlProdutos = 'https://sistemalift1.com/lift_ps/api/Produtos'
urlItens = 'https://sistemalift1.com/lift_ps/api/ItensPedido'

clientes = requests.get(urlClientes).json()
pedidos = requests.get(urlPedidos).json()
produtos = requests.get(urlProdutos).json()
itens = requests.get(urlItens).json()

listaClientes = [cliente['nome'] for cliente in clientes]
listaPedidos = [pedido['cliente'] for pedido in pedidos]
listaData = [pedido['data'] for pedido in pedidos]

def get_lista_pedidos():
    listaPedidosFinal = []

    for i in range(len(itens)):
        row = {}
        row['código'] = itens[i]['pedido']
        row['cliente'] = clientes[pedidos[itens[i]['pedido'] - 1]['cliente'] - 1]['nome']
        row['data'] = pedidos[itens[i]['pedido'] - 1]['data']
        row['valor'] = produtos[itens[i]['produto'] - 1]['valor']
        listaPedidosFinal.append(row)

    return listaPedidosFinal

def get_info_pedidos():
    infoPedidos = []
    for i in range(len(itens)):
        row = {}
        row['código'] = itens[i]['pedido']
        # row['cliente'] = clientes[pedidos[itens[i]['pedido'] - 1]['cliente'] - 1]['nome']
        # row['data'] = pedidos[itens[i]['pedido'] - 1]['data']
        row['produto'] = produtos[itens[i]['produto'] - 1]['nome']
        row['quantidade'] = itens[i]['quantidade']
        row['valor'] = produtos[itens[i]['produto'] - 1]['valor']
        infoPedidos.append(row)

    return infoPedidos


def get_info_clientes():

    dadosCliente = []
    for i in range(len(pedidos)):
        row = {}
        row['nome'] = clientes[pedidos[i]['cliente'] - 1]['nome']
        row['cpf'] = clientes[pedidos[i]['cliente'] - 1]['cpf']
        row['data'] = pedidos[i]['data']
        row['email'] = clientes[pedidos[i]['cliente'] - 1]['email']
        dadosCliente.append(row)

    return dadosCliente

def get_items():
    return itens

def get_pedidos():
    return pedidos

def get_clientes():
    return clientes

def get_pedidos():
    return pedidos