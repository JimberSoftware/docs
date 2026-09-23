# Comment configurer Microsoft Entra ID

## Créer un compte

Rendez-vous sur https://azure.microsoft.com/ et créez un compte Azure si vous n’en avez pas déjà un.

Après avoir créé un compte, vous pouvez accéder au [portail Azure](https://portal.azure.com/#home).

## Créer une inscription d’application

Dans le portail Azure, accédez à Inscriptions d’applications, qui se trouve sous « Services Azure ».

![azure_portal.png](./screenshots/azure_portal.png ":size=900")

Inscrivez une nouvelle application en cliquant sur « Nouvelle inscription » en haut à gauche.

![azure_new_registration.png](./screenshots/azure_new_registration.png ":size=900")

Choisissez un nom (par exemple JimberNetworkIsolation) et votre portée ; dans la plupart des cas, « Locataire unique » suffit.
Vous n’avez pas besoin d’un URI de redirection.
Cliquez ensuite sur « Inscrire » en bas à gauche de votre écran.

![azure_registration_info.png](./screenshots/azure_registration_info.png ":size=900")

## Autorisations

Accédez à l’inscription de l’application que vous venez de créer, puis choisissez « Autorisations d’API » dans le panneau du menu de droite.

![apipermissions.png](./screenshots/apipermissions.png ":size=900")

Les autorisations suivantes de l’API Microsoft Graph sont nécessaires :

- Group.Read.All (Application)
- User.Read (Déléguée) -> celle-ci devrait déjà être créée par défaut
- User.Read.All (Application)

Pour accorder de nouvelles autorisations, cliquez sur « Ajouter une autorisation », juste au-dessus des autorisations existantes.
Vous pouvez ensuite cliquer sur le bouton « Microsoft Graph ».

![azure_microsoft_graph.png](./screenshots/request_api.png ":size=900")

Comme indiqué précédemment, vous devez ajouter Group.Read.All et User.Read.All ; les deux sont des **autorisations d’application**.

> [!WARNING]
> Veillez à sélectionner le bon type d’autorisations !

![microsoft_graph_type_permissions.png](./screenshots/request_api_2.png ":size=900")

Vous obtiendrez une liste complète des différentes autorisations dans laquelle vous pourrez rechercher celles dont vous avez besoin : « Group.Read.All » et « User.Read.All ».

![permission_group.png](./screenshots/permission_group.png ":size=500")

![permission_user.png](./screenshots/permission_user.png ":size=500")

Une fois cette étape terminée, votre liste d’autorisations devrait ressembler à ceci :

![azure_permissions_list.png](./screenshots/azure_permissions_list.png ":size=900")

Le consentement de l’administrateur est obligatoire et doit être accordé pour votre répertoire de base dans Azure. Dans notre exemple, le répertoire de base est « Standaardmap ».

Pour ce faire, cliquez sur « Accorder le consentement de l’administrateur pour Standaardmap », à côté de « Ajouter une autorisation ». Le statut de chaque autorisation passera alors à « Accordé ».

![grand_admin_consent.png](./screenshots/grant_admin_consent.png ":size=900")

> [!NOTE]
> Si vous ne pouvez pas accorder le consentement de l’administrateur, c’est parce que votre utilisateur ne dispose pas des droits d’administrateur. Veuillez contacter l’administrateur de votre portail Azure pour qu’il accorde ce consentement.

Enfin, votre liste d’autorisations devrait ressembler à ceci :

![grand_admin_consent.png](./screenshots/configured_permissions.png ":size=900")

## Informations d’identification du client

Accédez à « Vue d’ensemble » dans le panneau du menu de gauche pour obtenir la liste des informations essentielles.

Vous devez ajouter ici les informations d’identification du client :

![azure_credentials.png](./screenshots/azure_credentials.png ":size=900")

Sur l’écran suivant, cliquez sur « Nouveau secret client ». Choisissez une description et une date d’expiration :

![new_client_secret.png](./screenshots/new_client_secret.png ":size=900")

> [!WARNING]
> Lorsque le jeton expire, une intervention manuelle est nécessaire pour que la synchronisation Entra ID continue de fonctionner.

Les informations suivantes sont nécessaires pour la configuration dans Jimber Network Isolation :

- Le secret client que vous venez de créer (valeur)
- L’ID client de votre application enregistrée (disponible dans la vue d’ensemble)
- L’ID du locataire de votre répertoire (disponible dans la vue d’ensemble)

![new_client_secret.png](./screenshots/secret_id.png ":size=900")

![needed_info.png](./screenshots/needed_info.png ":size=900")

Pour terminer la configuration de Network Isolation, accédez à la [page de documentation](/company/integrations/integrations.md) suivante.
