# ![](../../images/menu/menu_services.png ':size=28') Services

Au sein de la **_<span style="color: darkblue;">Jimber SASE Platform</span>_**
, un **service** représente une ressource numérique qui peut être mise à la disposition des utilisateurs. Ces services peuvent inclure des sites web, des portails internes, des bureaux à distance, des CRM ou toute autre application basée sur le réseau.

Pour rendre un service disponible, il doit être associé à un **groupe** et à une **destination** sur la page [**Politiques**](/./rules/firewall-policies/firewall-policies.md). Une fois cette configuration effectuée, le service apparaîtra dans le [**Panneau de sécurité**](/./rules/security_panel/security_panel.md) des utilisateurs membres du groupe sélectionné.

Les utilisateurs peuvent ouvrir le Panneau de sécurité en cliquant sur l’**icône Jimber SASE dans la barre d’état système** de leur barre des tâches.

![Capture d’écran du menu Jimber dans la barre d’état système](./screenshots/security_panel.png ':size=300')

Un panneau de sécurité comportant plusieurs services peut ressembler à ceci :

![Capture d’écran de l’onglet Services du Panneau de sécurité](./screenshots/security_panel_overview.png ':size=600')


### Créer des services

Pour créer un service sur la plateforme, cliquez sur le bouton `+ Create new` situé dans le coin supérieur droit de l’interface.

![Capture d’écran de la page Services](./screenshots/services.png ':size=600')

L’écran suivant s’ouvrira. Vous pourrez y saisir les détails de votre service :

![Capture d’écran de la page de création d’un service](./screenshots/create_service.png ':size=600')

1. **Choisir un nom** : commencez par donner à votre service un nom clair et reconnaissable.

> [!NOTE]
> Vous pouvez commencer avec un modèle (voir ci-dessous) ou créer un service entièrement nouveau. 


<!-- 2. **Create a New Service Entry**: Click `+ Create new service entry`. This defines how the service behaves.

    - **Name**: Provide a recognizable name to the service entry.
    - **Action**: Currently, the only available option is **"Open website"**.
    - **URL/Path**: Enter the web address or internal path the service should open. -->

2. **Ajouter une règle d’accès** : cliquez sur `+ Add Access Rule`. Cela définit le trafic autorisé pour le service.

    - **Description** : décrivez brièvement l’objectif de la règle.
    - **Port de début / Port de fin** : indiquez la plage de ports à autoriser. Si ces champs sont laissés vides, les valeurs par défaut sont `1` et `65535`.
    - **Protocole** : choisissez le protocole utilisé par le service (TCP, UDP ou ICMP).
    
    ![add_access_rule.png](./screenshots/add_access_rule.png ':size=500')

3. **Soumettre le service** en cliquant sur le bouton `➢ Submit`. 
Si vous quittez la page alors que des modifications ne sont pas enregistrées, un message d’avertissement s’affichera :

    ![Capture d’écran de l’avertissement concernant les modifications non enregistrées](../../images/notifications/unsaved_changes.png ':size=300')

**Répétez ces étapes** pour configurer d’autres règles d’accès si nécessaire. 

Après avoir créé le service, vous pouvez accéder à [Politiques](/./rules/firewall-policies/firewall-policies.md) pour en préciser les détails.

### Modèles de service

Vous pouvez enregistrer la configuration de votre service en cliquant sur le bouton `📄Save template`. Lorsque vous y êtes invité, saisissez un nom distinctif et un résumé clair et descriptif afin de pouvoir facilement l’identifier et le réutiliser par la suite. 

![save_template.png](./screenshots/save_template.png ':size=500')

 
 Tous les modèles enregistrés peuvent être utilisés lors de la création d’un nouveau service. Pour cela, cliquez sur le bouton `📄Load template` au bas de la page, sélectionnez le modèle de service approprié, puis cliquez sur le bouton `➢ Apply template`.

![load_template.png](./screenshots/load_template.png ':size=500')


### Rechercher des services

Vous pouvez rechercher un service dans la liste à l’aide du champ de recherche situé en haut de la page. Cela vous permet de trouver et de gérer rapidement le service recherché.

> [!TIP]
> Vous pouvez actualiser la liste des services en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

### Mettre à jour des services
Vous pouvez modifier les services en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') dans leur ligne.

![update_service.png](./screenshots/update_service.png ':size=800')

Vous pouvez alors :

- Modifier le **nom du service**.
- Ajouter, supprimer ou modifier des **règles d’accès**.

> [!IMPORTANT]
> N’oubliez pas de soumettre le service en cliquant sur le bouton `➢ Submit`.

Vous pouvez utiliser le bouton `Clear changes` si vous décidez de ne pas soumettre les modifications.


### Supprimer des services

Vous pouvez supprimer des services en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') dans leur ligne.

 Vous recevrez un avertissement avant la suppression définitive du service :
 
![Capture d’écran de l’avertissement de suppression](./screenshots/delete_service.png ':size=400')
