File: company/integrations/integrations.md

# ![](../../images/menu/menu_integrations.png ':size=25') Intégrations

<!-- ## Identifiants : clé API

Les clés API permettent de s’authentifier et d’accéder à diverses ressources d’une application ou d’une plateforme via son API. Elles sont généralement utilisées pour faciliter l’interaction entre des logiciels tiers et votre application, en permettant l’automatisation, l’intégration et d’autres fonctionnalités avancées.

![api_key.png](api_key.png) -->


## DNS

Un redirecteur DNS redirige les requêtes DNS d’un serveur vers un autre. Il est utile pour gérer et accélérer les requêtes DNS en redirigeant les demandes vers un serveur DNS plus rapide ou plus à jour que celui défini par défaut.
Pour cela, saisissez l’adresse IP du serveur DNS et cliquez sur le bouton Appliquer.

![dns_forwarder.png](./screenshots/dns_forwarder.png ":size=500")



## Microsoft Entra ID

Synchronisez facilement vos données utilisateur de Microsoft Entra ID vers la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***. Les informations utilisateur restent ainsi cohérentes sur les deux plateformes, ce qui facilite la gestion des utilisateurs.

> [!INFO]
> Consultez le [guide d’inscription d’une application Entra](/advanced/entraid/entraid.md) et [la configuration et la vérification de la connexion automatique à Windows](/advanced/entraid/windows-autologin.md).

![micro_entra_id.png](./screenshots/micro_entra_id.png ":size=500")

<!-- >[!IMPORTANT]
>Pour activer **Enable Synchronization** dans Microsoft Entra ID, vous devez désactiver la synchronisation d’Active Directory comme indiqué. -->

> [!CAUTION]
> Assurez-vous de disposer des autorisations appropriées dans Microsoft Entra ID pour activer la synchronisation et sauvegardez toujours les données utilisateur dans la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** avant de commencer le processus.

#### **Étapes pour activer la synchronisation** :

1. **Groupe SASE** : nom d’un groupe dans Microsoft Entra ID auquel appartiennent tous les groupes à synchroniser. Tous les groupes membres de ce groupe (et leurs utilisateurs) seront synchronisés avec la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***.

2. **ID du locataire** : identifiant unique représentant votre organisation Microsoft Entra ID.

3. **ID client** : représente l’inscription de l’application dans Microsoft Entra ID.

4. **Secret client** : mot de passe créé pour l’inscription de l’application dans Microsoft Entra ID. Il sert à authentifier l’application pendant le processus de synchronisation.


>[!TIP]
>Le bouton *Tester la synchronisation* vous permet de vérifier si l’authentification auprès d’EntraID a réussi.
<!-- 

> [!INFO]
> Des instructions détaillées sont disponibles dans la section Avancé [ici](/./advanced/ad_integration/ad_integration.md).

![integration_ad.png](./screenshots/integration_ad.png ":size=800")

> [!IMPORTANT]
>Pour activer **Enable Synchronization** dans Active Directory, vous devez désactiver la synchronisation de Microsoft Entra ID comme indiqué.
 -->
