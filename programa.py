import funcoes as f
cartela = {
    'regra_simples': {i: -1 for i in range(1, 7)},
    'regra_avancada': {
        k: -1 for k in [
            'sem_combinacao', 'quadra', 'full_house',
            'sequencia_baixa', 'sequencia_alta', 'cinco_iguais'
        ]
    }
}

f.imprime_cartela(cartela)

rodadas = 0

while (-1 in cartela['regra_simples'].values() or -1 in cartela['regra_avancada'].values()) and rodadas < 12:
    dados_rolados = f.rolar_dados(5)
    dados_guardados = []
    reroladas = 0
    rodada_em_andamento = True
    rodadas += 1
    invalido = False

    while rodada_em_andamento:
        if not invalido:
            print(f"\nDados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")
            print("Digite:")
            print("  1 para guardar um dado")
            print("  2 para remover um dado")
            print("  3 para rerrolar")
            print("  4 para ver a cartela")
            print("  0 para marcar a pontuação")

        opcao = input("Opção: ").strip()
        invalido = False

        if opcao == '1':
            try:
                indice = int(input("Digite o índice do dado a ser guardado (0 a 4): "))
                dados_rolados, dados_guardados = f.guardar_dado(dados_rolados, dados_guardados, indice)
            except (ValueError, IndexError):
                print("Índice inválido.")
                invalido = True

        elif opcao == '2':
            try:
                indice = int(input("Digite o índice do dado a ser removido (0 a 4): "))
                dados_rolados, dados_guardados = f.remover_dado(dados_rolados, dados_guardados, indice)
            except (ValueError, IndexError):
                print("Índice inválido.")
                invalido = True

        elif opcao == '3':
            if reroladas < 2:
                dados_rolados = f.rolar_dados(len(dados_rolados))
                reroladas += 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif opcao == '4':
            f.imprime_cartela(cartela)

        elif opcao == '0':
            print("Digite a combinação desejada:")
            while True:
                resposta = input().strip()
                resposta_int = None
                if resposta.isdigit():
                    resposta_int = int(resposta)

                if resposta_int in cartela['regra_simples']:
                    if cartela['regra_simples'][resposta_int] == -1:
                        f.faz_jogada(dados_rolados + dados_guardados, resposta, cartela)
                        break
                    else:
                        print("Essa combinação já foi utilizada.")
                elif resposta in cartela['regra_avancada']:
                    if cartela['regra_avancada'][resposta] == -1:
                        f.faz_jogada(dados_rolados + dados_guardados, resposta, cartela)
                        break
                    else:
                        print("Essa combinação já foi utilizada.")
                else:
                    print("Combinação inválida. Tente novamente.")

            rodada_em_andamento = False

        else:
            print("Opção inválida. Tente novamente.")
            invalido = True

total_simples = sum(v for v in cartela['regra_simples'].values() if v != -1)
total_avancada = sum(v for v in cartela['regra_avancada'].values() if v != -1)
bonus = 35 if total_simples >= 63 else 0
total = total_simples + total_avancada + bonus

f.imprime_cartela(cartela)
print(f"\nPontuação total: {total}")
