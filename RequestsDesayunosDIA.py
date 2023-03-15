from bs4 import BeautifulSoup
import requests
import pandas as pd
import json

url = 'https://diaonline.supermercadosdia.com.ar/desayuno'
session = requests.Session()
session.verify=False
session.proxies={'http':'http://127.0.0.1:8888/', 'https':'http://127.0.0.1:8888/'}
page = session.get(url)
indiceInicial = page.text.find('<script type="application/ld+json">{')
indiceFinal = page.text.find('}}}]}</script>')
jsonLimpio = page.text[indiceInicial+35:indiceFinal]+'}}}]}'
jsonLimpio = json.loads(jsonLimpio)
lista = jsonLimpio['itemListElement']


f = open("bbdd.txt", "a")
f.write("----------------------------------------------------------------------------------------------------------------\n")
for Product in lista:
    nombreProducto = 'Nombre del producto: ' + Product['item']['name']
    linkProducto = 'Link del producto: ' + Product['item']['@id']
    skuProducto = 'SKU del producto: ' + Product['item']['sku']
    precioProducto = 'Precio del producto: ' + str(Product['item']['offers']['lowPrice'])
    datoCompleto = nombreProducto + '\n' + linkProducto + '\n' + skuProducto + '\n' + precioProducto + '\n\n'
    f.write(datoCompleto)
f.write("----------------------------------------------------------------------------------------------------------------\n")
f.close()