import pandas as pd
from tableone import TableOne

dados = pd.read_csv('Dados/Metadados.csv', sep=',', decimal='.')
dados['Data'] = dados['Data'].apply(lambda data: int(data[6:]))

colunas = ['FC', 'Pi', 'PRi', 'QRSi', 'QTi', 'QTc', 'RRi', 'SAP', 'SAQRS', 'SAT', 'Idade', 'Data']

for col in ['Pi', 'PRi', 'QRSi', 'QTi', 'QTc', 'RRi']:
    dados[col] *= 1000
rename = {'Idade': 'Age', 'Sexo': 'Gender', 'Data': 'Date'}
categorical = ['Data']
ordem = {}
groupby = ['Sexo']
tabela = TableOne(dados, categorical=categorical, columns=colunas, rename=rename, groupby=groupby)
tabela.to_latex('teste.tex')


