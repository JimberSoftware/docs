# ![](../../images/menu/menu_scripts.png ':size=28') Scripts d’appareil utilisateur

Dans la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***, vous pouvez créer et gérer des scripts pour les appareils utilisateur dans la section **Scripts d’appareil utilisateur**. Ces scripts sont exécutés sur l’appareil de l’utilisateur et prennent en charge deux types de déclencheurs :

- **À la connexion** – déclenché lorsque l’appareil se connecte à la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** via le **_Jimber SASE Client_**.  
- **À la déconnexion** – déclenché lorsque l’appareil se déconnecte de la plateforme.

Vous pouvez écrire des scripts pour différents systèmes d’exploitation :

- **Windows**
- **macOS**
- **Linux**
- **Windows Server**
- **Linux Server**

![Capture d’écran de la page Scripts d’appareil utilisateur](./screenshots/scripts.png ':size=700')

Cela permet d’automatiser facilement des tâches côté appareil en fonction de l’état de connexion, par exemple en appliquant des règles de pare-feu, en démarrant des services en arrière-plan ou en supprimant des ressources temporaires.

### Créer des scripts d’appareil utilisateur

Pour créer un script dans la plateforme, cliquez sur le bouton `+ Create new` et suivez les étapes ci-dessous :

![Capture d’écran de la fenêtre de création d’un script d’appareil utilisateur](./screenshots/create_script.png ':size=300')


1. **Nom** : Saisissez un nom descriptif pour le script afin de faciliter l’identification de son objectif.
2. **Sélectionner un groupe** : Choisissez le groupe d’utilisateurs auquel le script doit s’appliquer. Le script sera exécuté uniquement pour les utilisateurs membres de ce groupe.
> [!ATTENTION]
> Il est essentiel de sélectionner le bon **groupe** lors de la création du script. Le script sera exécuté uniquement sur les appareils appartenant au groupe spécifié, lorsque la condition de déclenchement définie est remplie. Si le script est associé au mauvais groupe, il risque de ne pas s’exécuter sur les appareils prévus.
3. **Occurrence** : Choisissez si le script doit s’exécuter `On Connect` ou `On Disconnect`.
4. **Plateforme** : Choisissez le système d’exploitation pour lequel le script est prévu (par exemple, Windows, macOS, Linux, etc.).
5. **Activer ou désactiver** : Utilisez le curseur pour activer ou désactiver le script.
6. **Champ de script** : Rédigez ou collez le contenu de votre script dans l’éditeur prévu à cet effet. Assurez-vous qu’il respecte les exigences de la plateforme cible :
> [!ATTENTION]
>- .bat ou .ps1 pour les systèmes basés sur Windows
>- .sh (Bash) pour les systèmes basés sur Linux/macOS
7. **Activer les modifications** : Cliquez sur le bouton `Create` pour enregistrer et appliquer le nouveau script d’appareil utilisateur.



<!-- > [!ATTENTION]
> Use the proper syntax when writing the script (Powershell or bash). -->


### Filtrer les scripts d’appareil utilisateur

Vous pouvez rechercher des scripts dans la liste à l’aide du champ de recherche en haut de la page. Cela vous permet de trouver et de gérer rapidement le script recherché.

- Utilisez le champ de recherche pour saisir des mots-clés et filtrer la liste des scripts.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher les options de filtrage avancées, qui vous permettent de définir des critères supplémentaires à partir des trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir la manière de faire correspondre la valeur (`EQUALS`, `CONTAINS` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à rechercher, selon la propriété sélectionnée.

![filter_scripts.png](./screenshots/filter_scripts.png ':size=400')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../../images/icons/icon_filter.png ':size=20'), puis cliquez sur le bouton `+`.

> [!TIP]
> Vous pouvez actualiser la liste des scripts en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.


### Détails des scripts d’appareil utilisateur

Cliquez sur la ligne correspondant à un script pour ouvrir une vue détaillée contenant des informations supplémentaires.


![script_details.png](./screenshots/script_details.png ':size=500')

### Modifier des scripts d’appareil utilisateur

Vous pouvez modifier des scripts en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') dans leur ligne.

![edit_script.png](./screenshots/edit_script.png ':size=400')

### Supprimer des scripts d’appareil utilisateur

Vous pouvez supprimer des scripts en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') dans leur ligne.

Un avertissement s’affichera avant la suppression définitive de l’utilisateur :

![delete_script.png](./screenshots/delete_script.png ':size=400')
