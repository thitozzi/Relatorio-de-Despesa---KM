import getpass
import re
from funções_km import abrir_portal, despesa_ida, despesa_volta

user = input('Digite seu e-mail: ')
while '@algartech.com' not in user:
    user = input('E-mail errado! Digite seu e-mail novamente: ')
password = getpass.getpass('Digite sua senha: ') #ocultar senha

formato_data = re.compile('^\d{2}/\d{2}/\d{4}$')
data = str(input('Digite a data [DD/MM/AAAA]: '))
while not formato_data.match(data):
    data = str(input('Data errada! Digite a data novamente [DD/MM/AAAA]: '))

abrir_portal(user, password)
despesa_ida(data)
despesa_volta(data)
