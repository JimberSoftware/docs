# ![](../../images/menu/menu_policies.png ':size=28') Politiques

Les **politiques** de la **_Plateforme Jimber SASE_** offrent une approche complète et centralisée de la gestion des règles de sécurité réseau. Contrairement aux systèmes traditionnels fondés sur des règles, les politiques définissent les autorisations d’accès en précisant les **sources**, les **destinations** et les **services** dans un cadre unifié.

Les politiques offrent plusieurs avantages par rapport aux configurations de règles traditionnelles :

- **Gestion simplifiée** : créez une politique au lieu de plusieurs règles individuelles
- **Sécurité axée sur les services** : associez directement les services aux autorisations d’accès
- **Contrôle basé sur les entités** : utilisez des groupes, des appareils, des utilisateurs et des réseaux comme composants des politiques
- **Vue d’ensemble centralisée** : consultez toutes les règles d’accès dans une interface unique et organisée

> [!INFO]
> Les politiques remplacent et regroupent les fonctionnalités des anciennes options telles que Group Traffic, Allow Custom Ports et Attribute Services, offrant une approche plus intuitive et évolutive de la gestion de la sécurité.

## Prérequis

Avant de créer des politiques, assurez-vous que les composants suivants sont configurés :

#### 1. Dépendances requises

- **Services** : au moins un service doit être créé pour être associé à une politique
- **Contrôleur réseau** : un contrôleur cloud doit être en cours d’exécution pour activer la connectivité SASE

#### 2. Sources d’entités facultatives

Les politiques peuvent utiliser n’importe quelle combinaison des types d’entités suivants comme sources et destinations :

- **[Groupes](/./company/groups/groups.md)** : groupes d’utilisateurs ou d’appareils
- **[Serveurs](/./devices/servers/servers.md)** : serveurs principaux et infrastructure
- **[NIACs](/./devices/niacs/niacs.md)** : clients d’accès à l’isolation réseau
- **[Appareils natifs](/./devices/nativedevices/nativedevices.md)** : appareils physiques sur le réseau
- **[Utilisateurs de l’isolation réseau](/./company/users/users.md)** : utilisateurs individuels ayant accès au réseau
- **[Appareils utilisateur](/./devices/userdevices/userdevices.md)** : appareils des utilisateurs finaux (ordinateurs portables, mobiles, etc.)
- **[Réseaux natifs](/./devices/nativenetworks/index.md)** : segments de réseau physiques

## Créer une politique

Pour créer une nouvelle politique, cliquez sur le bouton `+ Create new` dans le coin supérieur droit de la page Politiques.

![create_policy.png](./screenshots/create_policy.png ':size=500')

#### Paramètres de base

1. **Nom de la politique** : donnez à la politique un nom clair et descriptif
2. **Activée** : utilisez l’interrupteur pour activer ou désactiver la politique
3. **Source de migration** (le cas échéant) : indique la source de la règle d’origine si cette politique a été migrée depuis une configuration précédente

#### Configurer les services

Sélectionnez les services régis par cette politique. Les services définissent les applications, les sites web ou les ressources auxquels les utilisateurs peuvent accéder par l’intermédiaire de cette politique.

1. Cliquez sur `+ Add Service` pour sélectionner des services disponibles.
2. Vous pouvez ajouter plusieurs services à une même politique.
<!-- 3. Chaque service affiche ses règles d’accès et ses destinations configurées. -->

![add_service.png](./screenshots/add_service.png ':size=500')



#### Définir les sources

Les sources représentent **qui** peut accéder aux services définis dans cette politique. Vous pouvez ajouter plusieurs entités sources :

1. Cliquez sur `+ Add Source` pour ouvrir la boîte de dialogue de sélection des entités
2. Choisissez parmi les types d’entités disponibles :

    - **[Groupes](/./company/groups/groups.md)** : sélectionnez des groupes d’utilisateurs ou d’appareils
    - **[Serveurs](/./devices/servers/servers.md)** : choisissez des serveurs spécifiques
    - **[NIACs](/./devices/niacs/niacs.md)** : sélectionnez des clients d’accès à l’isolation réseau
    - **[Appareils natifs](/./devices/nativedevices/nativedevices.md)** : sélectionnez des appareils réseau physiques
    - **[Utilisateurs](/./company/users/users.md)** : choisissez des utilisateurs individuels
    - **[Appareils utilisateur](/./devices/userdevices/userdevices.md)** : sélectionnez des appareils spécifiques appartenant à un utilisateur
    - **[Réseaux natifs](/./devices/nativenetworks/index.md)** : sélectionnez des segments réseau

3. **Rechercher et filtrer** : utilisez la fonction de recherche pour trouver rapidement des entités spécifiques

![add_source.png](./screenshots/add_source.png ':size=500')

4. **Sélection multiple** : ajoutez autant d’entités sources que nécessaire pour votre politique

#### Définir les destinations

Les destinations représentent **où** les sources peuvent se connecter. Elles définissent les ressources cibles auxquelles les sources peuvent accéder :

1. Cliquez sur `+ Add Destination` pour sélectionner des entités de destination
2. Choisissez parmi les mêmes types d’entités que ceux disponibles pour les sources
3. Les destinations comprennent généralement :
    - **[Serveurs](/./devices/servers/servers.md)** hébergeant les services
    - **[Groupes](/./company/groups/groups.md)** contenant les ressources cibles
    - **[Réseaux natifs](/./devices/nativenetworks/index.md)** contenant des ressources accessibles
    - **Toutes les autres entités** fournissant des services


![add_destination.png](./screenshots/add_destination.png ':size=500')

> [!INFO]
> N’oubliez pas de cliquer sur le bouton Enregistrer au bas de chaque fenêtre.

#### Entrées de service

1. Cliquez sur `+ Add Service entry` pour saisir une entrée de service.
2. Choisissez un nom pour l’entrée.
3. Choisissez une action.
4. Saisissez l’URL ou le chemin d’accès correct dont le service a besoin pour effectuer l’action.

![service_entry.png](./screenshots/service_entry.png ':size=800')


<!-- #### Actions de service

Configurez la manière dont la politique gère l’accès aux services :

- **Autoriser** : autoriser l’accès aux services spécifiés
- **Superviser** : consigner les tentatives d’accès à des fins d’audit (si cette option est disponible)
- **Règles personnalisées** : définir des plages de ports ou des protocoles spécifiques si nécessaire -->

#### Soumettre la politique

Une fois toutes les sections configurées :

1. Vérifiez la configuration de votre politique
2. Cliquez sur `➢ Submit` pour enregistrer et activer la politique
3. Si elle est activée, la politique prend effet immédiatement

## Gérer les politiques existantes

#### Afficher la liste des politiques

La page principale Politiques affiche toutes les politiques configurées sous forme de tableau :

**Colonnes du tableau :**

- **Nom** : identifiant de la politique
- **Services** : services régis par cette politique
- **Sources** : entités pouvant initier un accès
- **Destinations** : entités cibles auxquelles accéder
- **Activée** : état actuel de la politique (active/inactive)

![policies_overview.png](./screenshots/policies_overview.png ':size=800')

##### Activer/désactiver des politiques

Modifiez l’état des politiques directement depuis le tableau principal :

1. Cliquez sur **l’interrupteur Activer/Désactiver** de la ligne de la politique
2. L’état de la politique est mis à jour immédiatement
3. Les politiques désactivées n’appliquent plus les règles d’accès, mais restent configurées


#### Mettre à jour des politiques

Pour modifier une politique existante :

1. Cliquez sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de la ligne de la politique
2. Apportez les modifications nécessaires à n’importe quelle section
3. Cliquez sur `➢ Submit` pour enregistrer les modifications

![update_policy.png](./screenshots/update_policy.png ':size=800')

#### Supprimer des politiques

Cliquez sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') de la ligne de la politique pour supprimer une politique.

Un avertissement s’affichera avant la suppression définitive de la politique :

![delete_policy.png](./screenshots/delete_policy.png ':size=300')

> [!WARNING]
> La suppression d’une politique supprime immédiatement et définitivement toutes les règles d’accès qui lui sont associées. Les utilisateurs peuvent perdre l’accès aux services si aucune autre politique ne leur accorde cette autorisation.

## Migration des politiques

Le système migre automatiquement les anciennes règles issues de configurations précédentes :

- **Règles Attribute Service** → politiques basées sur les services
- **Règles Group Traffic** → politiques de groupe à groupe
- **Règles Allow Custom Ports** → politiques propres aux ports

Les politiques migrées indiquent leur source d’origine dans la section Paramètres de base, ce qui vous aide à comprendre l’historique et le contexte de la règle.

## Bonnes pratiques

### Organisation des politiques

- **Utilisez des noms descriptifs** qui indiquent clairement l’objectif de la politique
- **Regroupez les services associés** dans une même politique lorsque cela est approprié
- **Séparez les règles d’accès critiques et non critiques** dans des politiques différentes
- **Utilisez des groupes** plutôt que des entités individuelles lorsque cela est possible

### Considérations de sécurité

- **Appliquez le principe du moindre privilège** : n’accordez que les accès nécessaires
- **Examinez régulièrement les politiques** pour vérifier qu’elles répondent aux besoins actuels de l’entreprise
- **Utilisez des groupes plutôt que des entités individuelles** pour faciliter la gestion

> [!INFO]
> Les politiques fournissent des pistes d’audit et des fonctionnalités de journalisation, ce qui facilite la supervision de l’utilisation et la résolution des problèmes de connexion.
<!-- ce qui facilite le suivi des habitudes d’accès et le dépannage des problèmes de connectivité.-->
## Dépannage

### Problèmes courants

**La politique ne prend pas effet**

- Vérifiez que la politique est **activée**
- Vérifiez que le **contrôleur réseau est en cours d’exécution**
- Assurez-vous que les **sources et les destinations** sont correctement configurées
- Vérifiez que les **services** sont correctement définis et actifs

**Accès refusé malgré la politique**

- Vérifiez que les **règles d’accès aux services** utilisent les plages de ports appropriées
- Vérifiez les **appartenances aux entités** (utilisateurs dans des groupes, appareils dans des réseaux)
- Assurez-vous que les **destinations comprennent les ressources cibles**
