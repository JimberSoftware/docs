File: rules/webfiltering/webfiltering.md



# ![](../../images/menu/menu_webfiltering.png ':size=28') Filtrage web

Le filtrage web vous permet de contrôler et de gérer les sites web auxquels un groupe spécifique peut accéder sur le réseau. Vous pouvez bloquer des catégories de contenu telles que le contenu pour adultes, les fausses informations, les jeux d’argent, les logiciels malveillants/publicitaires et les réseaux sociaux.

Vous pouvez également configurer des restrictions horaires, non seulement pour certaines heures de la journée, mais aussi pour certains jours de la semaine. Cela vous permet d’adapter plus précisément l’accès en restreignant le contenu uniquement à certaines heures ou certains jours de la semaine.

Le trafic vers les sites bloqués peut être supervisé, ce qui permet de savoir quels utilisateurs ont tenté d’accéder à du contenu restreint. Vous pouvez personnaliser davantage le filtrage web en utilisant une liste de blocage pour bloquer des sites spécifiques ou une liste d’autorisation pour autoriser l’accès à certains sites web. Tous ces paramètres sont configurables par groupe, afin que vous puissiez appliquer différentes règles selon les besoins de chaque groupe de votre réseau.

Le filtrage web utilise des listes régulièrement mises à jour pour chaque catégorie afin de garantir que les nouvelles menaces et les contenus indésirables sont automatiquement détectés et bloqués dès leur apparition.

![Capture d’écran de la page Filtrage web](./screenshots/webfiltering.png ':size=800')

> [!WARNING]
> Pour que les règles de filtrage web soient efficaces, le remplacement DNS doit être activé pour le même groupe. Sans cela, les règles de filtrage ne seront pas appliquées.

### Configurer le filtrage web

Pour configurer le filtrage web pour un groupe, procédez comme suit :

1. **Sélectionner un groupe** : commencez par sélectionner le groupe pour lequel vous souhaitez configurer des règles de filtrage.

> [!INFO] 
> Si un utilisateur appartient à plusieurs groupes dont les règles de filtrage web sont contradictoires, le blocage prévaut sur l’autorisation. Cela signifie que si un groupe bloque un site et qu’un autre l’autorise, le site sera bloqué pour cet utilisateur.

2. **Bloquer des catégories** : choisissez et bloquez des catégories de contenu spécifiques (par exemple, le contenu pour adultes, les logiciels malveillants ou les jeux d’argent) afin d’en restreindre l’accès pour le groupe sélectionné. Utilisez le bouton correspondant pour activer ou désactiver chaque catégorie.

3. **Gérer les sites web** :
   - **Liste de blocage** : ajoutez les sites web que vous souhaitez bloquer en saisissant leurs URL dans la liste de blocage.
   - **Liste d’autorisation** : ajoutez les sites web de confiance à la liste d’autorisation afin qu’ils restent accessibles, même s’ils appartiennent à une catégorie bloquée.
   - **Supprimer des sites web** : pour supprimer un site web de l’une ou l’autre liste, cliquez sur l’icône de corbeille rouge à côté du nom du site.

4. **Règles horaires** : définissez des règles horaires pour contrôler l’accès à certains sites pendant des plages horaires spécifiques. Cliquez sur l’icône en forme d’horloge pour définir quand les restrictions doivent s’appliquer.

5. **Superviser le trafic** : vous pouvez également superviser le trafic vers les sites web bloqués ou autorisés afin de suivre les habitudes d’utilisation et de vérifier que les règles de filtrage sont respectées. Utilisez le bouton correspondant pour activer ou désactiver chaque catégorie.

6. **Activer les modifications** : une fois vos modifications effectuées, cliquez sur le bouton `➢ Submit rules` pour les appliquer et activer les règles.

> [!WARNING] 
> Vérifiez toujours attentivement les règles avant de les soumettre afin de vous assurer que la configuration est correcte. Si vous effectuez des modifications que vous ne souhaitez pas conserver, utilisez le bouton `Clear changes` pour rétablir la version précédemment enregistrée.

> [!INFO]
> Si des modifications n’ont pas été enregistrées, un message d’avertissement s’affichera afin que vous n’oubliiez pas de mettre à jour vos paramètres.
>
>![Capture d’écran de l’avertissement indiquant que des modifications n’ont pas été enregistrées](../../images/notifications/unsaved_changes.png ':size=400')
