File: rules/scripts/scripts.md

# ![](../../images/menu/menu_scripts.png ':size=28') Scripts d’appareil utilisateur

Au sein de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***, vous pouvez créer et gérer des scripts d’appareil utilisateur dans la section **Scripts d’appareil utilisateur**. Ces scripts sont exécutés sur l’appareil de l’utilisateur et prennent en charge deux types de déclencheurs :

- **À la connexion** – déclenché lorsque l’appareil se connecte à la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** via le **_Jimber SASE Client_**.  
- **À la déconnexion** – déclenché lorsque l’appareil se déconnecte de la plateforme.

Vous pouvez écrire des scripts pour différents systèmes d’exploitation :

- **Windows**
- **macOS**
- **Linux**
- **Windows Server**
- **Linux Server**

![Capture d’écran de la page Scripts d’appareil utilisateur](./screenshots/scripts.png ':size=700')

Cela permet de mettre en place une automatisation flexible sur l’appareil en fonction de son état de connexion, par exemple pour appliquer des règles de pare-feu, démarrer des services en arrière-plan ou supprimer des ressources temporaires.

### Créer des scripts d’appareil utilisateur

Pour créer un script dans la plateforme, cliquez sur le bouton `+ Create new` et suivez les étapes ci-dessous :

![Capture d’écran de la fenêtre de création d’un script d’appareil utilisateur](./screenshots/create_script.png ':size=300')


1. **Nom** : saisissez un nom descriptif pour le script afin d’identifier sa fonction.
2. **Sélectionner un groupe** : choisissez le groupe d’utilisateurs auquel ce script doit s’appliquer. Le script sera exécuté uniquement pour les utilisateurs membres de ce groupe.
> [!ATTENTION]
> Il est essentiel de sélectionner le **groupe** approprié lors de la création du script. Le script sera exécuté uniquement sur les appareils appartenant au groupe spécifié, lorsque la condition de déclenchement définie est remplie. Si vous affectez le script au mauvais groupe, il risque de ne pas s’exécuter sur les appareils concernés.
3. **Occurrence** : choisissez si le script doit s’exécuter `On Connect` ou `On Disconnect`.
4. **Plateforme** : choisissez le système d’exploitation pour lequel le script est prévu (par exemple, Windows, macOS, Linux, etc.).
5. **Activer ou désactiver** : utilisez le curseur pour activer ou désactiver le script.
6. **Champ du script** : écrivez ou collez le contenu de votre script dans l’éditeur prévu à cet effet. Assurez-vous qu’il répond aux exigences de la plateforme cible :
> [!ATTENTION]
>- .bat ou .ps1 pour les systèmes Windows
>- .sh (Bash) pour les systèmes Linux/macOS
7. **Activer les modifications** : cliquez sur le bouton `Create` pour enregistrer et appliquer le nouveau script d’appareil utilisateur.



<!-- > [!ATTENTION]
> Utilisez la syntaxe appropriée pour écrire le script (PowerShell ou bash). -->


### Filtrer les scripts d’appareil utilisateur

Vous pouvez rechercher des scripts dans la liste à l’aide du champ de recherche situé en haut de la page. Cela vous permet de trouver et de gérer rapidement le script souhaité.

- Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des scripts.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher des options de filtrage avancées, qui vous permettent de définir des conditions supplémentaires selon les trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir comment faire correspondre la valeur (`is`, `contains` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur à faire correspondre, selon la propriété sélectionnée.

![filter_scripts.png](./screenshots/filter_scripts.png ':size=400')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

> [!TIP]
> Vous pouvez actualiser la liste des scripts en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.


### Détails des scripts d’appareil utilisateur

Cliquez sur la ligne correspondant à un script pour ouvrir une vue détaillée contenant des informations supplémentaires.


![script_details.png](./screenshots/script_details.png ':size=500')

### Modifier des scripts d’appareil utilisateur

Vous pouvez modifier les scripts en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de leur ligne.

![edit_script.png](./screenshots/edit_script.png ':size=400')

### Supprimer des scripts d’appareil utilisateur

Vous pouvez supprimer des scripts en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') de leur ligne.

Un avertissement s’affiche avant la suppression définitive de l’utilisateur :

![delete_script.png](./screenshots/delete_script.png ':size=400')
