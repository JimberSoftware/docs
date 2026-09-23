# ![](../../images/menu/menu_niacs.png ':size=25') Client d'accès à l'isolation réseau - NIAC

Un client d'accès à l'isolation réseau (NIAC) est un appareil matériel spécialisé conçu pour établir des connexions réseau sécurisées. Il peut être intégré à un large éventail d'appareils, notamment des imprimantes, des caméras IP, des disques durs et des machines industrielles. En servant de passerelle distincte pour ces appareils, les NIAC améliorent leur accessibilité et garantissent que toutes les données en transit restent chiffrées pour une sécurité optimale.


![niacs.png](./screenshots/niacfront.png ':size=300')
 

![niacs.png](./screenshots/niacback.png ':size=300')


Un NIAC dispose de quatre ports : un port WAN pour la connexion Internet, deux ports LAN et un port USB. Le port USB n'est actuellement pas pris en charge ; seuls les appareils réseau peuvent donc être connectés.
Un port LAN sert généralement à connecter des appareils locaux au sein d'un réseau. Voici quelques exemples d'appareils pouvant être connectés à un port LAN :
- Ordinateurs (de bureau, portables)
- Téléviseurs intelligents
- Périphériques de stockage réseau (NAS)
- Imprimantes réseau
- ...

Une fois un appareil connecté, vous pouvez voir l'adresse IP qui lui a été attribuée via DHCP dans l'aperçu du NIAC. Dans cet aperçu, vous pouvez également supprimer un appareil et activer ou désactiver le mode sécurisé. 


![niac_overview.png](./screenshots/niac_overview.png ':size=800')

> [!INFO]
> Si vous êtes un client final et souhaitez intégrer des NIAC à vos appareils, veuillez contacter l'intégrateur qui vous a été attribué. 

> [!INFO]
> Si vous êtes un intégrateur et avez besoin de NIAC, vous pouvez contacter votre distributeur ou joindre directement Jimber par e-mail à l'adresse security@jimber.io.

### Créer un NIAC

> [!WARNING]
> Seuls les super administrateurs de Jimber peuvent créer un NIAC.

Pour créer un NIAC sur la plateforme, cliquez sur le bouton `+ Create new` situé dans le coin supérieur droit de l'interface.


![create_niac.png](./screenshots/create_niac.png ':size=400')

> [!INFO]
> Le nom d'hôte doit être une chaîne en minuscules.



<!-- ![group_details_niac.png](/group_details_niac.png ':size=600') -->

### Filtrer les NIAC

Vous pouvez rechercher dans la liste des NIAC à l'aide du champ de recherche situé en haut de la page. Cela vous permet de trouver et de gérer rapidement le NIAC recherché.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Lorsque vous cliquez dessus, des options de filtrage avancées s'affichent et vous permettent de définir des conditions supplémentaires selon les trois éléments suivants :

- **Propriété** : menu déroulant permettant de choisir le champ à filtrer.
- **Type de correspondance** : menu déroulant permettant de sélectionner la manière dont la valeur doit correspondre (`EQUALS`, `CONTAINS` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur recherchée, selon la propriété sélectionnée.


![filter_niac.png](./screenshots/filter_niac.png ':size=600')

Pour ajouter plusieurs filtres, vous pouvez cliquer de nouveau sur l'icône de filtre ![](../../images/icons/icon_filter.png ':size=20'), puis cliquer sur le bouton `+`.


> [!TIP]
> Vous pouvez actualiser la liste des NIAC en cliquant sur l'icône d'actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

### Examiner un NIAC

Cliquez sur la ligne correspondante du NIAC pour ouvrir une nouvelle fenêtre. Le premier onglet fournit plus de détails, tandis que le deuxième onglet présente un aperçu des politiques liées au NIAC :

![niac_details.png](./screenshots/niac_details.png ':size=500')

![niac_details_security.png](./screenshots/niac_details_security.png ':size=500')


- #### Libérer un appareil
Vous pouvez libérer l'un des appareils connectés au NIAC en cliquant sur l'icône de cadenas rouge ![](../../images/icons/icon_lock.png ':size=20') de sa ligne.

  ![deleting_dhcp_lease.png](./screenshots/deleting_dhcp_lease.png ':size=400')

- #### Mettre à jour un appareil
Vous pouvez ajouter ou supprimer des alias pour un appareil en cliquant sur l'icône de modification ![](../../images/icons/icon_edit.png ':size=20') de sa ligne.

  ![update_device.png](./screenshots/update_device.png ':size=400')

>[!ATTENTION]
> Pour ajouter un alias, saisissez le nom et appuyez sur **Entrée ou la barre d'espace** **_avant_** de cliquer sur Submit.

> [!WARNING]
> Un appareil connecté à un NIAC ne pourra pas accéder à Internet, sauf si le NIAC est membre d'un groupe pour lequel la passerelle WAN est activée. Par exemple : si un NIAC est membre du groupe WanGateway et que WAN GATEWAY est activé pour ce groupe dans Configuration de groupe, l'appareil connecté pourra accéder à Internet. Des instructions détaillées sur la Configuration de groupe sont disponibles [ici](./rules/groupconfiguration/groupconfiguration.md).


![group_config.png](./screenshots/group_config.png ':size=800') 


### Modifier un NIAC

Vous pouvez modifier les NIAC en cliquant sur l'icône de modification ![](../../images/icons/icon_edit.png ':size=20') de leur ligne.

![edit_niac.png](./screenshots/edit_niac.png ':size=400')

### Supprimer un NIAC

Vous pouvez supprimer les NIAC en cliquant sur l'icône de suppression ![](../../images/icons/icon_delete.png ':size=20') de leur ligne.

Un avertissement s'affichera avant la suppression définitive du NIAC :
 
![delete_niac.png](./screenshots/delete_niac.png ':size=400')
