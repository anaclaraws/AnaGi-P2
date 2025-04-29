import random
def rolar_dados(n):
    i = 0
    lista = []
    while i < n:
        lista.append(random.randint(1, 6))
        i += 1
    return lista

def guardar_dado (dados_rolados, dados_guardados, número_dado):
    dado = dados_rolados[número_dado]
        novos_dados_rolados = dados_rolados[:número_dado] + dados_rolados[número_dado+1:]
        novos_dados_no_estoque = dados_no_estoque + [dado]
        return [novos_dados_rolados, novos_dados_no_estoque]
    else:
        return [dados_rolados, dados_no_estoque]