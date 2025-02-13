def criar_arquivo():
    """Cria um arquivo e escreve o texto do usuário nele."""
    nome_arquivo = input("Digite o nome do arquivo (com .txt): ")

    # Solicita o conteúdo do arquivo
    conteudo = input("Digite o texto para salvar no arquivo: ")

    # Cria e escreve no arquivo
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)

    print(f"\nArquivo '{nome_arquivo}' criado com sucesso!")

def ler_arquivo():
    """Lê e exibe o conteúdo de um arquivo."""
    nome_arquivo = input("\nDigite o nome do arquivo para ler: ")

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            print("\nConteúdo do arquivo:")
            print(conteudo)
    except FileNotFoundError:
        print("\nErro: O arquivo não foi encontrado.")

# Executando o exercício
criar_arquivo()
ler_arquivo()
