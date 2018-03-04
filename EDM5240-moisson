#coding:utf-8

import csv
import requests
from bs4 import BeautifulSoup

fichier="ebay.csv"

for n in range(1,101):
	url="https://www.cafr.ebay.ca/sch/Telephones/38036/i.html?_pgn={}&_skc=100&rt=nc".format(n)
	#print(url)

	contenu=requests.get(url)
	page=BeautifulSoup(contenu.text,"html.parser")
	#print(page)

	urltelephones=page.find_all("li",class_="sresult lvresult clearfix li")

	#print(len(urltelephones))

	for urltelephone in urltelephones:
		try:
			telephone = []
			url2 = urltelephone.a["href"]
			print(url2)
			telephone.append(url2)

			contenu2=requests.get(url2)
			page2=BeautifulSoup(contenu2.text,"html.parser")

			titre=page2.find("h1",id="itemTitle").text
			print(titre)
			telephone.append(titre)

			prix=page2.find("span",class_="notranslate").text
			print(prix)
			telephone.append(prix)

			lieuobjet=page2.find("div",class_="iti-eu-bld-gry ").text
			#lieu où l'objet se trouve
			print(lieuobjet)
			telephone.append(lieuobjet)

			lieuexpedition=page2.find("div",class_="iti-eu-bld-gry vi-shp-pdg-rt").text
			#Les lieux où l'objet peut être expédié
			print(lieuexpedition)
			telephone.append(lieuexpedition)

			renvoi=page2.find("span",class_=" vi-no-ret-accrd-txt").text
			#Les renvois sont-ils permis ou non?
			print(renvoi)
			telephone.append(renvoi)

			#en imprimant (téléphone), nous aurons toutes les informations mises en append entre crochets.

			print(telephone)

			f=open(fichier,"a")
			gnagna=csv.writer(f)
			gnagna.writerow(telephone)

		except:
			print("Nada")



		



