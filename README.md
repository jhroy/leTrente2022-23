# Médias du Québec et réseaux sociaux (Facebook, Instagram et TikTok), 2011-2023

Code et données utilisées pour un article sur la présence des médias québécois dans trois réseaux sociaux (Facebook, Instagram et TikTok) publié dans *Le Trente*, magazine annuel de la [Fédération professionnelle des journalistes du Québec (FPJQ)](https://www.fpjq.org/fr/).

## Facebook et Instagram

Les données sur les contenus journalistiques québécois dans Facebook et Instagram ont été obtenues à partir de deux tableaux de bord créés dans [CrowdTangle](https://www.crowdtangle.com/), un outil d'analyse de contenus appartenant à Meta Platforms, la société mère des deux réseaux sociaux. Dans ces tableaux de bord, deux listes ont été créées:
* une liste de 309 pages Facebook médiatiques appelée MediasQuebec
* une liste de 85 comptes Instagram médiatiques appelée MediasQC

[!)(CT-Facebook.png)

[!](CT-Insta.png)

## TikTok

Pour recueillir les métadonnées des vidéos diffusées par les médias du Québec dans TikTok, l'API [TikAPI](https://tikapi.io/) ($) a été utilisée. Ce moissonnage a été effectué en trois étapes.

### Échantillonnage ❄️

La méthode d'échantillonnage [boule de neige](https://fr.wikipedia.org/wiki/%C3%89chantillonnage_boule_de_neige) a été utilisée. À partir de comptes préalablement identifiés, comme ceux de certains médias ([@tvanouvelles](https://www.tiktok.com/@tvanouvelles), [@ledevoir](https://www.tiktok.com/@ledevoir), etc.) ou de certaines organisations qui ont à traiter régulièrement avec des médias ([@quebecsolidaire](https://www.tiktok.com/@quebecsolidaire), [@uqam](https://www.tiktok.com/@uqam), etc.), un premier script fouille dans la liste des autres comptes TikTok qui sont suivis par ce compte afin d'identifier des comptes de médias:
* [**tt0-following.py**](tt0-following.py)

### Détails des comptes médiatiques

Une fois les comptes de médias établie, un deuxième script va chercher des métadonnées sur ces comptes. À noter que j'ai ajouté des médias européens dans ce script pour d'autres projets de recherche:
* [**tt1-comptes.py**](tt1-comptes.py)

### Détails des vidéos

À partir des métadonnées de base sur les comptes qui nous intéressent, ce troisième script recueille des données sur toutes les vidéos diffusées dans TikTok par ces comptes depuis qu'ils y sont abonnés.
* [**tt2-videos.py**](tt2-videos.py)

## 
