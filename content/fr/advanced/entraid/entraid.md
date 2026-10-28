# Comment configurer Microsoft Entra ID

### Créer un compte

Accédez à https://azure.microsoft.com/ et créez un compte Azure si vous n’en avez pas déjà un.

Après avoir créé un compte, vous pouvez accéder au [portail Azure](https://portal.azure.com/#home).

### Créer une inscription d’application

Dans le portail Azure, accédez à Inscriptions d’applications, sous « Services Azure ».

![azure_portal.png](./screenshots/azure_portal.png ":size=700")

Inscrivez une nouvelle application en cliquant sur « Nouvelle inscription » en haut à gauche.

![azure_new_registration.png](./screenshots/azure_new_registration.png ":size=700")

Choisissez un nom (par exemple JimberNetworkIsolation) et votre portée. En général, « Locataire unique » suffit.
Vous n’avez pas besoin d’URI de redirection.
Cliquez ensuite sur « Inscrire » en bas à gauche de votre écran.

![azure_registration_info.png](./screenshots/azure_registration_info.png ":size=700")

### Autorisations

Accédez à l’inscription d’application que vous venez de créer, puis choisissez « Autorisations d’API » dans le menu de droite.

![apipermissions.png](./screenshots/apipermissions.png ":size=700")

Les autorisations suivantes de l’API Microsoft Graph sont nécessaires :

- Group.Read.All (Application)
- User.Read (Déléguée) -> celle-ci devrait déjà être créée par défaut
- User.Read.All (Application)
- Device.Read.All (Application) -> nécessaire pour la **connexion automatique** ; voir [Connexion automatique](#auto-login-microsoft-entra-id-sso-on-windows)

Pour accorder de nouvelles autorisations, cliquez sur « Ajouter une autorisation », juste au-dessus des autorisations existantes.
Vous pouvez ensuite cliquer sur le bouton « Microsoft Graph ».

![azure_microsoft_graph.png](./screenshots/request_api.png ":size=700")

Comme indiqué précédemment, vous devez ajouter Group.Read.All, User.Read.All et Device.Read.All, qui sont toutes les trois des **autorisations d’application**.

> [!WARNING]
> Veillez à sélectionner le bon type d’autorisations !

![microsoft_graph_type_permissions.png](./screenshots/request_api_2.png ":size=700")

Une liste complète d’autorisations s’affichera. Vous pourrez y rechercher les autorisations appropriées : « Group.Read.All », « User.Read.All » et « Device.Read.All ».

![permission_group.png](./screenshots/permission_group.png ":size=500")

![permission_user.png](./screenshots/permission_user.png ":size=500")

Une fois cette étape terminée, votre liste d’autorisations devrait ressembler à ceci (elle comportera une ligne supplémentaire, `Device.Read.All`, par rapport à la capture d’écran) :

![azure_permissions_list.png](./screenshots/azure_permissions_list.png ":size=700")

Le consentement de l’administrateur est requis et doit être accordé pour votre répertoire de base dans Azure. Dans notre exemple, le répertoire de base est « Standaardmap ».

Pour ce faire, cliquez sur « Accorder le consentement de l’administrateur pour Standaardmap », à côté de « Ajouter une autorisation ». Le statut de chaque autorisation passera alors à « accordé ».

![grand_admin_consent.png](./screenshots/grant_admin_consent.png ":size=700")

> [!NOTE]
> Si vous ne pouvez pas accorder le consentement de l’administrateur, c’est parce que votre utilisateur ne dispose pas des droits d’administrateur. Contactez l’administrateur de votre portail Azure pour qu’il accorde le consentement de l’administrateur.

À la fin, votre liste d’autorisations devrait ressembler à ceci :

![grand_admin_consent.png](./screenshots/configured_permissions.png ":size=700")

### Connexion automatique (SSO Microsoft Entra ID sous Windows)

Le client Jimber SASE sous Windows peut connecter automatiquement un utilisateur avec son identité Microsoft Entra ID, sans afficher la page de connexion du navigateur. Avant de passer outre cette page, la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** vérifie, par l’intermédiaire de Microsoft Graph, que l’appareil est joint à Entra et que l’utilisateur connecté est enregistré sur cet appareil.

Cette vérification utilise les points de terminaison Graph `/devices`, raison pour laquelle l’autorisation d’application **Device.Read.All** est nécessaire, en plus de `Group.Read.All` et `User.Read.All`. Elle doit être ajoutée en tant qu’**autorisation d’application**, et le consentement de l’administrateur doit lui être accordé, comme pour les deux autres autorisations.

> [!NOTE]
> La connexion automatique est également un paramètre par groupe dans la configuration de groupe. Lorsqu’elle n’est pas activée pour un groupe, la plateforme n’interroge pas du tout Microsoft Graph pour cet utilisateur.

> [!WARNING]
> Si `Device.Read.All` est manquante, a été ajoutée en tant qu’autorisation *Déléguée* ou n’a pas reçu le consentement de l’administrateur, Microsoft Graph répond par *Insufficient privileges to complete the operation*. La plateforme consigne alors le message `Device query failed: Insufficient privileges to complete the operation.` dans **Activité récente**, et les utilisateurs concernés sont redirigés vers la connexion interactive dans le navigateur.

### Informations d’identification du client

Accédez à « Vue d’ensemble » dans le menu de gauche pour afficher la liste des informations essentielles.

Vous devez ajouter ici les informations d’identification du client :

![azure_credentials.png](./screenshots/azure_credentials.png ":size=700")

Dans l’écran suivant, cliquez sur « Nouveau secret client ». Choisissez une description et une date d’expiration :

![new_client_secret.png](./screenshots/new_client_secret.png ":size=700")

> [!WARNING]
> À l’expiration du jeton, une intervention manuelle est nécessaire pour garantir le bon fonctionnement de la synchronisation Entra ID.

Les informations suivantes sont nécessaires pour la configuration dans Jimber Network Isolation :

- Le secret client que vous venez de créer (valeur)
- L’ID client de votre application inscrite (dans la vue d’ensemble)
- L’ID du locataire de votre répertoire (dans la vue d’ensemble)

![new_client_secret.png](./screenshots/secret_id.png ":size=700")

![needed_info.png](./screenshots/needed_info.png ":size=700")

Pour terminer la configuration de Network Isolation, accédez à la [page de documentation](/company/integrations/integrations.md) suivante.
