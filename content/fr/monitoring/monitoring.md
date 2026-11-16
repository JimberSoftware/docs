File: monitoring/monitoring.md

# ![](../images/menu/menu_monitoring.png ':size=25') Supervision

>[!ATTENTION]
>Selon les options installées, le menu peut être différent et comporter plus ou moins d’éléments.

![monitoring.png](./screenshots/monitoring.png ":size=300")

### Activité

Vous trouverez ici un aperçu de toutes les activités sur le réseau. Les options sont `create`, `update` et `delete`.

![recent_activity.png](./screenshots/recent_activity.png ":size=700")

##### Détails d’une activité

Cliquez sur la ligne correspondante à une activité pour ouvrir une fenêtre contenant les informations sur cette activité.

![activity_details.png](./screenshots/activity_details.png ":size=400")

##### Tri de la liste des activités

Vous pouvez trier la liste par ordre alphabétique en fonction de n’importe quel champ affiché : type, date de création, acteur.

##### Filtrage de la liste des activités

Vous pouvez rechercher dans la liste à l’aide du champ de recherche situé en haut de la page.

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des activités.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher les options de filtrage avancées, qui vous permettent de définir des conditions supplémentaires en fonction des trois éléments suivants :

- **Propriété** : menu déroulant permettant de choisir le champ à filtrer.
- **Type de correspondance** : menu déroulant permettant de choisir le mode de correspondance de la valeur (`is`, `contains` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur recherchée, en fonction de la propriété sélectionnée.

![act_monitoring_filter.png](./screenshots/act_monitoring_filter.png ':size=500')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_act.png ':size=700')

> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.


### Inspection des paquets

L’inspection des paquets consiste à examiner les paquets de données qui circulent sur un réseau afin d’en déterminer le contenu. Cela permet aux appareils tels que les pare-feu de détecter et de bloquer les menaces comme les logiciels malveillants, d’identifier des applications spécifiques ou de gérer plus efficacement le flux de trafic.

![packet_inspection.png](./screenshots/packet_inspection.png ":size=700")

>[!ATTENTION]
>Pour le moment, vous pouvez uniquement superviser les paquets *_dropped_*.

##### Tri de la liste d’inspection des paquets

Vous pouvez trier la liste par ordre alphabétique en fonction de n’importe quel champ affiché : horodatage, action, source, type de source, destination, type de destination, protocole.

##### Filtrage de la liste d’inspection des paquets

Vous pouvez rechercher dans la liste à l’aide du champ de recherche situé en haut de la page.

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste d’inspection des paquets.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher les options de filtrage avancées, qui vous permettent de définir des conditions supplémentaires en fonction des trois éléments suivants :

- **Propriété** : menu déroulant permettant de choisir le champ à filtrer.
- **Type de correspondance** : menu déroulant permettant de choisir le mode de correspondance de la valeur (`is`, `contains` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur recherchée, en fonction de la propriété sélectionnée.

![pi_monitoring_filter.png](./screenshots/pi_monitoring_filter.png ':size=500')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_pi.png ':size=700')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.



### Supervision du filtrage web

La supervision du filtrage web consiste à observer et à analyser en continu le système de noms de domaine afin de garantir une résolution des noms de domaine fiable, rapide et sécurisée. Ce processus vérifie que le DNS traduit systématiquement les noms de domaine en adresses IP, sans retard, erreur ni modification malveillante, ce qui est essentiel pour maintenir la disponibilité et la sécurité des sites web.

![dns_monitoring.png](./screenshots/dns_monitoring.png ":size=700")

##### Tri de la liste de supervision du filtrage web

Vous pouvez trier la liste par ordre alphabétique en fonction de n’importe quel champ affiché : nom d’hôte, type d’appareil, type, action, catégorie de contenu, adresse, horodatage.

##### Filtrage de la liste de supervision du filtrage web

Vous pouvez rechercher dans la liste à l’aide du champ de recherche situé en haut de la page.

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste de supervision du filtrage web.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher les options de filtrage avancées, qui vous permettent de définir des conditions supplémentaires en fonction des trois éléments suivants :

- **Propriété** : menu déroulant permettant de choisir le champ à filtrer.
- **Type de correspondance** : menu déroulant permettant de choisir le mode de correspondance de la valeur (`is`, `contains` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur recherchée, en fonction de la propriété sélectionnée.

![dns_monitoring_filter.png](./screenshots/dns_monitoring_filter.png ':size=500')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_DNS.png ':size=700')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.


## EDR

<!-- tabs:start -->

### **Fichiers malveillants**

Les fichiers malveillants détectés se trouvent dans cette section. Vous pouvez voir la date et l’heure de la détection, l’appareil sur lequel le fichier a été détecté, l’utilisateur concerné et le nom du fichier, le niveau de gravité ainsi que l’action effectuée.

  ![malicious_file.png](./screenshots/malicious_file.png ":size=700")

>[!NOTE]
>Vous pouvez ajouter un fichier à la liste blanche en cliquant sur le signe plus à la fin de sa ligne.

##### Détails d’un fichier malveillant

Cliquez sur la ligne correspondant à un fichier malveillant pour ouvrir une vue détaillée contenant des informations supplémentaires.

![malicious_file_details.png](./screenshots/malicious_file_details.png ":size=500")

##### Tri de la liste des fichiers malveillants

Vous pouvez trier la liste par ordre alphabétique en fonction de n’importe quel champ affiché : horodatage, appareil, utilisateur, niveau de sécurité, nom de fichier, action effectuée.

##### Filtrage de la liste des fichiers malveillants

Vous pouvez rechercher dans la liste à l’aide du champ de recherche situé en haut de la page.

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des fichiers malveillants.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher les options de filtrage avancées, qui vous permettent de définir des conditions supplémentaires en fonction des trois éléments suivants :

- **Propriété** : menu déroulant permettant de choisir le champ à filtrer.
- **Type de correspondance** : menu déroulant permettant de choisir le mode de correspondance de la valeur (`is`, `contains` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur recherchée, en fonction de la propriété sélectionnée.

![malicious_file_filter.png](./screenshots/malicious_file_filter.png ':size=500')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_malfiles.png ':size=600')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.

### **Anomalies de fichiers**

Les anomalies de fichiers sont des changements ou comportements inattendus dans les systèmes de fichiers. Les outils de sécurité les détectent souvent comme des signes de logiciels malveillants (par exemple, un rançongiciel qui chiffre des fichiers), de corruption de données ou de violations des politiques. Il peut s’agir de créations, suppressions ou modifications soudaines à grande échelle, de problèmes d’accès (changements d’autorisations) ou d’anomalies structurelles dans les fichiers exécutables (fichiers PE).

![file_anomalies.png](./screenshots/file_anomalies.png ":size=700")

##### Détails d’une anomalie de fichier

Cliquez sur la ligne correspondant à une anomalie de fichier pour ouvrir une vue détaillée contenant des informations supplémentaires.

![file_anomalies_details.png](./screenshots/file_anomalies_details.png ":size=500")

##### Tri de la liste des anomalies de fichiers

Vous pouvez trier la liste par ordre alphabétique en fonction de n’importe quel champ affiché : horodatage, appareil, utilisateur, niveau de sécurité, type d’anomalie, processus, action effectuée.

##### Filtrage de la liste des anomalies de fichiers

Vous pouvez rechercher dans la liste à l’aide du champ de recherche situé en haut de la page.

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des anomalies de fichiers.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher les options de filtrage avancées, qui vous permettent de définir des conditions supplémentaires en fonction des trois éléments suivants :

- **Propriété** : menu déroulant permettant de choisir le champ à filtrer.
- **Type de correspondance** : menu déroulant permettant de choisir le mode de correspondance de la valeur (`is`, `contains` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur recherchée, en fonction de la propriété sélectionnée.

![file_anomaly_filter.png](./screenshots/file_anomaly_filter.png ':size=500')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_anomalies.png ':size=600')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.

  

### **Anomalies réseau**

La détection des anomalies réseau repère les schémas inhabituels dans le trafic réseau. Elle va au-delà des menaces connues (signatures) pour détecter de nouvelles attaques (zero-day), des violations des politiques ou des problèmes de performances, en établissant une référence du comportement normal et en signalant les écarts importants.

![network_anomalies.png](./screenshots/network_anomalies.png ":size=700")

##### Détails d’une anomalie réseau

Cliquez sur la ligne correspondant à une anomalie réseau pour ouvrir une vue détaillée contenant des informations supplémentaires.

![nw_anomalies_details.png](./screenshots/nw_anomalies_details.png ":size=500")

##### Tri de la liste des anomalies réseau

Vous pouvez trier la liste par ordre alphabétique en fonction de n’importe quel champ affiché : horodatage, appareil, utilisateur, niveau de sécurité, type d’anomalie, source, destination, action effectuée.

##### Filtrage de la liste des anomalies réseau

Vous pouvez rechercher dans la liste à l’aide du champ de recherche situé en haut de la page.

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des anomalies réseau.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher les options de filtrage avancées, qui vous permettent de définir des conditions supplémentaires en fonction des trois éléments suivants :

- **Propriété** : menu déroulant permettant de choisir le champ à filtrer.
- **Type de correspondance** : menu déroulant permettant de choisir le mode de correspondance de la valeur (`is`, `contains` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur recherchée, en fonction de la propriété sélectionnée.

![nw_anomaly_filter.png](./screenshots/nw_anomaly_filter.png ':size=500')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_nw_anomalies.png ':size=600')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.





### **Binaires non signés**

La détection des binaires non signés est une pratique de sécurité essentielle qui permet d’identifier les logiciels malveillants potentiels ou les logiciels non autorisés sur un système. Les binaires (fichiers exécutables, DLL, etc.) doivent idéalement être signés numériquement par un éditeur de confiance à l’aide d’un certificat afin de vérifier leur origine et de garantir qu’ils n’ont pas été altérés. Les binaires non signés ou dont la signature est incorrecte sont souvent utilisés par des acteurs malveillants pour contourner les mesures de sécurité.

![unsigned_binaries.png](./screenshots/unsigned_binaries.png ":size=700")

##### Détails d’un binaire non signé

Cliquez sur la ligne correspondant à une anomalie réseau pour ouvrir une vue détaillée contenant des informations supplémentaires.

![binary_details.png](./screenshots/binary_details.png ":size=500")

##### Tri de la liste des binaires non signés

Vous pouvez trier la liste par ordre alphabétique en fonction de n’importe quel champ affiché : horodatage, appareil, utilisateur, niveau de sécurité, nom de fichier, action effectuée.

##### Filtrage de la liste des binaires non signés

Vous pouvez rechercher dans la liste à l’aide du champ de recherche situé en haut de la page.

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des binaires non signés.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher les options de filtrage avancées, qui vous permettent de définir des conditions supplémentaires en fonction des trois éléments suivants :

- **Propriété** : menu déroulant permettant de choisir le champ à filtrer.
- **Type de correspondance** : menu déroulant permettant de choisir le mode de correspondance de la valeur (`is`, `contains` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur recherchée, en fonction de la propriété sélectionnée.

![unsigned_binary_filter.pn](./screenshots/unsigned_binary_filter.png ':size=500')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_unsigned_binary.png ':size=600')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.

<!-- tabs:end -->
