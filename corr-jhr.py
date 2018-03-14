#coding:utf-8

### BONJOUR, ICI Jean-Hugues ###
### Comme toujours, mes notes et corrections sont précédées de trois dièses ###

### Difficile de comprendre ce que fait ton script avec aussi peu de commentaires...
### Mais je comprends que tu t'intéresses aux appareils téléphoniques vintage...

import csv
import requests
from bs4 import BeautifulSoup

fichier="ebay.csv"

for n in range(1,101):
	url="https://www.cafr.ebay.ca/sch/Telephones/38036/i.html?_pgn={}&_skc=100&rt=nc".format(n)
### Légère correction dans ton url pour aller chercher plus d'annonces par page
	url="https://www.cafr.ebay.ca/sch/Telephones/38036/i.html?_pgn={}&_skc=200".format(n)
	#print(url)

	contenu=requests.get(url)
	page=BeautifulSoup(contenu.text,"html.parser")
	#print(page)

	urltelephones=page.find_all("li",class_="sresult lvresult clearfix li")

	#print(len(urltelephones))

	for urltelephone in urltelephones:

### Un «try» à la grandeur de ton moissonnage fait en sorte qu'il n'y avait jamais rien d'enregistré
### Puisqu'à la moindre erreur, ça répondait «Nada».
		# try:
		telephone = []

### Allons-y plutôt avec des «try» localisés
### Avec ce premier, si on ne trouve pas d'URL,
### la commande «break» fait que l'on quitte la boucle pour passer à l'«urltelephone» suivant

		try:
			url2 = urltelephone.a["href"]
			print(url2)
			telephone.append(url2)
		except:
			break

		contenu2=requests.get(url2)
		page2=BeautifulSoup(contenu2.text,"html.parser")

### Ensuite, on fait des «try» pour chacun des éléments qu'on cherche
		try:
			titre=page2.find("h1",id="itemTitle").text
		except:
			titre="?"
		print(titre)
		telephone.append(titre)

		try:
			prix=page2.find("span",class_="notranslate").text
		except:
			prix="?"
		print(prix)
		telephone.append(prix)

### Pour le lieu, il fallait procéder à un .strip() pour retirer les espaces blancs en trop
		try:
			lieuobjet=page2.find("div",class_="iti-eu-bld-gry ").text.strip()
		except:
			lieuobjet = "?"
		#lieu où l'objet se trouve
		print(lieuobjet)
		telephone.append(lieuobjet)

### Même chose pour cette autre variable
		try:
			lieuexpedition=page2.find("div",class_="iti-eu-bld-gry vi-shp-pdg-rt").text.strip()
		except:
			lieuexpedition = "?"
		#Les lieux où l'objet peut être expédié
		print(lieuexpedition)
		telephone.append(lieuexpedition)

### Ici, ton code ne marchait pas pour trois raisons:
### Un espace de trop
### Pas le bon nom de classe
### Et en fait, l'élément n'est pas une classe, mais un id
		# renvoi=page2.find("span",class_=" vi-no-ret-accrd-txt").text
		try:
			renvoi=page2.find("span",id="vi-ret-accrd-txt").text.strip()
		except:
			renvoi = "?"
		#Les renvois sont-ils permis ou non?
		print(renvoi)
		telephone.append(renvoi)

		#en imprimant (téléphone), nous aurons toutes les informations mises en append entre crochets.

		print(telephone)

		f=open(fichier,"a")
		gnagna=csv.writer(f)
		gnagna.writerow(telephone)

		# except:
		# 	print("Nada")

### En terminant, il semble y avoir un problème qui fait que les annonces se répètent...
### Mais dans le cas d'un site comme eBay, il existe un API qui permettrait de trouver les infos qui t'intéressent plus facilement:
### https://developer.ebay.com/api-docs/buy/browse/static/overview.html