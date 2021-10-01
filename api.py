import requests
import pandas

#==========Clientes

urlClientes = 'https://sistemalift1.com/lift_ps/api/Clientes'
clientes = requests.get(urlClientes).json()

listaNomeClientes = [cliente['nome'] for cliente in clientes]

for i in range(len(listaNomeClientes)):
    ide = i + 1
    print(ide, listaNomeClientes[ide - 1])



#=========Produtos

urlProdutos = 'https://sistemalift1.com/lift_ps/api/Produtos'
produtos = requests.get(urlProdutos).json()
# idProduto =





#=======Items Pedido

urlItensPedido = 'https://sistemalift1.com/lift_ps/api/ItensPedido'
itensPedido = requests.get(urlItensPedido).json()



#======Pedido

urlPedido = 'https://sistemalift1.com/lift_ps/api/Pedido'
pedido = requests.get(urlPedido).json()


# for cliente in clientes:
#     for key, value in cliente.items():
#         print(key, value, end=" ")
#     print()

# print (getattr(clientes,'name')) 


#            0                        1                     2                   3                           4                             5                             6                       7
# ['Vitória Luzia da Rocha', 'Yuri Arthur Sales', 'Sérgio Theo Galvão', 'Cláudia Emilly Monteiro', 'Bernardo Kaique Souza', 'Elaine Helena Jennifer da Rosa', 'Malu Tereza Duarte', 'Isadora Giovanna Assis']

"""
PEDIDO  CLIENTE    DATA   VALOR
1       ariel     05/06   200.00
2       
"""