# ©2022-23, Jean-Hugues Roy - Licence GNU GPL v3
# coding: utf-8

### Ce code utilise TikAPI, une API de TikTok
### Pour recueillir des infos de base sur une série de comptes qu'on a identifiés dans la variable «liste» ci-dessous

from tikapi import TikAPI
from blackTiger import sexMachine ### Ma clé pour l'API de Tiktok est cachée dans un fichier externe que j'importe d'entrée de jeu
import json, csv, datetime

api = TikAPI(sexMachine)

liste = [
"m6info_",
"journalmetro",
"majmonactu",
"ledevoir",
"noovo.info",
"latribune",
"ledroitnumerique",
"rtlinfo",
"heidi.news",
"letemps",
"radpointca",
"tvasports",
"tvanouvelles",
"radio.canada.info",
"24heuresca",
"_urbania",
"miseajour",
"lequipe",
"infobref",
"rds.ca",
"loopsider",
"rtsinfo",
"bfmtv",
"tf1info",
"konbini",
"lemondefr",
"rmcsport",
"brutofficiel",
"hugodecrypte",
"hamza.sdt",
"lavoixdunord",
"ouestfrance",
"leprogres.lyon",
"lefigarofr",
"leparisien",
"sudouestfr",
"marseillefaitsdivers",
"tdg.ch",
"cnews",
"franceinfo",
"radio.canada.estrie",
"radio.canada.bsl",
"lapochebleue",
"narcityquebec",
"mtlblog",
"radio.canada.ottgat",
"lesacdechips",
"radio.canada.sports",
"radio.canada.quebec",
"pivot.quebec"
]

n = 1

for compte in liste:
	print(compte)

	lecompte = api.public.check(username=compte).json()

	if lecompte["status"] == "success":

		# print(lecompte)
		# break

		### On va chercher les infos suivantes:

		lecode = lecompte["userInfo"]["user"]["secUid"] ### L'identifiant «sécuritaire» du compte
		sig = lecompte["userInfo"]["user"]["signature"] ### La signature (ou description) du compte
		nom = lecompte["userInfo"]["user"]["nickname"] ### Le nom du compte
		sonId = lecompte["userInfo"]["user"]["id"] ### Un autre identifiant dont l'utilité n'est pas claire
		followers = lecompte["userInfo"]["stats"]["followerCount"] ### Le nombre de followers du compte
		suivis = lecompte["userInfo"]["stats"]["followingCount"] ### Le nombre d'autres comptes suivis par ce compte
		likes = lecompte["userInfo"]["stats"]["heartCount"] ### Le nombre de «likes» sur ce compte
		videos = lecompte["userInfo"]["stats"]["videoCount"] ### Le nombre de vidéos publiées par ce compte
		
		# derniereModif = datetime.datetime.fromtimestamp(lecompte["userInfo"]["user"]["nickNameModifyTime"])

		infos = [compte,nom,sonId,sig,followers,suivis,likes,videos,lecode]
		print(infos)

		### Les infos sont ensuite consignées dans un fichier CSV pour la prochaine étape

		tik = open("lescomptes-medias.csv","a")
		# tik = open("lescomptes-voxpop.csv","a")
		tok = csv.writer(tik)
		tok.writerow(infos)

	else:
		print("YOOOO, rien pour {}".format(compte))
		break