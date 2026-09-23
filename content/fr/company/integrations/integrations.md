# ![](../../images/menu/menu_integrations.png ':size=25') Intégrations

<!-- ## Credentials: API Key

API keys are a way to authenticate and grant access to various resources of an application or platform via its API. They are typically used to facilitate the interaction of third-party software with your application, enabling automation, integration, and other advanced functionalities.

![api_key.png](api_key.png) -->


## DNS

Un redirecteur DNS redirige les requêtes DNS d’un serveur vers un autre. Il est utile pour gérer et accélérer les requêtes DNS en redirigeant les demandes vers un serveur DNS plus rapide ou plus à jour que celui défini par défaut.
Pour ce faire, saisissez l’adresse IP du serveur DNS et cliquez sur le bouton Appliquer.

![dns_forwarder.png](./screenshots/dns_forwarder.png ":size=500")



## Microsoft Entra ID

Synchronisez facilement vos données utilisateur depuis Microsoft Entra ID vers la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***. Les informations utilisateur restent ainsi cohérentes sur les deux plateformes, ce qui facilite la gestion des utilisateurs.

> [!INFO]
> Des instructions détaillées sont disponibles dans la section Avancé [ici](/./advanced/entraid/entraid.md).

![micro_entra_id.png](./screenshots/micro_entra_id.png ":size=500")

<!-- >[!IMPORTANT]
>To activate **Enable Synchronization** in Microsoft Entra ID, you have to disable Active Directory syncing as indicated. -->

> [!CAUTION]
> Assurez-vous de disposer des autorisations appropriées dans Microsoft Entra ID pour activer la synchronisation et sauvegardez toujours les données utilisateur de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** avant de lancer le processus.

#### **Étapes pour activer la synchronisation** :

1. **Groupe SASE** : nom d’un groupe dans Microsoft Entra ID auquel appartiennent tous les groupes à synchroniser. Tous les groupes membres de ce groupe (ainsi que leurs utilisateurs) seront synchronisés avec la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***.

2. **ID du locataire** : identifiant unique qui représente votre organisation Microsoft Entra ID.

3. **ID client** : représente l’inscription de l’application dans Microsoft Entra ID.

4. **Secret client** : mot de passe créé pour l’inscription de l’application dans Microsoft Entra ID. Il est utilisé pour authentifier l’application pendant le processus de synchronisation.


>[!TIP]
>Le bouton *Tester la synchronisation* vous permet de vérifier si l’authentification avec EntraID a réussi.
<!-- 

> [!INFO]
> Detailed instructions are available in the Advanced section [here](/./advanced/ad_integration/ad_integration.md).

![integration_ad.png](./screenshots/integration_ad.png ":size=800")

> [!IMPORTANT]
>To activate **Enable Synchronization** in Active Directory, you have to disable Microsoft Entra ID syncing as indicated.
 -->
