# import random
from funcoes import *

cartela = {
    'regra_simples': {i: -1 for i in range(1, 7)},
    'regra_avancada': {
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'quadra': -1,
        'full_house': -1,
        'cinco_iguais': -1,
        'sem_combinacao': -1
    }
}

rodada = 0

while rodada < 12:
    dados_guardados = []
    dados_rolados = rolar_dados(5)
    rerrolagens = 0
    terminou_rodada = False

    while not terminou_rodada:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = input()

        if opcao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            try:
                indice = int(input())
                dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, indice)
            except:
                continue

        elif opcao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            try:
                indice = int(input())
                dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, indice)
            except:
                continue

        elif opcao == '3':
            if rerrolagens < 2:
                dados_rolados = rolar_dados(len(dados_rolados))
                rerrolagens += 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif opcao == '4':
            imprime_cartela(cartela)

        elif opcao == '0':
            print("Digite a combinação desejada:")
            categoria = input()

            if categoria in ['1', '2', '3', '4', '5', '6']:
                if cartela['regra_simples'][int(categoria)] != -1:
                    print("Essa combinação já foi utilizada.")
                else:
                    dados_totais = dados_rolados + dados_guardados
                    cartela = faz_jogada(dados_totais, categoria, cartela)
                    terminou_rodada = True

            elif categoria in cartela['regra_avancada']:
                if cartela['regra_avancada'][categoria] != -1:
                    print("Essa combinação já foi utilizada.")
                else:
                    dados_totais = dados_rolados + dados_guardados
                    cartela = faz_jogada(dados_totais, categoria, cartela)
                    terminou_rodada = True

            else:
                print("Combinação inválida. Tente novamente.")

        else:
            print("Opção inválida. Tente novamente.")

    rodada += 1

# Cálculo de pontuação final
pontos_simples = 0
for valor in cartela['regra_simples'].values():
    if valor != -1:
        pontos_simples += valor

pontos_avancada = 0
for valor in cartela['regra_avancada'].values():
    if valor != -1:
        pontos_avancada += valor

# Impressão final
imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao_total}")
