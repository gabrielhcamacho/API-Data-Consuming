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
print(listaClientes)

listaPedidos = [pedido['cliente'] for pedido in pedidos]
print(listaPedidos)

listaData = [pedido['data'] for pedido in pedidos]
print(listaData)

tabela = {'codigo': '1', 'nome': "Sérgio Theo Galvão", "data": "29-01-2000"}