import pandas as pd
import requests


def fetch_sidra_data():
    # URL para buscar todas as variáveis e períodos de 2007-2020
    url = "https://apisidra.ibge.gov.br/values/t/1757/v/all/p/2007-2020/n1/all/n3/all"
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Converte os dados para JSON
        data = response.json()

        # Converte os dados JSON em DataFrame
        df = pd.DataFrame(data)
        return df
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")


# Chama a função para buscar os dados
try:
    data = fetch_sidra_data()
    print("Dados carregados com sucesso!")

    # Salvar como CSV
    data.to_csv("dados_sidra_empresas.csv", index=False, encoding="utf-8")
    print("Arquivo CSV salvo como 'dados_sidra_empresas.csv'.")

except Exception as e:
    print(f"Erro ao buscar ou salvar os dados: {e}")
