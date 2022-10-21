"""
                        PRE-REQUIS POUR L'UTILISATION ET LA COMPREHENSION DU PROJET
-Lire et comprendre la documentation de l'api openai (https://openai.com/) pour pouvoir comprendre facilement ce projet
-Posseder un compte et avoir une clé d'api de l'open ai (la clé d'api est gratuite pendant un temps et s'avère payante
au bout du délai)
-Lire le guide d'utilisation et d'exploitation  du document de ce projet
-Charger toutes les importations et installations contenues dans le app.py


                        LES PRINCIPAUX FICHIERS QUI ONT PERMIS LA REALISATION DE CE PROJET

-Le fichier "mainbot.html" contenu dans le dossier templates qui sert d'interface web de demo pour montrer les différentes
fonctionnalités du système
-le fichier "app.py" qui contient toutes les fonctions renfermant les fonctionnalités  importantes et nécessaires  du système

                 PROCESSUS PRIMORDIAL DE BASE A COMPRENDRE POUR UNE EVENTUELLE CONTINUITE OU MODIFICATION DU SYSTEME

   Concernant toutes les fonctions par rapport à une fonctionnalité du système , que ce soient, les fonctions sentiment() , return_response(),
conversation(text), le travaille ou le socle de leurs définitions et de leur habilité de réponse logique , se trouvent dans leur différent "Prompt".

Prompt: Dans ce prompt, nous définissons les élements nécessaires pour pouvoir permettre au système de donner les réponses que nous attendons ou expérons.
Nous y referons des exemples indicatifs pour montrer au système comment répondre ou réagir.

EXEMPLE : Prenons le cas de la fonction sentiment()  dans app.py

  Le  but est de déterminer le sentiment de chaque phrase qui sera entrée par l'utilisateur de sorte qu'il soit positive , neutre ou
  negative.

 -D'abord tous les texts sont faits sur le site de l'open ai dans le playground .De là , nous définissons des exemples pour montrer au
 système ce qu'on veut faire
 -Après avoir effectué ces tests, le code source de la fonction sentiment() est générée depuis le site avec un "prompt" contenant les exemples de détections de sentiment


 Ce scénario est identique aux autres fonctions face aux différentes fonctionnalités du système.


 Concernant les fonctions sqlquery() et returnresponse(), les tables nécessaires de la base de données de l'entreprise sont définies dans
 le prompt pour dire au système que ce sont ces tables qu'ils doivent utiliser pour les différentes actions.

 Spécifiquement pour les données contenues dans une table de la base d'une entreprise spécifique,pour une éventuelle recherche du bot,il faut le définir dans une
 variable  dans le prompt dans la méthode retrunresponse() après avoir définit les tables aussi.

 EXEMPLE: Pour ce projet dans le prompt de la fonction returnresponse() dans app.py il est définit une valeur ''Value'' qui renferme
 une liste de certains produits.
"""