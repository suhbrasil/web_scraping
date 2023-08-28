from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
from time import sleep
from selenium import webdriver


url = 'https://portal.gupy.io/job-search/term=desenvolvedor'

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

# Salva o conteúdo da página após rolagem
site_content = driver.page_source
driver.quit()

# Pega o conteúdo do site e coloca na variável soup
soup = BeautifulSoup(site_content, 'html.parser')

# Lista que irá guardar as informações que foram selecionadas da vaga
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

    # Faz um loop em cada vaga e coleta as informações especificadas
    for vaga in vagas:
        cargo = vaga.find('h2', class_=re.compile('XNNQK')).get_text().strip()
        empresa = vaga.find('p', class_=re.compile('cQyvth')).get_text().strip()
        local = vaga.find('span', class_=re.compile('cezNaf')).get_text().strip()


        # Adiciona as informações encontradas à lista criada
        lista_vagas['cargo'].append(cargo)
        lista_vagas['empresa'].append(empresa)
        lista_vagas['local'].append(local)

# Salva a lista com as informações da vaga no arquivo csv
dataframe = pd.DataFrame(lista_vagas)
dataframe.to_csv('/Users/suzanabrasil/Downloads/gupyvagas.csv', encoding='utf-8', sep=';')
