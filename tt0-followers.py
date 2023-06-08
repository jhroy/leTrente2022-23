# ©2022-23, Jean-Hugues Roy - Licence GNU GPL v3
# coding: utf-8

### Ce code utilise TikAPI, une API de TikTok, pour identifier les comptes suivis par un compte donné
### Pratique pour faire de l'échantillonnage exploratoire

from tikapi import TikAPI, ValidationException, ResponseException
from blackTiger import sexMachine ### Ma clé pour l'API de Tiktok est cachée dans un fichier externe que j'importe d'entrée de jeu
import json, csv, datetime

api = TikAPI(sexMachine) ### Remplacez la variable sexMachine par votre clé pour TikAPI

compte = "quebecsolidaire" # On indique ici le compte TikTok dont on souhaite recueillir les comptes qu'il suit

print(compte)

lecompte = api.public.check(username=compte).json()
# print(lecompte)
numero = lecompte["userInfo"]["user"]["secUid"]

if lecompte["status"] == "success":
	print("succès", numero)

	### Si le compte existe bel et bien, on recueille la liste des comptes qu'il suit
	### avec la méthode .followingList()

	reponse = api.public.followingList(secUid=numero)

	matos = reponse.json()

	### Simple boucle ci-dessous pour afficher dans le terminal les infos suivantes à propos du compte suivi:
	### Son nom (nickname), son identifiant, sa signature, et quelques stats (nb de comptes qu'il suit, de followers, de vidéos publiées)

	for util in matos["userList"]:
		print(util["user"]["nickname"])
		print(util["user"]["uniqueId"])
		print(util["user"]["signature"])
		print(util["stats"]["followingCount"],util["stats"]["followerCount"],util["stats"]["videoCount"])
		print("---")
	print("*****")

	# print(matos)

	### L'API ne permet de traiter que 30 comptes à la fois
	### On passe aux suivants avec la boucle while ci-dessous
	### Le code plante quand il n'y en a plus. Pas élégant. Je sais. Je ne suis pas un programmeur.

	while(reponse):
		# prochains = reponse.json().get("cursor")
		reponse = reponse.next_items()
		matos = reponse.json()
		# print(matos)
		print("On pogne les prochains ", len(matos["userList"]))
		for util in matos["userList"]:
			print(util["user"]["nickname"])
			print(util["user"]["uniqueId"])
			print(util["user"]["signature"])
			print(util["stats"]["diggCount"],util["stats"]["followerCount"],util["stats"]["videoCount"])
			print("---")
		print("*****")


else:
	print("YOOOO, rien pour {}".format(compte))
	break