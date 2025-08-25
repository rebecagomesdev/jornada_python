# --- 1. PREPARAÇÃO ---
# Lista vazia para guardar os IDs que vou filtrar.
ids_selecionados = [] 
# Contador para os positivos, começa em 0.
contador_positivos = 0

# Abre o arquivo CSV para leitura ('r'). O 'with' fecha o arquivo sozinho.
with open('pacientes.csv', 'r', encoding='utf-8') as arquivo_csv:
    # Pula a primeira linha, que é o cabeçalho.
    next(arquivo_csv)
    
    # --- 2. PROCESSAMENTO ---
    # Passa por cada linha do arquivo, da segunda em diante.
    for linha in arquivo_csv:
        # Limpa espaços e quebra a linha pela vírgula, gerando uma lista.
        # Ex: ['PAC001', '45', 'Positivo']
        dados_paciente = linha.strip().split(',')
        
        # Lógica do contador (índice 2 = Marcador).
        marcador = dados_paciente[2]
        if marcador == "Positivo":
            contador_positivos = contador_positivos + 1

        # Lógica do filtro de idade (índice 1 = Idade).
        # Converte a idade de texto para número para poder comparar.
        idade_numero = int(dados_paciente[1])
        if idade_numero > 40:
            # Pega o ID (índice 0).
            id_paciente = dados_paciente[0]
            # Adiciona o ID na minha lista de selecionados.
            ids_selecionados.append(id_paciente) 
        
# --- 3. RESULTADO ---
# Mostra os resultados acumulados no terminal.
print(f"Total de pacientes positivos: {contador_positivos}")
print(f"IDs de pacientes com mais de 40 anos: {ids_selecionados}")

# Mensagem de status para o usuário.
print("\nIniciando a escrita do arquivo de resultados...")

# Abre/cria um arquivo para escrita ('w'). CUIDADO: apaga o conteúdo anterior se já existir.
with open('pacientes_selecionados.txt', 'w', encoding='utf-8') as arquivo_saida:
    # Passa por cada ID que foi coletado na lista 'ids_selecionados'.
    for id_paciente in ids_selecionados:
        # Escreve o ID + uma quebra de linha ('\n') no arquivo.
        arquivo_saida.write(f"{id_paciente}\n")

# Mensagem final de confirmação.
print("Arquivo 'pacientes_selecionados.txt' criado com sucesso!")