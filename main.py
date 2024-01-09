import time
import pyautogui as pag
import pandas as pd

# DEFINICOES/VARIAVEIS
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login".lower()
dados = r"produtos.csv".lower()
email = "teste@exemplo.com"
senha = "teste123"
pag.PAUSE = 0.1

# PASSO A PASSO
# Passo 1 - Abrir o programa
pag.press("win")
pag.write("edge")
pag.press("enter")
time.sleep(1)
pag.write(site)
pag.press("enter")

# Passo 2 - Fazer o login
time.sleep(1)
pag.click(x=720, y=460)
pag.write(email)
pag.press("tab")
pag.write(senha)
pag.press("enter")

# Passo 3 - Importar base de dados
tabela = pd.read_csv(dados)

# Passo 4 - Cadastrar produtos
time.sleep(1)
for linha in tabela.index:
    # codigo
    pag.click(x=639, y=299)
    pag.write(str(tabela.loc[linha, "codigo"]).upper())
    pag.press("tab")
    # marca
    pag.write(str(tabela.loc[linha, "marca"]))
    pag.press("tab")
    # tipo
    pag.write(str(tabela.loc[linha, "tipo"]))
    pag.press("tab")
    # categoria
    pag.write(str(tabela.loc[linha, "categoria"]))
    pag.press("tab")
    # preco_unitario
    pag.write(str(tabela.loc[linha, "preco_unitario"]))
    pag.press("tab")
    # custo
    pag.write(str(tabela.loc[linha, "custo"]))
    pag.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pag.write(str())
    pag.press("tab")
    # confirmar cadastro
    pag.press("enter")
    pag.scroll(5000)
