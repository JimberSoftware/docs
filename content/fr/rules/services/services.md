File: rules/services/services.md

# ![](../../images/menu/menu_services.png ':size=28') Services

Au sein de la **_Plateforme Jimber SASE_**, un **service** représente une ressource numérique pouvant être mise à la disposition des utilisateurs. Ces services peuvent inclure des sites web, des portails internes, des bureaux à distance, des CRM ou toute autre application basée sur le réseau.

Pour rendre un service disponible, il doit être associé à un **groupe** et à une **destination** sur la page [**Politiques**](/./rules/firewall-policies/firewall-policies.md). Une fois cette configuration effectuée, le service apparaît dans le [**Panneau de sécurité**](/./rules/security_panel/security_panel.md) des utilisateurs membres du groupe sélectionné.

Les utilisateurs peuvent ouvrir le Panneau de sécurité en cliquant sur l’**icône Jimber SASE dans la zone de notification** de leur barre des tâches.

![Capture d’écran du menu de la zone de notification Jimber](./screenshots/security_panel.png ':size=300')

Un panneau de sécurité comportant plusieurs services peut se présenter ainsi :

![Capture d’écran de l’onglet Services du Panneau de sécurité](./screenshots/security_panel_overview.png ':size=600')


### Créer des services

Pour créer un service sur la plateforme, cliquez sur le bouton `+ Create new` situé dans le coin supérieur droit de l’interface.

![Capture d’écran de la page Services](./screenshots/services.png ':size=700')

L’écran suivant s’ouvre. Vous pouvez y saisir les détails de votre service :

![Capture d’écran de la page de création d’un service](./screenshots/create_service.png ':size=700')

1. **Choisir un nom** : Commencez par donner à votre service un nom clair et facile à reconnaître.

> [!NOTE]
> Vous pouvez commencer avec un modèle (voir ci-dessous) ou créer un service entièrement nouveau. 


<!-- 2. **Create a New Service Entry**: Click `+ Create new service entry`. This defines how the service behaves.

    - **Name**: Provide a recognizable name to the service entry.
    - **Action**: Currently, the only available option is **"Open website"**.
    - **URL/Path**: Enter the web address or internal path the service should open. -->

2. **Ajouter une règle d’accès** : Cliquez sur `+ Add Access Rule`. Cela définit le trafic autorisé pour le service.

    - **Description** : Décrivez brièvement l’objectif de la règle.
    - **Port de début / port de fin** : Indiquez la plage de ports à autoriser. Si les champs sont laissés vides, les valeurs par défaut `1` et `65535` sont utilisées.
    - **Protocole** : Choisissez le protocole utilisé par le service (TCP, UDP ou ICMP).
    
    ![add_access_rule.png](./screenshots/add_access_rule.png ':size=500')

3. **Envoyer le service** en cliquant sur le bouton `➢ Submit`. 
Si vous quittez la page alors que des modifications ne sont pas enregistrées, un message d’avertissement s’affiche :

    ![Capture d’écran de l’avertissement relatif aux modifications non enregistrées](../../images/notifications/unsaved_changes.png ':size=300')

**Répétez ces étapes** pour configurer d’autres règles d’accès, si nécessaire. 

Après avoir créé le service, vous pouvez accéder à la page [Politiques](/./rules/firewall-policies/firewall-policies.md) pour en préciser les détails.

### Modèle de service

Vous pouvez enregistrer la configuration de votre service en cliquant sur le bouton `📄Save template`. Lorsque vous y êtes invité, saisissez un nom distinctif et un résumé clair et descriptif afin de pouvoir facilement l’identifier et le réutiliser ultérieurement. 

![save_template.png](./screenshots/save_template.png ':size=500')

 
 Tous les modèles enregistrés peuvent être utilisés lors de la création d’un service en cliquant sur le bouton `📄Load template` en bas de la page, en sélectionnant le modèle de service approprié, puis en cliquant sur le bouton `➢ Apply template`.

![load_template.png](./screenshots/load_template.png ':size=500')


### Rechercher des services

Vous pouvez rechercher des services dans la liste à l’aide du champ de recherche situé en haut de la page. Vous pouvez ainsi trouver et gérer rapidement le service recherché.

### Mettre à jour des services
Vous pouvez modifier les services en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de leur ligne.

![update_service.png](./screenshots/update_service.png ':size=800')

Vous pouvez :

- Modifier le **nom du service**.
- Ajouter, supprimer ou modifier des **règles d’accès**.

> [!IMPORTANT]
> N’oubliez pas d’envoyer le service en cliquant sur le bouton `➢ Submit`.

Vous pouvez utiliser le bouton `Clear changes` si vous décidez de ne pas envoyer les modifications.


### Supprimer des services

Vous pouvez supprimer des services en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') de leur ligne.

 Un avertissement s’affiche avant la suppression définitive du service :
 
![Capture d’écran de l’avertissement de suppression](./screenshots/delete_service.png ':size=300')
