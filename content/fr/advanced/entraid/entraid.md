# Comment configurer Microsoft Entra ID

### Créer un compte

Rendez-vous sur https://azure.microsoft.com/ et créez un compte Azure si vous n’en avez pas déjà un.

Après avoir créé un compte, vous pouvez accéder au [portail Azure](https://portal.azure.com/#home).

### Créer une inscription d’application

Dans le portail Azure, accédez à Inscriptions d’applications, sous « Services Azure ».

![azure_portal.png](./screenshots/azure_portal.png ":size=700")

Inscrivez une nouvelle application en cliquant sur « Nouvelle inscription », en haut à gauche.

![azure_new_registration.png](./screenshots/azure_new_registration.png ":size=700")

Choisissez un nom (par exemple JimberNetworkIsolation) et votre type de compte. Dans la plupart des cas, « Locataire unique » suffit.
Vous n’avez pas besoin d’un URI de redirection.
Cliquez ensuite sur « Inscrire », en bas à gauche de votre écran.

![azure_registration_info.png](./screenshots/azure_registration_info.png ":size=700")

### Autorisations

Accédez à l’inscription d’application que vous venez de créer, puis sélectionnez « Autorisations d’API » dans le panneau de menu à droite.

![apipermissions.png](./screenshots/apipermissions.png ":size=700")

Les autorisations suivantes de l’API Microsoft Graph sont nécessaires :

- Group.Read.All (Application)
- User.Read (Déléguée) -> celle-ci devrait déjà être créée par défaut
- User.Read.All (Application)

Pour ajouter de nouvelles autorisations, cliquez sur « Ajouter une autorisation », juste au-dessus des autorisations existantes.
Cliquez ensuite sur le bouton « Microsoft Graph ».

![azure_microsoft_graph.png](./screenshots/request_api.png ":size=700")

Comme indiqué précédemment, vous devez ajouter Group.Read.All et User.Read.All. Il s’agit dans les deux cas d’**autorisations d’application**.

> [!WARNING]
> Veillez à sélectionner le bon type d’autorisations !

![microsoft_graph_type_permissions.png](./screenshots/request_api_2.png ":size=700")

Une liste complète des différentes autorisations s’affiche. Vous pouvez y rechercher les autorisations voulues : « Group.Read.All » et « User.Read.All ».

![permission_group.png](./screenshots/permission_group.png ":size=500")

![permission_user.png](./screenshots/permission_user.png ":size=500")

Une fois cette étape terminée, votre liste d’autorisations devrait ressembler à ceci :

![azure_permissions_list.png](./screenshots/azure_permissions_list.png ":size=700")

Le consentement de l’administrateur est requis et doit être accordé pour votre répertoire de base dans Azure. Dans notre exemple, le répertoire de base est « Standaardmap ».

Pour ce faire, cliquez sur « Accorder le consentement de l’administrateur pour Standaardmap », à côté de « Ajouter une autorisation ». Le statut de chaque autorisation passera alors à « Accordée ».

![grand_admin_consent.png](./screenshots/grant_admin_consent.png ":size=700")

> [!NOTE]
> Si vous ne pouvez pas accorder le consentement de l’administrateur, c’est que votre utilisateur ne dispose pas des droits d’administrateur. Veuillez contacter l’administrateur de votre portail Azure pour qu’il accorde le consentement.

Votre liste d’autorisations devrait finalement ressembler à ceci :

![grand_admin_consent.png](./screenshots/configured_permissions.png ":size=700")

### Informations d’identification du client

Accédez à « Vue d’ensemble » dans le panneau de menu à gauche pour obtenir la liste des informations essentielles.

Vous devez ajouter ici les informations d’identification du client :

![azure_credentials.png](./screenshots/azure_credentials.png ":size=700")

Sur l’écran suivant, cliquez sur « Nouveau secret client ». Choisissez une description et une date d’expiration :

![new_client_secret.png](./screenshots/new_client_secret.png ":size=700")

> [!WARNING]
> À l’expiration du jeton, une intervention manuelle est nécessaire pour que la synchronisation Entra ID continue de fonctionner.

Les informations suivantes sont nécessaires pour la configuration de Jimber Network Isolation :

- Le secret client que vous venez de créer (Valeur)
- L’ID client de votre application inscrite (visible dans la vue d’ensemble)
- L’ID de locataire de votre répertoire (visible dans la vue d’ensemble)

![new_client_secret.png](./screenshots/secret_id.png ":size=700")

![needed_info.png](./screenshots/needed_info.png ":size=700")

Pour terminer la configuration de Network Isolation, consultez la [page de documentation suivante](/company/integrations/integrations.md).
