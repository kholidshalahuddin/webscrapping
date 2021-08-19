from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
page_source = driver.get(
    'https://www.detik.com/search/searchall?query=Kemerdekaan&siteid=2')
soup = BeautifulSoup(driver.page_source, 'html.parser')
tanggals = []
kategoris = []
juduls = []
gambar = []
links = []

search_results = soup.select('article a')

for link in search_results:
    cari = link.find('span', class_='date')
    if cari == None:
        print("x")
    else:
        jdl = link.find('h2')
        juduls.append(jdl.text)

        kategori = link.find('span', class_='category')
        kategoris.append(kategori.text)

        dateku = link.find('span', class_='date')
        tgl = dateku.contents[1]
        cek = tgl.name
        if cek == None:
            tanggals.append(dateku.contents[1])
        else:
            tanggals.append(dateku.contents[0])

        gbr = link.find('img')
        p = gbr.get('src')
        gambar.append(p)

        tautan = link.get('href')
        links.append(tautan)


df = pd.DataFrame({'Kategori Berita ': kategoris, 'Judul Berita': juduls,
                  'Gambar': gambar, 'Link': links, 'Tanggal Berita ': tanggals})
df.to_excel('berita.xls', index=False, encoding='utf-8')
