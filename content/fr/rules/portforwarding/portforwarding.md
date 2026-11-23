# ![](../../images/menu/menu_portforwarding.png ':size=28') Redirection de ports

La redirection de ports permet aux utilisateurs externes qui ne sont pas membres de la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_** de se connecter aux services internes. L’accès est fourni par l’adresse IP publique du contrôleur réseau Cloud ou par l’adresse IP du contrôleur réseau sur site.

![Capture d’écran de la page des règles de redirection de ports](./screenshots/portforward.png ':size=700')

### Créer une règle de redirection de ports

Cliquez sur le bouton `+ Create a new rule` et suivez les étapes ci-dessous :

1. **Description** : Fournissez une description claire de la règle pour pouvoir la retrouver ultérieurement.
2. **Contrôleur réseau** : Sélectionnez le contrôleur qui reçoit le trafic entrant. La règle s’applique uniquement à ce contrôleur.
3. **Port source** : Saisissez le numéro de port que les clients externes utiliseront pour se connecter.
4. **Port de destination** : Indiquez le numéro de port interne vers lequel le trafic doit être redirigé.
5. **Destination** : Choisissez la destination interne qui doit recevoir le trafic redirigé.
6. **Protocole** : Sélectionnez TCP ou UDP selon les exigences de votre service.
7. **Activer ou désactiver** : Utilisez le curseur pour activer ou désactiver la règle.
8. **Facultatif : ajouter une note** ![](../../images/icons/icon_note.png ':size=20') : Si la règle a un objectif ou un contexte particulier, il est utile d’ajouter une note pour plus de clarté.
9. **Activer les modifications** : Une fois la règle configurée, cliquez sur le bouton `➢ Submit` pour appliquer vos modifications.

Vous pouvez utiliser le même port source et le même protocole sur différents contrôleurs. Les règles actives sur un même contrôleur doivent utiliser un port source ou un protocole différent.

### Restrictions par pays

Chaque règle utilise un mode de restriction par pays. Par défaut, les règles existantes et nouvelles n’ont **Aucune restriction par pays**.

- **Aucune restriction par pays** : Le pays ne restreint pas la règle.
- **Autoriser uniquement les pays sélectionnés** : N’autoriser un pays connu que s’il est sélectionné. Bloquer tout pays inconnu.
- **Bloquer les pays sélectionnés** : Bloquer un pays sélectionné. Autoriser un pays inconnu lorsque la base de données est utilisable.

Sélectionnez des pays, des régions prédéfinies en lecture seule et des régions de l’entreprise. Leurs pays forment un seul ensemble. Les doublons n’ont aucun effet supplémentaire. Un mode avec restriction doit comporter au moins un pays ou une région. Utilisez **Aucune restriction par pays** pour supprimer la restriction.

Le contrôleur vérifie l’IP source publique entrante avant de remplacer l’adresse source. Les VPN, les proxys et le remplacement de l’adresse en amont peuvent modifier le pays que voit le contrôleur. Cette estimation ne prouve pas la localisation d’une personne. Elle ne remplace ni l’authentification ni les autres protections du service.

Les modifications s’appliquent aux nouvelles connexions IPv4 TCP et UDP. Les connexions existantes peuvent se poursuivre jusqu’à leur fermeture ou leur expiration. Si aucune base de données de pays utilisable n’est disponible, les deux modes avec restriction bloquent toutes les nouvelles connexions et signalent une erreur. Les règles sans restriction ne sont pas affectées.

Le contrôleur utilise une base de données locale des pays. Il vérifie quotidiennement si une mise à jour est disponible. Il valide chaque remplacement et conserve le dernier fichier valide si une mise à jour échoue.

### Régions

Gérez les régions sous **Sécurité → Régions**. Les régions prédéfinies apparaissent dans le tableau et ne peuvent être ni modifiées ni supprimées. Une région personnalisée peut contenir des pays et des régions prédéfinies, mais pas une autre région personnalisée. Les régions vides ne sont pas autorisées. Les modifications mettent à jour toutes les règles qui utilisent la région. Une région personnalisée ne peut pas être supprimée tant qu’une règle l’utilise. Sélectionnez le nombre de règles pour afficher ces règles.

Les régions prédéfinies en lecture seule sont l’Afrique (région UN M49 002), les Amériques (019), l’Asie (142, y compris Taïwan), l’Europe (150), l’Océanie (009) et le Benelux (BE, NL, LU). Leurs pays membres sont affichés dans le sélecteur de pays.

Les administrateurs d’entreprise et les consultants en sécurité peuvent gérer les groupes et les restrictions. Ils doivent disposer du rôle requis dans l’entreprise cible. L’accès à la fonctionnalité de redirection de ports est également requis.

Le trafic bloqué apparaît sous **Supervision → Blocages de redirection de ports**, avec des colonnes distinctes pour l’ID et le nom de la règle, le pays source ou la valeur « inconnu », et le motif du blocage. La recherche, les filtres, le tri, les détails des paquets et les exportations CSV utilisent les mêmes événements enregistrés. L’inspection des paquets inclut toujours ces événements, avec les détails du pays dans le panneau des détails du paquet.

Le rejet lié au pays et l’indisponibilité des données de pays sont des motifs distincts. Les regroupements de cinq minutes séparent les règles, les pays et les motifs. La livraison des événements n’est pas garantie en cas d’attaque ou lorsque les files d’attente sont saturées. Les modifications de régions et les modifications des pays d’une règle apparaissent séparément dans l’historique des activités.

Les règles existantes sont copiées sur chaque contrôleur pendant la mise à niveau. Chaque entreprise disposant de règles de redirection de ports doit avoir un contrôleur réseau avant la mise à niveau. La migration échoue si cette condition n’est pas remplie. Les nouveaux contrôleurs ne reçoivent pas automatiquement les règles existantes.

> [!TIP]
> Vous pouvez télécharger un aperçu des règles de redirection de ports associées à une destination en cliquant sur l’icône de téléchargement ![](../../images/icons/icon_download.png ':size=20') située au-dessus de l’aperçu, à droite, à côté du bouton `➢ Submit`. L’aperçu sera téléchargé sous forme de fichier CSV.

> [!IMPORTANT]
> Vérifiez régulièrement vos règles de redirection de ports afin de vous assurer qu’elles répondent aux besoins actuels et aux normes de sécurité de votre organisation.

### Filtrer les règles de redirection de ports

Vous pouvez filtrer la liste des règles de redirection de ports à l’aide du champ situé en haut de la page. Cela vous permet de trouver et de gérer rapidement des règles spécifiques.

### Modifier les règles de redirection de ports

Vous pouvez modifier librement les règles de redirection de ports répertoriées. Si vous effectuez des modifications que vous ne souhaitez pas conserver, utilisez le bouton `Clear changes` pour revenir à la version précédemment enregistrée.

Les notes des règles de redirection de ports peuvent être mises à jour en cliquant sur l’icône de mise à jour ![](../../images/icons/icon_note.png ':size=20') dans leur ligne. La fenêtre suivante apparaît :

![Capture d’écran de la fenêtre de mise à jour d’une note](./screenshots/update_note_rule.png ':size=400')

> [!WARNING]
> N’oubliez pas d’enregistrer vos modifications pour appliquer les mises à jour à l’aide du bouton `➢ Save`.

Si des modifications ne sont pas enregistrées lorsque vous quittez la page, un message d’avertissement s’affiche pour vous éviter d’oublier de soumettre les règles.
![Capture d’écran de l’avertissement concernant les modifications non enregistrées](../../images/notifications/unsaved_changes.png ':size=400')

### Supprimer des règles de redirection de ports

Les règles de redirection de ports peuvent être supprimées en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') dans leur ligne.

> [!WARNING]
> La règle de redirection de ports sera supprimée sans autre avertissement. Si vous cliquez par erreur sur le bouton de suppression, vous pouvez restaurer les paramètres d’origine en cliquant sur `Clear changes`, tant que vous n’avez pas encore cliqué sur le bouton `Submit`.
