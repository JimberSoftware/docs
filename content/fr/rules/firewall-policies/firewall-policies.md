# ![](../../images/menu/menu_policies.png ':size=28') Politiques

<!-- tabs:start -->

## **![](../../images/menu/menu_services.png ':size=28') Services de pare-feu**

Au sein de la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_**, un **service** représente une ressource numérique qui peut être mise à la disposition des utilisateurs. Ces services peuvent inclure des sites web, des portails internes, des bureaux à distance, des CRM ou toute autre application réseau.

Pour mettre un service à disposition, il doit être attribué à un **groupe** et à une **destination** sur la page [**Politiques**](/./rules/firewall-policies/firewall-policies.md). Une fois cette configuration effectuée, le service apparaît dans le [**Panneau de sécurité**](/./rules/security_panel/security_panel.md) des utilisateurs membres du groupe sélectionné.

Les utilisateurs peuvent ouvrir le Panneau de sécurité en cliquant sur l’**icône Jimber dans la zone de notification** de leur barre des tâches.

![Capture d’écran du menu de la zone de notification Jimber](./screenshots/security_panel.png ':size=300')

Un panneau de sécurité comprenant plusieurs services peut ressembler à ceci :

![Capture d’écran de l’onglet Services du Panneau de sécurité](./screenshots/security_panel_overview.png ':size=600')


#### Créer des services

Pour créer un service sur la plateforme, cliquez sur le bouton `+ Create new` situé dans le coin supérieur droit de l’interface.

![Capture d’écran de la page Services](./screenshots/services.png ':size=700')

L’écran suivant s’ouvre et vous permet de saisir les détails de votre service :

![Capture d’écran de la page de création d’un service](./screenshots/create_service.png ':size=700')

1. **Choisir un nom** : commencez par donner à votre service un nom clair et reconnaissable.

> [!NOTE]
> Vous pouvez commencer avec un modèle (voir ci-dessous) ou créer un service entièrement nouveau. 


<!-- 2. **Create a New Service Entry**: Click `+ Create new service entry`. This defines how the service behaves.

    - **Name**: Provide a recognizable name to the service entry.
    - **Action**: Currently, the only available option is **"Open website"**.
    - **URL/Path**: Enter the web address or internal path the service should open. -->

2. **Ajouter une règle d’accès** : cliquez sur `+ Add Access Rule`. Cette règle définit le trafic autorisé pour le service.

    - **Description** : décrivez brièvement l’objectif de la règle.
    - **Port de début / Port de fin** : indiquez la plage de ports à autoriser. Si ces champs sont laissés vides, les valeurs par défaut `1` et `65535` sont utilisées.
    - **Protocole** : choisissez le protocole utilisé par le service (TCP, UDP ou ICMP).
    
    ![add_access_rule.png](./screenshots/add_access_rule.png ':size=500')

3. **Soumettre le service** en cliquant sur le bouton `➢ Submit`. 
Si vous quittez la page alors que des modifications ne sont pas enregistrées, un message d’avertissement apparaît :

    ![Capture d’écran de l’avertissement concernant les modifications non enregistrées](../../images/notifications/unsaved_changes.png ':size=300')

**Répétez ces étapes** pour configurer d’autres règles d’accès, selon vos besoins. 

Après avoir créé le service, vous pouvez passer à la page [Politiques](/./rules/firewall-policies/firewall-policies.md) pour spécifier ses détails.

#### Modèle de service

Vous pouvez enregistrer la configuration de votre service en cliquant sur le bouton `📄Save template`. Lorsque vous y êtes invité, saisissez un nom distinctif et un résumé clair et descriptif pour pouvoir le retrouver et le réutiliser facilement ultérieurement. 

![save_template.png](./screenshots/save_template.png ':size=500')

 
 Vous pouvez utiliser les modèles enregistrés lors de la création d’un nouveau service en cliquant sur le bouton `📄Load template` en bas de la page, en sélectionnant le modèle de service approprié et en cliquant sur le bouton `➢ Apply template`.

![load_template.png](./screenshots/load_template.png ':size=500')


#### Rechercher des services

Vous pouvez rechercher un service dans la liste à l’aide du champ de recherche situé en haut de la page. Cela vous permet de trouver et de gérer rapidement le service recherché.

#### Mettre à jour des services
Vous pouvez modifier les services en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de leur ligne.

![update_service.png](./screenshots/update_service.png ':size=800')

Vous pouvez alors :

- Modifier le **nom du service**.
- Ajouter, supprimer ou modifier des **règles d’accès**.

> [!IMPORTANT]
> N’oubliez pas de soumettre le service en cliquant sur le bouton `➢ Submit`.

Vous pouvez utiliser le bouton `Clear changes` si vous décidez de ne pas soumettre les modifications.


#### Supprimer des services

Vous pouvez supprimer des services en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') de leur ligne.

 Un avertissement s’affiche avant la suppression définitive du service :
 
![Capture d’écran de l’avertissement de suppression](./screenshots/delete_service.png ':size=400')


## **![](../../images/menu/menu_services.png ':size=28') Politiques de pare-feu**

Les **politiques** de la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_** offrent une approche complète et centralisée de la gestion des règles de sécurité réseau. Contrairement aux systèmes traditionnels fondés sur des règles, les politiques définissent les autorisations d’accès en spécifiant les **sources**, les **destinations** et les **services** dans un cadre unifié.

Les politiques offrent plusieurs avantages par rapport aux configurations de règles traditionnelles :

- **Gestion simplifiée** : créez une seule politique au lieu de plusieurs règles individuelles
- **Sécurité centrée sur les services** : associez directement les services aux autorisations d’accès
- **Contrôle basé sur les entités** : utilisez des groupes, des appareils, des utilisateurs et des réseaux comme composants des politiques
- **Vue d’ensemble centralisée** : affichez toutes les règles d’accès dans une interface unique et organisée

> [!INFO]
> Les politiques remplacent et regroupent les fonctionnalités d’anciennes options telles que Group Traffic, Allow Custom Ports et Attribute Services, pour offrir une approche de gestion de la sécurité plus intuitive et évolutive.

### Prérequis

Avant de créer des politiques, assurez-vous que les composants suivants sont configurés :

#### 1. Dépendances requises

- **Services** : au moins un service doit être créé pour pouvoir l’associer à une politique
- **Contrôleur réseau** : un contrôleur cloud doit être en cours d’exécution pour activer la connectivité SASE

#### 2. Sources d’entités facultatives

Les politiques peuvent utiliser n’importe quelle combinaison des types d’entités suivants comme sources et destinations :

- **[Groupes](/./company/groups/groups.md)** : groupes d’utilisateurs ou d’appareils
- **[Serveurs](/./devices/servers/servers.md)** : serveurs backend et infrastructure
- **[NIAC](/./devices/niacs/niacs.md)** : Network Isolation Access Clients
- **[Appareils natifs](/./devices/nativedevices/nativedevices.md)** : appareils physiques sur le réseau
- **[Utilisateurs Network Isolation](/./company/users/users.md)** : utilisateurs individuels ayant accès au réseau
- **[Appareils utilisateur](/./devices/userdevices/userdevices.md)** : appareils des utilisateurs finaux (ordinateurs portables, mobiles, etc.)
- **[Réseaux natifs](/./devices/nativenetworks/index.md)** : segments de réseau physiques

### Créer une politique

Pour créer une nouvelle politique, cliquez sur le bouton `+ Create new` dans le coin supérieur droit de la page Politiques.

![create_policy.png](./screenshots/create_policy.png ':size=500')

##### Paramètres de base

 1. **Nom de la politique** : donnez à la politique un nom clair et descriptif
 2. **Activée** : utilisez le bouton bascule pour activer ou désactiver la politique
 3. **Source de migration** (le cas échéant) : affiche la source de la règle d’origine si cette politique a été migrée depuis une ancienne configuration.
    <!-- Click [here](#policy-migration) for migration overview.  -->

##### Configurer les services

Sélectionnez les services régis par cette politique. Les services définissent les applications, les sites web ou les ressources auxquels les utilisateurs peuvent accéder par l’intermédiaire de cette politique.

 1. Cliquez sur `+ Add Services` pour choisir parmi les services disponibles.
 2. Plusieurs services peuvent être ajoutés à une même politique.
<!-- 3. Each service shows its configured access rules and destinations. -->

![add_service.png](./screenshots/add_service.png ':size=500')



##### Définir les sources

Les sources représentent **qui** peut accéder aux services définis dans cette politique. Comme indiqué précédemment, vous pouvez ajouter plusieurs entités sources :

 1. Cliquez sur `+ Add Sources` pour ouvrir la boîte de dialogue de sélection des entités
 2. Choisissez parmi les types d’entités disponibles :

    - **[Groupes](/./company/groups/groups.md)** : sélectionnez des groupes d’utilisateurs ou d’appareils
    - **[Serveurs](/./devices/servers/servers.md)** : choisissez des serveurs spécifiques
    - **[NIAC](/./devices/niacs/niacs.md)** : choisissez des Network Isolation Access Clients
    - **[Appareils natifs](/./devices/nativedevices/nativedevices.md)** : sélectionnez des appareils réseau physiques
    - **[Utilisateurs](/./company/users/users.md)** : choisissez des utilisateurs individuels
    - **[Appareils utilisateur](/./devices/userdevices/userdevices.md)** : choisissez des appareils spécifiques d’un utilisateur
    - **[Réseaux natifs](/./devices/nativenetworks/index.md)** : sélectionnez des segments de réseau

 3. **Rechercher et filtrer** : utilisez la fonction de recherche pour trouver rapidement des entités spécifiques

![add_source.png](./screenshots/add_source.png ':size=500')

 4. **Sélection multiple** : ajoutez autant d’entités sources que nécessaire pour votre politique

##### Définir les destinations

Les destinations représentent **où** les sources peuvent se connecter. Elles définissent les ressources cibles auxquelles les sources peuvent accéder :

 1. Cliquez sur `+ Add Destinations` pour sélectionner des entités de destination
 2. Choisissez parmi les mêmes types d’entités que ceux disponibles pour les sources
 3. Les destinations comprennent généralement :
    - **[Serveurs](/./devices/servers/servers.md)** hébergeant les services
    - **[Groupes](/./company/groups/groups.md)** contenant les ressources cibles
    - **[Réseaux natifs](/./devices/nativenetworks/index.md)** contenant des ressources accessibles
    - **Toutes les autres entités** fournissant des services


![add_destination.png](./screenshots/add_destination.png ':size=500')

> [!INFO]
> N’oubliez pas de cliquer sur le bouton d’enregistrement en bas de chaque fenêtre. 

##### Entrées de service

 1. Cliquez sur `+ Add Service entry` pour ajouter une entrée de service.
 2. Choisissez un nom pour l’entrée.
 3. Choisissez une action.
 4. Saisissez l’URL ou le chemin d’accès correct dont le service a besoin pour effectuer l’action.

![service_entry.png](./screenshots/service_entry.png ':size=700')



##### Soumettre la politique

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
- **Destinations** : entités cibles accessibles
- **Activée** : état actuel de la politique (active/inactive)

![policies_overview.png](./screenshots/policies_overview.png ':size=700')

> [!NOTE]
>Si l’un des champs est laissé vide, un point d’exclamation jaune apparaît sur la ligne de la politique.

###### Activer/désactiver des politiques

Modifiez l’état de la politique directement depuis le tableau principal :

 1. Cliquez sur le **bouton bascule Activer/Désactiver** de la ligne de la politique
 2. L’état de la politique est mis à jour immédiatement
 3. Les politiques désactivées cessent d’appliquer les règles d’accès, mais leur configuration est conservée

> [!TIP]
> Vous pouvez actualiser la liste des politiques en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

##### Mettre à jour des politiques

Pour modifier une politique existante :

 1. Cliquez sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de la ligne de la politique.
 2. Apportez les modifications nécessaires dans les sections concernées
 3. Cliquez sur `➢ Submit` pour enregistrer les modifications

![update_policy.png](./screenshots/update_policy.png ':size=500')

##### Supprimer des politiques

Cliquez sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') de la ligne de la politique pour la supprimer.

Un avertissement s’affiche avant la suppression définitive de la politique :

![delete_policy.png](./screenshots/delete_policy.png ':size=400')

> [!WARNING]
> La suppression d’une politique supprime immédiatement et définitivement toutes les règles d’accès qui lui sont associées. Les utilisateurs peuvent perdre l’accès aux services si aucune autre politique ne leur en accorde l’autorisation.

### Migration des politiques

Le système migre automatiquement les anciennes règles des configurations précédentes :

- Règles **Attribute Service** → politiques basées sur les services
- Règles **Group Traffic** → politiques de groupe à groupe
- Règles **Allow Custom Ports** → politiques spécifiques aux ports

Les politiques migrées affichent leur source d’origine dans la section Paramètres de base, ce qui vous aide à comprendre l’historique et le contexte de la règle.

### Bonnes pratiques

#### Organisation des politiques

- **Utilisez des noms descriptifs** qui indiquent clairement l’objectif de la politique
- **Regroupez les services associés** dans une même politique, le cas échéant
- **Séparez les règles d’accès critiques et non critiques** dans différentes politiques
- **Utilisez des groupes** plutôt que des entités individuelles lorsque cela est possible

#### Considérations de sécurité

- **Appliquez le principe du moindre privilège** : n’accordez que les accès nécessaires
- **Examinez régulièrement les politiques** pour vous assurer qu’elles répondent aux besoins actuels de l’entreprise
- **Utilisez des groupes plutôt que des entités individuelles** pour faciliter la gestion

> [!INFO]
> Les politiques offrent des pistes d’audit et des fonctionnalités de journalisation qui facilitent la supervision de l’utilisation et la résolution des problèmes de connexion.
<!-- making it easier to track access patterns and troubleshoot connectivity issues.-->
### Dépannage

#### Problèmes courants

 **La politique ne prend pas effet**

  - Vérifiez que la politique est **activée**
  - Vérifiez que le **contrôleur réseau est en cours d’exécution**
  - Assurez-vous que les **sources et les destinations** sont correctement configurées
  - Vérifiez que les **services** sont correctement définis et actifs

 **Accès refusé malgré la politique**

- Vérifiez que les **règles d’accès aux services** définissent des plages de ports correctes
- Vérifiez les **appartenances aux entités** (utilisateurs dans des groupes, appareils dans des réseaux)
- Assurez-vous que les **destinations incluent les ressources cibles**

## **![](../../images/menu/menu_services.png ':size=28') Politiques de posture**


## **![](../../images/menu/menu_services.png ':size=28') Politiques sans agent**


<!-- tabs:end -->
