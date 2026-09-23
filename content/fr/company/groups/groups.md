File: company/groups/groups.md

# ![](../../images/menu/menu_groups.png ':size=25') Groupes

Les groupes dans l’environnement réseau constituent un mécanisme précieux pour appliquer des règles réseau uniformes à plusieurs utilisateurs, serveurs et clients NIAC (Network Isolation Access Clients).

Le concept de groupes apporte un haut niveau de polyvalence et de contrôle à la gestion de votre réseau. Comme indiqué dans les [Bonnes pratiques](/./advanced/bestpractices/bestpractices.md), il est préférable de choisir des noms de groupe qui reflètent leur fonction, tels que « AllowFileServer », « ForceOneGateway »...

Par exemple, un groupe nommé « AllowServerAccess » peut être configuré avec des règles permettant à ses membres d’accéder aux appareils du groupe « Servers ». Dans le même temps, un groupe distinct, tel que « NoServerAccess », peut être configuré pour ne pas disposer de cet accès.

<!-- Une segmentation supplémentaire de ces groupes peut être effectuée en fonction du poste ou du service. -->

<!-- Par exemple, un groupe nommé « Developers » peut être configuré avec des règles permettant à ses membres de communiquer avec les appareils du groupe « Servers ». Dans le même temps, un groupe distinct, tel que « Sales », peut être configuré pour ne pas disposer de cet accès, afin de segmenter les interactions réseau en fonction du poste ou du service. -->

Cette approche contribue à créer un environnement réseau adapté aux spécificités opérationnelles de votre organisation, en gérant les accès et les communications en fonction des besoins et des rôles propres à chaque groupe. En somme, l’utilisation de groupes facilite la mise en place d’un environnement réseau plus rationalisé, mieux contrôlé et plus sécurisé.


![groups.png](./screenshots/groups.png ':size=800')

Dans l’aperçu des groupes, vous pouvez voir les différentes entrées d’un groupe :

![group_entry.png](./screenshots/group_entry_2.png ':size=800')

<!-- ### Groupes principaux et groupes supplémentaires

Chaque utilisateur ou appareil de votre réseau peut être affecté à un groupe principal ainsi qu’à plusieurs groupes supplémentaires.

Le groupe principal définit le sous-réseau de l’utilisateur ou de l’appareil et détermine également son principal ensemble de règles réseau. Les groupes supplémentaires, quant à eux, complètent les règles réseau appliquées à l’appareil ; ils n’ont aucune incidence sur son sous-réseau.

Prenons l’exemple d’un utilisateur ou d’un appareil affecté à un groupe principal et à quatre groupes supplémentaires. L’utilisateur ou l’appareil obtient son sous-réseau à partir de la plage d’adresses IP définie par le groupe principal. Les règles réseau du groupe principal et de tous les groupes supplémentaires sont ensuite regroupées et appliquées à l’utilisateur ou à l’appareil.

Cette structure flexible permet une approche de la gestion réseau précise et à plusieurs niveaux. Les utilisateurs ou les appareils peuvent bénéficier d’une combinaison de règles réseau provenant de plusieurs groupes, tout en respectant les limites de sous-réseau clairement définies par leur groupe principal. -->


<!-- ![edit-server.png](/edit-server.png ':size=600') -->

### Créer un groupe

Pour créer un groupe dans la plateforme, cliquez sur le bouton `+ Create new` situé dans le coin supérieur droit de l’interface.

> [!WARNING]
> Veillez à configurer les paramètres du groupe de manière à éviter tout chevauchement avec le réseau physique existant de votre organisation, ses VPN ou tout autre réseau auquel votre personnel accède.

Pour créer un groupe, vous devez lui attribuer un nom, que vous pourrez modifier ultérieurement si nécessaire.


![create_group.png](./screenshots/create_group.png ':size=400')

### Filtrer les groupes

Vous pouvez rechercher des groupes dans la liste à l’aide du champ de recherche situé en haut de la page. Cela vous permet de trouver et de gérer rapidement le groupe recherché.

<!-- - Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des groupes. -->

> [!TIP]
> Vous pouvez actualiser la liste des groupes en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.


### Détails du groupe

Cliquez sur la ligne d’un groupe pour ouvrir une fenêtre contenant deux onglets. Le premier présente un aperçu des appareils du groupe. Le second présente un aperçu des règles de sécurité associées.

![group_details.png](./screenshots/group_details.png ':size=500')

![group_security.png](./screenshots/group_security.png ':size=500')



> [!ATTENTION]
> Les appareils et les utilisateurs ne peuvent être ajoutés au groupe qu’à partir de leur propre page :
>
>    - Vous trouverez [ici](/./rules/firewall-policies/firewall-policies.md) des informations détaillées sur les politiques.
>    - Vous trouverez [ici](/./rules/groupconfiguration/groupconfiguration.md) des informations détaillées sur la configuration de groupe.
>    - Vous trouverez [ici](/./company/users/users.md) des informations détaillées sur l’ajout d’utilisateurs.
>    - Vous trouverez des informations détaillées sur l’ajout d’appareils dans la section [**DEVICES**](/devices.md) de la barre latérale.




### Modifier un groupe
Vous pouvez modifier un groupe en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') dans sa ligne.

 Vous pourrez alors modifier le nom du groupe selon vos besoins :

![edit_group.png](./screenshots/edit_group.png ':size=400')


<!-- ### Dupliquer un groupe
Vous pouvez dupliquer un groupe en cliquant sur l’icône de duplication ![](../../images/icons/icon_copy.png ':size=20') dans sa ligne.

 Vous pourrez alors choisir un nom pour le nouveau groupe :

![copy_group.png](./screenshots/copy_group.png ':size=500')

Le nouveau groupe affichera les mêmes détails que le groupe d’origine : règles de pare-feu, règles de trafic de groupe, règles de port et services attribués. -->




### Supprimer un groupe
Vous pouvez supprimer un groupe en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') dans sa ligne.

> [!WARNING]
> Cette opération est irréversible.

Un avertissement s’affichera avant la suppression définitive du groupe :

![delete_group.png](./screenshots/delete_group.png ':size=400')





<!-- [devices]: /./devices -->
