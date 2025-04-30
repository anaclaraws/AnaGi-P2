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
        novos_dados_rolados = []
        for i, valor in enumerate(dados_rolados):
            if i != numero_dado:
                novos_dados_rolados.append(valor)                
        novos_dados_guardados = dados_guardados + [dado]
        return [novos_dados_rolados, novos_dados_guardados]
    else:
        return [dados_rolados, dados_guardados]

def remover_dado(dados_rolados, dados_guardados, numero_removido):
    if 0 <= numero_removido < len(dados_guardados):
        dados_rolados.append(dados_guardados[numero_removido])
        lista_guardados = []
        for i in range(len(dados_guardados)):
            if i != numero_removido:
                lista_guardados.append(dados_guardados[i])
        dados_guardados = lista_guardados
    return [dados_rolados, dados_guardados]

def calcula_pontos_regra_simples (números):
    dicio_somas = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for número in números:
        if número in dicio_somas:
            dicio_somas[número] += número
    return dicio_somas

def calcula_pontos_soma (lista_números):
    soma=0
    for números in lista_números:
        soma+=números
    return soma

def calcula_pontos_sequencia_baixa(lista_números):
    for i in range(1, len(lista_números)):
        if lista_números[i] != lista_números[i - 1] + 1:
            return 0
    return 15