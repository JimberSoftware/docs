# Groupes

Les groupes dans la configuration réseau constituent un mécanisme précieux pour appliquer des règles réseau uniformes à plusieurs utilisateurs, serveurs et clients d'accès d'isolation réseau (NIAC). Il est important de garder à l'esprit que tous les appareils affectés au même groupe PRINCIPAL partagent automatiquement le même sous-réseau, ce qui garantit une interface réseau unifiée.

Le concept de groupes offre une grande souplesse et un contrôle accru de la gestion de votre réseau. Par exemple, vous pouvez créer un groupe nommé « Développeurs » et définir des règles qui leur permettent de communiquer avec les appareils du groupe « Serveurs ». Parallèlement, vous pouvez configurer un groupe distinct, tel que « Ventes », sans lui accorder cet accès, afin de segmenter les interactions réseau en fonction des fonctions ou des services.

Cette approche contribue à créer un environnement réseau adapté aux spécificités opérationnelles de votre organisation, en gérant les accès et les communications selon les besoins et les rôles propres à chaque groupe. En somme, les groupes permettent de mettre en place un environnement réseau plus rationalisé, contrôlé et sécurisé.

![groups.png](/networkisolation/groups.png  =900x){.decor-shadow .radius-5}
Dans la vue d’ensemble des groupes, vous pouvez consulter les différentes entrées d’un groupe :
![group-entry.png](/networkisolation/group-entry_2.png =900x){.decor-shadow .radius-5}



### Groupes principaux et supplémentaires

Chaque utilisateur ou appareil de votre réseau peut être affecté à un groupe principal, ainsi qu’à plusieurs groupes supplémentaires.

Le groupe principal définit non seulement le sous-réseau de l’utilisateur ou de l’appareil, mais aussi son ensemble principal de règles réseau. Les groupes supplémentaires, quant à eux, complètent les règles réseau appliquées à l’appareil ; ils n’ont aucune incidence sur son sous-réseau.

Par exemple, un utilisateur ou un appareil peut être affecté à un groupe principal et à quatre groupes supplémentaires. Son sous-réseau est alors déterminé par la plage IP définie par le groupe principal. Les règles réseau du groupe principal et de tous les groupes supplémentaires sont ensuite combinées et appliquées à l’utilisateur ou à l’appareil.

Cette structure souple permet une gestion du réseau précise et à plusieurs niveaux. Les utilisateurs ou les appareils peuvent bénéficier d’un ensemble de règles réseau provenant de plusieurs groupes, tout en respectant les limites de sous-réseau clairement définies par leur groupe principal.

![edit-server.png](/networkisolation/edit-server.png =600x){.decor-shadow .radius-5}

## Créer un groupe

Pour créer un groupe dans la plateforme, cliquez sur le bouton `Create new` 
![create_new.png](/create_new.png){ .radius-5}
situé bien en évidence dans le coin supérieur droit de l’interface.

> Veillez à configurer les paramètres du groupe de manière à éviter tout chevauchement avec le réseau physique existant de votre organisation, ses VPN ou tout autre réseau auquel votre personnel accède. {.is-warning}

Pour créer un groupe, vous devez fournir les informations suivantes :

- Nom du groupe : identifiant du groupe, qui peut être modifié ultérieurement selon les besoins.
- Numéro du groupe : valeur numérique utilisée par l’interface du contrôleur réseau.
- Plage IP : plage du réseau privé attribuée au groupe.

![create-group.png](/networkisolation/create-group.png =600x){.decor-shadow .radius-5}

## Détails du groupe
Pour accéder aux détails d’un groupe, sélectionnez l’entrée correspondante dans le tableau (évitez de cliquer sur les boutons à l’extrémité). Les règles réseau associées au groupe choisi s’affichent, ainsi que les appareils qui en dépendent.

![group-details.png](/networkisolation/group-entry.png =900x){.decor-shadow .radius-5}

## Modifier un groupe
Vous pouvez modifier un groupe en cliquant sur l’icône de crayon jaune située à côté de son nom ![pencil_2.png](/pencil_2.png){.radius-5}.
 Vous pourrez alors modifier le nom du groupe selon vos besoins :
![create-group.png](/networkisolation/edit-group.png =600x){.decor-shadow .radius-5}


## Supprimer un groupe
Vous pouvez supprimer un groupe en cliquant sur l’icône de corbeille rouge située à côté de son nom ![recycle_bin.png](/recycle_bin.png){.radius-5}.

![delete-group.png](/networkisolation/delete-group.png =500x){.decor-shadow .radius-5}


> Un groupe ne peut être supprimé que s’il ne comporte aucun appareil associé ni règle réseau active. {.is-warning}

Pour procéder à la suppression :

1. Consultez la section « Détails du groupe » pour identifier les appareils associés au groupe et ses règles réseau actives.
2. Supprimez toutes les règles réseau associées au groupe.
3. Réaffectez les appareils du groupe à un autre groupe.

> Une fois ces étapes effectuées, vous devriez pouvoir supprimer le groupe.
{.is-success}
