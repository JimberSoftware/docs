File: devices/networkcontrollers/networkcontrollers.md

# ![](../../images/menu/menu_networkcontrollers.png ':size=25') Contrôleurs réseau
> [!INFO]
> Les contrôleurs réseau peuvent être hébergés dans le cloud ou sur site.

Un contrôleur réseau est un équipement réseau qui achemine des paquets de données entre les réseaux. Les contrôleurs réseau jouent un rôle crucial dans la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***. Isoler un réseau consiste à restreindre son accessibilité aux seules entités de confiance et à empêcher tout accès non autorisé. 

> [!INFO]
> Un contrôleur réseau garantit qu’aucune partie de votre réseau, qu’il s’agisse d’un appareil, d’un utilisateur ou d’une application, ne peut accéder à une autre partie sans autorisation explicite.


![contrôleurs réseau.png](./screenshots/networkcontrollers.png ':size=800')

### Filtrer les contrôleurs réseau

Vous pouvez rechercher des contrôleurs réseau dans la liste à l’aide du champ de recherche en haut de la page. Cela vous permet de trouver et de gérer rapidement le contrôleur réseau recherché.

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des contrôleurs réseau.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Lorsque vous cliquez dessus, des options de filtrage avancées s’affichent. Elles vous permettent de définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ sur lequel appliquer le filtre.
- **Type de correspondance** : menu déroulant qui vous permet de choisir comment faire correspondre la valeur (`is`, `contains` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur à faire correspondre, selon la propriété choisie.

![filter_nc.png](./screenshots/filter_nc.png ':size=400')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.


> [!TIP]
> Vous pouvez actualiser la liste des contrôleurs réseau en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

### Contrôleur réseau cloud (par défaut)

Chaque entreprise qui utilise la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** dispose **par défaut** d’un contrôleur réseau cloud. Ce contrôleur réseau garantit que tous les appareils et utilisateurs de l’entreprise, internes comme externes, peuvent accéder au réseau de manière sécurisée et cohérente. Le contrôleur réseau cloud sert de point d’entrée et de sortie au trafic réseau, afin que chacun puisse se connecter et accéder aux ressources nécessaires.

### Contrôleur réseau sur site (facultatif)

L’approche reposant uniquement sur le cloud peut toutefois poser un problème. Sans contrôleur réseau sur site, le trafic interne ou sur site est acheminé par Internet, ce qui peut entraîner une latence inutile.

Pour répondre à cette préoccupation, les entreprises peuvent ajouter un contrôleur réseau sur site à leur configuration. 

> [!INFO]
> Le trafic local reste ainsi local et n’est pas acheminé vers Internet, ce qui garantit des temps de réponse plus courts pour les opérations du réseau interne.

##### Types de contrôleurs réseau sur site :
1. **Appliance virtuelle** : contrôleur réseau logiciel qui peut être installé sur une infrastructure virtualisée, ce qui facilite son déploiement, sa mise à l’échelle et sa gestion.
2. **Appliance physique** : équipement matériel installé dans le centre de données ou l’armoire réseau de l’entreprise.

### Haute disponibilité

Deux contrôleurs réseau sur site peuvent être configurés en paire à haute disponibilité. Une appliance est **principale** et traite normalement le trafic réseau. L’autre appliance est **secondaire** et reste en veille jusqu’à ce que l’appliance principale devienne indisponible.

Les deux appliances représentent le même contrôleur réseau dans la Plateforme Jimber SASE et doivent utiliser le même jeton de contrôleur réseau. Chaque appliance conserve sa propre clé publique et sa propre clé privée générées. Ne copiez pas les clés de l’appliance principale sur l’appliance secondaire.

Les appliances nécessitent une interface physique dédiée à la connexion HA. Le contrôleur réseau configure automatiquement cette interface avec les adresses suivantes :

| Rôle | Adresse HA | Port TCP |
| --- | --- | --- |
| Principal | `198.51.100.1/30` | `49152` |
| Secondaire | `198.51.100.2/30` | Se connecte à `198.51.100.1:49152` |

Connectez directement les deux interfaces HA ou placez-les sur un réseau de couche 2 isolé. Ne configurez pas ces adresses manuellement et n’utilisez pas l’interface HA pour le trafic réseau normal. Le port TCP `49152` doit être autorisé entre les deux appliances.

Les interfaces physiques utilisées pour le trafic WAN et LAN doivent avoir les mêmes noms d’interface Linux sur les deux appliances. Par exemple, si l’appliance principale utilise `enp1s0` et `enp2s0`, l’appliance secondaire doit exposer ces interfaces sous les mêmes noms. L’interface HA dédiée n’est pas concernée par cette exigence, car elle est configurée séparément sur chaque appliance.

#### Configurer l’appliance principale

Ajoutez les champs suivants à `/etc/jimber/settings.json` sur l’appliance principale. Remplacez `enp6s0` par l’interface physique dédiée à la connexion HA.

```json
{
  "token": "same-network-controller-token",
  "highAvailable": "primary",
  "highAvailableInterface": "enp6s0"
}
```

#### Configurer l’appliance secondaire

Utilisez le même jeton de contrôleur réseau sur l’appliance secondaire et définissez son rôle sur `secondary` :

```json
{
  "token": "same-network-controller-token",
  "highAvailable": "secondary",
  "highAvailableInterface": "enp6s0"
}
```

Redémarrez le service Jimber Network Controller sur les deux appliances après avoir mis à jour les paramètres.

#### Comportement du basculement

L’appliance principale démarre les services du contrôleur réseau et écoute l’appliance secondaire sur la connexion HA dédiée. L’appliance secondaire maintient les interfaces HA et loopback actives, mais désactive toutes les autres interfaces tant que l’appliance principale est disponible.

Lorsque l’appliance secondaire ne parvient plus à joindre l’appliance principale, elle active ses interfaces de données et démarre les services du contrôleur réseau. Elle s’annonce à l’aide du jeton partagé. La plateforme associe alors le contrôleur réseau à la clé publique de l’appliance secondaire et envoie sa configuration via la hiérarchie de contrôleurs.

Lorsque l’appliance principale revient et indique que ses services de contrôleur réseau sont opérationnels, l’appliance secondaire arrête ses services actifs, supprime l’état réseau géré par Jimber, remet ses interfaces de données en veille et redémarre le binaire Jimber en mode veille. L’appliance principale reprend alors le rôle actif.

> [!WARNING]
> La connexion HA détecte la disponibilité de l’appliance, et non l’état du réseau en amont. Une panne qui laisse l’appliance principale en fonctionnement et joignable via la liaison HA ne provoque pas la promotion de l’appliance secondaire.

> [!INFO]
> Lorsqu’une mise à jour pour un contrôleur réseau est disponible, une icône verte de mise à jour ![](../../images/icons/icon_update.png ':size=20') apparaît. Cliquez sur l’icône pour lancer la mise à jour.
>
> ![nc_onpremise_update.png](./screenshots/nc_onpremise_update.png ':size=800')

<!-- ## Create on-premise Network Controllers -->
### Créer un contrôleur réseau

Pour ajouter un contrôleur réseau à la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***, cliquez sur le bouton `+ Create new` situé dans le coin supérieur droit de l’interface.

![create_networkcontroller.png](./screenshots/create_networkcontroller.png ':size=400')


Le nom d’hôte et l’adresse du point de terminaison sont obligatoires. Le nom d’hôte ne doit contenir que des lettres, des chiffres et, éventuellement, des traits d’union.

> [!INFO]
> Des instructions détaillées sur l’installation d’un contrôleur réseau sur site sont disponibles [ici](/./advanced/networkcontrollerssetup/SettingUpServer.md). 
> Les spécifications minimales d’un contrôleur réseau sur site sont les suivantes :
> 
> **Généralités** :
> - Disque dur de 25GB
> **Pour 50 utilisateurs :**
> - 2 CPU
> - 4GB RAM

### Connexion SSH à un contrôleur réseau

![network controllers_1.png](./screenshots/networkcontrollers_1.png ':size=700x40')


En cliquant sur l’icône de cadenas, vous pouvez établir une connexion SSH au contrôleur réseau. Vous recevrez alors un code TOTP que vous pourrez saisir dans la session SSH.

![totp_nc.png](./screenshots/totp_nc.png ':size=500')


<!-- ### Edit on-premise Network Controller -->
### Modifier un contrôleur réseau

 Vous pouvez modifier un contrôleur réseau en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de sa ligne.

![edit_networkcontroller.png](./screenshots/edit_networkcontroller.png ':size=400') 


<!-- ### Delete on-premise Network Controllers -->
### Supprimer un contrôleur réseau

 Vous pouvez supprimer des contrôleurs réseau en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') de leur ligne.

 Un avertissement s’affiche avant la suppression définitive de l’appareil :

![delete_networkcontroller.png](./screenshots/delete_networkcontroller.png ':size=350')
