File: rules/firewall-policies/firewall-policies.md

# ![](../../images/menu/menu_policies.png ':size=28') Politiques

<!-- tabs:start -->

## **![](../../images/menu/menu_services.png ':size=28') Services de pare-feu**

Au sein de la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_**, un **service** représente une ressource numérique pouvant être rendue accessible aux utilisateurs. Ces services peuvent inclure des sites web, des portails internes, des bureaux à distance, des CRM ou toute autre application basée sur le réseau.

Pour rendre un service disponible, vous devez l’attribuer à un **groupe** et à une **destination** sur la page [**Politiques**](/./rules/firewall-policies/firewall-policies.md). Une fois cette configuration effectuée, le service apparaîtra dans le [**Panneau de sécurité**](/./rules/security_panel/security_panel.md) des utilisateurs membres du groupe sélectionné.

Les utilisateurs peuvent ouvrir le Panneau de sécurité en cliquant sur l’**icône Jimber SASE de la barre d’état système** dans leur barre des tâches.

![Capture d’écran du menu de la barre d’état système de Jimber](./screenshots/security_panel.png ':size=300')

Voici à quoi peut ressembler un panneau de sécurité contenant plusieurs services :

![Capture d’écran de l’onglet Services du Panneau de sécurité](./screenshots/security_panel_overview.png ':size=600')


#### Créer des services

Pour créer un service sur la plateforme, cliquez sur le bouton `+ Create new` situé en haut à droite de l’interface.

![Capture d’écran de la page Services](./screenshots/services.png ':size=600')

L’écran suivant s’ouvre. Vous pouvez y saisir les détails de votre service :

![Capture d’écran de la page de création d’un service](./screenshots/create_service.png ':size=600')

1. **Choisir un nom** : commencez par donner à votre service un nom clair et reconnaissable.

> [!NOTE]
> Vous pouvez commencer avec un modèle (voir ci-dessous) ou créer un service entièrement nouveau.


<!-- 2. **Créer une nouvelle entrée de service** : cliquez sur `+ Create new service entry`. Cela définit le comportement du service.

    - **Name** : donnez un nom reconnaissable à l’entrée de service.
    - **Action** : actuellement, la seule option disponible est **"Open website"**.
    - **URL/Path** : saisissez l’adresse web ou le chemin interne que le service doit ouvrir. -->

2. **Ajouter une règle d’accès** : cliquez sur `+ Add Access Rule`. Cela définit les règles d’autorisation du trafic pour le service.

    - **Description** : décrivez brièvement l’objectif de la règle.
    - **Port de début / port de fin** : indiquez la plage de ports à autoriser. Si ces champs sont laissés vides, les valeurs par défaut `1` et `65535` sont utilisées.
    - **Protocole** : choisissez le protocole utilisé par le service (TCP, UDP ou ICMP).
    
    ![add_access_rule.png](./screenshots/add_access_rule.png ':size=500')

3. **Soumettre le service** en cliquant sur le bouton `➢ Submit`.
Si vous quittez la page alors que des modifications ne sont pas enregistrées, un avertissement s’affiche :

    ![Capture d’écran de l’avertissement indiquant que des modifications ne sont pas enregistrées](../../images/notifications/unsaved_changes.png ':size=300')

**Répétez ces étapes** pour configurer des règles d’accès supplémentaires si nécessaire.

Après avoir créé le service, vous pouvez passer à la page [Politiques](/./rules/firewall-policies/firewall-policies.md) pour définir les détails du service.

#### Modèle de service

Vous pouvez enregistrer la configuration de votre service en cliquant sur le bouton `📄Save template`. Lorsque vous y êtes invité, saisissez un nom distinctif et un résumé clair et descriptif afin de pouvoir facilement l’identifier et le réutiliser ultérieurement.

![save_template.png](./screenshots/save_template.png ':size=500')

 
 Vous pouvez utiliser les modèles enregistrés lors de la création d’un nouveau service en cliquant sur le bouton `📄Load template` en bas de la page, en sélectionnant le modèle de service approprié, puis en cliquant sur le bouton `➢ Apply template`.

![load_template.png](./screenshots/load_template.png ':size=500')


#### Rechercher des services

Vous pouvez rechercher un service dans la liste à l’aide du champ de recherche situé en haut de la page. Vous trouverez ainsi rapidement le service que vous recherchez et pourrez le gérer.

> [!TIP]
> Vous pouvez actualiser la liste des services en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

#### Mettre à jour des services
Vous pouvez modifier des services en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') dans leur ligne.

![update_service.png](./screenshots/update_service.png ':size=800')

Vous pouvez alors :

- Modifier le **nom du service**.
- Ajouter, supprimer ou modifier des **règles d’accès**.

> [!IMPORTANT]
> N’oubliez pas de soumettre le service en cliquant sur le bouton `➢ Submit`.

Vous pouvez utiliser le bouton `Clear changes` si vous décidez de ne pas soumettre les modifications.


#### Supprimer des services

Vous pouvez supprimer des services en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') dans leur ligne.

 Un avertissement s’affiche avant la suppression définitive du service :
 
![Capture d’écran de l’avertissement de suppression](./screenshots/delete_service.png ':size=400')


## **![](../../images/menu/menu_services.png ':size=28') Politiques de pare-feu**

Les **politiques** de la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_** fournissent une approche complète et centralisée de la gestion des règles de sécurité réseau. Contrairement aux systèmes traditionnels fondés sur des règles, les politiques définissent les autorisations d’accès en spécifiant les **sources**, les **destinations** et les **services** au sein d’un cadre unifié.

Les politiques offrent plusieurs avantages par rapport aux anciennes configurations de règles :

- **Gestion simplifiée** : créez une seule politique au lieu de plusieurs règles individuelles
- **Sécurité axée sur les services** : associez directement les services aux autorisations d’accès
- **Contrôle fondé sur les entités** : utilisez des groupes, des appareils, des utilisateurs et des réseaux comme composants de politique
- **Vue d’ensemble centralisée** : consultez toutes les règles d’accès dans une interface unique et organisée

> [!INFO]
> Les politiques remplacent et regroupent les fonctionnalités d’anciennes options comme Group Traffic, Allow Custom Ports et Attribute Services, pour offrir une approche de la gestion de la sécurité plus intuitive et évolutive.

### Prérequis

Avant de créer des politiques, assurez-vous que les composants suivants sont configurés :

#### 1. Dépendances requises

- **Services** : au moins un service doit être créé pour pouvoir l’associer à une politique
- **Contrôleur réseau** : un contrôleur cloud doit être en cours d’exécution pour permettre la connectivité SASE

#### 2. Sources d’entités facultatives

Les politiques peuvent utiliser toute combinaison des types d’entités suivants comme sources et destinations :

- **[Groupes](/./company/groups/groups.md)** : groupes d’utilisateurs ou d’appareils
- **[Serveurs](/./devices/servers/servers.md)** : serveurs dorsaux et infrastructure
- **[NIAC](/./devices/niacs/niacs.md)** : clients d’accès à l’isolation réseau
- **[Appareils natifs](/./devices/nativedevices/nativedevices.md)** : appareils physiques sur le réseau
- **[Utilisateurs de l’isolation réseau](/./company/users/users.md)** : utilisateurs individuels ayant accès au réseau
- **[Appareils utilisateur](/./devices/userdevices/userdevices.md)** : appareils des utilisateurs finaux (ordinateurs portables, téléphones mobiles, etc.)
- **[Réseaux natifs](/./devices/nativenetworks/index.md)** : segments de réseau physiques

### Créer une politique

Pour créer une nouvelle politique, cliquez sur le bouton `+ Create new` dans le coin supérieur droit de la page Politiques.

![create_policy.png](./screenshots/create_policy.png ':size=500')

##### 1. Paramètres de base

 1. **Nom de la politique** : choisissez un nom clair et descriptif pour la politique
 2. **Activée** : utilisez le bouton bascule pour activer ou désactiver la politique
 3. **Source de migration** (le cas échéant) : indique la source de la règle d’origine si cette politique a été migrée à partir d’anciennes configurations.
    <!-- Cliquez [ici](#policy-migration) pour consulter la présentation de la migration.  -->

##### 2. Configurer les services

Sélectionnez les services régis par cette politique. Les services définissent les applications, les sites web ou les ressources auxquels les utilisateurs peuvent accéder par l’intermédiaire de cette politique.

 1. Cliquez sur `+ Add Services` pour sélectionner des services disponibles.
 2. Vous pouvez ajouter plusieurs services à une même politique.
<!-- 3. Chaque service affiche ses règles d’accès et ses destinations configurées. -->

![add_service.png](./screenshots/add_service.png ':size=500')



##### 3. Définir les sources

Les sources représentent **qui** peut accéder aux services définis dans cette politique. Comme indiqué précédemment, vous pouvez ajouter plusieurs entités sources :

 1. Cliquez sur `+ Add Sources` pour ouvrir la boîte de dialogue de sélection des entités
 2. Choisissez parmi les types d’entités disponibles :

    - **[Groupes](/./company/groups/groups.md)** : sélectionnez des groupes d’utilisateurs ou d’appareils
    - **[Serveurs](/./devices/servers/servers.md)** : choisissez des serveurs spécifiques
    - **[NIAC](/./devices/niacs/niacs.md)** : sélectionnez des clients d’accès à l’isolation réseau
    - **[Appareils natifs](/./devices/nativedevices/nativedevices.md)** : sélectionnez des appareils réseau physiques
    - **[Utilisateurs](/./company/users/users.md)** : choisissez des utilisateurs individuels
    - **[Appareils utilisateur](/./devices/userdevices/userdevices.md)** : sélectionnez des appareils spécifiques d’un utilisateur
    - **[Réseaux natifs](/./devices/nativenetworks/index.md)** : sélectionnez des segments de réseau

 3. **Rechercher et filtrer** : utilisez la fonction de recherche pour trouver rapidement des entités spécifiques

![add_source.png](./screenshots/add_source.png ':size=500')

 4. **Sélection multiple** : ajoutez autant d’entités sources que nécessaire pour votre politique

##### 4. Définir les destinations

Les destinations représentent **où** les sources peuvent se connecter. Elles définissent les ressources cibles auxquelles les sources peuvent accéder :

 1. Cliquez sur `+ Add Destinations` pour sélectionner des entités de destination
 2. Choisissez parmi les mêmes types d’entités que ceux disponibles pour les sources
 3. Les destinations incluent généralement :
    - les **[Serveurs](/./devices/servers/servers.md)** hébergeant les services
    - les **[Groupes](/./company/groups/groups.md)** contenant les ressources cibles
    - les **[Réseaux natifs](/./devices/nativenetworks/index.md)** qui hébergent les ressources accessibles
    - **toutes les autres entités** fournissant des services


![add_destination.png](./screenshots/add_destination.png ':size=500')

> [!INFO]
> N’oubliez pas de cliquer sur le bouton d’enregistrement en bas de chaque fenêtre.

##### 5. Entrées de service

 1. Cliquez sur `+ Add Service entry` pour ajouter une entrée de service.
 2. Choisissez un nom pour l’entrée.
 3. Choisissez une action.
 4. Saisissez l’URL ou le chemin correct dont le service aura besoin pour effectuer l’action.

![service_entry.png](./screenshots/service_entry.png ':size=700')



##### 6. Soumettre la politique

Une fois toutes les sections configurées :

 1. Vérifiez la configuration de votre politique
 2. Cliquez sur `➢ Submit` pour enregistrer et activer la politique
 3. Si elle est activée, la politique prend effet immédiatement

### Gérer les politiques existantes

##### Afficher la liste des politiques

La page principale Politiques affiche toutes les politiques configurées dans un tableau :

**Colonnes du tableau :**

- **Nom** : identifiant de la politique
- **Services** : services régis par cette politique
- **Sources** : entités pouvant initier un accès
- **Destinations** : entités cibles de l’accès
- **Activée** : état actuel de la politique (active/inactive)

![policies_overview.png](./screenshots/policies_overview.png ':size=700')

> [!NOTE]
>Si l’un des éléments est laissé vide, un point d’exclamation jaune apparaîtra dans la ligne de la politique.

###### Activer/désactiver des politiques

Vous pouvez modifier l’état d’une politique directement dans le tableau principal :

 1. Cliquez sur le **bouton bascule Activer/Désactiver** dans la ligne de la politique
 2. L’état de la politique est mis à jour immédiatement
 3. Les politiques désactivées cessent d’appliquer les règles d’accès, mais restent configurées

> [!TIP]
> Vous pouvez actualiser la liste des politiques en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

##### Mettre à jour des politiques

Pour modifier une politique existante :

 1. Cliquez sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') dans la ligne de la politique.
 2. Effectuez les modifications nécessaires dans les sections concernées
 3. Cliquez sur `➢ Submit` pour enregistrer les modifications

![update_policy.png](./screenshots/update_policy.png ':size=500')

##### Supprimer des politiques

Cliquez sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') dans la ligne de la politique pour la supprimer.

Un avertissement s’affiche avant la suppression définitive de la politique :

![delete_policy.png](./screenshots/delete_policy.png ':size=400')

> [!WARNING]
> La suppression d’une politique supprime immédiatement et définitivement toutes les règles d’accès qui lui sont associées. Les utilisateurs risquent de perdre l’accès aux services si aucune autre politique ne l’autorise.

### Migration des politiques

Le système migre automatiquement les anciennes règles des configurations précédentes :

- Règles **Attribute Service** → politiques fondées sur les services
- Règles **Group Traffic** → politiques de groupe à groupe
- Règles **Allow Custom Ports** → politiques spécifiques aux ports

Les politiques migrées indiquent leur source d’origine dans la section Paramètres de base, ce qui vous aide à comprendre l’historique et le contexte de la règle.

### Bonnes pratiques

#### Organisation des politiques

- **Utilisez des noms descriptifs** qui indiquent clairement l’objectif de la politique
- **Regroupez les services associés** dans une même politique lorsque cela est approprié
- **Séparez les règles d’accès critiques et non critiques** dans différentes politiques
- **Utilisez des groupes** plutôt que des entités individuelles lorsque cela est possible

#### Considérations de sécurité

- **Appliquez le principe du moindre privilège** : n’accordez que les accès nécessaires
- **Examinez régulièrement les politiques** pour vous assurer qu’elles répondent aux besoins actuels de l’entreprise
- **Utilisez des groupes plutôt que des entités individuelles** pour faciliter la gestion

> [!INFO]
> Les politiques fournissent des pistes d’audit et des fonctionnalités de journalisation, ce qui facilite la supervision de l’utilisation et la résolution des problèmes de connexion.
<!-- ce qui facilite le suivi des modèles d’accès et le dépannage des problèmes de connectivité.-->
### Dépannage

#### Problèmes courants

 **La politique ne prend pas effet**

  - Vérifiez que la politique est **activée**
  - Vérifiez que le **contrôleur réseau est en cours d’exécution**
  - Assurez-vous que les **sources et les destinations** sont correctement configurées
  - Vérifiez que les **services** sont correctement définis et actifs

 **Accès refusé malgré la politique**

  - Vérifiez que les **règles d’accès aux services** définissent les plages de ports correctes
  - Vérifiez les **appartenances aux entités** (utilisateurs dans les groupes, appareils dans les réseaux)
  - Assurez-vous que les **destinations incluent les ressources cibles**

## **![](../../images/menu/menu_services.png ':size=28') Politiques de posture**


## **![](../../images/menu/menu_services.png ':size=28') Politiques sans agent**


<!-- tabs:end -->
