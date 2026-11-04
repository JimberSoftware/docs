# ![](../../images/menu/menu_webfiltering.png ':size=28') Filtrage DNS

Le filtrage DNS vous permet de contrôler et de gérer les sites web auxquels un groupe spécifique peut accéder sur le réseau. Vous pouvez bloquer des catégories de contenu telles que le contenu pour adultes, les fausses informations, les jeux d’argent, les logiciels malveillants/logiciels publicitaires et les réseaux sociaux.

Vous pouvez également configurer des restrictions horaires, non seulement pour certaines heures de la journée, mais aussi pour certains jours de la semaine. Vous pouvez ainsi adapter plus précisément l’accès en limitant le contenu uniquement à certaines heures ou certains jours de la semaine.

Le trafic vers les sites bloqués peut être supervisé, ce qui vous permet de savoir quels utilisateurs ont tenté d’accéder à du contenu restreint. Vous pouvez personnaliser davantage le filtrage DNS en utilisant une liste de blocage pour bloquer des sites spécifiques ou une liste d’autorisation pour autoriser l’accès à certains sites web. Tous ces paramètres sont configurables par groupe, afin que vous puissiez appliquer différentes règles selon les besoins de chaque groupe au sein de votre réseau.

Le filtrage DNS utilise des listes régulièrement mises à jour pour chaque catégorie afin de garantir que les nouvelles menaces et les contenus indésirables sont automatiquement détectés et bloqués dès leur apparition.

![Capture d’écran de la page de filtrage DNS](./screenshots/webfiltering.png ':size=800')

> [!WARNING]
> Le filtrage DNS ne sera appliqué que si _DNS Override_ **et/ou** _SSL Inspection_ est activé pour le groupe choisi. Si aucune de ces options n’est activée, les règles de filtrage ne seront pas appliquées.

![dns_override_ssl_inspection.png](./screenshots/dns_override_ssl_inspection.png ':size=300')

### Configurer le filtrage DNS

Pour configurer le filtrage DNS d’un groupe, procédez comme suit :

1. **Sélectionner un groupe** : commencez par sélectionner le groupe pour lequel vous souhaitez configurer les règles de filtrage.

> [!INFO]
> Si un utilisateur appartient à plusieurs groupes dont les règles de filtrage DNS sont contradictoires, le blocage prévaut sur l’autorisation. Cela signifie que si un groupe bloque un site et qu’un autre l’autorise, le site sera bloqué pour cet utilisateur.

2. **Bloquer des catégories** : choisissez et bloquez certaines catégories de contenu (p. ex. contenu pour adultes, logiciels malveillants, jeux d’argent) afin d’en restreindre l’accès pour le groupe sélectionné. Utilisez le bouton correspondant pour activer ou désactiver chaque catégorie.

    ![block.png](./screenshots/block.png ':size=350')

3. **Gérer les sites web** :
    - **Liste de blocage** : ajoutez les sites web que vous souhaitez bloquer en saisissant leurs URL dans la liste de blocage. Cliquez sur + pour ajouter un site web. Vous pouvez configurer un créneau horaire :

        ![blocklist.png](./screenshots/blocklist.png ':size=350')

    - **Liste d’autorisation** : ajoutez des sites web de confiance à la liste d’autorisation afin qu’ils restent accessibles, même s’ils appartiennent à une catégorie bloquée. Vous pouvez également y ajouter des sites web et configurer un créneau horaire.

        ![allowlist.png](./screenshots/allowlist.png ':size=350')

    - **Supprimer des sites web** : pour supprimer un site web de l’une ou l’autre liste, cliquez sur l’icône de corbeille rouge ![](../../images/icons/icon_delete.png ':size=15') à côté du nom du site web.

4. **Règles horaires** : définissez des règles horaires pour contrôler l’accès (bloquer) à certains sites pendant des créneaux horaires spécifiques. Cliquez sur l’icône d’horloge pour définir quand les restrictions doivent s’appliquer. Vous pouvez définir un horaire pour chaque jour et ajouter plusieurs créneaux horaires. Cliquez sur + pour ajouter un créneau horaire :

    ![weekly_schedule.png](./screenshots/weekly_schedule.png ':size=350')

    Pour supprimer un créneau horaire, cliquez sur l’icône de corbeille ![](../../images/icons/icon_delete.png ':size=15') à côté du créneau horaire à supprimer.

5. **Superviser le trafic** : vous pouvez également superviser le trafic vers les sites web bloqués ou autorisés afin de suivre les habitudes d’utilisation et de vous assurer que les règles de filtrage sont respectées. Utilisez le bouton correspondant pour activer ou désactiver chaque catégorie.

    ![monitor.png](./screenshots/monitor.png ':size=350')

6. **Activer les modifications** en cliquant sur le bouton `➢ Submit`. Les règles deviennent actives.

> [!WARNING]
> Vérifiez toujours les règles avant de les soumettre afin de vous assurer que la configuration est correcte. Si vous effectuez des modifications que vous ne souhaitez pas conserver, utilisez le bouton `Clear changes` pour revenir à la version précédemment enregistrée.

> [!INFO]
> Si des modifications n’ont pas été enregistrées et que vous quittez la page, un message d’avertissement s’affichera.
>
> ![Capture d’écran de l’avertissement relatif aux modifications non enregistrées](../../images/notifications/unsaved_changes.png ':size=300')
