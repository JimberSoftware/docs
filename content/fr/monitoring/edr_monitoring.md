# Supervision EDR

<!-- tabs:start -->

### **Fichiers malveillants**

Les fichiers malveillants détectés se trouvent dans cette section. Vous pouvez voir la date et l’heure de la détection, l’appareil sur lequel le fichier a été détecté, l’utilisateur concerné et le nom du fichier, le niveau de gravité ainsi que l’action effectuée. 

  ![malicious_file.png](./screenshots/malicious_file.png ":size=700")

>[!NOTE]
>Vous pouvez ajouter un fichier à la liste blanche en cliquant sur le signe plus à la fin de sa ligne.

##### Détails d’un fichier malveillant

Cliquer sur la ligne correspondante d’un fichier malveillant ouvre une vue détaillée contenant des informations supplémentaires. 

![malicious_file_details.png](./screenshots/malicious_file_details.png ":size=500")

##### Trier la liste des fichiers malveillants

Vous pouvez trier la liste par ordre alphabétique selon n’importe quel champ affiché : horodatage, appareil, utilisateur, niveau de sécurité, nom du fichier, action effectuée.

##### Filtrer la liste des fichiers malveillants

Vous pouvez rechercher dans la liste à l’aide du champ de recherche situé en haut de la page. 

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des fichiers malveillants.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher les options de filtrage avancées, qui vous permettent de définir des conditions supplémentaires selon les trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir comment faire correspondre la valeur (`equals`, `contains` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à rechercher, selon la propriété choisie.

![malicious_file_filter.png](./screenshots/malicious_file_filter.png ':size=500')

Pour ajouter plusieurs filtres, vous pouvez cliquer à nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_malfiles.png ':size=600')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.

### **Anomalies de fichiers**

Les anomalies de fichiers sont des modifications ou des comportements inattendus dans les systèmes de fichiers. Les outils de sécurité les détectent souvent comme des signes de logiciels malveillants (par exemple, un rançongiciel qui chiffre des fichiers), de corruption de données ou de non-respect des politiques. Elles peuvent notamment prendre la forme de créations, suppressions ou modifications soudaines à grande échelle, de problèmes d’accès (changements d’autorisations) ou d’anomalies structurelles dans les fichiers exécutables (fichiers PE).

![file_anomalies.png](./screenshots/file_anomalies.png ":size=700")

##### Détails d’une anomalie de fichier

Cliquer sur la ligne correspondante d’une anomalie de fichier ouvre une vue détaillée contenant des informations supplémentaires. 

![file_anomalies_details.png](./screenshots/file_anomalies_details.png ":size=500")

##### Trier la liste des anomalies de fichiers

Vous pouvez trier la liste par ordre alphabétique selon n’importe quel champ affiché : horodatage, appareil, utilisateur, niveau de sécurité, type d’anomalie, processus, action effectuée.

##### Filtrer la liste des anomalies de fichiers

Vous pouvez rechercher dans la liste à l’aide du champ de recherche situé en haut de la page. 

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des anomalies de fichiers.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher les options de filtrage avancées, qui vous permettent de définir des conditions supplémentaires selon les trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir comment faire correspondre la valeur (`equals`, `contains` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à rechercher, selon la propriété choisie.

![file_anomaly_filter.png](./screenshots/file_anomaly_filter.png ':size=500')

Pour ajouter plusieurs filtres, vous pouvez cliquer à nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_anomalies.png ':size=600')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.

  

### **Anomalies réseau**

La détection des anomalies réseau identifie les schémas inhabituels dans le trafic réseau. Au-delà des menaces connues (signatures), elle permet de repérer de nouvelles attaques (zero-day), des violations de politiques ou des problèmes de performances en établissant une base de référence du comportement normal et en signalant les écarts importants.

![network_anomalies.png](./screenshots/network_anomalies.png ":size=700")

##### Détails d’une anomalie réseau

Cliquer sur la ligne correspondante d’une anomalie réseau ouvre une vue détaillée contenant des informations supplémentaires. 

![nw_anomalies_details.png](./screenshots/nw_anomalies_details.png ":size=500")

##### Trier la liste des anomalies réseau

Vous pouvez trier la liste par ordre alphabétique selon n’importe quel champ affiché : horodatage, appareil, utilisateur, niveau de sécurité, type d’anomalie, source, destination, action effectuée.

##### Filtrer la liste des anomalies réseau

Vous pouvez rechercher dans la liste à l’aide du champ de recherche situé en haut de la page. 

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des anomalies réseau.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher les options de filtrage avancées, qui vous permettent de définir des conditions supplémentaires selon les trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir comment faire correspondre la valeur (`equals`, `contains` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à rechercher, selon la propriété choisie.

![nw_anomaly_filter.png](./screenshots/nw_anomaly_filter.png ':size=500')

Pour ajouter plusieurs filtres, vous pouvez cliquer à nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_nw_anomalies.png ':size=600')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.





### **Binaires non signés**

La détection des binaires non signés est une pratique de sécurité essentielle qui permet d’identifier les logiciels malveillants potentiels ou les logiciels non autorisés au sein d’un système. Les binaires (fichiers exécutables, DLL, etc.) devraient idéalement être signés numériquement par un éditeur de confiance au moyen d’un certificat, afin de vérifier leur origine et de s’assurer qu’ils n’ont pas été altérés. Les binaires non signés ou signés de manière incorrecte sont souvent utilisés par des adversaires pour contourner les mesures de sécurité. 

![unsigned_binaries.png](./screenshots/unsigned_binaries.png ":size=700")

##### Détails d’un binaire non signé

Cliquer sur la ligne correspondante d’une anomalie réseau ouvre une vue détaillée contenant des informations supplémentaires. 

![binary_details.png](./screenshots/binary_details.png ":size=500")

##### Trier la liste des binaires non signés

Vous pouvez trier la liste par ordre alphabétique selon n’importe quel champ affiché : horodatage, appareil, utilisateur, niveau de sécurité, nom du fichier, action effectuée.

##### Filtrer la liste des binaires non signés

Vous pouvez rechercher dans la liste à l’aide du champ de recherche situé en haut de la page. 

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des binaires non signés.

À côté du champ de recherche se trouve une icône de filtre ![](../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher les options de filtrage avancées, qui vous permettent de définir des conditions supplémentaires selon les trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir comment faire correspondre la valeur (`equals`, `contains` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à rechercher, selon la propriété choisie.

![unsigned_binary_filter.pn](./screenshots/unsigned_binary_filter.png ':size=500')

Pour ajouter plusieurs filtres, vous pouvez cliquer à nouveau sur l’icône de filtre ![](../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

Les filtres actifs apparaissent en haut de la page :

![active_filters.png](./screenshots/active_filters_unsigned_binary.png ':size=600')


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../images/icons/icon_reload.png ':size=20') en haut de la page.

<!-- tabs:end -->
