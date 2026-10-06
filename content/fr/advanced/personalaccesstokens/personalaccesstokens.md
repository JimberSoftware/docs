# Jeton d’accès personnel (PAT)

Tout **utilisateur administrateur** peut créer un jeton d’accès personnel (PAT) depuis la page **Paramètres** ![](../../images/menu/menu_settings.png ':size=20'). Ce jeton vous permet d’accéder à l’API de manière sécurisée à l’aide de vos identifiants utilisateur.

---

### Créer un jeton d’accès personnel

1. Accédez à la page **Paramètres** de votre tableau de bord d’administration.

2. Cliquez sur **Créer un nouveau PAT**.  

![pat.png](/screenshots/pat.png ':size=600')


3. Saisissez un **nom** clair et descriptif pour votre PAT afin de pouvoir en identifier l’usage ultérieurement.  
4. Si vous le souhaitez, définissez une **date d’expiration** pour le jeton afin de renforcer la sécurité.



![create_pat.png](/screenshots/create_pat.png ':size=300')

5. Une fois créé, le jeton ne sera affiché **qu’une seule fois** : veillez à le copier en cliquant sur l’icône de copie ![](../../images/icons/icon_copy.png ':size=20') et à le conserver en lieu sûr.

![copy_pat.png](/screenshots/copy_pat.png ':size=600')

6. Votre jeton actif sera répertorié dans cette section. Vous pouvez supprimer le jeton avant sa date d’expiration en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') sur sa ligne. 

![active_pat.png](/screenshots/active_pat.png ':size=600')

> [!WARNING]  
> Le jeton n’est affiché qu’une seule fois lors de sa création. Si vous le perdez, vous devrez en générer un nouveau.

---

## Remarques importantes

- Le PAT est **lié à votre compte utilisateur individuel**, et non au compte de l’entreprise.
- Vous pouvez révoquer ou supprimer à tout moment les jetons existants depuis vos paramètres utilisateur.
- Les dates d’expiration permettent de limiter la durée de vie du jeton et de réduire les risques de sécurité.

---

## Utiliser le PAT dans l’API (interface utilisateur Swagger)

Après avoir créé votre jeton, vous pouvez l’utiliser pour authentifier les appels à l’API via le site de documentation Swagger :

👉 [https://sase.jimber.io/api/docs](https://sase.jimber.io/api/docs)

### Actions possibles sur la page Swagger :

- **S’authentifier avec un PAT :**  
  Cliquez sur le bouton **Autoriser** (en haut à droite) et saisissez votre jeton d’accès personnel dans l’en-tête `x-pat` pour authentifier vos requêtes.

    ![authorize_pat.png](/screenshots/authorize_pat.png ':size=500')
    ![loggedin_pat.png](/screenshots/loggedin_pat.png ':size=500')

- **Explorer les points de terminaison de l’API :**  
  L’interface utilisateur Swagger répertorie tous les points de terminaison de l’API disponibles, regroupés par fonctionnalité. Vous pouvez parcourir et consulter les détails des paramètres de requête, des formats de réponse et des exemples d’appels. Par exemple, cette section contient les points de terminaison de l’API pour les utilisateurs :
    ![swagger_user.png](/screenshots/swagger_user.png ':size=800')

- **Tester directement les appels à l’API :**  
  Grâce à l’interface interactive, vous pouvez envoyer des requêtes à l’API directement depuis le navigateur. Cela vous permet de vérifier le comportement de l’API avant de l’intégrer à vos applications.

- **Consulter les détails des requêtes et des réponses :**  
  Swagger affiche l’intégralité des requêtes et des réponses HTTP, y compris les en-têtes, les codes d’état et les corps des réponses. Ces informations sont très utiles pour le débogage et pour comprendre le fonctionnement de l’API.

- **Essayer différentes méthodes HTTP :**  
  L’interface prend en charge toutes les méthodes proposées par l’API (GET, POST, PUT, DELETE, etc.), ce qui vous permet d’effectuer interactivement toutes les opérations CRUD.

---

## Récapitulatif

| Étape                | Action                                              |
| -------------------- | --------------------------------------------------- |
| Créer un PAT         | L’administrateur crée un jeton sur la page Paramètres |
| Enregistrer le jeton | Copier le jeton et le conserver en lieu sûr (affiché une seule fois) |
| Utiliser le jeton    | Authentifier les appels à l’API via Swagger UI (`x-pat`) |
| Gérer les jetons     | Les révoquer ou définir leur date d’expiration depuis les paramètres utilisateur |

---

Si vous avez besoin d’aide pour créer le jeton ou utiliser l’API, n’hésitez pas à contacter votre administrateur ou l’équipe d’assistance.
