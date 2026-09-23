File: nativenetworks/virtualinterfaces.md

# ![native_networks](../images/menu/menu_virtualinterfaces.png ':size=25') Interfaces virtuelles

Une interface virtuelle est une connexion réseau logique basée sur un logiciel, qui agit comme un point de terminaison distinct sans nécessiter son propre port matériel physique dédié.

### Créer une interface virtuelle

![create_virtual_interface.png](./screenshots/create_virtual_interface.png ':size=800')


- **Interface**
    - Choisissez le type d’interface. Pour le moment, vous ne pouvez choisir que IPSec.  
    - Choisissez un contrôleur réseau (obligatoire).
    - Saisissez le point de terminaison local et le point de terminaison distant (obligatoire).
- **Sécurité**
    - Choisissez les paramètres IKE. Pour le moment, vous ne pouvez choisir que IKEv2.
    - Choisissez la proposition IKE.
    - Choisissez le mode d’authentification : clé prépartagée ou certificat.
    - Recherchez des propositions ESP ou saisissez une proposition personnalisée (obligatoire).
- **Authentification**
    - Si le mode d’authentification est la clé prépartagée :
        - Saisissez l’ID local et l’ID distant.
        - Saisissez la clé prépartagée (obligatoire).
    - Si le mode d’authentification est le certificat :
        - Saisissez l’ID local.
        - Saisissez l’ID distant (obligatoire).
        - Collez le certificat de l’AC (obligatoire).
        - Collez le certificat local (obligatoire).
        - Collez la clé privée (obligatoire).



### Filtrer les interfaces virtuelles

Vous pouvez rechercher dans la liste des interfaces à l’aide du champ de recherche en haut de la page. Cela vous permet de trouver et de gérer rapidement l’interface recherchée.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher des options de filtrage avancées et définir des conditions supplémentaires en fonction des trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir comment faire correspondre la valeur (`EQUALS`, `CONTAINS` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à faire correspondre, selon la propriété sélectionnée.

![filter_interface.png](./screenshots/filter_interface.png ':size=500')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../../images/icons/icon_filter.png ':size=20'), puis cliquez sur le bouton `+`.

> [!TIP]
> Vous pouvez actualiser la liste des interfaces en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

### Détails de l’interface virtuelle

Cliquez sur la ligne correspondante de l’interface virtuelle pour ouvrir une nouvelle fenêtre contenant deux onglets.

Le premier onglet affiche les détails de l’interface virtuelle :

![details_interface.png](./screenshots/details_interface.png ':size=400')

Le deuxième onglet affiche un fichier journal :

![virtual_interface_log.png](./screenshots/virtual_interface_log.png ':size=400')


### Modifier une interface virtuelle

Vous pouvez modifier une interface virtuelle en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') dans sa ligne.

![update_virtual_interface.png](./screenshots/update_virtual_interface.png ':size=500')


Toutes les options sont identiques à celles de la création d’une interface virtuelle.

### Supprimer une interface virtuelle

![delete_virtual_interface.png](./screenshots/delete_virtual_interface.png ':size=300')
