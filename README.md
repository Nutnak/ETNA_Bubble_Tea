Projet BubbleTea: Bubbolitas le site e-commerce de vente de bubble tea.

--- Résumé du projet ---

Ce programme permet aux utilisateurs de se connecter à un serveur Ecommerce et de commander les bubbleteas de leur choix. Il a été réalisé avec Python3 et Django en utilisant bcrypt, jwt et MySQL pour la base de données.

-Il est possible de visiter la page principale de notre site internet sans devoir créer de compte. 
-Vous pouvez vous créer un compte et y modifier les informations si nécessaire. 
-Sécurisation des sessions grâce aux tokens.

Nous espérons que vous l'apprécierez !

--- Comment l'utiliser ---

1. Créez un environnement viturel.
2. pip install requirements.txt
3. Créer un utilisateur admin avec admin en mdp sur mySQL.
4. Lui donner tous les droits.
5. Ensuite à la racine du projet, faire : mysql -u admin -p bubbolitas_db < bubbolitas.sql.
6. Faire les migrations : python3 manage.py migrate && python3 manage.py makemigrations
7. Pour lancer le serveur, faites : python3 manage.py runserver
8. Amusez-vous :) 
