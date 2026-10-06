# ![](../../images/menu/menu_portforwarding.png ':size=28') Redirection de port

La redirection de port permet aux utilisateurs externes qui ne sont pas membres de la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_** de se connecter aux services internes. L’accès est fourni via l’IP publique du contrôleur réseau cloud ou l’adresse IP du contrôleur réseau sur site.


![Capture d’écran de la page des règles de redirection de port](./screenshots/portforward.png ':size=700')

### Créer une règle de redirection de port

Cliquez sur le bouton `+ Create a new rule` et suivez les étapes ci-dessous :

1. **Description** : Saisissez une description claire de la règle pour pouvoir la retrouver ultérieurement.
2. **Port source** : Saisissez le numéro de port que les clients externes utiliseront pour se connecter.
3. **Port de destination** : Indiquez le numéro de port interne vers lequel le trafic doit être redirigé.
4. **Destination** : Choisissez la destination interne qui doit recevoir le trafic redirigé.
5. **Protocole** : Sélectionnez TCP ou UDP selon les exigences de votre service.
6. **Activer ou désactiver** : Utilisez le curseur pour activer ou désactiver la règle.
7. **Facultatif : créer une note** ![](../../images/icons/icon_note.png ':size=20') : Si la règle a un objectif ou un contexte particulier, il est utile d’ajouter une note pour plus de clarté.
8. **Activer les modifications** : Une fois la règle configurée, appuyez sur le bouton `➢ Submit` pour appliquer vos modifications.

> [!TIP]
> Vous pouvez télécharger un aperçu des règles de redirection de port associées à une destination en cliquant sur l’icône de téléchargement ![](../../images/icons/icon_download.png ':size=20') située au-dessus de l’aperçu, à droite, à côté du bouton `➢ Submit`. L’aperçu sera téléchargé sous forme de fichier CSV.

> [!IMPORTANT] 
>  Passez régulièrement en revue vos règles de redirection de port afin de vérifier qu’elles répondent aux besoins actuels et aux normes de sécurité de votre organisation.

### Filtrer les règles de redirection de port

Vous pouvez filtrer la liste des règles de redirection de port à l’aide du champ situé en haut de la page. Cela vous permet de retrouver et de gérer rapidement des règles spécifiques.


### Modifier les règles de redirection de port

Vous pouvez modifier librement les règles de redirection de port répertoriées. Si vous effectuez des modifications que vous ne souhaitez pas conserver, utilisez le bouton `Clear changes` pour revenir à la version enregistrée précédemment.

Vous pouvez mettre à jour les notes des règles de redirection de port en cliquant sur l’icône de mise à jour ![](../../images/icons/icon_note.png ':size=20') dans leur ligne. La fenêtre suivante s’affiche : 

![Capture d’écran de la fenêtre de mise à jour de la note](./screenshots/update_note_rule.png ':size=400')

> [!WARNING]
> N’oubliez pas d’enregistrer vos modifications pour appliquer les mises à jour à l’aide du bouton `➢ Save`.


Si des modifications ne sont pas enregistrées lorsque vous quittez la page, un message d’avertissement s’affiche afin que vous n’oubliiez pas de soumettre les règles.
![Capture d’écran de l’avertissement concernant les modifications non enregistrées](../../images/notifications/unsaved_changes.png ':size=400')

### Supprimer des règles de redirection de port

Vous pouvez supprimer des règles de redirection de port en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') dans leur ligne.

> [!WARNING]
> La règle de redirection de port sera supprimée sans autre avertissement. Si vous avez cliqué par erreur sur le bouton de suppression, vous pouvez restaurer les paramètres d’origine en cliquant sur `Clear changes`, à condition de ne pas avoir encore cliqué sur le bouton `Submit`.
