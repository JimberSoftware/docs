File: company/customers/customers.md

# ![](../../images/menu/menu_customers.png ':size=25') Clients
> [!WARNING]
> Cette section *Clients* est exclusivement réservée aux **partenaires**. Si vous êtes un client final, vous serez directement redirigé vers la configuration de votre entreprise dans ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***.

Sur notre plateforme, un **client** désigne une entreprise qui souhaite utiliser ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***. Les intégrateurs peuvent gérer ces clients afin de garantir le bon déroulement des opérations et la prestation des services.

Pour plus de clarté, prenons l’exemple d’une entreprise nommée *`Astral Voyage`* qui souhaite utiliser ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***. Vous devez d’abord créer *`Astral Voyage`* en tant que client sur la plateforme avant de pouvoir procéder à toute autre configuration ou prestation de service.

![list_customers.png](./screenshots/list_customers.png ':size=800')

### Créer un client

Pour ajouter un nouveau client à la plateforme, cliquez sur le bouton `+ Create new` situé dans le coin supérieur droit de l’interface.

Selon le forfait choisi, quelques autres options sont à prendre en compte :

<!-- tabs:start -->

# **SASE**


_![create_customer.png](./screenshots/create_customer_SASE.png ':size=350')_


- Les champs suivants sont obligatoires :	
    - Nom. 
    - Nom d’affichage. Le nom d’affichage peut contenir des lettres et des chiffres.
    - Adresse e-mail du contact principal.
- Activez **_Provision Cloud Controller_** lorsqu’un contrôleur réseau doit être provisionné.
- Activez **_Enable ZTO_** pour utiliser Zero Trust Outbound. 
  
<!-- - Options à déterminer :

    - Quel forfait choisir : SASE, ViPN ou SSE ?
    - Activez ***Provision Cloud Controller*** lorsqu’un contrôleur réseau doit être provisionné. -->

- Le renseignement du site web fera apparaître une icône devant le nom du client.


# **ViPN**


_![create_customer.png](./screenshots/create_customer_ViPN.png ':size=350')_


- Les champs suivants sont obligatoires :	
    - Nom. 
    - Nom d’affichage. Le nom d’affichage peut contenir des lettres et des chiffres.
    - Adresse e-mail du contact principal.
  
<!-- - Options à déterminer :

    - Quel forfait choisir : SASE, ViPN ou SSE ?
    - Activez ***Provision Cloud Controller*** lorsqu’un contrôleur réseau doit être provisionné. -->

- Le renseignement du site web fera apparaître une icône devant le nom du client.

# **SSE**


_![create_customer.png](./screenshots/create_customer_SSE.png ':size=350')_


- Les champs suivants sont obligatoires :	
    - Nom. 
    - Nom d’affichage. Le nom d’affichage peut contenir des lettres et des chiffres.
    - Adresse e-mail du contact principal.
- Activez **_Enable ZTO_** pour utiliser Zero Trust Outbound. 
  
<!-- - Options à déterminer :

    - Quel forfait choisir : SASE, ViPN ou SSE ?
    - Activez ***Provision Cloud Controller*** lorsqu’un contrôleur réseau doit être provisionné. -->

- Le renseignement du site web fera apparaître une icône devant le nom du client.

<!-- tabs:end -->

> [!WARNING]
> Le nom ne peut contenir que des lettres et des chiffres. Les espaces, caractères spéciaux et symboles ne sont pas autorisés.
>
> Vous pouvez toutefois utiliser ces caractères dans le champ Nom d’affichage.




### Filtrer les clients

Vous pouvez rechercher des clients dans la liste à l’aide du champ de recherche situé en haut de la page. Cela vous permet de trouver et de gérer rapidement le client recherché.


- Utilisez le champ de recherche pour saisir des mots-clés et filtrer la liste des clients.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Lorsque vous cliquez dessus, des options de filtrage avancées s’affichent. Elles vous permettent de définir des conditions supplémentaires selon les trois éléments suivants :

- **Propriété** : menu déroulant permettant de choisir le champ sur lequel appliquer le filtre.
- **Type de correspondance** : menu déroulant permettant de choisir comment faire correspondre la valeur (`EQUALS`, `CONTAINS` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à faire correspondre, selon la propriété sélectionnée.

![filter_customer.png](./screenshots/filter_customer.png ':size=400' )

Vous pouvez appuyer sur le bouton `+` pour ajouter plusieurs filtres.


> [!TIP]
> Vous pouvez actualiser la liste des clients en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

### Détails du client

Cliquez sur la ligne correspondant à un client pour ouvrir une vue détaillée contenant des informations supplémentaires.

Vous obtenez un aperçu des ressources créées, de l’activité récente et des appareils en attente d’approbation :

![overview_customer.png](./screenshots/overview_customer.png ':size=700')

> [!NOTE]
> Un client nouvellement créé n’a pas encore de ressources à afficher.

Si aucun contrôleur cloud n’est démarré, un avertissement vous indique que vous devez en démarrer un pour activer la connectivité SASE :

![warning_cloudcontroller.png](./screenshots/warning_cloudcontroller.png ':size=600')

![start_networkcontroller.png](./screenshots/start_networkcontroller.png ':size=600')

### Modifier un client
Vous pouvez modifier les clients en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de leur ligne.

![edit_customer.png](./screenshots/edit_customer.png ':size=350')

> [!CAUTION]
> Un message vous indiquera que le changement de partenaire supprimera tous les rôles de consultant en sécurité actuels.



### Supprimer un client

Vous pouvez supprimer les clients en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') de leur ligne.

> [!WARNING]
> Toutes les ressources du client seront supprimées lors de sa suppression. Cette opération est irréversible.

Un avertissement s’affichera avant la suppression définitive du client :

![delete_customer.png](./screenshots/delete_customer.png ':size=400') 

<!-- Si `Provision Cloud Controller` est toujours activé, un avertissement s’affichera et vous ne pourrez pas supprimer le client :

![provisioned_nc.png](./screenshots/provisioned_nc.png ':size=250') -->
