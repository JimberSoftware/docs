# ![](../../images/menu/menu_groupconfig.png ':size=28') Configuration de groupe

La configuration de groupe permet aux administrateurs de définir et de gérer des politiques qui contrôlent le comportement de différents ensembles d’utilisateurs ou d’appareils au sein du réseau. En affectant des appareils à des groupes, vous pouvez adapter des fonctionnalités spécifiques — comme le comportement de routage, la résolution DNS, les règles d’intégration des appareils et l’application des règles relatives aux applications — aux besoins de l’organisation ou aux exigences de sécurité.

![Capture d’écran de la page Configuration de groupe](./screenshots/groupconfig.png ':size=800')

Cette approche modulaire facilite l’application de paramètres cohérents à des utilisateurs ou services similaires, le respect des normes de conformité et la simplification de la gestion à grande échelle. Chaque onglet ci-dessous représente une option configurable qui peut être activée, désactivée ou personnalisée pour chaque groupe.

> [!TIP]
> Vous pouvez télécharger une vue d’ensemble de la configuration de groupe en cliquant sur l’icône de téléchargement ![](../../images/icons/icon_download.png ':size=20') située au-dessus de la vue d’ensemble, à droite. La vue d’ensemble sera téléchargée sous forme de fichier CSV. 


### Modifier la configuration de groupe

Vous pouvez modifier la configuration de groupe en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de sa ligne.

![edit_group_configuration.png](./screenshots/edit_group_configuration.png ':size=300')

### Filtrer la configuration de groupe

Vous pouvez rechercher dans la liste des configurations de groupe à l’aide du champ de recherche situé en haut de la page. Cela vous permet de trouver et de gérer rapidement la configuration de groupe recherchée.

- Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des configurations de groupe.

Une icône de filtre ![](../../images/icons/icon_filter.png ':size=20') se trouve à côté du champ de recherche. Cliquez dessus pour afficher des options de filtrage avancées qui vous permettent de définir des conditions supplémentaires en fonction des trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ sur lequel appliquer le filtre.
- **Type de correspondance** : menu déroulant qui vous permet de choisir la manière de faire correspondre la valeur (`EQUALS` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à faire correspondre, selon la propriété sélectionnée.

![filter_groupconfig.png](./screenshots/filter_groupconfig.png ':size=400')

Pour ajouter plusieurs filtres, cliquez de nouveau sur l’icône de filtre ![](../../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

<!-- tabs:start -->

### **PASSERELLE WAN**
_Faites passer tout le trafic Internet des clients par le routeur cloud ou sur site._

#### Vue d’ensemble

En activant cette fonctionnalité, vous pouvez rendre certaines applications accessibles **uniquement** aux utilisateurs connectés de manière sécurisée via la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***.

#### Avantages de la passerelle WAN
- Faites passer le trafic par votre pare-feu ou proxy existant pour renforcer la sécurité ou la supervision.
- Assurez-vous que tout le trafic Internet semble provenir d’une seule adresse IP cohérente — ce qui est nécessaire pour que certaines applications SaaS (cloud) contrôlent les accès.

#### Fonctionnement

Lorsque cette option est activée, tout le trafic Internet des appareils connectés passe par le routeur cloud ou sur site, au lieu d’utiliser la connexion Internet propre à l’appareil.

> [!WARNING]
> Les appareils connectés via un client d’accès à l’isolation réseau (NIAC) **ne pourront pas accéder à Internet**, sauf s’ils appartiennent à un groupe pour lequel la **Passerelle WAN** est activée.

> [!INFO]
> **Points à garder à l’esprit lors de l’utilisation de la passerelle WAN :**
> - **Tout le trafic Internet** des clients passera par le **contrôleur réseau local sur site** ou le **contrôleur réseau cloud**, selon votre configuration.
> - **Les services liés à votre adresse IP WAN locale** peuvent cesser de fonctionner. Par exemple, certains paramètres DNS fournis par les fournisseurs d’accès Internet dépendent d’une adresse IP spécifique. Un problème connu concerne les **routeurs Telenet** qui utilisent `195.130.131.11` comme DNS : cette adresse **ne fonctionne pas** lorsque le trafic passe par le contrôleur cloud. Dans ce cas, utilisez le **remplacement DNS** pour résoudre le problème.
> - Une **légère augmentation de la latence** est possible, car le trafic transite par la passerelle, ce qui ajoute un saut.

##### Étapes de configuration
1. Activez la **Passerelle WAN** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.
2. Supervisez et ajustez l’utilisation au besoin.

### **REMPLACEMENT DNS**
_Résolvez les appareils internes par leur nom d’hôte ou leur alias et activez le filtrage web basé sur le DNS._

#### Vue d’ensemble

La fonctionnalité de **remplacement DNS** renforce le contrôle et la sécurité en vous permettant de personnaliser la résolution des noms de domaine au sein de votre réseau. Elle vous permet de résoudre les appareils internes à partir de leur nom d’hôte ou de leur alias, ce qui simplifie la gestion du réseau et améliore sa facilité d’utilisation. De plus, le remplacement DNS active le filtrage web, qui vous permet de bloquer l’accès à certains sites web pour renforcer la sécurité ou améliorer la productivité.


#### Avantages du remplacement DNS

##### 1. Résoudre les appareils internes par leur nom d’hôte ou leur alias
- **Facilité d’accès** : accédez rapidement et facilement aux appareils internes sans avoir à mémoriser leurs adresses IP.
- **Gestion du réseau simplifiée** : centralisez les enregistrements DNS de tous les appareils internes.
- **Conventions de nommage cohérentes** : réduisez la confusion et les risques d’erreur.

##### 2. Filtrage web
- **Sécurité renforcée** : bloquez l’accès aux sites web malveillants connus.
- **Amélioration de la productivité** : empêchez l’accès aux sites web distrayants.
- **Filtrage personnalisable** : adaptez les politiques de filtrage web à votre organisation.

#### Fonctionnement

La fonctionnalité de remplacement DNS intercepte les requêtes DNS au sein de votre réseau et applique des règles de résolution personnalisées.

##### Étapes de configuration
1. Définissez les noms d’hôte et les alias.
2. Configurez les règles de filtrage web.
3. Activez le **remplacement DNS** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.

#### Exemples d’utilisation

**Résolution des appareils internes :**
- Accédez à un serveur via `server.company.local` ou un alias tel que `fileserver`.

**Filtrage web :**
- Bloquez les sites d’hameçonnage ou les sites chronophages, comme ceux des réseaux sociaux.


### **APPROBATION DES APPAREILS**
_Exigez l’accord d’un administrateur avant que des appareils puissent accéder au réseau._

#### Vue d’ensemble

La fonctionnalité **Approbation des appareils** ajoute un niveau de sécurité supplémentaire en exigeant l’approbation d’un administrateur avant l’intégration d’un appareil.

#### Avantages de l’approbation des appareils

##### 1. Sécurité renforcée
- **Contrôle d’accès** : seuls les appareils approuvés peuvent rejoindre le réseau.
- **Conformité** : contribue au respect des politiques et réglementations internes.
- **Responsabilisation** : fournit une piste d’audit.

##### 2. Supervision administrative
- **Système de notification** : les administrateurs sont avertis (si cette option est activée).
- **Processus d’approbation** : interface simple pour gérer les demandes.
- **Supervision** : suivez tous les appareils connectés.

#### Fonctionnement

Lorsqu’un utilisateur tente d’intégrer un appareil, la fonctionnalité Approbation des appareils exige l’approbation d’un administrateur avant que l’appareil puisse accéder au réseau.

##### Étapes de configuration
1. Activez l’**Approbation des appareils** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.
2. Activez les notifications pour les nouvelles demandes.
3. Les administrateurs examinent et approuvent les appareils depuis le tableau de bord.


### **CONNEXION MOBILE**
_Connectez les appareils mobiles au réseau de manière sécurisée._

#### Vue d’ensemble

La fonctionnalité **Connexion mobile** permet aux utilisateurs de connecter en toute sécurité leurs appareils mobiles à la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** à l’aide de l’application Jimber Network Isolation. Une fois la fonctionnalité activée, les utilisateurs peuvent enregistrer et associer leurs appareils mobiles en suivant une procédure simple et sécurisée.

#### Avantages

- **Accès mobile sécurisé** : garantit que les appareils mobiles bénéficient des mêmes politiques d’isolation et de sécurité que les ordinateurs de bureau.
- **Configuration conviviale** : les utilisateurs peuvent rapidement associer leur appareil en scannant un code QR, ce qui facilite et accélère l’intégration.
- **Prise en charge du travail à distance** : permet aux utilisateurs mobiles de se connecter de manière sécurisée depuis l’extérieur du réseau de l’entreprise.
- **Application cohérente des politiques** : tous les appareils mobiles connectés suivent les mêmes configurations de groupe et de sécurité.

#### Fonctionnement

Lorsque la Connexion mobile est activée, les utilisateurs peuvent ajouter un appareil mobile depuis le panneau Sécurité de la plateforme. Ils sont guidés tout au long de la procédure de création d’une entrée pour un nouvel appareil mobile et de son association à l’aide d’un code QR. Le code QR est scanné à l’aide de l’application Jimber Network Isolation installée sur l’appareil mobile, qui établit alors une connexion sécurisée à la plateforme.

##### Étapes de configuration

1. Activez la **Connexion mobile** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.
2. Créez un nouvel appareil mobile dans le panneau Sécurité.
3. Associez l’appareil mobile en scannant le code QR avec l’application Jimber Network Isolation.


### **LIMITE D’APPAREILS**
_Limitez le nombre d’appareils que chaque utilisateur peut intégrer._

#### Vue d’ensemble

La fonctionnalité **Limite d’appareils** permet aux administrateurs de contrôler le nombre d’appareils que chaque utilisateur peut intégrer. Cela permet de s’assurer que seuls les appareils approuvés sont utilisés et d’éviter que des appareils anciens ou inutilisés restent connectés.

> [!NOTE]
> La limite d’appareils définie dans la configuration de groupe est prioritaire. La limite de l’entreprise s’applique uniquement lorsqu’aucune limite n’est définie pour un groupe.

#### Avantages

- **Imposer l’utilisation d’appareils approuvés** : limitez les utilisateurs aux ordinateurs portables fournis par l’entreprise ou autorisés.
- **Simplifier l’assistance informatique** : la standardisation des appareils réduit la complexité du dépannage.
- **Renforcer la sécurité** : évitez que des appareils inutilisés ou oubliés restent sur le réseau.
- **Faciliter la supervision** : aidez les administrateurs à auditer et à gérer les appareils actifs.

#### Fonctionnement

Une limite d’appareils est attribuée à chaque utilisateur. Lorsqu’il atteint cette limite, il doit supprimer un appareil existant ou demander l’autorisation d’en ajouter un autre.

##### Étapes de configuration
1. Activez la **Limite d’appareils** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.
2. Définissez le nombre d’appareils autorisés par utilisateur.
3. Supervisez et ajustez l’utilisation au besoin.


### **TOUJOURS ACTIVÉ**
_Garantissez que l’application fonctionne en continu afin d’appliquer les politiques réseau._

#### Vue d’ensemble

La fonctionnalité **Toujours activé** maintient le ***_<span style="color: darkblue;">Service Jimber SASE</span>_*** en fonctionnement à tout moment afin de garantir l’application constante des politiques réseau. Elle propose deux niveaux d’application : le **mode forcé** et le **mode démarrage automatique**, offrant ainsi aux organisations une certaine souplesse en fonction de leurs besoins en matière de sécurité.

#### Avantages

- **Application continue des politiques** : garantit que les politiques de sécurité sont toujours actives.
- **Conformité améliorée** : contribue au respect des exigences réglementaires et des exigences internes en matière de sécurité.
- **Contrôle de l’expérience utilisateur** : permet de trouver un équilibre entre application stricte et flexibilité.

#### Fonctionnement

Lorsque la fonctionnalité Toujours activé est activée, l’application démarre avec le système. Selon le mode sélectionné, les utilisateurs peuvent ou non la désactiver.

- **Mode forcé** : l’application démarre avec le système et l’utilisateur ne peut pas l’arrêter.
- **Mode démarrage automatique** : l’application démarre automatiquement, mais les utilisateurs peuvent se déconnecter au besoin.

##### Étapes de configuration

1. Activez la fonctionnalité **Toujours activé** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.
2. Choisissez le **Mode forcé** ou le **Mode démarrage automatique**.
3. Déployez les paramètres sur les appareils connectés.

### **EDR**

_Les systèmes EDR supervisent en continu l’activité des terminaux._

EDR signifie Endpoint Detection and Response (détection et réponse sur les terminaux). Il s’agit d’une solution de sécurité axée sur la supervision, la détection et la réponse aux menaces sur les terminaux, tels que les ordinateurs, les ordinateurs portables et les serveurs. Les solutions EDR contribuent à détecter les cyberattaques à un stade précoce et à limiter les dommages en permettant de réagir rapidement aux activités suspectes.

Vous trouverez plus d’informations sur l’EDR [ici](/./rules/edrconfiguration/edrconfiguration.md).

##### Étape de configuration

- Activez l’**EDR** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.


### **SSL**

_L’inspection SSL intercepte, déchiffre, analyse et rechiffre en temps réel le trafic web HTTPS chiffré afin de détecter les menaces de sécurité dissimulées._

##### Étape de configuration

- Activez le **SSL** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.


<!-- ### **IDS/IPS**

_Un IDS (système de détection des intrusions) identifie les intrusions potentielles, les accès non autorisés ou d’autres activités suspectes au sein d’un réseau._

_Un IPS (système de prévention des intrusions) détecte et empêche les intrusions, les accès non autorisés et d’autres activités suspectes au sein d’un réseau._


Les IDS et les IPS sont des systèmes de sécurité qui surveillent le trafic réseau afin de repérer toute activité malveillante. Un IDS détecte les menaces et génère des alertes, tandis qu’un IPS détecte les menaces et prend également des mesures pour les bloquer. -->


<!-- tabs:end -->
