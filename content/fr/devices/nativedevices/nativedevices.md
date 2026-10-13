File: devices/nativedevices/nativedevices.md

# ![](../../images/menu/menu_nativedevices.png ':size=25') Appareils natifs

Les appareils natifs peuvent être tous les appareils réseau accessibles via un contrôleur réseau. Une fois qu’un appareil natif a été créé, des règles peuvent lui être appliquées de la même manière que pour les serveurs et les NIAC. Bien que le trafic vers les appareils natifs ne soit pas chiffré au niveau réseau, ils peuvent néanmoins constituer un moyen sûr d’accéder à des appareils accessibles uniquement via le contrôleur réseau, en accordant au contrôleur réseau l’accès à un VLAN spécifique.

<!--Bien que le trafic vers les appareils natifs ne soit pas chiffré au niveau réseau, ils peuvent constituer un moyen sûr d’accéder à des appareils accessibles uniquement via le contrôleur réseau, en connectant le contrôleur réseau à un VLAN spécifique ou en lui donnant accès à ce VLAN.-->

Par exemple, si une caméra IP se trouve dans le VLAN des caméras et que certains utilisateurs doivent pouvoir y accéder, vous pouvez enregistrer l’adresse IP de la caméra en tant qu’appareil natif auprès du contrôleur réseau sur site. En configurant les règles d’accès appropriées, les utilisateurs pourront alors accéder à la caméra depuis n’importe quel endroit via la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***.

![scheme1.png](./screenshots/scheme1.png)



### Créer un appareil natif
Pour créer un nouvel appareil natif dans la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***, cliquez sur le bouton `+ Create new` situé dans le coin supérieur droit de l’interface.

![create_native.png](./screenshots/create_native.png ':size=400')
                    
Le nom d’hôte est obligatoire et doit être alphanumérique. L’adresse IP et le contrôleur réseau sont également requis.

Sélectionnez le contrôleur réseau approprié et saisissez une adresse IP valide.

<!-- > [!IMPORTANT] 
> Une fois l’appareil natif créé, l’administrateur doit ajouter une règle [Autoriser un port personnalisé](/./rules/customports/customports.md) qui donne à des groupes spécifiques accès à l’appareil natif (en tant que destination). -->
<!-- Nous ajoutons maintenant une nouvelle règle « Autoriser un port personnalisé » permettant au groupe testers77 d’envoyer un ping à l’appareil natif appelé « Websitetest ». 
 
 ![allow_custom_ports_2.png](./screenshots/allow_custom_ports_2.png ':size=800')
 
 Aucun autre groupe ne peut accéder à l’appareil natif, sauf si l’accès est explicitement autorisé en ajoutant une nouvelle règle « Autoriser un port personnalisé ».

> [!INFO] 
> Vous pouvez également ajouter des services d’attribut.

Choisissez l’appareil natif comme « Destination ».

![add_attr_services.png](./screenshots/add_attr_services.png ':size=800')
 -->

> [!IMPORTANT] 
> Une fois l’appareil natif créé, l’administrateur doit ajouter une [Politique](./rules/firewall-policies/firewall-policies) qui donne à des groupes spécifiques accès à l’appareil natif.

 **Par exemple :**

 Nous créons un appareil natif « Websitetest » :

![example_native_device.png](./screenshots/example_native_device.png ':size=700')

 Nous ajoutons maintenant une nouvelle [Politique](./rules/firewall-policies/firewall-policies) :
 - **Destinations** : nom de l’appareil natif.
 - **Sources** : groupes auxquels vous souhaitez accorder l’accès à l’appareil natif.
 - **Services** : [services](./rules/services/services) qui créent des règles d’accès définissant le port de début, le port de fin et le protocole utilisé par le service pour communiquer.

 ![policy_for_nd.png](./screenshots/policy_for_nd.png ':size=700')

 ![create_service_for_nd.png](./screenshots/create_service_for_nd.png ':size=700')
 
 >[!ATTENTION]Aucun autre groupe ne peut accéder à l’appareil natif, sauf si l’accès est explicitement autorisé en ajoutant un groupe comme nouvelle source.



### Détails d’un appareil natif

Cliquez sur la ligne correspondant à un appareil pour ouvrir une vue détaillée comportant deux onglets : Détails et Sécurité.  

L’onglet Détails fournit des informations supplémentaires.
 
![details_native.png](./screenshots/details_native.png ':size=500')

L’onglet Services présente un aperçu des services associés.

![services_native.png](./screenshots/services_native.png ':size=500')

### Filtrer les appareils natifs

Vous pouvez rechercher des appareils natifs dans la liste à l’aide du champ de recherche situé en haut de la page. Cela vous permet de trouver et de gérer rapidement l’appareil natif recherché.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher des options de filtrage avancées et définir des conditions supplémentaires selon les trois éléments suivants :

- **Propriété** : menu déroulant permettant de choisir le champ à filtrer.
- **Type de correspondance** : menu déroulant permettant de sélectionner le type de correspondance (`is`, `contains` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur recherchée, selon la propriété choisie.

![filter_nd.png](./screenshots/filter_nd.png ':size=500')

Pour ajouter plusieurs filtres, cliquez de nouveau sur l’icône de filtre ![](../../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

> [!TIP]
> Vous pouvez actualiser la liste des appareils natifs en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.


### Modifier un appareil natif
  
 Vous pouvez modifier un appareil natif en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de sa ligne.
 
  ![edit_native.png](./screenshots/edit_native.png ':size=400')

   
### Supprimer un appareil natif

 Vous pouvez supprimer un appareil natif en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') de sa ligne.
 
 Un avertissement s’affichera avant la suppression définitive de l’appareil :
 
 ![delete_native.png](./screenshots/delete_native.png ':size=400')
