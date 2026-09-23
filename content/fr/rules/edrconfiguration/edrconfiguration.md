File: rules/edrconfiguration/edrconfiguration.md

# ![](../../images/menu/menu_edr.png ':size=50') EDR

La configuration EDR (Endpoint Detection and Response) consiste à définir des politiques et des paramètres pour superviser, détecter et contrer les menaces sur les terminaux.
Le processus EDR implique une supervision constante et la collecte de données à partir des terminaux afin d’identifier les menaces et d’y répondre en temps réel. Il fournit également des informations sur les actions effectuées sur les terminaux, notamment des détails sur les cyberattaques tentées.


> [!IMPORTANT]
> Cette fonctionnalité doit être activée par un administrateur de l’entreprise.
  
### CONFIGURATION EDR

![edrconfiguration.png](./screenshots/edrconfiguration.png ':size=800')


> [!WARNING]
> Choisir un niveau de sensibilité plus élevé pour la détection des fichiers malveillants peut entraîner davantage de faux positifs.

> [!NOTE]
> Si l’EDR est configuré, vous pouvez utiliser la [page de supervision](/./monitoring/monitoring.md) pour examiner les activités et les menaces enregistrées.

> [!IMPORTANT]
> Si l’option « Verrouiller le réseau de l’appareil » est activée et qu’un problème survient, un administrateur doit déverrouiller à nouveau le réseau de l’appareil à l’aide de l’une des procédures Windows standard, par exemple via le Gestionnaire de périphériques.

### Liste blanche EDR

Une liste blanche EDR configure une plateforme Endpoint Detection and Response afin qu’elle ignore certains fichiers, dossiers, processus ou scripts. Cela empêche les outils d’administration légitimes ou les logiciels essentiels à l’activité de déclencher de fausses alertes, de bloquer l’exécution ou de consommer des ressources.

Utilisez les listes blanches dans l’EDR pour :
-  Empêcher les agents de sécurité de supprimer par erreur des applications essentielles ou des logiciels propriétaires, et ainsi assurer la continuité des activités.
-  Réduire le nombre de faux positifs, faire gagner du temps aux équipes de sécurité et ainsi réduire la fatigue liée aux alertes.

#### Créer une entrée de liste blanche

Pour créer une nouvelle entrée de liste blanche, cliquez sur le bouton `+ Create new` situé dans le coin supérieur droit de l’interface.

![create_whitelist.png](./screenshots/create_whitelist.png ':size=500')

- Saisissez le nom du fichier.
- Saisissez le hachage. Calculez le hachage, par exemple à l’aide d’un outil en ligne comme [Calculateur SHA256 en ligne](https://emn178.github.io/online-tools/sha256.html).


#### Modifier une entrée de liste blanche

Vous pouvez modifier les entrées de la liste blanche en cliquant sur l’icône de modification de leur ligne.

![edit_whitelist.png](./screenshots/edit_whitelist.png ':size=500')

Vous pouvez modifier le nom du fichier. Il n’est pas nécessaire de recalculer le hachage.
