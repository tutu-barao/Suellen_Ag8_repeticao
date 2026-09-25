#ESTRUTURA DE REPETIÇÃO
# Suellen Campos

# 1. contadores (começam em zero - uma caixa vazia para contar cada pessoa e nao esquecer as outras 49)
qtd_excelente = 0
qtd_ruim = 0

# 2. O loop FOR para repetir 50 vezes
for i in range(1, 51):
    print(f"\n--- Entrevistado {i} de 50 ---")
    
    # Dados de Entrada
    nome_cliente = input("Digite seu nome: ")
    
    idade_cliente = int(input("Digite sua idade: ")) 
    
    # Validação da opinião (garante que a pessoa digite 1, 2 ou 3)
    while True:
        try:
            # Mudamos o texto para pedir números
            opiniao = int(input("Digite sua opinião (1-EXCELENTE, 2-BOM, 3-RUIM): "))
            
            # Se digitou 1, 2 ou 3, sai do while e continua o código
            if opiniao in [1, 2, 3]:
                break 
            else:
                print("Opção inválida! Digite apenas 1, 2 ou 3.")
        except ValueError:
            print("️ Erro! Digite apenas números.")

    # 3. Processamento (Estrutura de Decisão para contar)
    if opiniao == 1:
        qtd_excelente += 1  # Soma 1 no contador de excelente
    elif opiniao == 3:
        qtd_ruim += 1       # Soma 1 no contador de ruim
        
    #  2 (BOM) NAO ENTROU

# 4. Saída (Mostra o resultado final depois que o loop de 50 acabar)
print("\n" + "=" * 40)
print("RELATÓRIO FINAL DA PESQUISA")
print("=" * 40)
print(f"Quantidade de respostas EXCELENTE: {qtd_excelente}")
print(f"Quantidade de respostas RUIM:      {qtd_ruim}")
print("=" * 40)
