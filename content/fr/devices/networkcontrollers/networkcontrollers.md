# ![](../../images/menu/menu_networkcontrollers.png ':size=25') Contrôleurs réseau
> [!INFO]
> Les contrôleurs réseau peuvent être hébergés dans le cloud ou installés sur site.

Un contrôleur réseau est un équipement réseau qui achemine des paquets de données au sein du réseau. Les contrôleurs réseau jouent un rôle essentiel dans la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***. Isoler un réseau consiste à en restreindre l'accès aux seules entités de confiance et à empêcher tout accès non autorisé.

> [!INFO]
> Un contrôleur réseau garantit qu'aucune partie de votre réseau, qu'il s'agisse d'un appareil, d'un utilisateur ou d'une application, ne peut accéder à une autre partie sans autorisation explicite.


![network controllers.png](./screenshots/networkcontrollers.png ':size=800')

### Filtrer les contrôleurs réseau

Vous pouvez rechercher des contrôleurs réseau à l'aide du champ de recherche situé en haut de la page. Cela vous permet de trouver rapidement le contrôleur réseau recherché et de le gérer.

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des contrôleurs réseau.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher des options de filtrage avancées qui vous permettent de définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : menu déroulant permettant de choisir le champ sur lequel effectuer le filtrage.
- **Type de correspondance** : menu déroulant permettant de choisir comment faire correspondre la valeur (`is`, `contains` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur à faire correspondre, en fonction de la propriété sélectionnée.

![filter_nc.png](./screenshots/filter_nc.png ':size=400')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l'icône de filtre ![](../../images/icons/icon_filter.png ':size=20'), puis cliquez sur le bouton `+`.


> [!TIP]
> Vous pouvez actualiser la liste des contrôleurs réseau en cliquant sur l'icône d'actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

### Contrôleur réseau cloud (par défaut)

Toute entreprise utilisant la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** disposera **par défaut** d'un contrôleur réseau cloud. Ce contrôleur réseau garantit que tous les appareils et utilisateurs de l'entreprise, qu'ils soient internes ou externes, peuvent accéder au réseau de manière sécurisée et cohérente. Le contrôleur réseau cloud sert de point d'entrée et de sortie pour le trafic réseau. Il permet à chacun de se connecter et d'accéder aux ressources nécessaires.

### Contrôleur réseau sur site (facultatif)

Toutefois, l'approche reposant uniquement sur le cloud peut présenter un problème. En l'absence d'un contrôleur réseau sur site, le trafic interne ou sur site est acheminé via Internet, ce qui peut entraîner une latence inutile.

Pour répondre à cette préoccupation, les entreprises peuvent ajouter un contrôleur réseau sur site à leur configuration.

> [!INFO]
> Cela garantit que le trafic local reste local et n'est pas acheminé via Internet, ce qui accélère les opérations du réseau interne.

##### Types de contrôleurs réseau sur site :
1. **Appliance virtuelle** : contrôleur réseau logiciel pouvant être installé sur une infrastructure virtualisée, ce qui en facilite le déploiement, la mise à l'échelle et la gestion.
2. **Appliance physique** : équipement matériel installé dans le centre de données ou l'armoire réseau de l'entreprise.

> [!INFO]
> Lorsqu'une mise à jour est disponible pour un contrôleur réseau, une icône de mise à jour verte ![](../../images/icons/icon_update.png ':size=20') apparaît. Cliquez sur l'icône pour lancer la mise à jour.
>
> ![nc_onpremise_update.png](./screenshots/nc_onpremise_update.png ':size=800')

<!-- ## Create on-premise Network Controllers -->
### Créer un contrôleur réseau

Pour ajouter un contrôleur réseau à la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***, cliquez sur le bouton `+ Create new` situé dans le coin supérieur droit de l'interface.

![create_networkcontroller.png](./screenshots/create_networkcontroller.png ':size=400')


Le nom d'hôte et l'adresse du point de terminaison sont obligatoires. Le nom d'hôte ne doit contenir que des lettres, des chiffres et, éventuellement, des traits d'union.

> [!INFO]
> Vous trouverez [ici](/./advanced/networkcontrollerssetup/SettingUpServer.md) des instructions détaillées pour installer un contrôleur réseau sur site.
> La configuration minimale requise pour un contrôleur réseau sur site est la suivante :
>
> **Général** :
> - Disque dur de 25GB
> **Pour 50 utilisateurs :**
> - 2 CPU
> - 4GB RAM

### Connexion SSH à un contrôleur réseau

![network controllers_1.png](./screenshots/networkcontrollers_1.png ':size=700x40')


En cliquant sur l'icône de cadenas, vous pouvez établir une connexion SSH au contrôleur réseau. Vous recevrez alors un code TOTP à saisir dans la session SSH.

![totp_nc.png](./screenshots/totp_nc.png ':size=500')


<!-- ### Edit on-premise Network Controller -->
### Modifier un contrôleur réseau

 Vous pouvez modifier un contrôleur réseau en cliquant sur l'icône de modification ![](../../images/icons/icon_edit.png ':size=20') dans sa ligne.

![edit_networkcontroller.png](./screenshots/edit_networkcontroller.png ':size=400')


<!-- ### Delete on-premise Network Controllers -->
### Supprimer un contrôleur réseau

 Vous pouvez supprimer un contrôleur réseau en cliquant sur l'icône de suppression ![](../../images/icons/icon_delete.png ':size=20') dans sa ligne.

 Un avertissement s'affichera avant la suppression définitive de l'appareil :

![delete_networkcontroller.png](./screenshots/delete_networkcontroller.png ':size=350')
