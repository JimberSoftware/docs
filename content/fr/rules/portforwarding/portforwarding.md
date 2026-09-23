File: rules/portforwarding/portforwarding.md

# ![](../../images/menu/menu_portforwarding.png ':size=28') Redirection de ports

La redirection de ports permet aux utilisateurs externes qui ne sont pas membres de la *`Jimber SASE Platform`* de se connecter aux services internes. L’accès est fourni par l’intermédiaire de l’adresse IP publique du contrôleur réseau cloud ou de l’adresse IP du contrôleur réseau sur site.


![Capture d’écran de la page des règles de redirection de ports](./screenshots/portforward.png ':size=800')

### Créer une règle de redirection de ports

Cliquez sur le bouton `+ Create a new rule` et suivez les étapes ci-dessous :

1. **Description** : fournissez une description claire de la règle pour pouvoir la consulter ultérieurement.
2. **Port source** : saisissez le numéro de port que les clients externes utiliseront pour se connecter.
3. **Port de destination** : indiquez le numéro de port interne vers lequel le trafic doit être redirigé.
4. **Destination** : choisissez la destination interne qui doit recevoir le trafic redirigé.
5. **Protocole** : sélectionnez TCP ou UDP selon les exigences de votre service.
6. **Activer ou désactiver** : utilisez le curseur pour activer ou désactiver la règle.
7. **Facultatif : créer une note** ![](../../images/icons/icon_note.png ':size=20') : si la règle a un objectif ou un contexte particulier, il est utile d’ajouter une note pour plus de clarté.
8. **Activer les modifications** : une fois la règle configurée, cliquez sur le bouton `➢ Submit rules` pour appliquer vos modifications.

> [!TIP]
> Vous pouvez télécharger un aperçu des règles de redirection de ports associées à une destination en cliquant sur l’icône de téléchargement ![](../../images/icons/icon_download.png ':size=20') située au-dessus de l’aperçu, à droite, à côté du bouton `➢ Submit`.. L’aperçu sera téléchargé sous forme de fichier CSV.

> [!IMPORTANT] 
>  Passez régulièrement en revue vos règles de redirection de ports pour vous assurer qu’elles répondent aux besoins actuels et aux normes de sécurité de votre organisation.

### Filtrer les règles de redirection de ports

Vous pouvez filtrer la liste des règles de redirection de ports à l’aide du champ situé en haut de la page. Cela vous permet de trouver et de gérer rapidement des règles spécifiques.


### Modifier les règles de redirection de ports

Vous pouvez modifier librement les règles de redirection de ports répertoriées. Si vous effectuez des modifications que vous ne souhaitez pas conserver, utilisez le bouton `Clear changes` pour rétablir la version précédemment enregistrée.

Vous pouvez mettre à jour les notes des règles de redirection de ports en cliquant sur l’icône de mise à jour ![](../../images/icons/icon_note.png ':size=20') sur leur ligne. La fenêtre suivante apparaît : 

![Capture d’écran de la fenêtre de mise à jour de la note](./screenshots/update_note_rule.png ':size=400')

> [!WARNING]
> N’oubliez pas d’enregistrer vos modifications pour appliquer les mises à jour à l’aide du bouton `➢ Save`.


Si des modifications n’ont pas été enregistrées lorsque vous quittez la page, un message d’avertissement apparaît afin que vous n’oubliiez pas de soumettre les règles.
![Capture d’écran de l’avertissement relatif aux modifications non enregistrées](../../images/notifications/unsaved_changes.png ':size=400')

### Supprimer des règles de redirection de ports

Vous pouvez supprimer des règles de redirection de ports en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') sur leur ligne.

> [!WARNING]
> La règle de redirection de ports sera supprimée sans autre avertissement. Si vous avez cliqué sur le bouton de suppression par erreur, vous pouvez rétablir les paramètres d’origine en cliquant sur `Clear changes`, tant que vous n’avez pas encore cliqué sur le bouton `Submit`.
