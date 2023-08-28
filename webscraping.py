import requests
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import math
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

url = 'https://portal.gupy.io/job-search/term=desenvolvedor'

# Mostrar para a requisição que o acesso é confiável
headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

# Inicializar o navegador Chrome usando o Selenium
driver = webdriver.Chrome()
driver.get(url)

# Rolagem da página para exibir toda a lista
while True:
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.END)
    sleep(0.5)
    if driver.execute_script("return window.scrollY + window.innerHeight >= document.documentElement.scrollHeight"):
        break

# Salvar o conteúdo da página após rolagem
site_content = driver.page_source
driver.quit()

# Pega o conteúdo do site e coloca na variável soup
soup = BeautifulSoup(site_content, 'html.parser')

# Lista que irá guardar as informações que selecionei da vaga
lista_vagas = {'cargo':[],'empresa':[],'local':[]}

# Nomes de vagas para ampliar a busca
nome_vagas = ['desenvolvedor', 'estágio', 'engenharia']

for nome_vaga in nome_vagas:
    url_pag = f'https://portal.gupy.io/job-search/term={nome_vaga}'
    driver = webdriver.Chrome()
    driver.get(url_pag)

    while True:
        body = driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.END)
        sleep(0.5)
        if driver.execute_script("return window.scrollY + window.innerHeight >= document.documentElement.scrollHeight"):
            break

    site_content = driver.page_source
    driver.quit()

    soup = BeautifulSoup(site_content, 'html.parser')

    # Procura a div que está com as descrições da vaga
    vagas = soup.find_all('div', class_=re.compile('HCzvP'))

    # Loop em cada vaga e coleta as informações especificadas
    for vaga in vagas:
        cargo = vaga.find('h2', class_=re.compile('XNNQK')).get_text().strip()
        empresa = vaga.find('p', class_=re.compile('cQyvth')).get_text().strip()
        local = vaga.find('span', class_=re.compile('cezNaf')).get_text().strip()


        # Adiciona as informações encontrados à lista criada
        lista_vagas['cargo'].append(cargo)
        lista_vagas['empresa'].append(empresa)
        lista_vagas['local'].append(local)

dataframe = pd.DataFrame(lista_vagas)
dataframe.to_csv('/Users/suzanabrasil/Downloads/gupyvagas.csv', encoding='utf-8', sep=';')
