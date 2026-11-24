File: company/users/users.md

# ![](../../images/menu/menu_users.png ':size=25') Utilisateurs

Un utilisateur désigne un compte individuel au sein de la plateforme. Les utilisateurs peuvent avoir des rôles et être associés aux propriétés de différents produits.

> [!IMPORTANT]
> Une gestion efficace des utilisateurs est essentielle pour maintenir la sécurité et l’intégrité de votre plateforme.

### Créer un utilisateur

Pour créer un nouvel utilisateur sur la plateforme, cliquez sur le bouton `+ Create new`, situé dans le coin supérieur droit de l’interface.

> [!WARNING]
> Pour créer un nouvel utilisateur, l’entreprise **doit** d’abord ajouter un domaine. L’adresse e-mail de l’utilisateur doit correspondre au domaine ajouté. Vous trouverez plus d’informations sur les domaines [ici](/company/domains/domains.md).

L’**e-mail** sert d’identifiant principal pour un utilisateur. Il est essentiel pour l’authentification. Assurez-vous que l’adresse e-mail fournie est valide et accessible à l’utilisateur.

![create_user.png](./screenshots/create_user.png ':size=400')

<!-- > [!WARNING]
>  Notez que le nom d’utilisateur ne peut pas être modifié après la création de l’utilisateur. -->

#### Rôles des utilisateurs et autorisations associées

- **Admin** :
    - Activez cette option pour promouvoir un utilisateur au rang d’administrateur.
    - Permet à l’utilisateur de se connecter à la plateforme de sécurité.
    - Donne à l’utilisateur les privilèges nécessaires pour gérer les paramètres de l’entreprise.

<!-- - **Isolation réseau**
  - Activez cette option pour activer l’`Network Isolation` pour cet utilisateur en particulier et ajouter ainsi une couche de sécurité supplémentaire.
  - Lorsque l’isolation réseau est activée, des groupes peuvent être sélectionnés. Pour en savoir plus sur les groupes, cliquez [ici](/./company/groups/groups.md). -->

- **Activer l’isolation des appareils** :
    - Activez cette option pour activer l’isolation des appareils.
    - Si l’isolation des appareils est activée pour un appareil, tout le trafic entrant sera bloqué, sauf s’il provient de la **_Plateforme Jimber SASE_** :

    ![secure_mode_warning.png](./screenshots/secure_mode_warning.png ':size=400')

### Créer des consultants en sécurité

Pour créer un consultant en sécurité sur la plateforme, suivez les étapes ci-dessous.
Un consultant en sécurité peut gérer les configurations de ses clients.

> [!CAUTION] Cette option est uniquement disponible pour les **partenaires**.

- Accédez au partenaire **associé** au client pour lequel vous souhaitez ajouter le consultant en sécurité. Dans cet exemple, le partenaire de Space Odyssey est **Space Partner** :

![customer_partner.png](./screenshots/customer_partner.png ':size=800')

![user_in_integrator.png](./screenshots/user_in_integrator.png ':size=800x200')

- Vous pouvez procéder de deux manières : **créer** un utilisateur avec le rôle de consultant en sécurité,
  ou **modifier** un utilisateur existant et le promouvoir en activant l’option.

<!-- tabs:start -->

#### **Nouvel utilisateur**

Dans la section `Users` du partenaire, cliquez sur le bouton `+ Create new` pour créer un nouvel utilisateur, puis activez le bouton `Security Consultant` :

![create_sec_cons.png](./screenshots/create_sec_cons.png ':size=350')

#### **Promouvoir un utilisateur existant**

Dans la section `Users` du partenaire, cliquez sur le bouton `+ Add Security Consultant` pour promouvoir un utilisateur existant :

![promote_sec_consult.png](./screenshots/promote_sec_consult.png ':size=350')

Saisissez l’adresse e-mail de l’utilisateur à promouvoir.

<!-- tabs:end -->

### Filtrer les utilisateurs

Vous pouvez rechercher des utilisateurs dans la liste à l’aide du champ de recherche situé en haut de la page. Cela vous permet de trouver et de gérer rapidement l’utilisateur recherché.

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des utilisateurs.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher les options de filtrage avancées, qui vous permettent de définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : menu déroulant permettant de choisir le champ sur lequel appliquer le filtre.
- **Type de correspondance** : menu déroulant permettant de sélectionner la manière de comparer la valeur (`is`, `contains` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur à rechercher, selon la propriété sélectionnée.

![filter_user.png](./screenshots/filter_user.png ':size=500')

Pour ajouter plusieurs filtres, cliquez de nouveau sur l’icône de filtre ![](../../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters.png ':size=600')

<!-- Une fois les filtres appliqués :
- Les résultats sont mis à jour en fonction de vos conditions.
- Les filtres actifs apparaissent en haut de la page.
- Vous pouvez supprimer les filtres individuellement en cliquant sur le `X` correspondant, ou tous les supprimer en cliquant sur le bouton `Reset Filters`. -->

> [!TIP]
> Vous pouvez actualiser la liste des utilisateurs en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

### Détails de l’utilisateur

Dans la vue d’ensemble des utilisateurs, plusieurs propriétés clés sont immédiatement visibles : le rôle de l’utilisateur au sein de l’entreprise (par exemple, Admin ou User), son rôle sur la plateforme (généralement « User »), l’état de son compte (activé ou non) et l’isolation des appareils (activée ou non).

![overview_users.png](./screenshots/overview_users.png ':size=800')

Cliquez sur la ligne correspondant à un utilisateur pour ouvrir une vue détaillée contenant des informations supplémentaires, un onglet avec quelques détails et un onglet avec les paramètres de sécurité.

![properties_user.png](./screenshots/properties_user.png ':size=500')

![security_user.png](./screenshots/security_user.png ':size=500')

<!-- > [!INFO]
> Il n’y a pas d’informations supplémentaires pour les consultants en sécurité. -->

### Modifier un utilisateur

Vous pouvez modifier un utilisateur en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') dans sa ligne.

![edit_user.png](./screenshots/edit_user.png ':size=400')

Toutes les options sont identiques à celles disponibles lors de la création d’un utilisateur.

### Supprimer un utilisateur

Vous pouvez supprimer un utilisateur en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') dans sa ligne.

> [!WARNING]
> Cette action est irréversible.

Un avertissement s’affichera avant la suppression définitive de l’utilisateur :

![delete_user.png](./screenshots/delete_user.png ':size=350')
