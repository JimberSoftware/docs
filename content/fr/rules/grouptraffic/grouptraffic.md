File: rules/grouptraffic/grouptraffic.md

# ![](../../images/menu/menu_grouptraffic.png ':size=28') Trafic de groupe (archivé)

La fonctionnalité **Trafic de groupe** contrôle la manière dont les différents groupes peuvent communiquer entre eux au sein de votre configuration réseau. Sur la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_**, un **groupe** est un concept flexible qui peut représenter des utilisateurs, des serveurs ou des appareils connectés via un client d’accès à l’isolation réseau (NIAC).

![Capture d’écran de la page Trafic de groupe](./screenshots/group_traffic_start.png ':size=800')

Comme les groupes peuvent s’appliquer à différents types de terminaux, cette fonctionnalité vous permet de contrôler précisément le flux de trafic entre ces segments. Par exemple, vous pouvez :

<!-- - Autoriser un groupe de **développeurs (utilisateurs)** à accéder à un groupe contenant des **serveurs de préproduction**
- Autoriser les **appareils connectés via NIAC** à communiquer avec un groupe de **services d’infrastructure**
- Permettre la communication interne entre tous les appareils d’un **service spécifique**

> [!WARNING]  
> La fonctionnalité Trafic de groupe doit être utilisée avec précaution. Pour un contrôle plus ciblé de services spécifiques, envisagez d’utiliser **Autoriser les ports personnalisés**, qui offre une approche plus sécurisée et détaillée.

### Créer des règles de trafic de groupe

Cliquez sur le bouton `+ Create a new rule` et suivez les étapes ci-dessous :

1. **Sélectionner le groupe source** : choisissez le groupe autorisé à initier la connexion.
2. **Sélectionner le groupe de destination** : choisissez le groupe autorisé à recevoir la connexion.
3. **Port de début / Port de fin** : définissez la plage de ports autorisée. Si vous ne spécifiez pas de plage, la valeur par défaut sera `1–65535`, ce qui autorise tous les ports.
4. **Activer ou désactiver** : utilisez le curseur pour activer ou désactiver la règle.
5. **Remarque facultative** ![](../../images/icons/icon_note.png ':size=20') : ajoutez une courte explication pour préciser l’objectif de la règle.
6. **Activer les modifications** : cliquez sur le bouton `➢ Submit rules` pour enregistrer et appliquer la règle.

Par exemple, pour accorder au groupe **« Développeurs »** l’accès à vos **« Serveurs »**, définissez **« Développeurs »** comme groupe source et **« Serveurs »** comme groupe de destination.

![Capture d’écran de la configuration du scénario d’exemple](./screenshots/group_traffic.png ':size=800')

Si vous souhaitez que les membres d’un même groupe puissent communiquer entre eux, sélectionnez le même groupe comme source et comme destination.

![Capture d’écran de la configuration du trafic interne](./screenshots/group_traffic_intern.png ':size=800') -->

### Filtrer les règles de trafic de groupe

Vous pouvez filtrer la liste des règles de trafic de groupe à l’aide des champs situés en haut de la page. Cela vous permet de trouver et de gérer rapidement des règles spécifiques.

- **Groupe source** : filtrez les règles en fonction du groupe source sélectionné à l’aide du menu déroulant.
- **Destination** : affinez les résultats en sélectionnant une destination dans le menu déroulant.

<!-- ### Modifier les règles de trafic de groupe

Vous pouvez modifier librement les règles de trafic de groupe répertoriées. Si vous effectuez des modifications que vous ne souhaitez pas conserver, utilisez le bouton `Clear changes` pour rétablir la version enregistrée précédemment.

Vous pouvez mettre à jour les remarques des règles de trafic de groupe en cliquant sur l’icône de modification ![](../../images/icons/icon_note.png ':size=20') dans leur ligne. La fenêtre suivante s’affiche : 

![Capture d’écran de la fenêtre de mise à jour de la remarque](./screenshots/update_note_rule.png ':size=400')

> [!WARNING]
> N’oubliez pas d’enregistrer vos modifications pour appliquer les mises à jour en cliquant sur le bouton `➢ Submit rules`.

### Supprimer des règles de trafic de groupe

Vous pouvez supprimer des règles de trafic de groupe en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') dans leur ligne.

> [!WARNING]
> N’oubliez pas d’enregistrer vos modifications pour appliquer les mises à jour en cliquant sur le bouton `➢ Submit rules`.

> [!INFO]
> Si des modifications ne sont pas enregistrées lorsque vous quittez la page, un message d’avertissement s’affiche afin que vous n’oubliiez pas de soumettre les règles.
>
>![Capture d’écran de l’avertissement signalant des modifications non enregistrées](../../images/notifications/unsaved_changes.png ':size=400') -->

### Télécharger les règles de trafic de groupe

Vous pouvez télécharger toutes les règles de trafic de groupe dans un **fichier .csv** en cliquant sur l’icône de téléchargement ![](../../images/icons/icon_download.png ':size=20') située à côté du bouton `➢ Submit rules`.
