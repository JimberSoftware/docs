# ![native_networks](../../images/menu/menu_nativenetworks.png ':size=25') Réseaux natifs

Utilisez **Réseaux natifs** pour gérer les segments de réseau locaux au moyen d’un contrôleur réseau Jimber installé sur site.

## Qu’est-ce qu’un réseau natif ?

Un **réseau natif** est un segment de réseau géré par un contrôleur réseau Jimber installé sur site dans votre environnement local. Il étend aux appareils de votre réseau physique les fonctions de connectivité, de routage, de DNS, de DHCP et de filtrage de Jimber, y compris aux appareils qui ne peuvent pas exécuter le *Jimber SASE Client*.

Les réseaux natifs sont utiles pour les appareils tels que les imprimantes, les caméras, les serveurs, les appareils IoT et les autres terminaux non gérés qui ont néanmoins besoin d’un accès réseau contrôlé et d’une application cohérente des politiques.

## Fonctionnalités et capacités clés

Le module Réseaux natifs comprend les fonctionnalités suivantes :

- **Gestion des réseaux** pour les segments de réseau locaux.
- **Gestion des interfaces réseau** pour les ports physiques et les interfaces basées sur des VLAN.
- **Prise en charge des réseaux routés** pour les réseaux accessibles par l’intermédiaire d’un autre réseau local.
- **Services DHCP** pour l’attribution automatique des adresses IP.
- **Intégration DNS Jimber** pour la gestion DNS sur les réseaux natifs.
- **Équilibrage de charge et basculement WAN** entre plusieurs interfaces WAN.
- **Filtrage web** par catégorie et au moyen de listes d’autorisation ou de blocage personnalisées.

## Navigation dans l’interface

Ouvrez *Réseaux natifs* depuis le menu de la barre latérale gauche.

Le module comprend les pages suivantes :

- [Réseaux](./devices/nativenetworks/networks.md) pour consulter et gérer les réseaux natifs.
- [Interfaces réseau](./devices/nativenetworks/network-interfaces.md) pour configurer les interfaces physiques et celles basées sur des VLAN.
- [Équilibrage de charge WAN](./devices/nativenetworks/wan-load-balance.md) pour attribuer les interfaces WAN principales et de secours.
- [Serveur DHCP](./devices/nativenetworks/dhcp-server.md) pour activer DHCP et définir des plages d’adresses pour chaque réseau.
- [Filtrage web](./devices/nativenetworks/web-filtering.md) pour appliquer des catégories de filtrage et des règles de domaine personnalisées.

La plupart des pages de liste comprennent :

- Un champ *Rechercher* pour trouver rapidement des éléments.
- Un bouton *Filtrer* pour effectuer un filtrage avancé.
- Un bouton *Actualiser* pour recharger les données de la page.
- Des commandes de pagination en bas du tableau.

## Ordre de configuration recommandé

Pour une nouvelle configuration, procédez dans l’ordre suivant :

1. Configurez les [Interfaces réseau](./devices/nativenetworks/network-interfaces.md).
2. Créez ou vérifiez les [Réseaux](./devices/nativenetworks/networks.md).
3. Configurez l’[Équilibrage de charge WAN](./devices/nativenetworks/wan-load-balance.md) si plusieurs liaisons WAN sont disponibles.
4. Configurez le [Serveur DHCP](./devices/nativenetworks/dhcp-server.md) pour les réseaux natifs requis.
5. Appliquez le [Filtrage web](./devices/nativenetworks/web-filtering.md) si nécessaire.

## Résumé

Utilisez les réseaux natifs pour intégrer les appareils non gérés ou sans client au même modèle de mise en réseau contrôlé par Jimber que le reste de votre environnement.
