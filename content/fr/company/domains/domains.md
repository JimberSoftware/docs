File: company/domains/domains.md

# ![](../../images/menu/menu_domains.png ':size=25') Domaines

Les domaines jouent un rôle crucial dans le processus de configuration des paramètres de votre ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***. Ils constituent la base de la configuration des utilisateurs et des administrateurs, et permettent de gérer efficacement les connexions et les modifications de votre réseau.

> [!IMPORTANT]
> Commencez par enregistrer tous les domaines actuellement utilisés par votre organisation. Cette étape est nécessaire avant de créer des utilisateurs et des comptes d’administration.

Par exemple, pour créer un utilisateur tel que *'k.janeway@odyssey.com'*, vous devez d’abord enregistrer le domaine *'odyssey.com'*. Cela met en évidence le rôle des domaines dans la configuration de votre réseau.

![domains.png](./screenshots/domains.png  ':size=800')

### Créer un domaine

Pour créer un nouveau domaine, cliquez simplement sur le bouton `+ Create new` situé dans le coin supérieur droit de l’interface.

![create_new_domain.png](./screenshots/create_domain.png  ':size=350')

### Filtrer les domaines

Vous pouvez rechercher des domaines dans la liste à l’aide du champ de recherche situé en haut de la page. Cela vous permet de trouver et de gérer rapidement le domaine recherché.

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des domaines.

> [!TIP]
> Vous pouvez actualiser la liste des domaines en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

### Supprimer un domaine

Vous pouvez supprimer un domaine en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') dans sa ligne.

> [!WARNING]
> Un domaine ne peut pas être supprimé s’il est associé à des utilisateurs. Veillez à d’abord dissocier du domaine tous les utilisateurs associés dans la section [**_Utilisateurs_**](/company/users/users.md).

Un avertissement s’affiche avant la suppression définitive du domaine :

![delete-domain.png](./screenshots/delete_domain.png ':size=350')

Un avertissement apparaît dans le coin supérieur droit si certains utilisateurs n’ont pas été supprimés :

![warning.png](./screenshots/warning.png ':size=200')
