# ![réseaux_natifs](../../images/menu/menu_nativenetworks.png ':size=25') Réseaux natifs

Utilisez **Réseaux natifs** pour gérer des segments de réseau locaux au moyen d’un contrôleur réseau Jimber sur site.

## Qu’est-ce qu’un réseau natif ?

Un **réseau natif** est un segment de réseau géré par un contrôleur réseau Jimber sur site dans votre environnement local. Il étend la connectivité, le routage, le DNS, le DHCP et les contrôles de filtrage Jimber aux appareils de votre réseau physique, y compris ceux qui ne peuvent pas exécuter le _Jimber SASE Client_.

Les réseaux natifs sont utiles pour les appareils tels que les imprimantes, les caméras, les serveurs, les appareils IoT et autres terminaux non gérés qui ont néanmoins besoin d’un accès réseau contrôlé et d’une application cohérente des politiques.

## Fonctionnalités et capacités clés

Le module Réseaux natifs comprend les fonctionnalités suivantes :

- **Gestion des réseaux** pour les segments de réseau locaux.
- **Gestion des interfaces réseau** pour les ports physiques et les interfaces basées sur des VLAN.
- **Prise en charge des réseaux routés** pour les réseaux accessibles par l’intermédiaire d’un autre réseau local.
- **Services DHCP** pour l’attribution automatique d’adresses IP.
- **Intégration du DNS Jimber** pour la gestion du DNS sur les réseaux natifs.
- **Équilibrage de charge WAN et basculement** entre plusieurs interfaces WAN.
- **Filtrage DNS** par catégorie et au moyen de listes d’autorisation ou de blocage personnalisées.

## Navigation dans l’interface

Ouvrez _Réseaux natifs_ dans le menu de la barre latérale gauche.

Le module contient les pages suivantes :

- [Réseaux](./devices/nativenetworks/networks.md) pour afficher et gérer les réseaux natifs.
- [Interfaces réseau](./devices/nativenetworks/network-interfaces.md) pour configurer les interfaces physiques et celles basées sur des VLAN.
- [Équilibrage de charge WAN](./devices/nativenetworks/wan-load-balance.md) pour attribuer les interfaces WAN principales et de basculement.
- [Serveur DHCP](./devices/nativenetworks/dhcp-server.md) pour activer le DHCP et définir des plages d’adresses par réseau.
- [Filtrage DNS](./devices/nativenetworks/web-filtering.md) pour appliquer des catégories de filtrage et des règles de domaine personnalisées.

La plupart des pages de liste comprennent :

- Un champ _Recherche_ pour trouver rapidement des éléments.
- Un bouton _Filtrer_ pour effectuer un filtrage avancé.
- Un bouton _Actualiser_ pour recharger les données de la page.
- Des commandes de pagination au bas du tableau.

## Ordre de configuration recommandé

Pour une nouvelle configuration, procédez dans cet ordre :

1. Configurez les [interfaces réseau](./devices/nativenetworks/network-interfaces.md).
2. Créez ou vérifiez les [réseaux](./devices/nativenetworks/networks.md).
3. Configurez l’[équilibrage de charge WAN](./devices/nativenetworks/wan-load-balance.md) si plusieurs liaisons WAN sont disponibles.
4. Configurez le [serveur DHCP](./devices/nativenetworks/dhcp-server.md) pour les réseaux natifs concernés.
5. Appliquez le [filtrage DNS](./devices/nativenetworks/web-filtering.md) si nécessaire.

## Résumé

Utilisez les réseaux natifs pour intégrer les appareils non gérés ou sans client au même modèle de réseau contrôlé par Jimber que le reste de votre environnement.
