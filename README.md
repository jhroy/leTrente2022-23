# Médias du Québec et réseaux sociaux (Facebook, Instagram et TikTok), 2011-2023

Code et données utilisées pour un article sur la présence des médias québécois dans trois réseaux sociaux (Facebook, Instagram et TikTok) publié dans *Le Trente*, magazine annuel de la [Fédération professionnelle des journalistes du Québec (FPJQ)](https://www.fpjq.org/fr/).

## Méthodologie

### Facebook et Instagram

Les données sur les contenus journalistiques québécois dans Facebook et Instagram ont été obtenues à partir de deux tableaux de bord créés dans [CrowdTangle](https://www.crowdtangle.com/), un outil d'analyse de contenus appartenant à Meta Platforms, la société mère des deux réseaux sociaux. Dans ces tableaux de bord, deux listes ont été créées:
* une liste de 309 pages Facebook médiatiques appelée MediasQuebec
* une liste de 85 comptes Instagram médiatiques appelée MediasQC

![capture d'écran CrowdTangle de la liste Facebook](CT-Facebook.png)

![capture d'écran CrowdTangle de la liste Instagram](CT-Insta.png)

J'ai ensuite demandé à CrowdTangle de me fournir toutes les publications qu'il contient et qui ont été faites par les 309 pages Facebook et les 85 comptes Instagram identifiés entre le 1er janvier 2011 et le 31 mai 2023.

* Pour Facebook, CrowdTangle a retourné 60 fichiers différents contenant en tout **4&nbsp;549&nbsp;559 publications**.
* Pour Instagram, CrowdTangle a retourné 15 fichiers différents contenant en tout **140&nbsp;542 publications**.

Un premier traitement de l'ensemble de ces fichiers a été effectué à l'aide de [pandas](https://pandas.pydata.org/docs/), module python d'analyse de données. Les carnets qui détaillent cette première étape sont accessibles dans ce répertoire:
* [**FB_300médias_parMois.ipynb**](FB_300médias_parMois.ipynb)
* [**IG_85_médias_parMois.ipynb**](IG_85_médias_parMois.ipynb)

J'ai ensuite extrait les publications des 17 mois s'échelonnant du 1er janvier 2022 au 31 mai 2023 et les ai analysées, notamment à l'aide du module de traitement du langage naturel [spacy](https://spacy.io/), dans deux autres carnets:
* [**FB_Analyse_2022-23.ipynb**](FB_Analyse_2022-23.ipynb)
* [**IG_Analyse_2022-23.ipynb**](IG_Analyse_2022-23.ipynb)

### TikTok

Pour recueillir les métadonnées des vidéos diffusées par les médias du Québec dans TikTok, l'API [TikAPI](https://tikapi.io/) ($) a été utilisée. Ce moissonnage a été effectué en trois étapes.

#### Échantillonnage ❄️

La méthode d'échantillonnage [boule de neige](https://fr.wikipedia.org/wiki/%C3%89chantillonnage_boule_de_neige) a été utilisée. À partir de comptes préalablement identifiés, comme ceux de certains médias ([@tvanouvelles](https://www.tiktok.com/@tvanouvelles), [@ledevoir](https://www.tiktok.com/@ledevoir), etc.) ou de certaines organisations qui ont à traiter régulièrement avec des médias ([@quebecsolidaire](https://www.tiktok.com/@quebecsolidaire), [@uqam](https://www.tiktok.com/@uqam), etc.), un premier script fouille dans la liste des autres comptes TikTok qui sont suivis par ce compte afin d'identifier des comptes de médias:
* [**tt0-following.py**](tt0-following.py)

#### Détails des comptes médiatiques

Une fois les comptes de médias établie, un deuxième script va chercher des métadonnées sur ces comptes. À noter que j'ai ajouté des médias européens dans ce script pour d'autres projets de recherche:
* [**tt1-comptes.py**](tt1-comptes.py)

#### Détails des vidéos

À partir des métadonnées de base sur les comptes qui nous intéressent, ce troisième script recueille des données sur toutes les vidéos diffusées dans TikTok par ces comptes depuis qu'ils y sont abonnés.
* [**tt2-videos.py**](tt2-videos.py)

Une analyse textuelle a également été effectuée sur un sous-ensemble composé des publications TikTok diffusées en 2022 et en 2023 (jusqu'au 31 mai 2023). Elle est décrite dans ce carnet:
* [**TT_Analyse_2022-23.ipynb**](TT_Analyse_2022-23.ipynb)

## Données

### Facebook

Les [conditions d'utilisation](https://www.crowdtangle.com/terms) de CrowdTangle ne me permettent pas de rendre accessible l'ensemble des données colligées. Je demeure ouvert à les faire parvenir à toute personne chercheuse qui [m'en ferait la demande](mailto:roy.jean-hugues@uqam.ca?subject="Vos données CrowdTangle (2022-23)") dans le cadre d'un projet de recherche (s'applique aussi aux personnes étudiantes aux cycles supérieurs à l'université).

Je peux cependant donner accès à ces données agrégées qui donne une idée de l'activité Facebook d'un peu plus de 300 pages de médias québécois entre le 1er janvier 2022 et le 31 mai 2023:

* [**Facebook_medias_quebec_2022-2023.csv**](Facebook_medias_quebec_2022-2023.csv)

### Instagram

Les conditions d'utilisation de CrowdTangle s'appliquent également à mon corpus Instagram. Je suis disposé à y donner accès, mais sur demande seulement.

Et je peux donner accès à l'agrégation présentée dans le fichier CSV suivant, qui donne une idée de l'activité Instagram d'un peu plus de 80 comptes de médias québécois entre le 1er janvier 2022 et le 31 mai 2023:

* [**Instagram_medias_quebec_2022-2023.csv**](Instagram_medias_quebec_2022-2023.csv)

### TikTok

Je n'ai pas les même restrictions avec TikTok. Je peux rendre accessible l'ensemble des données que j'ai récoltées grâce à la métho décrite ci-dessus dans le fichier suivant:

* [**TikTok_medias_quebec_2019-2023.csv**](TikTok_medias_quebec_2019-2023.csv)
