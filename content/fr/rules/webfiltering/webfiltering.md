# ![](../../images/menu/menu_webfiltering.png ':size=28') Filtrage web

Le filtrage web vous permet de contrôler et de gérer les sites web auxquels un groupe spécifique peut accéder sur le réseau. Vous pouvez bloquer des catégories de contenu telles que les contenus pour adultes, les fausses informations, les jeux d’argent, les logiciels malveillants/publicitaires et les réseaux sociaux.

Vous pouvez également configurer des restrictions horaires, non seulement pour certaines heures de la journée, mais aussi pour certains jours de la semaine. Cela vous permet d’adapter plus précisément l’accès en restreignant le contenu uniquement à certaines heures ou certains jours de la semaine.

Le trafic vers les sites bloqués peut être supervisé, ce qui permet de savoir quels utilisateurs ont tenté d’accéder à du contenu restreint. Vous pouvez personnaliser davantage le filtrage web en utilisant une liste de blocage pour bloquer des sites spécifiques ou une liste d’autorisation pour autoriser l’accès à certains sites web. Tous ces paramètres sont configurables par groupe, ce qui vous permet d’appliquer différentes règles selon les besoins de chaque groupe de votre réseau.

Le filtrage web utilise des listes régulièrement mises à jour pour chaque catégorie afin de garantir que les nouvelles menaces et les contenus indésirables sont automatiquement détectés et bloqués dès leur apparition.

![Capture d’écran de la page Filtrage web](./screenshots/webfiltering.png ':size=800')

> [!WARNING]
> Le filtrage web ne sera appliqué que si le *remplacement DNS* **et/ou** l’*inspection SSL* est activé pour le groupe choisi. Si aucun des deux n’est activé, les règles de filtrage ne seront pas appliquées. 

![dns_override_ssl_inspection.png](./screenshots/dns_override_ssl_inspection.png ':size=300')

### Configurer le filtrage web

Pour configurer le filtrage web d’un groupe, procédez comme suit :

1. **Sélectionner un groupe** : commencez par sélectionner le groupe pour lequel vous souhaitez configurer des règles de filtrage.

> [!INFO] 
> Si un utilisateur appartient à plusieurs groupes ayant des règles de filtrage web contradictoires, le blocage est prioritaire sur l’autorisation. Ainsi, si un groupe bloque un site et qu’un autre l’autorise, ce site sera bloqué pour cet utilisateur.

2. **Bloquer des catégories** : choisissez et bloquez des catégories de contenu spécifiques (par exemple, les contenus pour adultes, les logiciels malveillants et les jeux d’argent) pour en restreindre l’accès au groupe sélectionné. Utilisez le bouton correspondant pour activer ou désactiver chaque catégorie.

   ![block.png](./screenshots/block.png ':size=350')

3. **Gérer les sites web** :
   - **Liste de blocage** : ajoutez les sites web que vous souhaitez bloquer en saisissant leurs URL dans la liste de blocage. Cliquez sur + pour ajouter un site web. Vous pouvez configurer une plage horaire :

      ![blocklist.png](./screenshots/blocklist.png ':size=350')

   - **Liste d’autorisation** : ajoutez les sites web de confiance à la liste d’autorisation pour garantir qu’ils restent accessibles, même s’ils appartiennent à une catégorie bloquée. Vous pouvez également y ajouter des sites web et configurer une plage horaire.

      ![allowlist.png](./screenshots/allowlist.png ':size=350')

   - **Supprimer des sites web** : pour supprimer un site web de l’une ou l’autre des listes, cliquez sur l’icône de corbeille rouge ![](../../images/icons/icon_delete.png ':size=15') à côté du nom du site web.

4. **Règles horaires** : définissez des règles horaires pour contrôler l’accès (bloquer) à certains sites pendant des plages horaires spécifiques. Cliquez sur l’icône d’horloge pour définir les heures d’application des restrictions. Vous pouvez définir un calendrier par jour et ajouter plusieurs plages horaires. Cliquez sur + pour ajouter une plage horaire :

    ![weekly_schedule.png](./screenshots/weekly_schedule.png ':size=350')

   Pour supprimer une plage horaire, cliquez sur l’icône de corbeille ![](../../images/icons/icon_delete.png ':size=15') à côté de la plage horaire à supprimer. 


5. **Superviser le trafic** : vous pouvez également superviser le trafic vers les sites web bloqués ou autorisés pour suivre les habitudes d’utilisation et vérifier que les règles de filtrage sont respectées. Utilisez le bouton correspondant pour activer ou désactiver chaque catégorie.

   ![monitor.png](./screenshots/monitor.png ':size=350')

6. **Activer les modifications** en cliquant sur le bouton `➢ Submit`. Les règles sont alors activées.

> [!WARNING] 
> Vérifiez toujours les règles avant de les soumettre pour vous assurer que la configuration est correcte. Si vous effectuez des modifications que vous ne souhaitez pas conserver, utilisez le bouton `Clear changes` pour revenir à la version précédemment enregistrée.

> [!INFO]
> Si des modifications n’ont pas été enregistrées, un message d’avertissement s’affichera lorsque vous quitterez la page.
>
>![Capture d’écran de l’avertissement concernant les modifications non enregistrées](../../images/notifications/unsaved_changes.png ':size=300')
