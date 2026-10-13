# ![](../images/menu/menu_monitoring.png ':size=25') Supervision

>[!ATTENTION]
>Selon les options installées, le menu peut être différent et comporter plus ou moins d’éléments.

![monitoring.png](./screenshots/monitoring.png ":size=200")

### Activité

Vous trouverez ici un aperçu de toutes les activités sur le réseau. Les options sont `create`, `update` et `delete`.

![recent_activity.png](./screenshots/recent_activity.png ":size=700")

##### Détails d’une activité

Cliquez sur la ligne correspondant à une activité pour ouvrir une fenêtre contenant les informations sur celle-ci.

![activity_details.png](./screenshots/activity_details.png ":size=400")

##### Trier la liste des activités

Vous pouvez trier la liste par ordre alphabétique selon n’importe quel champ affiché : type, date de création, acteur. 

##### Filtrer la liste des activités

Vous pouvez rechercher dans la liste à l’aide du champ de recherche en haut de la page. 

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des activités.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher des options de filtrage avancées qui vous permettent de définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir comment faire correspondre la valeur (`is`, `contains` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur à faire correspondre, selon la propriété sélectionnée.

![act_monitoring_filter.png](./screenshots/act_monitoring_filter.png ':size=500')

Pour ajouter plusieurs filtres, cliquez de nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_act.png ':size=700')

> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.


### Inspection des paquets

L’inspection des paquets consiste à examiner les paquets de données qui circulent sur un réseau afin d’en déterminer le contenu. Cela permet aux appareils tels que les pare-feu de détecter et de bloquer les menaces comme les logiciels malveillants, d’identifier des applications spécifiques ou de gérer plus efficacement le flux du trafic. 

![packet_inspection.png](./screenshots/packet_inspection.png ":size=700")

>[!ATTENTION]
>Pour le moment, vous ne pouvez superviser que les paquets *_dropped_*. 


##### Trier la liste d’inspection des paquets

Vous pouvez trier la liste par ordre alphabétique selon n’importe quel champ affiché : horodatage, action, source, type de source, destination, type de destination, protocole. 

##### Filtrer la liste d’inspection des paquets

Vous pouvez rechercher dans la liste à l’aide du champ de recherche en haut de la page. 

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste d’inspection des paquets.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher des options de filtrage avancées qui vous permettent de définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir comment faire correspondre la valeur (`is`, `contains` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur à faire correspondre, selon la propriété sélectionnée.

![pi_monitoring_filter.png](./screenshots/pi_monitoring_filter.png ':size=500')

Pour ajouter plusieurs filtres, cliquez de nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_pi.png ':size=700')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.



### Supervision du filtrage web

La supervision du filtrage web consiste à observer et à analyser en continu le système de noms de domaine afin de garantir une résolution des noms de domaine fiable, rapide et sécurisée. Ce processus vérifie que le DNS traduit constamment les noms de domaine en adresses IP sans délai, erreur ni modification malveillante, ce qui est essentiel pour garantir la disponibilité et la sécurité des sites web. 

![dns_monitoring.png](./screenshots/dns_monitoring.png ":size=700")

##### Trier la liste de supervision du filtrage web

Vous pouvez trier la liste par ordre alphabétique selon n’importe quel champ affiché : nom d’hôte, type d’appareil, type, action, catégorie de contenu, adresse, horodatage.

##### Filtrer la liste de supervision du filtrage web

Vous pouvez rechercher dans la liste à l’aide du champ de recherche en haut de la page. 

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste de supervision du filtrage web.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher des options de filtrage avancées qui vous permettent de définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir comment faire correspondre la valeur (`is`, `contains` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur à faire correspondre, selon la propriété sélectionnée.

![dns_monitoring_filter.png](./screenshots/dns_monitoring_filter.png ':size=500')

Pour ajouter plusieurs filtres, cliquez de nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_DNS.png ':size=700')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.


## EDR

<!-- tabs:start -->

### **Fichiers malveillants**

Les fichiers malveillants détectés se trouvent dans cette section. Vous pouvez consulter la date et l’heure de la détection, l’appareil sur lequel le fichier a été détecté, l’utilisateur concerné et le nom du fichier, le niveau de gravité et l’action effectuée. 

  ![malicious_file.png](./screenshots/malicious_file.png ":size=700")

>[!NOTE]
>Vous pouvez ajouter un fichier à la liste blanche en cliquant sur le signe plus à la fin de sa ligne.

##### Détails d’un fichier malveillant

Cliquez sur la ligne correspondant à un fichier malveillant pour ouvrir une vue détaillée contenant des informations supplémentaires. 

![malicious_file_details.png](./screenshots/malicious_file_details.png ":size=500")

##### Trier la liste des fichiers malveillants

Vous pouvez trier la liste par ordre alphabétique selon n’importe quel champ affiché : horodatage, appareil, utilisateur, niveau de sécurité, nom de fichier, action effectuée.

##### Filtrer la liste des fichiers malveillants

Vous pouvez rechercher dans la liste à l’aide du champ de recherche en haut de la page. 

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des fichiers malveillants.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher des options de filtrage avancées qui vous permettent de définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir comment faire correspondre la valeur (`is`, `contains` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur à faire correspondre, selon la propriété sélectionnée.

![malicious_file_filter.png](./screenshots/malicious_file_filter.png ':size=500')

Pour ajouter plusieurs filtres, cliquez de nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_malfiles.png ':size=600')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.

### **Anomalies de fichiers**

Les anomalies de fichiers sont des changements ou des comportements inattendus dans les systèmes de fichiers. Les outils de sécurité les détectent souvent comme des signes de logiciels malveillants (par exemple, un rançongiciel qui chiffre des fichiers), de corruption de données ou de violations des politiques. Elles peuvent se manifester par des créations, suppressions ou modifications soudaines à grande échelle, des problèmes d’accès (modifications des autorisations) ou des irrégularités structurelles dans les fichiers exécutables (fichiers PE).

![file_anomalies.png](./screenshots/file_anomalies.png ":size=700")

##### Détails d’une anomalie de fichier

Cliquez sur la ligne correspondant à une anomalie de fichier pour ouvrir une vue détaillée contenant des informations supplémentaires. 

![file_anomalies_details.png](./screenshots/file_anomalies_details.png ":size=500")

##### Trier la liste des anomalies de fichiers

Vous pouvez trier la liste par ordre alphabétique selon n’importe quel champ affiché : horodatage, appareil, utilisateur, niveau de sécurité, type d’anomalie, processus, action effectuée.

##### Filtrer la liste des anomalies de fichiers

Vous pouvez rechercher dans la liste à l’aide du champ de recherche en haut de la page. 

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des anomalies de fichiers.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher des options de filtrage avancées qui vous permettent de définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir comment faire correspondre la valeur (`is`, `contains` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur à faire correspondre, selon la propriété sélectionnée.

![file_anomaly_filter.png](./screenshots/file_anomaly_filter.png ':size=500')

Pour ajouter plusieurs filtres, cliquez de nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_anomalies.png ':size=600')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.

  

### **Anomalies réseau**

La détection des anomalies réseau identifie les schémas inhabituels dans le trafic réseau. Elle va au-delà des menaces connues (signatures) pour repérer de nouvelles attaques (vulnérabilités de type « zero-day »), des violations des politiques ou des problèmes de performance. Pour ce faire, elle établit une base de référence du comportement normal et signale les écarts importants.

![network_anomalies.png](./screenshots/network_anomalies.png ":size=700")

##### Détails d’une anomalie réseau

Cliquez sur la ligne correspondant à une anomalie réseau pour ouvrir une vue détaillée contenant des informations supplémentaires. 

![nw_anomalies_details.png](./screenshots/nw_anomalies_details.png ":size=500")

##### Trier la liste des anomalies réseau

Vous pouvez trier la liste par ordre alphabétique selon n’importe quel champ affiché : horodatage, appareil, utilisateur, niveau de sécurité, type d’anomalie, source, destination, action effectuée.

##### Filtrer la liste des anomalies réseau

Vous pouvez rechercher dans la liste à l’aide du champ de recherche en haut de la page. 

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des anomalies réseau.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher des options de filtrage avancées qui vous permettent de définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir comment faire correspondre la valeur (`is`, `contains` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur à faire correspondre, selon la propriété sélectionnée.

![nw_anomaly_filter.png](./screenshots/nw_anomaly_filter.png ':size=500')

Pour ajouter plusieurs filtres, cliquez de nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_nw_anomalies.png ':size=600')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.





### **Binaires non signés**

La détection des binaires non signés est une pratique de sécurité essentielle pour identifier les logiciels malveillants potentiels ou les logiciels non autorisés dans un système. Les binaires (fichiers exécutables, DLL, etc.) devraient idéalement être signés numériquement par un éditeur de confiance à l’aide d’un certificat afin de vérifier leur origine et de garantir qu’ils n’ont pas été altérés. Les adversaires utilisent souvent des binaires non signés ou signés de manière incorrecte pour contourner les mesures de sécurité. 

![unsigned_binaries.png](./screenshots/unsigned_binaries.png ":size=700")

##### Détails d’un binaire non signé

Cliquez sur la ligne correspondant à une anomalie réseau pour ouvrir une vue détaillée contenant des informations supplémentaires. 

![binary_details.png](./screenshots/binary_details.png ":size=500")

##### Trier la liste des binaires non signés

Vous pouvez trier la liste par ordre alphabétique selon n’importe quel champ affiché : horodatage, appareil, utilisateur, niveau de sécurité, nom de fichier, action effectuée.

##### Filtrer la liste des binaires non signés

Vous pouvez rechercher dans la liste à l’aide du champ de recherche en haut de la page. 

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des binaires non signés.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher des options de filtrage avancées qui vous permettent de définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir comment faire correspondre la valeur (`is`, `contains` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur à faire correspondre, selon la propriété sélectionnée.

![unsigned_binary_filter.pn](./screenshots/unsigned_binary_filter.png ':size=500')

Pour ajouter plusieurs filtres, cliquez de nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_unsigned_binary.png ':size=600')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.

<!-- tabs:end -->
