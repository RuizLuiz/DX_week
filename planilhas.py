import numpy as np
import pandas as pd
from openpyxl import load_workbook

def mostrar_planilha_completa():
    pd.set_option('display.max_rows', None)

def mostrar_planilha_resumida():
    pd.reset_option('^display.', silent=True)

def visualizar_inicio():
    print(df.head())

def visualizar_fim():
    print(df.tail())

def info_index():
    print(df.index)

def info_colunas():
    print(df.columns)

def ordenar_pela_coluna_x(coluna):
    print(df.sort_values(by=coluna))
    return df.sort_values(by=coluna)

def selecionar_coluna_x(coluna):
    print(df[coluna])
    return df[coluna]

def selecionar_linhas_de_x_y(x,y):
    print(df[x:y])
    return df[x:y]

def selecionar_objeto(x):
    print(df.loc[x])

def selecionar_multiplas_colunas(vetor):
    print(df.loc[:, vetor])
    return(df.loc[:, vetor])

def selecionar_linhas_colunas(x_linha, y_linha, x_coluna, y_coluna):
    print(df.iloc[x_linha:y_linha, x_coluna:y_coluna])
    return(df.iloc[x_linha:y_linha, x_coluna:y_coluna])

def selecionar_por_valor(coluna, valor):
    print(df[df[coluna] == valor])
    return(df[df[coluna] == valor])

def selecionar_mais_de_um_valor(coluna, vetor):
    print(df[df[coluna].isin(vetor)])
    return(df[df[coluna].isin(vetor)])

def selecionar_maior_que(coluna, quantidade):
    print(df[df[coluna] > quantidade])
    return(df[df[coluna] > quantidade])

def adicionar_coluna(coluna_nova, conteudo):
    df.loc[:, coluna_nova] = np.array([conteudo] * len(df))
    print(df)
    return(df)

def retirar_nulos():
    print(df.dropna(how="any"))
    return(df.dropna(how="any"))

def preencher_nulos(valor):
    print(df.fillna(value=valor))
    return(df.fillna(value=valor))

def retirar_duplicados(coluna):
    print(df.drop_duplicates(coluna))
    return(df.drop_duplicates(coluna))

def quebrando_em_pedacos():
    pedacos = [df[:1000], df[1000:2000], df[2000:]]
    print(pedacos)
    return(pedacos) 

def juntando_pedacos(pedacos):
    print(pd.concat(pedacos))
    return(pd.concat(pedacos)) 

def juntando_coluna_chave_nao_repetida():
    #criando um dataFrame para juntar ao dataframe principal
    direita = pd.DataFrame({"ScreenName": df["ScreenName"], "NovaColunaDireita": np.array(["Novos Elementos"] * (len(df)))})
    #comando para juntar
    print(pd.merge(df, direita, on="ScreenName"))
    return(pd.merge(df, direita, on="ScreenName"))

def juntando_coluna_chave_repetida():
    #criando um dataFrame para juntar ao dataframe principal
    esquerda = pd.DataFrame({"Sentiment": df["Sentiment"], "NovaColunaEsquerda": np.array(["Novos Elementos"] * (len(df)))})
    #comando para juntar
    print(pd.merge(esquerda, df, on="Sentiment"))
    return(pd.merge(esquerda, df, on="Sentiment"))

def filtrando_por_sub_string(coluna, conteudo):
    condicao = df[coluna].str.contains(conteudo, case = False)
    print(df.where((condicao)).dropna(subset=coluna))
    return(df.where((condicao)).dropna(subset=coluna))

def filtrando_por_mais_de_uma_sub_string(coluna, conteudo1, conteudo2):
    condicao1 = df[coluna].str.contains(conteudo1, case = False)
    condicao2 = df[coluna].str.contains(conteudo2, case = False)

    print(df.where((condicao1)|(condicao2)).dropna(subset=coluna))
    return(df.where((condicao1)|(condicao2)).dropna(subset=coluna))

def filtrando_por_elemento_especifico(coluna, conteudo1, conteudo2):
    condicao1 = df[coluna].str.contains(conteudo1, case = False)
    condicao2 = df[coluna] == conteudo2

    print(df.where((condicao1)|(condicao2)).dropna(subset=coluna))
    return(df.where((condicao1)|(condicao2)).dropna(subset=coluna))
    

df = pd.read_excel("C:\\Users\\Luiz Ruiz\\Documents\\python_planilhas\\planilha_excel\\dataset_covid.xlsx",'Sheet1', header=0)


#mostrar_planilha_completa()
#mostrar_planilha_resumida()
#print(df)
#visualizar_inicio()
#visualizar_fim()
#info_index()
#info_colunas()
#df = ordenar_pela_coluna_x("Sentiment")
#df = selecionar_coluna_x("Sentiment")
#df = selecionar_linhas_de_x_y(2000,2100)
#selecionar_objeto(0)
#df = selecionar_multiplas_colunas(["Location", "Sentiment"])
#df = selecionar_linhas_colunas(3,5,0,2)
df = selecionar_por_valor("Sentiment", 'Positive')
#df = selecionar_mais_de_um_valor("Sentiment",["Positive", "Negative"])
#df = selecionar_maior_que("UserName", 2000)
#df = adicionar_coluna("Resultado","Reprovado")
#df = retirar_nulos()
#df = preencher_nulos("valor ausente")
#df = retirar_duplicados("Sentiment")
#pedacos = quebrando_em_pedacos()
#df = juntando_pedacos(pedacos)
#df = juntando_coluna_chave_nao_repetida()
#df = juntando_coluna_chave_repetida()
#df = filtrando_por_sub_string('Sentiment', "Neutral")
#df = filtrando_por_mais_de_uma_sub_string('Sentiment', "Neutral", "Positive")
#df = filtrando_por_elemento_especifico('Sentiment', "Neutral", "Positive")


df.to_excel("NeutralPositive.xlsx", sheet_name="Sheet1", index=False)
