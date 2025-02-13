import pandas as pd
import matplotlib.pyplot as plt

def analisar_vendas(arquivo_csv):
    """Lê um arquivo CSV, exibe estatísticas e gera um gráfico de vendas por mês."""
    try:
        # Lê o arquivo CSV
        df = pd.read_csv(arquivo_csv, parse_dates=['Data'])

        # Verifica se as colunas esperadas estão presentes
        if 'Data' not in df.columns or 'Vendas' not in df.columns:
            print("Erro: O arquivo CSV deve conter as colunas 'Data' e 'Vendas'.")
            return

        # Extrai o mês e ano da coluna de datas
        df['Ano-Mês'] = df['Data'].dt.to_period('M')

        # Agrupa por mês e soma as vendas
        vendas_mensais = df.groupby('Ano-Mês')['Vendas'].sum()

        # Exibe estatísticas básicas
        print("\nEstatísticas de Vendas:")
        print(df.describe())

        # Gera o gráfico
        plt.figure(figsize=(10, 5))
        vendas_mensais.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title("Vendas por Mês")
        plt.xlabel("Mês")
        plt.ylabel("Total de Vendas")
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

    except FileNotFoundError:
        print("Erro: Arquivo não encontrado!")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Solicita o nome do arquivo CSV ao usuário
arquivo = input("Digite o nome do arquivo CSV: ")
analisar_vendas(arquivo)
