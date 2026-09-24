# ![](../../images/menu/menu_webfiltering.png ':size=28') Filtrage web

Le filtrage web vous permet de contrôler et de gérer les sites web auxquels un groupe spécifique peut accéder sur le réseau. Vous pouvez bloquer des catégories de contenu telles que les contenus pour adultes, les fausses informations, les jeux d’argent, les logiciels malveillants/publicitaires et les réseaux sociaux.

Vous pouvez également configurer des restrictions horaires, non seulement pour certaines heures de la journée, mais aussi pour certains jours de la semaine. Vous pouvez ainsi adapter plus précisément l’accès en limitant le contenu uniquement à certaines heures ou certains jours de la semaine.

Le trafic vers les sites bloqués peut être supervisé, ce qui vous permet de savoir quels utilisateurs ont tenté d’accéder à du contenu restreint. Vous pouvez personnaliser davantage le filtrage web en utilisant une liste de blocage pour bloquer des sites spécifiques ou une liste d’autorisation pour permettre l’accès à certains sites web. Tous ces paramètres sont configurables par groupe, ce qui vous permet d’appliquer différentes règles en fonction des besoins de chaque groupe de votre réseau.

Le filtrage web utilise des listes régulièrement mises à jour pour chaque catégorie afin de garantir que les nouvelles menaces et les contenus indésirables soient automatiquement détectés et bloqués dès leur apparition.

![Capture d’écran de la page Filtrage web](./screenshots/webfiltering.png ':size=800')

> [!WARNING]
> Le filtrage web ne sera appliqué que si *Surcharge DNS* et/ou *Inspection SSL* est activée pour le groupe choisi. Sans l’une ou l’autre de ces options, les règles de filtrage ne seront pas appliquées.

![dns_override_ssl_inspection.png](./screenshots/dns_override_ssl_inspection.png ':size=300')

### Configurer le filtrage web

Pour configurer le filtrage web pour un groupe, procédez comme suit :

1. **Sélectionner un groupe** : commencez par sélectionner le groupe pour lequel vous souhaitez configurer des règles de filtrage.

> [!INFO] 
> Si un utilisateur appartient à plusieurs groupes dont les règles de filtrage web sont contradictoires, le blocage est prioritaire sur l’autorisation. Cela signifie que si un groupe bloque un site et qu’un autre l’autorise, le site sera bloqué pour cet utilisateur.

2. **Bloquer des catégories** : choisissez des catégories de contenu spécifiques (par exemple, contenus pour adultes, logiciels malveillants, jeux d’argent) et bloquez-les afin d’en restreindre l’accès pour le groupe sélectionné. Utilisez le bouton correspondant pour activer ou désactiver chaque catégorie.

3. **Gérer les sites web** :
   - **Liste de blocage** : ajoutez les sites web que vous souhaitez bloquer en saisissant leurs URL dans la liste de blocage.
   - **Liste d’autorisation** : ajoutez les sites web de confiance à la liste d’autorisation afin qu’ils restent accessibles, même s’ils appartiennent à une catégorie bloquée.
   - **Supprimer des sites web** : pour supprimer un site web de l’une ou l’autre liste, cliquez sur l’icône de corbeille rouge située à côté du nom du site web.

4. **Règles horaires** : définissez des règles horaires pour contrôler l’accès (bloquer) à certains sites pendant des plages horaires spécifiques. Cliquez sur l’icône en forme d’horloge pour définir quand les restrictions doivent s’appliquer.

5. **Superviser le trafic** : vous pouvez également superviser le trafic vers les sites web bloqués ou autorisés afin de suivre les habitudes d’utilisation et de vérifier que les règles de filtrage sont respectées. Utilisez le bouton correspondant pour activer ou désactiver chaque catégorie.

6. **Activer les modifications** en cliquant sur le bouton `➢ Submit`. Les règles deviennent actives.

> [!WARNING] 
> Vérifiez toujours attentivement les règles avant de les soumettre afin de vous assurer que la configuration est correcte. Si vous apportez des modifications que vous ne souhaitez pas conserver, utilisez le bouton `Clear changes` pour revenir à la version précédemment enregistrée.

> [!INFO]
> Si des modifications n’ont pas été enregistrées, un message d’avertissement apparaîtra.
>
>![Capture d’écran de l’avertissement relatif aux modifications non enregistrées](./screenshots/unsaved_changes.png ':size=300')
