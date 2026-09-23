File: company/users/users.md

# ![](../../images/menu/menu_users.png ':size=25') Utilisateurs

Un utilisateur désigne un compte individuel au sein de la plateforme. Les utilisateurs peuvent avoir des rôles et être associés aux propriétés de différents produits.


> [!IMPORTANT]
> Une gestion efficace des utilisateurs est essentielle pour préserver la sécurité et l’intégrité de votre plateforme. 


### Créer un utilisateur
Pour créer un utilisateur sur la plateforme, cliquez sur le bouton `+ Create new` situé dans le coin supérieur droit de l’interface.

> [!WARNING]
> Pour créer un nouvel utilisateur, l’entreprise **doit** d’abord ajouter un domaine. L’adresse e-mail de l’utilisateur doit correspondre au domaine ajouté. Vous trouverez plus d’informations sur les domaines [ici](/company/domains/domains.md).

L’**adresse e-mail** est utilisée comme identifiant principal d’un utilisateur. Elle est essentielle à des fins d’authentification. Veillez à ce que l’adresse e-mail fournie soit valide et accessible à l’utilisateur. 

![create_user.png](./screenshots/create_user.png ':size=400')


<!-- > [!WARNING]
>  Notez que le nom d’utilisateur ne peut pas être modifié après la création de l’utilisateur. -->

#### Rôles des utilisateurs et autorisations

- **Administrateur** :
  - Activez cette option pour attribuer le rôle d’administrateur à un utilisateur.
  - Permet à l’utilisateur de se connecter à la plateforme de sécurité.
  - Accorde des privilèges pour gérer les paramètres de l’entreprise.
 
<!-- - **Isolation réseau** 
  - Activez cette option pour activer l’`Network Isolation` pour cet utilisateur, en ajoutant une couche de sécurité supplémentaire.
  - Lorsque l’isolation réseau est activée, des groupes peuvent être sélectionnés. Pour plus d’informations sur les groupes, cliquez [ici](/./company/groups/groups.md). -->

- **Activer le mode sécurisé** :
  - Activez cette option pour activer le mode sécurisé.
  - Si le mode sécurisé est ACTIVÉ pour un appareil, tout le trafic entrant sera bloqué, sauf s’il provient de la **_Plateforme Jimber SASE_** :

  ![secure_mode_warning.png](./screenshots/secure_mode_warning.png ':size=400')



### Créer des consultants en sécurité

Pour créer un consultant en sécurité sur la plateforme, suivez les étapes ci-dessous. 
Un consultant en sécurité peut gérer les configurations de ses clients.


> [!CAUTION] Cette option est uniquement disponible pour les **partenaires**.

- Accédez au partenaire **associé** au client pour lequel vous souhaitez ajouter le consultant en sécurité. Dans cet exemple, le partenaire de Space Odyssey est **Space Partner** :

![customer_partner.png](./screenshots/customer_partner.png ':size=800')

![user_in_integrator.png](./screenshots/user_in_integrator.png ':size=800x200')

- Deux possibilités s’offrent à vous : **créer** un nouvel utilisateur avec le rôle de consultant en sécurité,
ou **modifier** un utilisateur existant et lui attribuer ce rôle en activant l’option.

<!-- tabs:start -->
#### **Nouvel utilisateur**

Depuis le partenaire, accédez à la section `Users`, cliquez sur le bouton `+ Create new` pour créer un nouvel utilisateur, puis activez le bouton `Security Consultant` : 

![create_sec_cons.png](./screenshots/create_sec_cons.png ':size=350')

#### **Promouvoir un utilisateur existant**

Depuis le partenaire, accédez à la section `Users`, puis cliquez sur le bouton `+ Add Security Consultant` pour promouvoir un utilisateur existant :

 ![promote_sec_consult.png](./screenshots/promote_sec_consult.png ':size=350')

Saisissez l’adresse e-mail de l’utilisateur à promouvoir.


<!-- tabs:end -->

    
 

### Filtrer les utilisateurs

Vous pouvez rechercher des utilisateurs dans la liste à l’aide du champ de recherche situé en haut de la page. Vous pouvez ainsi rapidement trouver et gérer l’utilisateur recherché.

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des utilisateurs.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher les options de filtrage avancées, qui vous permettent de définir des conditions supplémentaires selon les trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir comment faire correspondre la valeur (`equals`, `contains` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à rechercher, en fonction de la propriété sélectionnée.

![filter_user.png](./screenshots/filter_user.png ':size=500')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters.png ':size=600')

<!-- Une fois les filtres appliqués :
- Les résultats sont mis à jour pour refléter vos conditions.
- Les filtres actifs apparaissent en haut de la page.
- Vous pouvez supprimer des filtres individuellement en cliquant sur le `X` situé à côté de chacun d’eux, ou tous les supprimer en cliquant sur le bouton `Reset Filters`. -->

> [!TIP]
> Vous pouvez actualiser la liste des utilisateurs en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

### Détails de l’utilisateur

Dans la vue d’ensemble des utilisateurs, plusieurs propriétés essentielles sont visibles immédiatement : le rôle de l’utilisateur au sein de l’entreprise (par exemple, Administrateur ou Utilisateur), son rôle sur la plateforme (généralement « Utilisateur »), l’état du compte (activé ou non) et le mode sécurisé (activé ou non).

 ![overview_users.png](./screenshots/overview_users.png ':size=800')

 Cliquez sur la ligne correspondant à un utilisateur pour ouvrir une vue détaillée contenant des informations supplémentaires, un onglet avec quelques détails et un onglet avec les paramètres de sécurité. 

![properties_user.png](./screenshots/properties_user.png ':size=500')

![security_user.png](./screenshots/security_user.png ':size=500')



<!-- > [!INFO] 
> Il n’y a pas d’informations supplémentaires pour les consultants en sécurité. -->

### Modifier un utilisateur
  
 Vous pouvez modifier un utilisateur en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de sa ligne.
 
  ![edit_user.png](./screenshots/edit_user.png ':size=400')
  
Toutes les options sont identiques à celles disponibles lors de la création d’un utilisateur.
  
### Supprimer un utilisateur

 Vous pouvez supprimer un utilisateur en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') de sa ligne.

> [!WARNING]
> Cette opération est irréversible.
 
 Un avertissement s’affiche avant la suppression définitive de l’utilisateur :
 
 ![delete_user.png](./screenshots/delete_user.png ':size=350')
