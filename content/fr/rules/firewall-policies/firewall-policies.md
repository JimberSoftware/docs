# ![](../../images/menu/menu_policies.png ':size=28') Politiques

<!-- tabs:start -->

## **![](../../images/menu/menu_services.png ':size=28') Services de pare-feu**

Au sein de la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_**, un **service** représente une ressource numérique pouvant être rendue accessible aux utilisateurs. Ces services peuvent inclure des sites web, des portails internes, des bureaux à distance, des CRM ou toute autre application réseau.

Pour rendre un service disponible, il doit être attribué à un **groupe** et à une **destination** sur la page [**Politiques**](/./rules/firewall-policies/firewall-policies.md). Une fois cette configuration effectuée, le service apparaîtra dans le [**Panneau de sécurité**](/./rules/security_panel/security_panel.md) des utilisateurs membres du groupe sélectionné.

Les utilisateurs peuvent ouvrir le Panneau de sécurité en cliquant sur l’**icône Jimber SASE dans la zone de notification** de leur barre des tâches.

![Capture d’écran du menu de la zone de notification Jimber](./screenshots/security_panel.png ':size=300')

Un panneau de sécurité avec plusieurs services peut se présenter ainsi :

![Capture d’écran de l’onglet Services du Panneau de sécurité](./screenshots/security_panel_overview.png ':size=600')


#### Créer des services

Pour créer un service sur la plateforme, cliquez sur le bouton `+ Create new` situé dans le coin supérieur droit de l’interface.

![Capture d’écran de la page Services](./screenshots/services.png ':size=600')

L’écran suivant s’ouvrira et vous permettra de saisir les détails de votre service :

![Capture d’écran de la page de création d’un service](./screenshots/create_service.png ':size=600')

1. **Choisir un nom** : Commencez par donner à votre service un nom clair et reconnaissable.

> [!NOTE]
> Vous pouvez commencer par utiliser un modèle (voir ci-dessous) ou créer un service entièrement nouveau.


<!-- 2. **Create a New Service Entry**: Click `+ Create new service entry`. This defines how the service behaves.

    - **Name**: Provide a recognizable name to the service entry.
    - **Action**: Currently, the only available option is **"Open website"**.
    - **URL/Path**: Enter the web address or internal path the service should open. -->

2. **Ajouter une règle d’accès** : Cliquez sur `+ Add Access Rule`. Cela définit la manière dont le trafic est autorisé pour le service.

    - **Description** : Décrivez brièvement l’objectif de la règle.
    - **Port de début / port de fin** : Indiquez la plage de ports à autoriser. Si vous laissez ces champs vides, les valeurs par défaut `1` et `65535` seront utilisées.
    - **Protocole** : Choisissez le protocole utilisé par le service (TCP, UDP ou ICMP).
    
    ![add_access_rule.png](./screenshots/add_access_rule.png ':size=500')

3. **Soumettre le service** en cliquant sur le bouton `➢ Submit`.
Si vous quittez la page alors que des modifications ne sont pas enregistrées, un message d’avertissement s’affichera :

    ![Capture d’écran de l’avertissement concernant les modifications non enregistrées](../../images/notifications/unsaved_changes.png ':size=300')

**Répétez ces étapes** pour configurer d’autres règles d’accès si nécessaire.

Après avoir créé le service, vous pouvez passer à la page [Politiques](/./rules/firewall-policies/firewall-policies.md) pour en préciser les détails.

#### Modèle de service

Vous pouvez enregistrer la configuration de votre service en cliquant sur le bouton `📄Save template`. Lorsque vous y êtes invité, saisissez un nom distinctif et un résumé clair et descriptif pour pouvoir facilement le reconnaître et le réutiliser ultérieurement.

![save_template.png](./screenshots/save_template.png ':size=500')

 
 Vous pouvez utiliser les modèles enregistrés lors de la création d’un service en cliquant sur le bouton `📄Load template` au bas de la page, en sélectionnant le modèle de service approprié, puis en cliquant sur le bouton `➢ Apply template`.

![load_template.png](./screenshots/load_template.png ':size=500')


#### Rechercher des services

Vous pouvez rechercher un service dans la liste à l’aide du champ de recherche situé en haut de la page. Cela vous permet de trouver et de gérer rapidement le service souhaité.

> [!TIP]
> Vous pouvez actualiser la liste des services en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

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

 Un avertissement s’affichera avant la suppression définitive du service :
 
![Capture d’écran de l’avertissement de suppression](./screenshots/delete_service.png ':size=400')


## **![](../../images/menu/menu_services.png ':size=28') Politiques de pare-feu**

Les **politiques** de la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_** offrent une approche complète et centralisée de la gestion des règles de sécurité réseau. Contrairement aux systèmes traditionnels fondés sur des règles, les politiques définissent les autorisations d’accès en précisant les **sources**, les **destinations** et les **services** dans un cadre unifié.

Les politiques présentent plusieurs avantages par rapport aux configurations de règles traditionnelles :

- **Gestion simplifiée** : Créez une politique au lieu de plusieurs règles individuelles
- **Sécurité axée sur les services** : Associez directement les services aux autorisations d’accès
- **Contrôle fondé sur les entités** : Utilisez des groupes, des appareils, des utilisateurs et des réseaux comme composants des politiques
- **Vue d’ensemble centralisée** : Consultez toutes les règles d’accès dans une interface unique et organisée

> [!INFO]
> Les politiques remplacent et regroupent les fonctionnalités des anciennes options telles que Group Traffic, Allow Custom Ports et Attribute Services, offrant ainsi une approche plus intuitive et évolutive de la gestion de la sécurité.

### Prérequis

Avant de créer des politiques, assurez-vous que les composants suivants sont configurés :

#### 1. Dépendances requises

- **Services** : Au moins un service doit être créé pour être associé à une politique
- **Contrôleur réseau** : Un contrôleur cloud doit être en cours d’exécution pour activer la connectivité SASE

#### 2. Sources d’entités facultatives

Les politiques peuvent utiliser n’importe quelle combinaison des types d’entités suivants comme sources et destinations :

- **[Groupes](/./company/groups/groups.md)** : Groupes d’utilisateurs ou d’appareils
- **[Serveurs](/./devices/servers/servers.md)** : Serveurs backend et infrastructure
- **[NIAC](/./devices/niacs/niacs.md)** : Clients d’accès pour l’isolation réseau
- **[Appareils natifs](/./devices/nativedevices/nativedevices.md)** : Appareils physiques sur le réseau
- **[Utilisateurs avec isolation réseau](/./company/users/users.md)** : Utilisateurs individuels disposant d’un accès réseau
- **[Appareils utilisateur](/./devices/userdevices/userdevices.md)** : Appareils des utilisateurs finaux (ordinateurs portables, mobiles, etc.)
- **[Réseaux natifs](/./devices/nativenetworks/index.md)** : Segments de réseau physiques

### Créer une politique

Pour créer une nouvelle politique, cliquez sur le bouton `+ Create new` dans le coin supérieur droit de la page Politiques.

![create_policy.png](./screenshots/create_policy.png ':size=500')

##### 1. Paramètres de base

 1. **Nom de la politique** : Donnez à la politique un nom clair et descriptif
 2. **Activée** : Utilisez le bouton bascule pour activer ou désactiver la politique
 3. **Source de migration** (le cas échéant) : Affiche la source de la règle d’origine si cette politique a été migrée à partir d’anciennes configurations.
    <!-- Click [here](#policy-migration) for migration overview.  -->

##### 2. Configurer les services

Sélectionnez les services régis par cette politique. Les services définissent les applications, les sites web ou les ressources auxquels les utilisateurs peuvent accéder par l’intermédiaire de cette politique.

 1. Cliquez sur `+ Add Services` pour choisir parmi les services disponibles.
 2. Plusieurs services peuvent être ajoutés à une seule politique.
<!-- 3. Each service shows its configured access rules and destinations. -->

![add_service.png](./screenshots/add_service.png ':size=500')



##### 3. Définir les sources

Les sources représentent **qui** peut accéder aux services définis dans cette politique. Comme indiqué précédemment, vous pouvez ajouter plusieurs entités sources :

 1. Cliquez sur `+ Add Sources` pour ouvrir la boîte de dialogue de sélection des entités
 2. Choisissez parmi les types d’entités disponibles :

    - **[Groupes](/./company/groups/groups.md)** : Sélectionnez des groupes d’utilisateurs ou d’appareils
    - **[Serveurs](/./devices/servers/servers.md)** : Choisissez des serveurs spécifiques
    - **[NIAC](/./devices/niacs/niacs.md)** : Sélectionnez des clients d’accès pour l’isolation réseau
    - **[Appareils natifs](/./devices/nativedevices/nativedevices.md)** : Sélectionnez des appareils réseau physiques
    - **[Utilisateurs](/./company/users/users.md)** : Choisissez des utilisateurs individuels
    - **[Appareils utilisateur](/./devices/userdevices/userdevices.md)** : Sélectionnez des appareils spécifiques d’un utilisateur
    - **[Réseaux natifs](/./devices/nativenetworks/index.md)** : Sélectionnez des segments de réseau

 3. **Rechercher et filtrer** : Utilisez la fonction de recherche pour trouver rapidement des entités spécifiques

![add_source.png](./screenshots/add_source.png ':size=500')

 4. **Sélection multiple** : Ajoutez autant d’entités sources que nécessaire pour votre politique

##### 4. Définir les destinations

Les destinations représentent **où** les sources peuvent se connecter. Elles définissent les ressources cibles auxquelles les sources peuvent accéder :

 1. Cliquez sur `+ Add Destinations` pour sélectionner des entités de destination
 2. Choisissez parmi les mêmes types d’entités que ceux disponibles pour les sources
 3. Les destinations comprennent généralement :
    - **[Serveurs](/./devices/servers/servers.md)** hébergeant les services
    - **[Groupes](/./company/groups/groups.md)** contenant les ressources cibles
    - **[Réseaux natifs](/./devices/nativenetworks/index.md)** donnant accès à des ressources
    - **Toutes les autres entités** fournissant des services


![add_destination.png](./screenshots/add_destination.png ':size=500')

> [!INFO]
> N’oubliez pas de cliquer sur le bouton d’enregistrement au bas de chaque fenêtre.

##### 5. Entrées de service

 1. Cliquez sur `+ Add Service entry` pour ajouter une entrée de service.
 2. Choisissez un nom pour l’entrée.
 3. Choisissez une action.
 4. Saisissez l’URL ou le chemin d’accès approprié dont le service a besoin pour exécuter l’action.

![service_entry.png](./screenshots/service_entry.png ':size=700')



##### 6. Soumettre la politique

Une fois toutes les sections configurées :

 1. Vérifiez la configuration de votre politique
 2. Cliquez sur `➢ Submit` pour enregistrer et activer la politique
 3. Si elle est activée, la politique prend effet immédiatement

### Gérer les politiques existantes

##### Afficher la liste des politiques

La page principale Politiques affiche toutes les politiques configurées sous forme de tableau :

**Colonnes du tableau :**

- **Nom** : Identifiant de la politique
- **Services** : Services régis par cette politique
- **Sources** : Entités pouvant initier un accès
- **Destinations** : Entités cibles accessibles
- **Activée** : État actuel de la politique (active/inactive)

![policies_overview.png](./screenshots/policies_overview.png ':size=700')

> [!NOTE]
>Si un élément est laissé vide, un point d’exclamation jaune apparaîtra sur la ligne de la politique.

###### Activer/désactiver des politiques

Modifiez l’état d’une politique directement depuis le tableau principal :

 1. Cliquez sur le **bouton bascule Activer/Désactiver** de la ligne de la politique
 2. L’état de la politique est mis à jour immédiatement
 3. Les politiques désactivées cessent d’appliquer les règles d’accès, mais restent configurées

> [!TIP]
> Vous pouvez actualiser la liste des politiques en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

##### Mettre à jour des politiques

Pour modifier une politique existante :

 1. Cliquez sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de la ligne de la politique.
 2. Apportez les modifications nécessaires à l’une des sections
 3. Cliquez sur `➢ Submit` pour enregistrer les modifications

![update_policy.png](./screenshots/update_policy.png ':size=500')

##### Supprimer des politiques

Cliquez sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') de la ligne de la politique pour supprimer celle-ci.

Un avertissement s’affichera avant la suppression définitive de la politique :

![delete_policy.png](./screenshots/delete_policy.png ':size=400')

> [!WARNING]
> La suppression d’une politique supprime immédiatement et définitivement toutes les règles d’accès qui lui sont associées. Les utilisateurs peuvent perdre l’accès aux services si aucune autre politique ne leur accorde l’autorisation.

### Migration des politiques

Le système migre automatiquement les anciennes règles des configurations précédentes :

- **Règles Attribute Service** → Politiques fondées sur les services
- **Règles Group Traffic** → Politiques de groupe à groupe
- **Règles Allow Custom Ports** → Politiques spécifiques aux ports

Les politiques migrées affichent leur source d’origine dans la section Paramètres de base, ce qui vous aide à comprendre l’historique et le contexte de la règle.

### Bonnes pratiques

#### Organisation des politiques

- **Utilisez des noms descriptifs** qui indiquent clairement l’objectif de la politique
- **Regroupez les services associés** dans une seule politique lorsque cela est approprié
- **Séparez les règles d’accès critiques et non critiques** dans différentes politiques
- **Utilisez des groupes** plutôt que des entités individuelles dans la mesure du possible

#### Considérations de sécurité

- **Appliquez le principe du moindre privilège** : n’accordez que les accès nécessaires
- **Examinez régulièrement les politiques** pour vous assurer qu’elles répondent aux besoins actuels de l’entreprise
- **Utilisez des groupes plutôt que des entités individuelles** pour faciliter la gestion

> [!INFO]
> Les politiques fournissent des pistes d’audit et des fonctionnalités de journalisation, ce qui facilite la supervision de l’utilisation et la résolution des problèmes de connexion.
<!-- making it easier to track access patterns and troubleshoot connectivity issues.-->
### Dépannage

#### Problèmes fréquents

 **La politique ne prend pas effet**

  - Vérifiez que la politique est **activée**
  - Vérifiez que le **contrôleur réseau est en cours d’exécution**
  - Assurez-vous que les **sources et les destinations** sont correctement configurées
  - Vérifiez que les **services** sont correctement définis et actifs

 **Accès refusé malgré la politique**

  - Vérifiez que les **règles d’accès des services** indiquent les plages de ports appropriées
  - Vérifiez les **appartenances aux entités** (utilisateurs dans des groupes, appareils dans des réseaux)
  - Assurez-vous que les **destinations incluent les ressources cibles**


## **![](../../images/menu/menu_services.png ':size=28') Politiques de posture**

Une politique de posture est un ensemble de règles et de critères de décision automatisés qui évaluent si un système, un appareil ou une application répond à une norme de conformité ou de sécurité requise avant d’être autorisé à accéder à un réseau ou à un environnement de production.

### Créer une politique de posture

Pour créer une politique de posture sur la plateforme, cliquez sur le bouton `+ Create new` situé dans le coin supérieur droit de l’interface.

![posture_policy.png](./screenshots/posture_policy.png ':size=600')

![create_posture_policy.png](./screenshots/create_posture_policy.png ':size=400')

1. Sélectionnez le contrôle de posture que cette politique doit évaluer.
2. Sélectionnez les systèmes d’exploitation sur lesquels cette politique de posture sera activée.
3. Choisissez les paramètres souhaités.
4. Choisissez où la politique est requise : pour la connexion au réseau SASE et/ou l’authentification cloud.
5. Créez la politique en cliquant sur le bouton `Create`.

![posture_policy_settings.png](./screenshots/posture_policy_settings.png ':size=400')

>[!ATTENTION]
>Un avertissement important s’affiche avant la création de la politique !
>
>![warning_posture_policy.png](./screenshots/warning_posture_policy.png ':size=400')

### Activer/désactiver des politiques

Modifiez l’état d’une politique directement depuis le tableau principal :

 1. Cliquez sur le **bouton bascule Activer/Désactiver** de la ligne de la politique.
 2. L’état de la politique est mis à jour immédiatement.
 3. Les politiques désactivées cessent d’appliquer les règles d’accès, mais restent configurées.

> [!TIP]
> Vous pouvez actualiser la liste des politiques en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

### Modifier une politique de posture

Vous pouvez modifier les politiques de posture en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de leur ligne.

Les options sont les mêmes que lors de la création de la politique. Naturellement, le contrôle de posture sélectionné ne peut pas être modifié.

### Supprimer une politique de posture

Vous pouvez supprimer les politiques de posture en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') de leur ligne.

 Un avertissement s’affichera avant la suppression définitive de la politique :

![Capture d’écran de l’avertissement de suppression](./screenshots/delete_posture_policy.png ':size=400')


## **![](../../images/menu/menu_services.png ':size=28') Politiques sans agent**

Les politiques sans agent sont des règles et des cadres de gouvernance appliqués aux systèmes, aux charges de travail cloud ou aux appareils réseau sans qu’il soit nécessaire d’installer un agent logiciel dédié directement sur chaque terminal cible.

### Créer une politique sans agent

Pour créer une politique sans agent sur la plateforme, cliquez sur le bouton `+ Create new` situé dans le coin supérieur droit de l’interface.

![agentless_policy.png](./screenshots/agentless_policies.png ':size=600')

![create_agentless_policy.png](./screenshots/create_agentless_policy.png ':size=300')

1. Choisissez un nom pour la politique (obligatoire).
2. Sélectionnez au moins un service : SSH et/ou RDP.
3. Ajoutez au moins une source : un groupe et/ou un utilisateur.
4. Ajoutez au moins une destination : un groupe, un serveur, un appareil natif et/ou un appareil NIAC.
5. Créez la politique en cliquant sur le bouton `Create`.

### Activer/désactiver des politiques

Modifiez l’état d’une politique directement depuis le tableau principal :

 1. Cliquez sur le **bouton bascule Activer/Désactiver** de la ligne de la politique.
 2. L’état de la politique est mis à jour immédiatement.
 3. Les politiques désactivées cessent d’appliquer les règles d’accès, mais restent configurées.

> [!TIP]
> Vous pouvez actualiser la liste des politiques en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.


### Modifier une politique sans agent

Vous pouvez modifier les politiques sans agent en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de leur ligne.

Les options sont les mêmes que lors de la création de la politique.

### Supprimer une politique sans agent

Vous pouvez supprimer les politiques sans agent en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') de leur ligne.

 Un avertissement s’affichera avant la suppression définitive de la politique :

![Capture d’écran de l’avertissement de suppression](./screenshots/delete_agentless_policy.png ':size=400')


<!-- tabs:end -->
