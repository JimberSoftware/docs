File: devices/nativedevices/nativedevices.md

# ![](../../images/menu/menu_nativedevices.png ':size=25') Appareils natifs

Les appareils natifs peuvent être n’importe quels appareils réseau accessibles via un contrôleur réseau. Une fois un appareil natif créé, des règles peuvent lui être appliquées de la même manière qu’aux serveurs et aux NIAC. Bien que le trafic vers les appareils natifs ne soit pas chiffré au niveau réseau, ils peuvent tout de même constituer un moyen sûr d’accéder aux appareils accessibles uniquement via le contrôleur réseau, en accordant au contrôleur réseau l’accès à un VLAN spécifique.

<!--While traffic to Native Devices is not encrypted on the network layer, they can be a safe way to reach devices that are only reachable by the Network Controller by connecting or giving access to the Network Controller to a specific VLAN.-->

Par exemple, si une caméra IP se trouve dans le VLAN des caméras et que des utilisateurs spécifiques doivent y accéder, vous pouvez enregistrer l’adresse IP de la caméra comme appareil natif auprès du contrôleur réseau sur site. En définissant les règles d’accès appropriées, les utilisateurs pourront alors accéder à la caméra depuis n’importe quel emplacement via la ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***.

![scheme1.png](./screenshots/scheme1.png)



### Créer un appareil natif
Pour créer un appareil natif dans la ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***, cliquez sur le bouton `+ Create new` situé dans le coin supérieur droit de l’interface.

![create_native.png](./screenshots/create_native.png ':size=400')
                    
Le nom d’hôte est obligatoire et doit être alphanumérique. L’adresse IP et le contrôleur réseau sont également obligatoires.

Sélectionnez le contrôleur réseau approprié et saisissez une adresse IP valide.

<!-- > [!IMPORTANT] 
> Once the Native Device is created, the admin needs to add a [Allow Custom Port](/./rules/customports/customports.md) rule that gives specific groups access to the Native Device (under destination). -->
<!-- Now we add a new 'Allow Custom Port' rule where group testers77 can ping the native device called 'Websitetest'. 
 
 ![allow_custom_ports_2.png](./screenshots/allow_custom_ports_2.png ':size=800')
 
 All other groups can't reach the Native Device unless specifically allowed by adding a new 'Allow Custom Port' rule.

> [!INFO] 
> You can also add attribute services. 

Choose the Native Device as 'Destination'.

![add_attr_services.png](./screenshots/add_attr_services.png ':size=800')
 -->

> [!IMPORTANT] 
> Une fois l’appareil natif créé, l’administrateur doit ajouter une [politique](./rules/firewall-policies/firewall-policies) qui accorde à des groupes spécifiques l’accès à l’appareil natif.

 **Par exemple :**

 Nous créons un appareil natif « Websitetest » :

![example_native_device.png](./screenshots/example_native_device.png ':size=700')

 Nous ajoutons maintenant une nouvelle [politique](./rules/firewall-policies/firewall-policies) :
 - **Destinations** : nom de l’appareil natif.
 - **Sources** : groupes auxquels vous souhaitez accorder l’accès à l’appareil natif.
 - **Services** : [services](./rules/services/services) qui créent des règles d’accès définissant le port de début et le port de fin, ainsi que le protocole utilisé par le service pour communiquer.

 ![policy_for_nd.png](./screenshots/policy_for_nd.png ':size=700')

 ![create_service_for_nd.png](./screenshots/create_service_for_nd.png ':size=700')
 
 >[!ATTENTION]Tous les autres groupes ne peuvent pas accéder à l’appareil natif, sauf si l’accès leur est explicitement autorisé en ajoutant un groupe comme nouvelle source.



### Détails d’un appareil natif

Cliquer sur la ligne correspondante d’un appareil ouvre une vue détaillée comportant deux onglets : Détails et Sécurité.  

L’onglet Détails fournit des informations supplémentaires.
 
![details_native.png](./screenshots/details_native.png ':size=500')

L’onglet des services présente une vue d’ensemble des services associés.

![services_native.png](./screenshots/services_native.png ':size=500')

### Filtrer les appareils natifs

Vous pouvez rechercher des appareils natifs dans la liste à l’aide du champ de recherche situé en haut de la page. Cela vous permet de trouver et de gérer rapidement l’appareil natif recherché.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Lorsque vous cliquez dessus, des options de filtrage avancées s’affichent. Vous pouvez alors définir des conditions supplémentaires selon les trois éléments suivants :

- **Propriété** : menu déroulant permettant de choisir le champ à filtrer.
- **Type de correspondance** : menu déroulant permettant de choisir comment faire correspondre la valeur (`EQUALS`, `CONTAINS` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à faire correspondre, selon la propriété sélectionnée.

![filter_nd.png](./screenshots/filter_nd.png ':size=500')

Pour ajouter plusieurs filtres, cliquez de nouveau sur l’icône de filtre ![](../../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

> [!TIP]
> Vous pouvez actualiser la liste des appareils natifs en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.


### Modifier un appareil natif
  
 Vous pouvez modifier un appareil natif en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de sa ligne.
 
  ![edit_native.png](./screenshots/edit_native.png ':size=400')

   
### Supprimer un appareil natif

 Vous pouvez supprimer un appareil natif en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') de sa ligne.
 
 Un avertissement s’affiche avant la suppression définitive de l’appareil :
 
 ![delete_native.png](./screenshots/delete_native.png ':size=400')
