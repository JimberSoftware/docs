File: rules/portforwarding/portforwarding.md

# ![](../../images/menu/menu_portforwarding.png ':size=28') Redirection de ports

La redirection de ports permet aux utilisateurs externes qui ne sont pas membres de la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_** de se connecter aux services internes. L’accès est fourni via l’IP publique du contrôleur réseau cloud ou l’adresse IP du contrôleur réseau sur site.

![Capture d’écran de la page des règles de redirection de ports](./screenshots/portforward.png ':size=700')

### Créer une règle de redirection de ports

Cliquez sur le bouton `+ Create a new rule` et suivez les étapes ci-dessous :

1. **Description** : fournissez une description claire de la règle pour pouvoir la retrouver facilement plus tard.
2. **Contrôleur réseau** : sélectionnez le contrôleur qui reçoit le trafic entrant. La règle s’applique uniquement à ce contrôleur.
3. **Port source** : saisissez le numéro de port que les clients externes utiliseront pour se connecter.
4. **Port de destination** : indiquez le numéro de port interne vers lequel le trafic doit être redirigé.
5. **Destination** : choisissez la destination interne qui doit recevoir le trafic redirigé.
6. **Protocole** : sélectionnez TCP ou UDP selon les exigences de votre service.
7. **Activer ou désactiver** : utilisez le curseur pour activer ou désactiver la règle.
8. **Facultatif : ajouter une note** ![](../../images/icons/icon_note.png ':size=20') : si la règle a un objectif ou un contexte particulier, il est utile d’ajouter une note pour plus de clarté.
9. **Activer les modifications** : une fois la règle configurée, cliquez sur le bouton `➢ Submit` pour appliquer vos modifications.

Vous pouvez utiliser le même port source et le même protocole sur différents contrôleurs. Les règles actives sur un même contrôleur doivent utiliser un port source ou un protocole différent.

Les règles existantes sont copiées sur chaque contrôleur pendant la mise à niveau. Chaque entreprise disposant de règles de redirection de ports doit avoir un contrôleur réseau avant la mise à niveau. La migration échoue si cette condition n’est pas remplie. Les nouveaux contrôleurs ne reçoivent pas automatiquement les règles existantes.

> [!TIP]
> Vous pouvez télécharger un aperçu des règles de redirection de ports associées à une destination en cliquant sur l’icône de téléchargement ![](../../images/icons/icon_download.png ':size=20') située au-dessus de l’aperçu, à droite, à côté du bouton `➢ Submit`.. L’aperçu sera téléchargé sous forme de fichier CSV.

> [!IMPORTANT]
> Examinez régulièrement vos règles de redirection de ports pour vous assurer qu’elles répondent aux besoins actuels et aux normes de sécurité de votre organisation.

### Filtrer les règles de redirection de ports

Vous pouvez filtrer la liste des règles de redirection de ports à l’aide du champ situé en haut de la page. Cela vous permet de trouver et de gérer rapidement des règles spécifiques.

### Modifier les règles de redirection de ports

Vous pouvez modifier librement les règles de redirection de ports répertoriées. Si vous effectuez des modifications que vous ne souhaitez pas conserver, utilisez le bouton `Clear changes` pour revenir à la version précédemment enregistrée.

Vous pouvez mettre à jour les notes des règles de redirection de ports en cliquant sur l’icône de mise à jour ![](../../images/icons/icon_note.png ':size=20') dans leur ligne. La fenêtre suivante apparaît :

![Capture d’écran de la fenêtre de mise à jour de la note](./screenshots/update_note_rule.png ':size=400')

> [!WARNING]
> N’oubliez pas d’enregistrer vos modifications pour appliquer les mises à jour en utilisant le bouton `➢ Save`.

Si des modifications n’ont pas été enregistrées lorsque vous quittez la page, un message d’avertissement apparaît pour vous rappeler de soumettre les règles.
![Capture d’écran de l’avertissement signalant des modifications non enregistrées](../../images/notifications/unsaved_changes.png ':size=400')

### Supprimer des règles de redirection de ports

Vous pouvez supprimer des règles de redirection de ports en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') dans leur ligne.

> [!WARNING]
> La règle de redirection de ports sera supprimée sans autre avertissement. Si vous avez cliqué par erreur sur le bouton de suppression, vous pouvez rétablir les paramètres d’origine en cliquant sur `Clear changes`, tant que vous n’avez pas encore cliqué sur le bouton `Submit`.
