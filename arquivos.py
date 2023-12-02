import pandas as pd
import os

# Diretório contendo as planilhas
diretorio = 'user/Dowloads/rafa1/rafa2/'

# Obter lista de arquivos no diretório
arquivos = os.listdir(diretorio)

# Criar um DataFrame vazio para armazenar os dados
dados_combinados = pd.DataFrame()

# Iterar sobre cada arquivo no diretório
for arquivo in arquivos:
    if arquivo.endswith('.xlsx') or arquivo.endswith('.xls'):
        # Ler a planilha e adicionar ao DataFrame
        caminho_arquivo = os.path.join(diretorio, arquivo)
        planilha = pd.read_excel(caminho_arquivo)
        dados_combinados = dados_combinados.append(planilha, ignore_index=True)

# Salvar o DataFrame combinado em um novo arquivo
caminho_saida = 'user/Dowloads/rafa1/rafa2/saida.xlsx'
dados_combinados.to_excel(caminho_saida, index=False)

print('Planilhas combinadas com sucesso! O arquivo de saída foi salvo em', caminho_saida)
