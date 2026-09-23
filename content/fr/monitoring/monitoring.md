# ![](../images/menu/menu_monitoring.png ':size=25') Supervision

>[!ATTENTION]
>Selon les options installées, le menu peut être différent et comporter plus ou moins d’éléments.

![monitoring.png](./screenshots/monitoring.png ":size=200")

### Activité

Vous trouverez ici un aperçu de toute l’activité sur le réseau. Les options sont `create`, `update` et `delete`.

![recent_activity.png](./screenshots/recent_activity.png ":size=700")

##### Détails d’une activité

En cliquant sur la ligne correspondante d’une activité, une fenêtre s’ouvre avec les informations relatives à cette activité.

![activity_details.png](./screenshots/activity_details.png ":size=400")

##### Trier la liste des activités

Vous pouvez trier la liste par ordre alphabétique selon n’importe quel champ affiché : type, date de création, acteur.

##### Filtrer la liste des activités

Vous pouvez effectuer une recherche dans la liste à l’aide du champ de recherche situé en haut de la page.

Utilisez le champ de recherche pour saisir des mots-clés et filtrer la liste des activités.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Lorsque vous cliquez dessus, des options de filtrage avancées s’affichent. Vous pouvez alors définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : un menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : un menu déroulant qui vous permet de choisir comment comparer la valeur (`equals`, `contains` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à rechercher, selon la propriété choisie.

![act_monitoring_filter.png](./screenshots/act_monitoring_filter.png ':size=500')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_act.png ':size=700')

> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.


### Inspection des paquets

L’inspection des paquets consiste à examiner les paquets de données lorsqu’ils circulent sur un réseau afin d’en déterminer le contenu. Cela permet aux appareils tels que les pare-feu de détecter et de bloquer les menaces comme les logiciels malveillants, d’identifier des applications spécifiques ou de gérer plus efficacement le flux de trafic.

![packet_inspection.png](./screenshots/packet_inspection.png ":size=700")

>[!ATTENTION]
>Pour le moment, vous pouvez uniquement superviser les paquets *_dropped_*.

##### Trier la liste d’inspection des paquets

Vous pouvez trier la liste par ordre alphabétique selon n’importe quel champ affiché : horodatage, action, source, type de source, destination, type de destination, protocole.

##### Filtrer la liste d’inspection des paquets

Vous pouvez effectuer une recherche dans la liste à l’aide du champ de recherche situé en haut de la page.

Utilisez le champ de recherche pour saisir des mots-clés et filtrer la liste d’inspection des paquets.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Lorsque vous cliquez dessus, des options de filtrage avancées s’affichent. Vous pouvez alors définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : un menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : un menu déroulant qui vous permet de choisir comment comparer la valeur (`equals`, `contains` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à rechercher, selon la propriété choisie.

![pi_monitoring_filter.png](./screenshots/pi_monitoring_filter.png ':size=500')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_pi.png ':size=700')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.



### Supervision du filtrage web

La supervision du filtrage web consiste à observer et analyser en continu le système de noms de domaine afin de garantir une résolution fiable, rapide et sécurisée des noms de domaine. Ce processus vérifie que le DNS convertit systématiquement les noms de domaine en adresses IP, sans retard, erreur ni modification malveillante, ce qui est essentiel pour maintenir la disponibilité et la sécurité des sites web.

![dns_monitoring.png](./screenshots/dns_monitoring.png ":size=700")

##### Trier la liste de supervision du filtrage web

Vous pouvez trier la liste par ordre alphabétique selon n’importe quel champ affiché : nom d’hôte, type d’appareil, type, action, catégorie de contenu, adresse, horodatage.

##### Filtrer la liste de supervision du filtrage web

Vous pouvez effectuer une recherche dans la liste à l’aide du champ de recherche situé en haut de la page.

Utilisez le champ de recherche pour saisir des mots-clés et filtrer la liste de supervision du filtrage web.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Lorsque vous cliquez dessus, des options de filtrage avancées s’affichent. Vous pouvez alors définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : un menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : un menu déroulant qui vous permet de choisir comment comparer la valeur (`equals`, `contains` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à rechercher, selon la propriété choisie.

![dns_monitoring_filter.png](./screenshots/dns_monitoring_filter.png ':size=500')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_DNS.png ':size=700')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.


## EDR

<!-- tabs:start -->

### **Fichiers malveillants**

Les fichiers malveillants détectés se trouvent dans cette section. Vous pouvez consulter la date et l’heure de la détection, l’appareil sur lequel le fichier a été détecté, l’utilisateur concerné et le nom du fichier, le niveau de gravité ainsi que l’action entreprise.

  ![malicious_file.png](./screenshots/malicious_file.png ":size=700")

>[!NOTE]
>Vous pouvez ajouter un fichier à la liste blanche en cliquant sur le signe plus à la fin de sa ligne.

##### Détails d’un fichier malveillant

En cliquant sur la ligne correspondante d’un fichier malveillant, une vue détaillée s’ouvre avec des informations supplémentaires.

![malicious_file_details.png](./screenshots/malicious_file_details.png ":size=500")

##### Trier la liste des fichiers malveillants

Vous pouvez trier la liste par ordre alphabétique selon n’importe quel champ affiché : horodatage, appareil, utilisateur, niveau de sécurité, nom de fichier, action entreprise.

##### Filtrer la liste des fichiers malveillants

Vous pouvez effectuer une recherche dans la liste à l’aide du champ de recherche situé en haut de la page.

Utilisez le champ de recherche pour saisir des mots-clés et filtrer la liste des fichiers malveillants.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Lorsque vous cliquez dessus, des options de filtrage avancées s’affichent. Vous pouvez alors définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : un menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : un menu déroulant qui vous permet de choisir comment comparer la valeur (`equals`, `contains` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à rechercher, selon la propriété choisie.

![malicious_file_filter.png](./screenshots/malicious_file_filter.png ':size=500')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_malfiles.png ':size=600')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.

### **Anomalies de fichiers**

Les anomalies de fichiers sont des changements ou comportements inattendus dans les systèmes de fichiers. Les outils de sécurité les détectent souvent comme des signes de logiciels malveillants (par exemple, un rançongiciel qui chiffre des fichiers), de corruption de données ou de violations de politiques. Il peut s’agir de créations, suppressions ou modifications soudaines à grande échelle, de problèmes d’accès (modifications des autorisations) ou d’irrégularités structurelles dans des fichiers exécutables (fichiers PE).

![file_anomalies.png](./screenshots/file_anomalies.png ":size=700")

##### Détails d’une anomalie de fichier

En cliquant sur la ligne correspondante d’une anomalie de fichier, une vue détaillée s’ouvre avec des informations supplémentaires.

![file_anomalies_details.png](./screenshots/file_anomalies_details.png ":size=500")

##### Trier la liste des anomalies de fichiers

Vous pouvez trier la liste par ordre alphabétique selon n’importe quel champ affiché : horodatage, appareil, utilisateur, niveau de sécurité, type d’anomalie, processus, action entreprise.

##### Filtrer la liste des anomalies de fichiers

Vous pouvez effectuer une recherche dans la liste à l’aide du champ de recherche situé en haut de la page.

Utilisez le champ de recherche pour saisir des mots-clés et filtrer la liste des anomalies de fichiers.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Lorsque vous cliquez dessus, des options de filtrage avancées s’affichent. Vous pouvez alors définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : un menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : un menu déroulant qui vous permet de choisir comment comparer la valeur (`equals`, `contains` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à rechercher, selon la propriété choisie.

![file_anomaly_filter.png](./screenshots/file_anomaly_filter.png ':size=500')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_anomalies.png ':size=600')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.

  

### **Anomalies réseau**

La détection des anomalies réseau identifie les schémas inhabituels dans le trafic réseau. Elle va au-delà des menaces connues (signatures) pour repérer de nouvelles attaques (zero-days), des violations de politiques ou des problèmes de performances. Pour cela, elle établit une base de référence du comportement normal et signale les écarts importants.

![network_anomalies.png](./screenshots/network_anomalies.png ":size=700")

##### Détails d’une anomalie réseau

En cliquant sur la ligne correspondante d’une anomalie réseau, une vue détaillée s’ouvre avec des informations supplémentaires.

![nw_anomalies_details.png](./screenshots/nw_anomalies_details.png ":size=500")

##### Trier la liste des anomalies réseau

Vous pouvez trier la liste par ordre alphabétique selon n’importe quel champ affiché : horodatage, appareil, utilisateur, niveau de sécurité, type d’anomalie, source, destination, action entreprise.

##### Filtrer la liste des anomalies réseau

Vous pouvez effectuer une recherche dans la liste à l’aide du champ de recherche situé en haut de la page.

Utilisez le champ de recherche pour saisir des mots-clés et filtrer la liste des anomalies réseau.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Lorsque vous cliquez dessus, des options de filtrage avancées s’affichent. Vous pouvez alors définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : un menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : un menu déroulant qui vous permet de choisir comment comparer la valeur (`equals`, `contains` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à rechercher, selon la propriété choisie.

![nw_anomaly_filter.png](./screenshots/nw_anomaly_filter.png ':size=500')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_nw_anomalies.png ':size=600')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.





### **Binaires non signés**

La détection des binaires non signés est une pratique de sécurité essentielle qui permet d’identifier les logiciels malveillants potentiels ou les logiciels non autorisés au sein d’un système. Les binaires (fichiers exécutables, DLL, etc.) devraient idéalement être signés numériquement par un éditeur de confiance à l’aide d’un certificat, afin de vérifier leur origine et de garantir qu’ils n’ont pas été modifiés. Les attaquants utilisent souvent des binaires non signés ou dont la signature est incorrecte pour contourner les mesures de sécurité.

![unsigned_binaries.png](./screenshots/unsigned_binaries.png ":size=700")

##### Détails d’un binaire non signé

En cliquant sur la ligne correspondante d’une anomalie réseau, une vue détaillée s’ouvre avec des informations supplémentaires.

![binary_details.png](./screenshots/binary_details.png ":size=500")

##### Trier la liste des binaires non signés

Vous pouvez trier la liste par ordre alphabétique selon n’importe quel champ affiché : horodatage, appareil, utilisateur, niveau de sécurité, nom de fichier, action entreprise.

##### Filtrer la liste des binaires non signés

Vous pouvez effectuer une recherche dans la liste à l’aide du champ de recherche situé en haut de la page.

Utilisez le champ de recherche pour saisir des mots-clés et filtrer la liste des binaires non signés.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Lorsque vous cliquez dessus, des options de filtrage avancées s’affichent. Vous pouvez alors définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : un menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : un menu déroulant qui vous permet de choisir comment comparer la valeur (`equals`, `contains` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à rechercher, selon la propriété choisie.

![unsigned_binary_filter.pn](./screenshots/unsigned_binary_filter.png ':size=500')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_unsigned_binary.png ':size=600')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.

<!-- tabs:end -->
