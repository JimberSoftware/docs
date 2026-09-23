File: devices/networkcontrollers/networkcontrollers.md

# ![](../../images/menu/menu_networkcontrollers.png ':size=25') Contrôleurs réseau
> [!INFO]
> Les contrôleurs réseau peuvent être dans le cloud ou installés sur site.

Un contrôleur réseau est un équipement réseau qui transfère des paquets de données entre les réseaux. Les contrôleurs réseau jouent un rôle crucial dans la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***. Isoler un réseau signifie en restreindre l’accès aux seules entités de confiance et veiller à empêcher tout accès non autorisé.

> [!INFO]
> Un contrôleur réseau garantit qu’aucune partie de votre réseau, qu’il s’agisse d’un appareil, d’un utilisateur ou d’une application, ne peut accéder à une autre partie sans autorisation explicite.


![network controllers.png](./screenshots/networkcontrollers.png ':size=800')

### Filtrer les contrôleurs réseau

Vous pouvez rechercher un contrôleur réseau dans la liste à l’aide du champ de recherche en haut de la page. Cela vous permet de trouver et de gérer rapidement le contrôleur réseau recherché.

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des contrôleurs réseau.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher les options de filtrage avancées et définir des conditions supplémentaires selon les trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir comment faire correspondre la valeur (`EQUALS`,`CONTAINS`, ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à faire correspondre, selon la propriété sélectionnée.

![filter_nc.png](./screenshots/filter_nc.png ':size=400')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../../images/icons/icon_filter.png ':size=20'), puis cliquez sur le bouton `+`.


> [!TIP]
> Vous pouvez actualiser la liste des contrôleurs réseau en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

### Contrôleur réseau dans le cloud (par défaut)

Chaque entreprise qui utilise la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** dispose **par défaut** d’un contrôleur réseau dans le cloud. Ce contrôleur réseau garantit que tous les appareils et utilisateurs de l’entreprise, aussi bien externes qu’internes, peuvent accéder au réseau de manière sécurisée et cohérente. Le contrôleur réseau dans le cloud sert de point d’entrée et de sortie pour le trafic réseau, en veillant à ce que chacun puisse se connecter et accéder aux ressources nécessaires.

### Contrôleur réseau sur site (facultatif)

L’approche reposant uniquement sur le cloud présente toutefois un inconvénient potentiel. Sans contrôleur réseau sur site, le trafic interne ou sur site est acheminé par Internet, ce qui peut entraîner une latence inutile.

Pour remédier à ce problème, les entreprises peuvent ajouter un contrôleur réseau sur site à leur configuration.

> [!INFO]
> Ainsi, le trafic local reste local et n’est pas acheminé par Internet, ce qui permet d’accélérer les opérations du réseau interne.

##### Types de contrôleurs réseau sur site :
1. **Appliance virtuelle** : contrôleur réseau logiciel pouvant être installé sur une infrastructure virtualisée, ce qui facilite son déploiement, sa mise à l’échelle et sa gestion.
2. **Appliance physique** : équipement matériel installé dans le centre de données ou l’armoire réseau de l’entreprise.

> [!INFO]
> Lorsqu’une mise à jour est disponible pour un contrôleur réseau, une icône de mise à jour verte ![](../../images/icons/icon_update.png ':size=20') apparaît. Cliquez sur l’icône pour lancer la mise à jour.
>
> ![nc_onpremise_update.png](./screenshots/nc_onpremise_update.png ':size=800')

<!-- ## Create on-premise Network Controllers -->
### Créer un contrôleur réseau

Pour ajouter un contrôleur réseau à la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***, cliquez sur le bouton `+ Create new` situé dans le coin supérieur droit de l’interface.

![create_networkcontroller.png](./screenshots/create_networkcontroller.png ':size=400')


Le nom d’hôte et l’adresse du point de terminaison sont obligatoires. Le nom d’hôte ne doit contenir que des lettres, des chiffres et, éventuellement, des traits d’union.

> [!INFO]
> Des instructions détaillées pour l’installation d’un contrôleur réseau sur site sont disponibles [ici](/./advanced/networkcontrollerssetup/SettingUpServer.md).
> La configuration minimale requise pour un contrôleur réseau sur site est la suivante :
>
> **Configuration générale** :
> - Disque dur de 25GB
> **Pour 50 utilisateurs :**
> - 2 CPU
> - 4GB RAM

### Connexion SSH à un contrôleur réseau

![network controllers_1.png](./screenshots/networkcontrollers_1.png ':size=700x40')


En cliquant sur l’icône de cadenas, vous pouvez établir une connexion SSH au contrôleur réseau. Vous recevrez alors un code TOTP que vous pourrez saisir dans la session SSH.

![totp_nc.png](./screenshots/totp_nc.png ':size=500')


<!-- ### Edit on-premise Network Controller -->
### Modifier un contrôleur réseau

 Un contrôleur réseau peut être modifié en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de sa ligne.

![edit_networkcontroller.png](./screenshots/edit_networkcontroller.png ':size=400')


<!-- ### Delete on-premise Network Controllers -->
### Supprimer un contrôleur réseau

 Les contrôleurs réseau peuvent être supprimés en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') de leur ligne.

 Un avertissement s’affiche avant la suppression définitive de l’appareil :

![delete_networkcontroller.png](./screenshots/delete_networkcontroller.png ':size=350')
