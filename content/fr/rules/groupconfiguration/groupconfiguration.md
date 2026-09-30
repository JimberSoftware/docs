File: rules/groupconfiguration/groupconfiguration.md

# ![](../../images/menu/menu_groupconfig.png ':size=28') Configuration de groupe

La configuration de groupe permet aux administrateurs de définir et de gérer des politiques qui contrôlent le comportement de différents groupes d’utilisateurs ou d’appareils sur le réseau. En affectant des appareils à des groupes, vous pouvez adapter des fonctionnalités spécifiques — telles que le comportement du routage, la résolution DNS, les règles d’intégration des appareils et l’application des applications — aux besoins de l’organisation ou aux exigences de sécurité.

![Capture d’écran de la page Configuration de groupe](./screenshots/groupconfig.png ':size=800')

Cette approche modulaire facilite l’application de paramètres cohérents à des utilisateurs ou des services similaires, l’application de normes de conformité et la simplification de la gestion à grande échelle. Chaque onglet ci-dessous représente une option configurable qui peut être activée, désactivée ou personnalisée pour chaque groupe.

> [!TIP]
> Vous pouvez télécharger un aperçu de la configuration de groupe en cliquant sur l’icône de téléchargement ![](../../images/icons/icon_download.png ':size=20') située en haut à droite de l’aperçu. L’aperçu sera téléchargé au format CSV.

### Modifier la configuration de groupe

Vous pouvez modifier la configuration de groupe en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de sa ligne.

![edit_group_configuration.png](./screenshots/edit_group_configuration.png ':size=300')

### Filtrer la configuration de groupe

Vous pouvez rechercher dans la liste des configurations de groupe à l’aide du champ de recherche en haut de la page. Cela vous permet de trouver et de gérer rapidement la configuration de groupe recherchée.

- Utilisez le champ de recherche pour saisir des mots-clés et filtrer la liste des configurations de groupe.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Lorsque vous cliquez dessus, des options de filtrage avancées s’affichent. Vous pouvez alors définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : menu déroulant permettant de choisir le champ sur lequel appliquer le filtre.
- **Type de correspondance** : menu déroulant permettant de choisir la manière dont la valeur doit correspondre (`EQUALS` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à rechercher, selon la propriété sélectionnée.

![filter_groupconfig.png](./screenshots/filter_groupconfig.png ':size=400')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../../images/icons/icon_filter.png ':size=20'), puis cliquez sur le bouton `+`.

> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

<!-- tabs:start -->

### **PASSERELLE WAN**
_Faites transiter tout le trafic Internet des clients par le routeur cloud ou sur site._

#### Aperçu

En activant cette fonctionnalité, vous pouvez rendre certaines applications accessibles **uniquement** aux utilisateurs connectés de manière sécurisée via la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***.

#### Avantages de la passerelle WAN
- Faites transiter le trafic par votre pare-feu ou proxy existant pour renforcer la sécurité ou la supervision.
- Assurez-vous que tout le trafic Internet semble provenir d’une seule adresse IP cohérente — une exigence de certaines applications SaaS (cloud) pour le contrôle d’accès.

#### Fonctionnement

Lorsque cette option est activée, tout le trafic Internet des appareils connectés est acheminé par le routeur cloud ou sur site, au lieu d’utiliser la propre connexion Internet de l’appareil.

> [!WARNING]
> Les appareils connectés via un client Network Isolation Access Client (NIAC) **ne pourront pas accéder à Internet**, sauf s’ils appartiennent à un groupe pour lequel la **Passerelle WAN** est activée.

> [!INFO]
> **Points à prendre en compte lors de l’utilisation de la passerelle WAN :**
> - **Tout le trafic Internet** des clients sera acheminé soit par le **contrôleur réseau local sur site**, soit par le **contrôleur réseau cloud**, selon votre configuration.
> - Les **services associés à votre adresse IP WAN locale** peuvent cesser de fonctionner. Par exemple, certains paramètres DNS des fournisseurs d’accès à Internet dépendent d’une adresse IP spécifique. Un problème connu concerne les **routeurs Telenet** utilisant `195.130.131.11` comme DNS : cette adresse **ne fonctionne pas** lorsque le trafic est acheminé par le contrôleur cloud. Dans ce cas, utilisez le **remplacement DNS** pour résoudre le problème.
> - Une **légère augmentation de la latence** est possible, car le trafic effectue un saut supplémentaire par la passerelle.

##### Étapes de configuration
1. Activez la **Passerelle WAN** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.
2. Supervisez et ajustez l’utilisation si nécessaire.

### **REMPLACEMENT DNS**
_Résolvez les appareils internes par leur nom d’hôte ou leur alias et activez le filtrage web basé sur DNS._

#### Aperçu

La fonctionnalité **Remplacement DNS** améliore le contrôle et la sécurité en vous permettant de personnaliser la résolution des noms de domaine au sein de votre réseau. Elle permet de résoudre les appareils internes à l’aide de leur nom d’hôte ou de leur alias, ce qui simplifie la gestion du réseau et améliore la facilité d’utilisation. En outre, le remplacement DNS active le filtrage web, qui vous permet de bloquer l’accès à certains sites web pour renforcer la sécurité ou accroître la productivité.

#### Avantages du remplacement DNS

##### 1. Résoudre les appareils internes par leur nom d’hôte ou leur alias
- **Facilité d’accès** : accédez rapidement et facilement aux appareils internes sans avoir à mémoriser leurs adresses IP.
- **Gestion simplifiée du réseau** : centralisez les enregistrements DNS de tous les appareils internes.
- **Conventions de nommage cohérentes** : réduisez la confusion et les erreurs potentielles.

##### 2. Filtrage web
- **Sécurité renforcée** : bloquez l’accès aux sites web malveillants connus.
- **Amélioration de la productivité** : empêchez l’accès aux sites web distrayants.
- **Filtrage personnalisable** : adaptez les politiques de filtrage web à votre organisation.

#### Fonctionnement

La fonctionnalité de remplacement DNS intercepte les requêtes DNS sur votre réseau et applique des règles de résolution personnalisées.

##### Étapes de configuration
1. Définissez les noms d’hôte et les alias.
2. Configurez les règles de filtrage web.
3. Activez le **Remplacement DNS** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.

#### Exemples de cas d’utilisation

**Résolution des appareils internes :**
- Accédez à un serveur via `server.company.local` ou un alias tel que `fileserver`.

**Filtrage web :**
- Bloquez les sites d’hameçonnage ou les sites chronophages tels que les réseaux sociaux.


### **APPROBATION DES APPAREILS**
_Exigez le consentement d’un administrateur avant que les appareils puissent accéder au réseau._

#### Aperçu

La fonctionnalité **Approbation des appareils** ajoute une couche de sécurité supplémentaire en exigeant l’approbation d’un administrateur avant l’intégration d’un appareil.

#### Avantages de l’approbation des appareils

##### 1. Sécurité renforcée
- **Contrôle d’accès** : seuls les appareils approuvés peuvent rejoindre le réseau.
- **Conformité** : aide à respecter les politiques et réglementations internes.
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

#### Aperçu

La fonctionnalité **Connexion mobile** permet aux utilisateurs de connecter leurs appareils mobiles de manière sécurisée à la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** à l’aide de l’application Jimber Network Isolation. Une fois la fonctionnalité activée, les utilisateurs peuvent enregistrer et associer leurs appareils mobiles en suivant une procédure simple et sécurisée.

#### Avantages

- **Accès mobile sécurisé** : garantit que les appareils mobiles bénéficient des mêmes politiques d’isolation et de sécurité que les ordinateurs de bureau.
- **Configuration conviviale** : les utilisateurs peuvent rapidement associer leur appareil en scannant un code QR, ce qui facilite et accélère l’intégration.
- **Prise en charge du travail à distance** : permet aux utilisateurs mobiles de se connecter de manière sécurisée en dehors du réseau de l’entreprise.
- **Application cohérente des politiques** : tous les appareils mobiles connectés respectent les mêmes configurations de groupe et de sécurité.

#### Fonctionnement

Lorsque la Connexion mobile est activée, les utilisateurs peuvent ajouter un appareil mobile depuis le panneau Sécurité de la plateforme. Ils sont guidés dans la création d’une entrée pour un nouvel appareil mobile et son association à l’aide d’un code QR. Le code QR est scanné à l’aide de l’application Jimber Network Isolation installée sur l’appareil mobile, qui établit ensuite une connexion sécurisée à la plateforme.

##### Étapes de configuration

1. Activez la **Connexion mobile** dans les paramètres de configuration de groupe de la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_** pour le groupe sélectionné.
2. Créez un appareil mobile dans le panneau Sécurité.
3. Associez l’appareil mobile en scannant le code QR avec l’application **_<span style="color: darkblue;">Jimber SASE</span>_**.
<!-- 3. Associez l’appareil mobile en scannant le code QR avec l’application Jimber Network Isolation. -->


### **LIMITE D’APPAREILS**
_Limitez le nombre d’appareils que chaque utilisateur peut intégrer._

#### Aperçu

La fonctionnalité **Limite d’appareils** permet aux administrateurs de contrôler le nombre d’appareils que chaque utilisateur peut intégrer. Elle permet de s’assurer que seuls les équipements approuvés sont utilisés et d’éviter que des appareils anciens ou inutilisés restent connectés.

> [!NOTE]
> La limite d’appareils de la configuration de groupe est prioritaire. La limite de l’entreprise ne s’applique que si aucune limite n’est définie pour un groupe.

#### Avantages

- **Imposer l’utilisation d’appareils approuvés** : limitez les utilisateurs aux ordinateurs portables fournis par l’entreprise ou autorisés.
- **Simplifier l’assistance informatique** : la standardisation des appareils réduit la complexité du dépannage.
- **Améliorer la sécurité** : évitez que des appareils inutilisés ou oubliés restent sur le réseau.
- **Faciliter la supervision** : aidez les administrateurs à auditer et à gérer les appareils actifs.

#### Fonctionnement

Une limite d’appareils est attribuée à chaque utilisateur. Lorsqu’il atteint cette limite, il doit supprimer un appareil existant ou demander l’autorisation d’en ajouter un autre.

##### Étapes de configuration
1. Activez la **Limite d’appareils** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.
2. Définissez le nombre d’appareils par utilisateur.
3. Supervisez et ajustez l’utilisation si nécessaire.


### **TOUJOURS ACTIVÉ**
_Garantissez le fonctionnement continu de l’application pour appliquer les politiques réseau._

#### Aperçu

La fonctionnalité **Toujours activé** maintient le ***_<span style="color: darkblue;">Jimber SASE Service</span>_*** en fonctionnement en permanence afin de garantir l’application cohérente des politiques réseau. Elle offre deux niveaux d’application : le **Mode forcé** et le **Mode démarrage automatique**, permettant aux organisations de choisir en fonction de leurs besoins de sécurité.

#### Avantages

- **Application continue des politiques** : garantit que les politiques de sécurité sont toujours actives.
- **Conformité renforcée** : aide à satisfaire aux exigences réglementaires et de sécurité internes.
- **Maîtrise de l’expérience utilisateur** : permet de trouver un équilibre entre application stricte et flexibilité.

#### Fonctionnement

Lorsque la fonctionnalité Toujours activé est activée, l’application démarre avec le système. Selon le mode sélectionné, les utilisateurs peuvent ou non la désactiver.

- **Mode forcé** : l’application démarre avec le système et l’utilisateur ne peut pas l’arrêter.
- **Mode démarrage automatique** : l’application démarre automatiquement, mais les utilisateurs peuvent se déconnecter si nécessaire.

##### Étapes de configuration

1. Activez la fonctionnalité **Toujours activé** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.
2. Choisissez entre le **Mode forcé** et le **Mode démarrage automatique**.
3. Déployez les paramètres sur les appareils connectés.

### **EDR**

_Les systèmes EDR supervisent en continu l’activité sur les terminaux._

EDR signifie Endpoint Detection and Response. Il s’agit d’une solution de sécurité axée sur la supervision, la détection et la réponse aux menaces sur des terminaux tels que les ordinateurs, les ordinateurs portables et les serveurs. Les solutions EDR contribuent à détecter les cyberattaques à un stade précoce et à limiter les dommages en permettant de réagir rapidement aux activités suspectes.

Vous trouverez [ici](/./rules/edrconfiguration/edrconfiguration.md) plus d’informations sur EDR.

##### Étape de configuration

- Activez **EDR** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.

edr_groupconfig.png
### **SSL**

_L’inspection SSL intercepte, déchiffre, analyse et rechiffre en temps réel le trafic web HTTPS chiffré afin de révéler les menaces de sécurité cachées._

##### Étape de configuration

- Activez **SSL** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.


<!-- ### **IDS/IPS**

_IDS (Intrusion Detection System) détecte les intrusions potentielles, les accès non autorisés et autres activités suspectes au sein d’un réseau._

_IPS (Intrusion Prevention System) détecte et empêche les intrusions, les accès non autorisés et autres activités suspectes au sein d’un réseau._


Les IDS et IPS sont des systèmes de sécurité qui surveillent le trafic réseau à la recherche d’activités malveillantes. Un IDS détecte les menaces et génère des alertes, tandis qu’un IPS ne se contente pas de détecter les menaces, mais prend également des mesures pour les arrêter. -->


<!-- tabs:end -->
