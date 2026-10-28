File: company/groups/groups.md

# ![](../../images/menu/menu_groups.png ':size=25') Groupes

Les groupes dans l’environnement réseau constituent un mécanisme précieux pour appliquer des règles réseau uniformes à plusieurs utilisateurs, serveurs et clients d’accès isolé au réseau (NIAC).

Le concept de groupes offre une grande souplesse et un contrôle accru de la gestion de votre réseau. Comme indiqué dans les [Bonnes pratiques](/./advanced/bestpractices/bestpractices.md), il est préférable de choisir des noms de groupe qui reflètent leur fonction, tels que « AllowFileServer », « ForceOneGateway », « WanGateway »…

Par exemple, un groupe nommé « AllowServerAccess » peut être configuré avec des règles permettant à ses membres d’accéder aux appareils du groupe « Servers ». Dans le même temps, un groupe distinct, comme « NoServerAccess », peut être configuré de manière à ne pas autoriser cet accès.

<!-- A further segmentation of these groups can be made based on job function or department. -->

<!-- For instance, a group named 'Developers' could be set up with rules allowing members of that group to communicate with the devices in the group 'Servers'. Simultaneously, a separate group such as 'Sales' could be configured not to have this access, thereby segmenting network interactions based on job function or department. -->

Cette approche contribue à créer un environnement réseau adapté aux spécificités opérationnelles de votre organisation, en gérant les accès et les communications selon les besoins et les rôles distincts des différents groupes. En somme, l’utilisation de groupes favorise un environnement réseau plus rationalisé, contrôlé et sécurisé.


![groups.png](./screenshots/groups.png ':size=800')

Dans la vue d’ensemble des groupes, vous pouvez voir les différentes entrées d’un groupe :

![group_entry.png](./screenshots/group_entry_2.png ':size=800')

<!-- ### Primary vs Additional groups

Each user or device on your network can be assigned to one primary group, as well as numerous additional groups.

The primary group not only establishes the subnet for the user or device, but also determines its primary set of network rules. On the other hand, the role of additional groups is to supplement the network rules that are applied to the device; they do not influence its subnet.

For instance, consider a scenario where a user or device is assigned to one primary group and four additional groups. The user or device would obtain its subnet based on the IP range designated by the primary group. Then, the network rules from both the primary and all additional groups are aggregated and enforced on the user or device.

This flexible structure allows for a fine-tuned, layered approach to network management. Users or devices can benefit from a blend of network rules across multiple groups while adhering to clear subnet boundaries defined by their primary group. -->


<!-- ![edit-server.png](/edit-server.png ':size=600') -->

### Créer un groupe

Pour créer un groupe sur la plateforme, cliquez sur le bouton `+ Create new` situé dans le coin supérieur droit de l’interface.

> [!WARNING]
> Veillez à configurer les paramètres du groupe de manière à éviter tout chevauchement avec le réseau physique existant de votre organisation, ses VPN ou tout autre réseau auquel son personnel accède.

Pour créer un groupe, vous devez lui donner un nom, que vous pourrez modifier ultérieurement si nécessaire.


![create_group.png](./screenshots/create_group.png ':size=400')

### Filtrer les groupes

Vous pouvez rechercher un groupe dans la liste à l’aide du champ de recherche en haut de la page. Vous pouvez ainsi trouver et gérer rapidement le groupe recherché.

<!-- - Use the search box to enter keywords and filter the group list. -->

> [!TIP]
> Vous pouvez actualiser la liste des groupes en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.


### Détails du groupe

En cliquant sur la barre d’un groupe, vous ouvrez une fenêtre contenant deux onglets. Le premier présente une vue d’ensemble des appareils du groupe. Le second présente une vue d’ensemble des règles de sécurité associées.

![group_details.png](./screenshots/group_details.png ':size=500')

![group_security.png](./screenshots/group_security.png ':size=500')



> [!ATTENTION]
> Les appareils et les utilisateurs ne peuvent être ajoutés au groupe qu’à partir de leur propre page :
>
>    - Vous trouverez [ici](/./rules/firewall-policies/firewall-policies.md) des informations détaillées sur les politiques.
>    - Vous trouverez [ici](/./rules/groupconfiguration/groupconfiguration.md) des informations détaillées sur la configuration de groupe.
>    - Vous trouverez [ici](/./company/users/users.md) des informations détaillées sur l’ajout d’utilisateurs.
>    - Vous trouverez des informations détaillées sur l’ajout d’appareils dans la section [**APPAREILS**](/devices.md) de la barre latérale.




### Modifier un groupe
Vous pouvez modifier un groupe en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de sa ligne.

 Vous pourrez alors modifier le nom du groupe selon vos besoins :

![edit_group.png](./screenshots/edit_group.png ':size=400')


<!-- ### Duplicate Group
Groups can be duplicated by clicking on the duplicate icon ![](../../images/icons/icon_copy.png ':size=20') in their row.

 You'll then be able to choose a name for the new group:

![copy_group.png](./screenshots/copy_group.png ':size=500')

The new group will show the same details as the original group: firewall rules, group traffic rules, port rules and attributed services. -->




### Supprimer un groupe
Vous pouvez supprimer un groupe en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') de sa ligne.

> [!WARNING]
> Cette opération est irréversible.

Un avertissement s’affichera avant la suppression définitive du groupe :

![delete_group.png](./screenshots/delete_group.png ':size=400')





<!-- [devices]: /./devices -->
