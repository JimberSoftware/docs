# ![](../../images/menu/menu_allowcustomports.png ':size=28') Autoriser les ports personnalisés (archivé)

Cette fonctionnalité est conçue pour contrôler avec précision les communications entre groupes. Elle vous permet de spécifier avec quel serveur un groupe peut communiquer, via quel port et avec quel protocole. C’est une solution idéale pour les groupes qui n’ont pas besoin d’un accès sans restriction à un autre groupe.

![Capture d’écran de la page Autoriser les ports personnalisés](./screenshots/allow_custom_ports.png ':size=800')

**Par exemple :** 

Vous avez un serveur web qui s’exécute sur un serveur, mais vous ne voulez pas que les utilisateurs aient un accès complet au serveur. Ce groupe n’aura donc pas de règles de trafic de groupe vers le serveur, mais uniquement une règle de port personnalisé spécifique pour le serveur web.

<!-- ### Créer des règles de ports personnalisés

Cliquez sur le bouton `+ Create a new rule` et suivez les étapes ci-dessous :

1. **Description** : Saisissez une description claire pour identifier la règle ultérieurement.
2. **Sélectionner le groupe source** : Choisissez le groupe autorisé à initier la connexion.
3. **Port de début / Port de fin** : Définissez la plage de ports de destination auxquels accéder. Pour un seul port, utilisez la même valeur dans les deux champs.
4. **Protocole** : Sélectionnez le protocole approprié.
5. **Activer ou désactiver** : Utilisez le curseur pour activer ou désactiver la règle.
6. **Note facultative** ![](../../images/icons/icon_note.png ':size=20') : Ajoutez une brève explication pour préciser l’objectif de la règle.
7. **Activer les modifications** : Appuyez sur le bouton `➢ Submit rules` pour enregistrer et appliquer la règle.

> [!INFO] 
> Il est essentiel d’examiner et d’ajuster régulièrement les règles de ports personnalisés afin de veiller à ce qu’elles répondent aux besoins de sécurité de votre organisation. -->

### Filtrer les règles de ports personnalisés

Vous pouvez filtrer la liste des règles de ports personnalisés à l’aide des champs en haut de la page. Cela vous aide à trouver et à gérer rapidement des règles spécifiques.

- **Rechercher** : Utilisez ce champ de texte pour effectuer une recherche par description.
- **Groupe source** : Filtrez les règles selon le groupe source sélectionné dans le menu déroulant.
- **Destination** : Affinez les résultats en sélectionnant une destination dans le menu déroulant.

<!-- ### Modifier les règles de ports personnalisés

Vous pouvez modifier librement les règles de ports personnalisés répertoriées. Si vous effectuez des modifications que vous ne souhaitez pas conserver, utilisez le bouton `Clear changes` pour revenir à la version précédemment enregistrée.

Vous pouvez mettre à jour les notes des règles de ports personnalisés en cliquant sur l’icône de mise à jour ![](../../images/icons/icon_note.png ':size=20') dans leur ligne. La fenêtre suivante s’affiche :

![Capture d’écran de la fenêtre Mettre à jour la note](./screenshots/update_note_rule.png ':size=400')

> [!WARNING]
> N’oubliez pas d’enregistrer vos modifications pour appliquer les mises à jour en utilisant le bouton `➢ Submit rules`.

### Supprimer des règles de ports personnalisés

Vous pouvez supprimer des règles de ports personnalisés en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') dans leur ligne.

> [!WARNING]
> N’oubliez pas d’enregistrer vos modifications pour appliquer les mises à jour en utilisant le bouton `➢ Submit rules`.


> [!INFO]
> Si des modifications ne sont pas enregistrées lorsque vous quittez la page, un message d’avertissement s’affiche afin que vous n’oubliiez pas d’envoyer les règles.
>
>![Capture d’écran de l’avertissement concernant les modifications non enregistrées](../../images/notifications/unsaved_changes.png ':size=400')
 -->
### Télécharger les règles de ports personnalisés

Vous pouvez télécharger toutes les règles de ports personnalisés dans un **fichier .csv** en cliquant sur l’icône de téléchargement ![](../../images/icons/icon_download.png ':size=20') située à côté du bouton `➢ Submit rules`.
