# ![native_networks](../images/menu/menu_webfiltering.png ':size=25') Filtrage web

Utilisez la page _Filtrage web_ pour appliquer des politiques de filtrage à un réseau natif sélectionné.

> [!ATTENTION]
> Le filtrage web ne sera appliqué que si vous utilisez le DNS Jimber.

Vous pouvez contrôler les catégories de contenu courantes, les plateformes de réseaux sociaux, les outils d’IA et les domaines personnalisés au moyen d’une liste d’autorisation ou d’une liste de blocage.

### Configurer le filtrage web

![web-filtering.png](./screenshots/web-filtering.png ':size=600')

- Choisissez un _Réseau natif_ dans la liste déroulante en haut à gauche de la page.
- Examinez les cartes de filtrage de la page.
- Pour chaque catégorie ou service, activez le bouton _Bloquer_ ou _Superviser_ selon la politique que vous souhaitez appliquer.

> [!Attention]
> N’oubliez pas de cliquer sur _Soumettre_ en haut à droite de la page !

### Modes Bloquer et Superviser

Chaque élément de filtrage comprend deux options :

- _Bloquer_ pour empêcher l’accès.
- _Superviser_ pour observer le trafic associé à cette catégorie ou à ce service.

Choisissez le paramètre correspondant à la politique que vous souhaitez appliquer au réseau sélectionné.

### Ajouter un domaine à la liste de blocage

![blocklist.png](./screenshots/blocklist.png ':size=500')

- Choisissez un _Réseau natif_ dans la liste déroulante en haut à gauche de la page.
- Dans la carte _Liste de blocage_, cliquez sur le bouton _+_.
- Saisissez le domaine lorsque l’interface vous y invite.
- Cliquez sur _Ajouter_ pour enregistrer l’entrée.

> [!Attention]
> N’oubliez pas de cliquer sur _Soumettre_ en haut à droite de la page !

Si aucun domaine personnalisé n’a encore été ajouté, la page affiche _Aucun domaine dans la liste de blocage_ :

![no_blocklist.png](./screenshots/no_blocklist.png ':size=500')

### Ajouter un domaine à la liste d’autorisation

![allowlist.png](./screenshots/allowlist.png ':size=500')

- Choisissez un _Réseau natif_ dans la liste déroulante en haut à gauche de la page.
- Dans la carte _Liste d’autorisation_, cliquez sur le bouton _+_.
- Saisissez le domaine lorsque l’interface vous y invite.
- Cliquez sur _Ajouter_ pour enregistrer l’entrée.

> [!Attention]
> N’oubliez pas de cliquer sur _Soumettre_ en haut à droite de la page !

Si aucun domaine personnalisé n’a encore été ajouté, la page affiche _Aucun domaine dans la liste d’autorisation_ :

![no_allowlist.png](./screenshots/no_allowlist.png ':size=500')

### Remarque

Si vous cliquez sur la petite icône d’horloge en bas à droite, une nouvelle fenêtre s’ouvre pour vous permettre d’indiquer les jours pendant lesquels la liste de blocage ou la liste d’autorisation s’applique :

![weekly_schedule.png](./screenshots/weekly_schedule.png ':size=500')

## Résumé

Utilisez le *Filtrage web* pour appliquer des contrôles de contenu au niveau du réseau aux appareils connectés par l’intermédiaire d’un réseau natif, y compris aux appareils non gérés sur lesquels le ***_<span style="color: darkblue;">Jimber SASE Client</span>_*** n’est pas installé.
