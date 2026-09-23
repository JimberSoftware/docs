File: nativenetworks/networks.md

# ![native_networks](../images/menu/menu_nativenetworks.png ':size=25') Réseaux

Utilisez la page *Réseaux* pour afficher les réseaux existants et gérer les réseaux natifs directs et routés.

### Liste des réseaux

![networks.png](./screenshots/networks.png ':size=800')

La liste *Réseaux* affiche le nom, le contrôleur réseau, l’adresse réseau, l’état du DHCP et le type.


### Filtrer les réseaux

Vous pouvez rechercher dans la liste des réseaux à l’aide du champ de recherche situé en haut de la page. Cela vous permet de trouver et de gérer rapidement le réseau recherché.

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des réseaux.

À côté du champ de recherche se trouve une icône de filtre. Cliquez dessus pour afficher les options de filtrage avancées, qui vous permettent de définir des conditions supplémentaires en fonction des trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir la manière de faire correspondre la valeur (`EQUALS`, `CONTAINS` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à faire correspondre, selon la propriété sélectionnée.


<!-- You can use the search field, filter button, refresh button, and pagination controls to find the network you need. -->

![networks-filter.png](./screenshots/networks-filter.png ':size=500')

> [!TIP]
> Vous pouvez actualiser la liste des utilisateurs en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page

## Réseaux routés

Cliquez sur `+ Create new` pour ouvrir la fenêtre *Créer un réseau routé*. 
Choisissez le type de réseau à créer : **natif** ou **virtuel**.

<!-- tabs:start -->

### **Créer un réseau natif routé**


>[!NOTE]
>Utilisez cette option lorsque le réseau que vous souhaitez ajouter est accessible via un réseau natif direct existant.

![create-routed-network.png](./screenshots/create-routed-network.png ':size=350')


 Dans la fenêtre *Créer un réseau routé*, renseignez les champs suivants :

 - **Nom** : saisissez un nom explicite pour le réseau.
 - **Contrôleur réseau** : sélectionnez le contrôleur qui gérera le réseau.
 - **Réseau natif (direct)** : sélectionnez le réseau natif directement connecté qui donne accès à ce réseau routé.
 - **Adresse réseau (CIDR)** : saisissez l’adresse du réseau routé au format CIDR.
 - **Prochain saut** : saisissez l’adresse IP de la passerelle menant au réseau routé.

> [!IMPORTANT]
> L’adresse du *Prochain saut* doit être accessible via le *Réseau natif (direct)* sélectionné.

> [!WARNING]
> Assurez-vous que l’adresse réseau et le prochain saut correspondent à votre plan de routage existant afin d’éviter les problèmes de connectivité.


### **Créer un réseau virtuel routé**

![create-virtual-network.png](./screenshots/create-virtual_network.png ':size=350')

Dans la fenêtre *Créer un réseau routé*, renseignez les champs suivants :

 - **Interface virtuelle** : sélectionnez l’interface virtuelle qui gérera le réseau.
 - **Adresse réseau (CIDR)** : saisissez l’adresse du réseau routé au format CIDR.
 

<!-- tabs:end -->



#### Détails d’un réseau natif

 Cliquer sur l’extrémité de la ligne correspondant à un réseau natif ouvre une vue détaillée contenant des informations supplémentaires sur les politiques installées.

![details_native_networks.png](./screenshots/details_native_networks.png ':size=700')


#### Modifier un réseau natif routé

Vous pouvez modifier les réseaux natifs routés en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') dans leur ligne.

![edit_routed_native_network.png](./screenshots/edit_routed_native_network.png ':size=600')

Toutes les options sont identiques à celles disponibles lors de la création d’un réseau natif routé.


<!-- 1. Open *Networks*.
2. Find the routed native network in the table.
3. Click the edit icon in the *Actions* column.
4. Update the same fields that are available in the create window.
5. Save your changes. -->

#### Supprimer un réseau natif routé

 Vous pouvez supprimer les réseaux natifs routés en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') dans leur ligne.


 > [!WARNING]
> Cette opération est irréversible.
 
 Un avertissement s’affiche avant la suppression définitive du réseau :

  ![deleting_routed_network.png](./screenshots/deleting_routed_network.png ':size=300')

### Réseaux natifs directs

Les réseaux natifs directs sont associés à une interface réseau et fournissent la connectivité de base que les réseaux natifs routés peuvent utiliser.

#### Modifier un réseau natif direct


Vous pouvez modifier les réseaux natifs directs en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') dans leur ligne.

![edit-network.png](./screenshots/edit-network.png ':size=600')

Vous pouvez modifier le nom du réseau natif direct. 

<!-- 1. Open *Networks*.
2. Find the direct native network in the table.
3. Click the edit icon in the *Actions* column.
4. If the direct native network is a *LAN* network, enable or disable internet access using the *Allow Internet* toggle.
5. Save your changes. -->

> [!NOTE]
> Si le réseau natif direct est un réseau *LAN*, vous pouvez gérer l’accès à Internet à l’aide de l’option *Autoriser Internet*. Pour les réseaux natifs directs *WAN*, cette option n’est pas affichée.

#### Supprimer un réseau natif direct

Pour supprimer un réseau natif direct, supprimez l’interface réseau associée.

## Résumé

Utilisez la page *Réseaux* pour gérer les segments de réseau logiques que le contrôleur réseau doit router et maintenir, y compris les réseaux natifs **directs** et **routés**.
