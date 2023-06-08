# ©2022, Jean-Hugues Roy - Licence GNU GPL v3
# coding: utf-8

### Ce code utilise TikAPI, une API de TikTok
### Pour recueillir des métadonnées sur toutes les vidéos publiées par
### Une série de comptes TikTok identifiés à l'étape préalable et consignés dans un fichier CSV

from tikapi import TikAPI
from blackTiger import sexMachine ### Ma clé pour l'API de Tiktok est cachée dans un fichier externe que j'importe d'entrée de jeu
import json, csv, datetime

api = TikAPI(sexMachine)

n = 0

### Noms des fichiers CSV dans lesquels on va lire les infos de départ
### Et dans lesquels ont va enregistrer les infos qu'on va recueillir

fichier = "lescomptes-medias.csv"
# fichier = "lescomptes-medias-europe.csv"
fichierOut = "lesvideos-medias-juin-2023.csv"
# fichierOut = "lesvideos-medias-juin-2023-europe.csv"

f0 = open(fichier)
comptes = csv.reader(f0)
# next(comptes)

for compte in comptes:
	
	secuid = compte[-1]

	reponse = api.public.posts(secUid=secuid)
	rep = reponse.json()

	### L'API nous donne des infos pour une trentaine de vidéos à la fois
	### Les métadonnées sont dans une clé appelée «itemsList»

	for vid in rep["itemList"]:
		n += 1

		### Pour chaque vidéo, on va chercher les infos suivantes:

		date = datetime.datetime.fromtimestamp(vid["createTime"]) ### La date de publication
		desc = vid["desc"] ### Le texte de la description
		comm = vid["stats"]["commentCount"] ### Le nombre de commentaires
		likes = vid["stats"]["diggCount"] ### Le nombre de likes
		vues = vid["stats"]["playCount"] ### Le nombre de vues
		part = vid["stats"]["shareCount"] ### Le nombre de partages
		
		### On va aussi chercher, si disponible, des infos sur la musique entendue pendant la vidéo

		try:
			chansonTitre = vid["music"]["title"]
			chansonAuteur = vid["music"]["authorName"]
		except:
			chansonTitre = ""
			chansonAuteur = ""
		
		### Si c'est disponible, également, on va cherche le texte qui apparaît en surimposition pendant que la vidéo joue

		texte = ""
		try:
			for t in vid["stickersOnItem"][0]["stickerText"]:
				texte += t + ". "
			while "  " in texte:
				texte = texte.replace("  "," ")
			while ".." in texte:
				texte = texte.replace("..",".")
			texte = texte.strip()
		except:
			pass

		### On recueille enfin la durée de la vidéo et son URL unique

		duree = vid["video"]["duration"]
		url = "https://www.tiktok.com/@{}/video/{}".format(compte[0],vid["id"])

		infos = [n, compte[0], date, desc, comm, likes, vues, part, texte, url, duree, chansonTitre, chansonAuteur]
		print(infos)
		print("="*15)

		### On consigne ces infos dans un CSV

		tik = open(fichierOut,"a")
		tok = csv.writer(tik)
		tok.writerow(infos)

	### La boucle while ci-dessous traite les 30 vidéos suivantes publiées (par ordre chronologique inverse) par le compte auquel on est rendu

	try:
		while(reponse):
			cursor = reponse.json().get("cursor")
			print("Getting next items ", cursor)
			print("*"*10)
			reponse = reponse.next_items()
			rep = reponse.json()

			for vid in rep["itemList"]:
				n += 1
				date = datetime.datetime.fromtimestamp(vid["createTime"])
				desc = vid["desc"]
				comm = vid["stats"]["commentCount"]
				likes = vid["stats"]["diggCount"]
				vues = vid["stats"]["playCount"]
				part = vid["stats"]["shareCount"]
				
				try:
					chansonTitre = vid["music"]["title"]
					chansonAuteur = vid["music"]["authorName"]
				except:
					chansonTitre = ""
					chansonAuteur = ""
				
				texte = ""
				try:
					for t in vid["stickersOnItem"][0]["stickerText"]:
						texte += t + ". "
					while "  " in texte:
						texte = texte.replace("  "," ")
					while ".." in texte:
						texte = texte.replace("..",".")
					texte = texte.strip()
				except:
					pass

				duree = vid["video"]["duration"]
				url = "https://www.tiktok.com/@{}/video/{}".format(compte[0],vid["id"])

				infos = [n, compte[0], date, desc, comm, likes, vues, part, texte, url, duree, chansonTitre, chansonAuteur]
				print(infos)
				print("="*15)

				tik = open(fichierOut,"a")
				tok = csv.writer(tik)
				tok.writerow(infos)

	except:
		pass
