from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
from time import sleep

def abrir_portal(user, password):
    global lancamento_km
    lancamento_km = webdriver.Chrome(executable_path=r'C:\Users\brtozzit\VSProjects\Python\Tetra Pak - Algar Tech.py\chromedriver.exe')      
    lancamento_km.get('https://portal.expensemobi.com.br/#/login')
    lancamento_km.maximize_window()
    sleep(4)
    lancamento_km.find_element(By.XPATH, '//*[@id="email"]').send_keys(user) #colocar o nome do usuário
    lancamento_km.find_element(By.XPATH, '//*[@id="senha"]').send_keys(password) #colocar a senha do usuário
    lancamento_km.find_element(By.XPATH, '//*[@id="content"]/div/div/form/div[1]/div/div[8]/input').click() #entrar
    sleep(5)
    lancamento_km.find_element(By.XPATH, '//*[@id="left"]/md-list/nav/div/ul/li[2]/a[5]').click() #Meus Relatórios
    sleep(5)

def despesa_ida(data):
    #Criar despesa
    pyautogui.click(x=1839, y=697) #mais
    pyautogui.click(x=1750, y=771) #Nova Despesa KM
    sleep(7)

    #Colocar Data
    pyautogui.press(['tab', 'tab', 'tab', 'tab', 'tab'])
    sleep(3)
    pyautogui.write(data)
    
    #Saída
    pyautogui.click(x=1377, y=428) 
    pyautogui.write('Rua Abilio Ferreira Quental')
    sleep(2)
    pyautogui.press('tab')

    #Chegada
    pyautogui.click(x=1318, y=511)
    pyautogui.write('Tetra Pak Monte Mor')
    sleep(2)
    pyautogui.press('tab')
    sleep(4)

    #Selecionando cliente Tetra Pak - Monte Mor
    pyautogui.click(x=701, y=682)
    sleep(1.5) 
    pyautogui.click(x=586, y=794) 
    sleep(2)

    #Selecionando Tipo de Despesa
    pyautogui.click(x=600, y=857)
    sleep(1.5)
    pyautogui.click(x=600, y=936)
    sleep(2)

    #Observação
    lancamento_km.find_element(By.XPATH, '//*[@id="content"]/md-content/div/div[2]/div/div[1]/div/form/div[12]/div/textarea').send_keys(str('Km rodado ao cliente Tetra Pak. Despesa 100% reembolsado pelo cliente.'))

    #Salvar
    lancamento_km.find_element(By.XPATH, '//*[@id="content"]/md-content/div/div[2]/div/div[1]/div/form/div[13]/div/button').click()

    sleep(5)

def despesa_volta(data):
    #Nova Despesa KM
    pyautogui.click(x=1837, y=690)
    pyautogui.click(x=1750, y=771) 

    #Colocar Data
    sleep(7)
    pyautogui.press(['tab', 'tab', 'tab', 'tab', 'tab'])
    sleep(3)
    pyautogui.write(data)

    #Saída
    pyautogui.click(x=1377, y=428) 
    pyautogui.write('Tetra Pak Monte Mor')
    sleep(2)
    pyautogui.press('tab')

    #Chegada
    sleep(1)
    pyautogui.click(x=1318, y=511)
    pyautogui.write('Rua Abilio Ferreira Quental')
    sleep(2)
    pyautogui.press('tab')
    sleep(4)

    #Selecionando cliente Tetra Pak - Monte Mor
    pyautogui.click(x=701, y=682)
    sleep(1.5) 
    pyautogui.click(x=586, y=794) 
    sleep(2)

    #Selecionando Tipo de Despesa
    pyautogui.click(x=600, y=857)
    sleep(1.5)
    pyautogui.click(x=600, y=936)
    sleep(2)

    #Observação
    lancamento_km.find_element(By.XPATH, '//*[@id="content"]/md-content/div/div[2]/div/div[1]/div/form/div[12]/div/textarea').send_keys(str('Km rodado ao cliente Tetra Pak. Despesa 100% reembolsado pelo cliente.'))

    #Salvar
    lancamento_km.find_element(By.XPATH, '//*[@id="content"]/md-content/div/div[2]/div/div[1]/div/form/div[13]/div/button').click()

    sleep(15)
