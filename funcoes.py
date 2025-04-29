import random
def rolar_dados(n):
    i = 0
    lista = []
    while i < n:
        lista.append(random.randint(1, 6))
        i += 1
    return lista

def guardar_dado (dados_rolados, dados_guardados, número_dado):
    if 0 <= indice < len(dados_rolados):
        dado = dados_rolados.pop(número_dado)
        dados_no_estoque.append(dado)
    return [dados_rolados, dados_no_estoque]