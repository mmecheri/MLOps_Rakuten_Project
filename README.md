# Projet Append Engineer - Mourad MECHERI
## Déploiement du projet: Rakuten France Multimodal Product Data Classification
 
 
### Contexte du projet

Ce projet porte sur le dépoilement d’un projet de Machine Learning dans le cadre de ma formation de ML Engineer au sein de l’organisme DataScientest. 
L’objectif étant de déployer en API et de conteneuriser un modèle de prédiction en Machine ou Deep Learning. 
Dans ce projet , je reprends mon projet  fil rouge : Rakuten France Multimodal Product Data Classification réalisé au cours de ma précédente formation de Data Scientist  au sein du même organisme de formation. 
Contexte et solution retenue lors du projet de formation Data Scientist 
Dans un contexte de classification des produits « e-commerce » ,  dans la partie modélisation et prédiction, l’objectif était de prédire le code type (prdtypecode) de chaque produit en utilisant des données textuelles (désignation et description du produit) ainsi que des données images (image du produit) tel qu'il est défini dans le catalogue de Rakuten France.

A l’issu du projet , nous avons proposé une solution qui permet de réaliser des prédictions avec un modèle basé sur les données Texte ou Images ou les deux combines(Bimodal). 
Voici les modèles et les combinations que nous avons retenus:

-	Une classification basée sur le Texte: 
     >- Conv1D et Simple DNN
     
-	Une classification basée sur les Images: 
	 >-  Xception et InceptionV3
-	Une classification Bimodal - Texte et Images:

     >- Conv1D, Simple DNN et Xception  
     >- Conv1D, Simple DNN et InceptionV3

#### Etape du projet  :
-	Reprendre les modèle de classification de produits e-commerce Rakuten France et les déployer sur une API :  créer des Endpoints pour réaliser des prédictions
-	Créer une base de données en Backend pour l’API avec la gestion et l'authentification des utilisateurs 
-	Conteneuriser avec Docker et Docker-compose
-	Réaliser des tests  d’ Authentification , d’Autorisation  et de prédictions via des containers distincts



Pour utiliser ce repo, il suffit de le cloner: 

*git clone https://github.com/mmecheri/Append_Engineer_Project.git*

*cd Append_Engineer_Project*

Puis de lancer le fichier `setup.sh`: 
 chmod +x setup.sh
 *'./setup.sh*'


L'API est ensuite disponible à l'adresse *[http://localhost:8000](http://localhost:8000")* 

La documentation est présente au point d'entrée '/docs'



**Réalisé par:** 
  Mourad MECHERI

**Supervisé par:**
  Anthony JAILLET

