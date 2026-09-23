# Groupes

Les groupes dans la configuration réseau constituent un mécanisme précieux pour appliquer des règles réseau uniformes à plusieurs utilisateurs, serveurs et clients NIAC (Network Isolation Access Clients). Il est important de noter que tous les appareils attribués au même groupe PRINCIPAL partagent intrinsèquement le même sous-réseau, ce qui garantit une interface réseau unifiée.

Le concept de groupes offre une grande polyvalence et un contrôle accru de la gestion de votre réseau. Par exemple, vous pouvez créer un groupe nommé « Developers » et définir des règles autorisant ses membres à communiquer avec les appareils du groupe « Servers ». Parallèlement, vous pouvez configurer un autre groupe, comme « Sales », de manière à lui refuser cet accès, segmentant ainsi les interactions réseau en fonction du poste ou du service.

Cette approche permet de créer un environnement réseau adapté aux particularités opérationnelles de votre organisation, en gérant les accès et les communications selon les besoins et les rôles distincts des différents groupes. En somme, l’utilisation de groupes contribue à créer un environnement réseau plus fluide, contrôlé et sécurisé.


![groups.png](/networkisolation/groups.png ':size=900')

Dans l’aperçu des groupes, vous pouvez voir les différentes entrées d’un groupe :

![group-entry.png](/networkisolation/group-entry_2.png ':size=900')




### Groupes principaux et groupes supplémentaires

Chaque utilisateur ou appareil de votre réseau peut être affecté à un groupe principal, ainsi qu’à plusieurs groupes supplémentaires.

Le groupe principal définit non seulement le sous-réseau de l’utilisateur ou de l’appareil, mais détermine également son ensemble principal de règles réseau. En revanche, les groupes supplémentaires servent à compléter les règles réseau appliquées à l’appareil ; ils n’ont aucune incidence sur son sous-réseau.

Prenons par exemple le cas d’un utilisateur ou d’un appareil affecté à un groupe principal et à quatre groupes supplémentaires. Son sous-réseau sera déterminé par la plage d’adresses IP attribuée au groupe principal. Les règles réseau du groupe principal et de tous les groupes supplémentaires seront ensuite regroupées et appliquées à l’utilisateur ou à l’appareil.

Cette structure flexible permet une gestion du réseau nuancée et à plusieurs niveaux. Les utilisateurs ou les appareils peuvent bénéficier d’un ensemble de règles réseau provenant de plusieurs groupes, tout en respectant les limites de sous-réseau clairement définies par leur groupe principal.


![edit-server.png](/networkisolation/edit-server.png ':size=600')


## Créer un groupe

Pour créer un groupe sur la plateforme, cliquez sur le bouton `Create new` 

![create_new.png](/create_new.png)

situé bien en évidence dans le coin supérieur droit de l’interface.

> [!WARNING]
> Veillez à configurer les paramètres du groupe de façon à éviter tout chevauchement avec le réseau physique existant de votre organisation, ses VPN ou tout autre réseau auquel son personnel accède.

La création d’un groupe nécessite les informations suivantes :

- Nom du groupe : identifiant du groupe, modifiable ultérieurement au besoin.
- Numéro du groupe : valeur numérique utilisée par l’interface du contrôleur réseau.
- Plage d’adresses IP : plage du réseau privé attribuée au groupe.


![create-group.png](/networkisolation/create-group.png ':size=600')


## Détails du groupe
Pour accéder aux détails d’un groupe spécifique, sélectionnez l’entrée correspondante dans le tableau (évitez de cliquer sur les boutons situés à l’extrémité). Les règles réseau associées au groupe sélectionné s’afficheront, ainsi que les appareils relevant de ce groupe.


![group-details.png](/networkisolation/group-entry.png ':size=900')


## Modifier un groupe
Vous pouvez modifier un groupe en cliquant sur l’icône de crayon jaune située à côté de son nom 
![pencil_2.png](/pencil_2.png)
.
 Vous pourrez alors modifier le nom du groupe au besoin :

![create-group.png](/networkisolation/edit-group.png ':size=600')



## Supprimer un groupe
Vous pouvez supprimer un groupe en cliquant sur l’icône de corbeille rouge située à côté de son nom 
![recycle_bin.png](/recycle_bin.png)
.


![delete-group.png](/networkisolation/delete-group.png ':size=500')



> [!WARNING]
> Un groupe ne peut être supprimé que s’il n’a aucun appareil associé ni aucune règle réseau active.

Pour procéder à la suppression :

1. Consultez la section « Détails du groupe » pour identifier les appareils associés au groupe et ses règles réseau actives.
2. Supprimez toutes les règles réseau associées au groupe.
3. Réaffectez les appareils du groupe à un autre groupe.

> Une fois ces étapes effectuées, vous devriez pouvoir supprimer le groupe.
