File: nativenetworks/web-filtering.md

# ![](../images/menu/menu_dns.png ':size=25') Filtrage web

Utilisez la page *Filtrage web* pour appliquer des politiques de filtrage à un réseau natif sélectionné.

>[!ATTENTION]
>Le filtrage web sera appliqué uniquement si vous utilisez le DNS Jimber.

Vous pouvez contrôler les catégories de contenu courantes, les plateformes de réseaux sociaux, les outils d’IA et les domaines personnalisés au moyen d’une liste d’autorisation ou d’une liste de blocage.

### Configurer le filtrage web

![web-filtering.png](./screenshots/web-filtering.png ':size=700')


- Sélectionnez un *Réseau natif* dans la liste déroulante en haut à gauche de la page.
- Consultez les cartes de filtrage affichées sur la page.
- Pour chaque catégorie ou service, activez l’option *Bloquer* ou *Superviser* correspondant à votre politique.

>[!Attention]
>N’oubliez pas de cliquer sur *Soumettre* en haut à droite de la page !


### Modes de blocage et de supervision

Chaque élément de filtrage comprend deux options :

- *Bloquer* pour empêcher l’accès.
- *Superviser* pour observer le trafic associé à cette catégorie ou à ce service.

Choisissez le paramètre correspondant à votre politique pour le réseau sélectionné.

### Ajouter un domaine à la liste de blocage

![blocklist.png](./screenshots/blocklist.png ':size=500')

- Sélectionnez un *Réseau natif* dans la liste déroulante en haut à gauche de la page.
- Dans la carte *Liste de blocage*, cliquez sur le bouton *+*.
- Saisissez le domaine lorsque l’interface vous le demande.
- Cliquez sur *Ajouter* pour enregistrer l’entrée.

>[!Attention]
>N’oubliez pas de cliquer sur *Soumettre* en haut à droite de la page !

Si aucun domaine personnalisé n’a encore été ajouté, la page affiche *Aucun domaine dans la liste de blocage* :

![no_blocklist.png](./screenshots/no_blocklist.png ':size=500')


### Ajouter un domaine à la liste d’autorisation

![allowlist.png](./screenshots/allowlist.png ':size=500')

- Sélectionnez un *Réseau natif* dans la liste déroulante en haut à gauche de la page.
- Dans la carte *Liste d’autorisation*, cliquez sur le bouton *+*.
- Saisissez le domaine lorsque l’interface vous le demande.
- Cliquez sur *Ajouter* pour enregistrer l’entrée.

>[!Attention]
>N’oubliez pas de cliquer sur *Soumettre* en haut à droite de la page !

Si aucun domaine personnalisé n’a encore été ajouté, la page affiche *Aucun domaine dans la liste d’autorisation* :

![no_allowlist.png](./screenshots/no_allowlist.png ':size=500')

### Remarque

Si vous cliquez sur la petite icône d’horloge en bas à droite, une nouvelle fenêtre apparaît. Vous pouvez alors indiquer les jours où la liste de blocage ou la liste d’autorisation s’appliquent :

![weekly_schedule.png](./screenshots/weekly_schedule.png ':size=500')

## Résumé

Utilisez le *Filtrage web* pour appliquer des contrôles de contenu au niveau du réseau aux appareils connectés par l’intermédiaire d’un réseau natif, y compris aux appareils non gérés qui n’exécutent pas le *client Jimber SASE*.
