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
    if len(lista_números) < 4:
        return 0
    numeros_unicos = []
    for numeros in lista_números:
        if numeros not in numeros_unicos:
            numeros_unicos.append(numeros)
    for i in range(len(numeros_unicos)):
        sequencia_encontrada = True
        for j in range(1, 4):
            if numeros_unicos[i] + j not in numeros_unicos:
                sequencia_encontrada = False
                break
        if sequencia_encontrada:
            return 15
    return 0


def calcula_pontos_sequencia_alta(lista):
    if len(lista) < 5:
        return 0
    numeros_unicos = []
    for numero in lista:
        if numero not in numeros_unicos:
            numeros_unicos.append(numero)
    for i in range(len(numeros_unicos)):
        sequencia_encontrada = True
        for j in range(1, 5):
            if numeros_unicos[i] + j not in numeros_unicos:
                sequencia_encontrada = False
                break
        if sequencia_encontrada:
            return 30
    return 0

def calcula_pontos_full_house(lista_faces):
    if len(lista_faces) < 5:
        return 0
    numeros_unicos = []
    quantidades = []
    for numero in lista_faces:
        if numero not in numeros_unicos:
            numeros_unicos.append(numero)
            quantidade = 0
            for n in lista_faces:
                if n == numero:
                    quantidade += 1
            quantidades.append(quantidade)
    if (2 in quantidades) and (3 in quantidades) and (len(numeros_unicos) == 2):
        soma = 0
        for i in lista_faces:
            soma += i
        return soma
    return 0

def calcula_pontos_quadra(lista_faces):
    contagem={}
    for número in lista_faces:
        if número in contagem:
            contagem[número] +=1
        else:
            contagem[número]= 1
    for número in contagem:
        if contagem[número] >= 4:
            soma=0
            for valor in lista_faces:
                soma+=valor
            return soma
    return 0

def calcula_pontos_quina(lista_faces):
    contagem={}
    for número in lista_faces:
        if número in contagem:
            contagem[número] +=1
        else:
            contagem[número]= 1
    for número in contagem:
        if contagem[número] >=5:
            return 50
    return 0

def calcula_pontos_regra_avancada (lista_faces):
    return {
        'cinco_iguais': calcula_pontos_quina(lista_faces),
        'full_house': calcula_pontos_full_house(lista_faces),
        'quadra': calcula_pontos_quadra(lista_faces),
        'sem_combinacao': calcula_pontos_soma(lista_faces),
        'sequencia_alta': calcula_pontos_sequencia_alta(lista_faces),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(lista_faces)
    }

def faz_jogada(dados, categoria, cartela):
    if categoria in ['1', '2', '3', '4', '5', '6']: 
        categoria = int(categoria)
        pontos = calcula_pontos_regra_simples(dados)[categoria]
        cartela['regra_simples'][categoria] = pontos 
    elif categoria in cartela['regra_avancada']:
        pontos = calcula_pontos_regra_avancada(dados)[categoria]
        cartela['regra_avancada'][categoria] = pontos 
    return cartela
