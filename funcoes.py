import random
def rolar_dados(n):
    i = 0
    lista = []
    while i < n:
        lista.append(random.randint(1, 6))
        i += 1
    return lista

def guardar_dado(dados_rolados, dados_guardados, numero_dado):
    if 0 <= numero_dado < len(dados_rolados):
        dado = dados_rolados[numero_dado]
        novos_dados_rolados = dados_rolados[:numero_dado] + dados_rolados[numero_dado+1:]
        novos_dados_guardados = dados_guardados + [dado]
        return [novos_dados_rolados, novos_dados_guardados]
    else:
        return [dados_rolados, dados_guardados]
    
def remover_dado(dados_rolados, dados_guardados, dado_para_remover):