from bs4 import BeautifulSoup
import requests
site = requests.get("http://maximanet.net.br/").content
soup = BeautifulSoup(site, 'html.parser')
print(soup.prettify()) #PRINTA CODIGO FONTE DA PAGINA
#print(soup.title) #PRINTA O TITULO DA PAGINA
#print(soup.usuario) #PRINTA USUARIO CASO HAJA
#print(soup.social)