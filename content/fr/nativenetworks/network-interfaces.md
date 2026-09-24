# ![native_networks](../images/menu/menu_networkinterfaces.png ':size=25') Interfaces réseau

Utilisez la page *Interfaces réseau* pour connecter des ports physiques et des VLAN à vos réseaux natifs.

### Liste des interfaces réseau

Vous pouvez rechercher des interfaces réseau à l’aide du champ de recherche situé en haut de la page.

![network-interfaces.png](./screenshots/network-interfaces.png ':size=700')

Le tableau comprend la description de l’interface, le rôle WAN ou LAN, le port, le contrôleur réseau, l’adresse et le mode d’adressage.

### Filtrer les interfaces réseau

Utilisez le champ de recherche pour saisir des mots-clés et filtrer la liste des interfaces réseau.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Lorsque vous cliquez dessus, des options de filtrage avancées s’affichent. Elles vous permettent de définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir comment la valeur doit correspondre (`EQUALS`, `CONTAINS` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à rechercher, selon la propriété sélectionnée.

![filter_native_networks.png](./screenshots/filter_native_networks.png ':size=500')

Pour ajouter plusieurs filtres, cliquez de nouveau sur l’icône de filtre ![](../../images/icons/icon_filter.png ':size=20'), puis cliquez sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters.png ':size=700')

> [!TIP]
> Vous pouvez actualiser la liste des utilisateurs en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.


### Créer une interface réseau

Pour créer une interface réseau sur la plateforme, cliquez sur le bouton `+ Create new` situé dans le coin supérieur droit de l’interface.

![create-network-interface.png](./screenshots/create-network-interface.png ':size=700')

Sur la page *Créer une interface réseau*, remplissez la section *Interface* :

- **Description** : saisissez un libellé clair pour l’interface.
- **VLAN** : choisissez *Non balisé* pour le trafic par défaut sur le port, ou **Balisé** pour le trafic sur un VLAN spécifique.
    -   Si vous sélectionnez *Balisé*, saisissez l’*ID du VLAN*.
- **Contrôleur réseau** : sélectionnez le contrôleur réseau sur site qui gérera l’interface.
- **WAN/LAN** : choisissez si l’interface est utilisée pour le trafic WAN ou LAN.
- **Port** : sélectionnez le port physique du contrôleur réseau.
- **DHCP/Statique** : choisissez comment l’interface obtient son adresse IP.
- Si vous avez sélectionné **Statique**, remplissez la section *Statique* :
    - **Adresse IP (CIDR)** : saisissez l’adresse IP de l’interface au format CIDR, par exemple *192.168.1.1/24*.
    - **Adresse IP de la passerelle** : saisissez l’adresse IP de la passerelle.
- Si vous avez sélectionné **DHCP**, la section Statique n’est pas disponible :


 ![static_not_available.png](./screenshots/static_not_available.png ':size=700')


> [!NOTE]
> N’oubliez pas de cliquer sur **Envoyer**



### Mettre à jour une interface réseau

 Les interfaces réseau peuvent être modifiées en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de leur ligne.

![edit-network-interfaces.png](./screenshots/edit-network-interfaces.png ':size=700')

Toutes les options sont les mêmes que lors de la création d’une interface réseau.


> [!IMPORTANT]
> Si vous modifiez l’*Adresse IP (CIDR)* ou l’*Adresse IP de la passerelle*, le serveur DHCP de ce réseau sera automatiquement désactivé afin d’éviter une configuration non valide. Vous pourrez le réactiver ultérieurement depuis la page [Serveur DHCP](./dhcp-server.md).

### Supprimer une interface réseau

Les interfaces réseau peuvent être supprimées en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') de leur ligne.

Un avertissement s’affichera avant la suppression définitive de l’utilisateur :

![delete-network-interface.png](./screenshots/delete-network-interface.png ':size=400')


> [!IMPORTANT]
> La suppression d’une interface réseau supprime également le réseau associé. Cette action est irréversible.

> [!WARNING]
> Soyez prudent lorsque vous modifiez ou supprimez des interfaces actives, car ces paramètres affectent la connectivité réseau en temps réel.


### Conseils concernant les VLAN et l’adressage

- Utilisez *Non balisé* lorsque l’interface doit transporter le trafic par défaut d’un port.
- Utilisez *Balisé* lorsque l’interface doit être associée à un VLAN spécifique.
- Utilisez *DHCP* lorsque l’interface doit recevoir automatiquement son adresse.
- Utilisez *Statique* lorsque l’interface doit utiliser une configuration IP fixe.

## Résumé

Utilisez la page *Interfaces réseau* pour définir comment le trafic WAN et LAN entre dans le contrôleur réseau sur site et en sort.
