File: rules/groupconfiguration/groupconfiguration.md

# ![](../../images/menu/menu_groupconfig.png ':size=28') Configuration de groupe

La configuration de groupe permet aux administrateurs de définir et de gérer des politiques qui contrôlent le comportement de différents ensembles d’utilisateurs ou d’appareils au sein du réseau. En attribuant des appareils à des groupes, vous pouvez adapter des fonctionnalités spécifiques — comme le comportement du routage, la résolution DNS, les règles d’intégration des appareils et l’application des applications — aux besoins de l’organisation ou aux exigences de sécurité.

![Capture d’écran de la page Configuration de groupe](./screenshots/groupconfig.png ':size=800')

Cette approche modulaire facilite l’application de paramètres cohérents à des utilisateurs ou services similaires, l’application des normes de conformité et la simplification de la gestion à grande échelle. Chaque onglet ci-dessous représente une option configurable qui peut être activée, désactivée ou personnalisée pour chaque groupe.

> [!TIP]
> Vous pouvez télécharger un aperçu de la configuration de groupe en cliquant sur l’icône de téléchargement ![](../../images/icons/icon_download.png ':size=20') située en haut à droite de l’aperçu. L’aperçu sera téléchargé au format CSV. 


### Modifier la configuration de groupe

Vous pouvez modifier la configuration de groupe en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de sa ligne.

![edit_group_configuration.png](./screenshots/edit_group_configuration.png ':size=300')

### Filtrer la configuration de groupe

Vous pouvez rechercher dans la liste des configurations de groupe à l’aide du champ de recherche situé en haut de la page. Vous pouvez ainsi trouver et gérer rapidement la configuration de groupe recherchée.

- Utilisez le champ de recherche pour saisir des mots-clés et filtrer la liste des configurations de groupe.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Lorsque vous cliquez dessus, des options de filtrage avancées s’affichent. Elles vous permettent de définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir comment comparer la valeur (`is` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur à rechercher, selon la propriété sélectionnée.

![filter_groupconfig.png](./screenshots/filter_groupconfig.png ':size=400')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

<!-- tabs:start -->

### **PASSERELLE WAN**
_Faites passer tout le trafic Internet des clients par le routeur cloud ou sur site._

#### Présentation

En activant cette fonctionnalité, vous pouvez rendre certaines applications accessibles **uniquement** aux utilisateurs connectés de manière sécurisée via la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***.

#### Avantages de la passerelle WAN
- Faites passer le trafic par votre pare-feu ou proxy existant pour renforcer la sécurité ou la supervision.
- Faites en sorte que tout le trafic Internet semble provenir d’une seule adresse IP cohérente — ce qui est exigé par certaines applications SaaS (cloud) pour le contrôle d’accès.

#### Fonctionnement

Lorsque cette option est activée, tout le trafic Internet des appareils connectés passe par le routeur cloud ou sur site, au lieu d’utiliser la connexion Internet propre à l’appareil.

> [!WARNING]
> Les appareils connectés via un Network Isolation Access Client (NIAC) **ne pourront pas accéder à Internet** à moins d’appartenir à un groupe pour lequel la **passerelle WAN** est activée.

> [!INFO]
> **Points à prendre en compte lorsque vous utilisez la passerelle WAN :**
> - **Tout le trafic Internet** des clients passe par le **contrôleur réseau local sur site** ou le **contrôleur réseau cloud**, selon votre configuration.
> - **Les services associés à votre IP WAN locale** risquent de ne plus fonctionner. Par exemple, certains paramètres DNS des fournisseurs d’accès à Internet reposent sur une adresse IP spécifique. Un problème connu concerne les **routeurs Telenet** qui utilisent `195.130.131.11` comme DNS : cette adresse ne **fonctionne pas** lorsque le trafic passe par le contrôleur cloud. Dans ce cas, utilisez la **surcharge DNS** pour résoudre le problème.
> - Une **légère augmentation de la latence** est possible, car le trafic passe par une étape supplémentaire via la passerelle.

##### Étapes de configuration
1. Activez la **passerelle WAN** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.
2. Supervisez et ajustez l’utilisation si nécessaire.

### **SURCHARGE DNS**
_Résolvez les appareils internes par nom d’hôte ou alias et activez le filtrage web basé sur le DNS._

#### Présentation

La fonctionnalité **Surcharge DNS** renforce le contrôle et la sécurité en vous permettant de personnaliser la résolution des noms de domaine au sein de votre réseau. Elle permet de résoudre les appareils internes par leur nom d’hôte ou leur alias, ce qui simplifie la gestion du réseau et améliore la facilité d’utilisation. De plus, la surcharge DNS permet d’activer le filtrage web afin de bloquer l’accès à certains sites web pour renforcer la sécurité ou accroître la productivité.


#### Avantages de la surcharge DNS

##### 1. Résoudre les appareils internes par nom d’hôte ou alias
- **Facilité d’accès** : accédez rapidement et facilement aux appareils internes sans avoir à retenir leurs adresses IP.
- **Gestion simplifiée du réseau** : centralisez les enregistrements DNS de tous les appareils internes.
- **Conventions de nommage cohérentes** : réduisez les risques de confusion et d’erreurs.

##### 2. Filtrage web
- **Sécurité renforcée** : bloquez l’accès aux sites web malveillants connus.
- **Amélioration de la productivité** : empêchez l’accès aux sites web susceptibles de distraire les utilisateurs.
- **Filtrage personnalisable** : adaptez les politiques de filtrage web à votre organisation.

#### Fonctionnement

La fonctionnalité de surcharge DNS intercepte les requêtes DNS au sein de votre réseau et applique des règles de résolution personnalisées.

> [!IMPORTANT]
> Sous Linux, la surcharge DNS est prise en charge uniquement avec **systemd-resolved**.

##### Étapes de configuration
1. Définissez les noms d’hôte et les alias.
2. Configurez les règles de filtrage web.
3. Activez la **surcharge DNS** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.

#### Exemples d’utilisation

**Résolution des appareils internes :**
- Accédez à un serveur via `server.company.local` ou un alias tel que `fileserver`.

**Filtrage web :**
- Bloquez les sites d’hameçonnage ou les sites chronophages comme les réseaux sociaux.


### **APPROBATION DES APPAREILS**
_Exigez le consentement d’un administrateur avant d’autoriser les appareils à accéder au réseau._

#### Présentation

La fonctionnalité **Approbation des appareils** ajoute une couche de sécurité supplémentaire en exigeant l’approbation d’un administrateur avant l’intégration d’un appareil.

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

Lorsqu’un utilisateur tente d’intégrer un appareil, la fonctionnalité d’approbation des appareils exige l’approbation d’un administrateur avant d’autoriser l’accès de l’appareil au réseau.

##### Étapes de configuration
1. Activez l’**approbation des appareils** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.
2. Activez les notifications pour les nouvelles demandes.
3. Les administrateurs examinent et approuvent les appareils depuis le tableau de bord.


### **CONNEXION MOBILE**
_Connectez les appareils mobiles au réseau en toute sécurité._

#### Présentation

La fonctionnalité **Connexion mobile** permet aux utilisateurs de connecter leurs appareils mobiles en toute sécurité à la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** à l’aide de l’application Jimber Network Isolation. Une fois cette fonctionnalité activée, les utilisateurs peuvent enregistrer et associer leurs appareils mobiles selon une procédure simple et sécurisée.

#### Avantages

- **Accès mobile sécurisé** : garantit que les appareils mobiles bénéficient des mêmes politiques d’isolation et de sécurité que les ordinateurs de bureau.
- **Configuration conviviale** : les utilisateurs peuvent rapidement associer leur appareil en scannant un code QR, ce qui simplifie et accélère son intégration.
- **Prise en charge du télétravail** : permet aux utilisateurs mobiles de se connecter en toute sécurité en dehors du réseau de l’entreprise.
- **Application cohérente des politiques** : tous les appareils mobiles connectés suivent les mêmes configurations de groupe et de sécurité.

#### Fonctionnement

Lorsque la connexion mobile est activée, les utilisateurs peuvent ajouter un appareil mobile depuis le panneau Sécurité de la plateforme. Ils sont guidés tout au long de la procédure de création d’une entrée pour un nouvel appareil mobile et de son association au moyen d’un code QR. Le code QR est scanné à l’aide de l’application Jimber Network Isolation installée sur l’appareil mobile, qui établit alors une connexion sécurisée à la plateforme.

##### Étapes de configuration

1. Activez la **connexion mobile** dans les paramètres de configuration de groupe de la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_** pour le groupe sélectionné.
2. Créez un nouvel appareil mobile dans le panneau Sécurité.
3. Associez l’appareil mobile en scannant le code QR avec l’**_<span style="color: darkblue;">application Jimber SASE</span>_**.
<!-- 3. Link the mobile device by scanning the QR code with the Jimber Network Isolation app. -->


### **LIMITE D’APPAREILS**
_Limitez le nombre d’appareils que chaque utilisateur peut intégrer._

#### Présentation

La fonctionnalité **Limite d’appareils** permet aux administrateurs de contrôler le nombre d’appareils que chaque utilisateur peut intégrer. Elle contribue à garantir que seuls les équipements approuvés sont utilisés et à éviter que des appareils anciens ou inutilisés restent connectés.

> [!NOTE]
> La limite d’appareils définie dans la configuration de groupe est prioritaire. La limite de l’entreprise ne s’applique que si aucune limite n’est définie pour un groupe.

#### Avantages

- **Utilisation d’appareils approuvés** : limitez les utilisateurs aux ordinateurs portables fournis par l’entreprise ou autorisés.
- **Simplification du support informatique** : les appareils standardisés réduisent la complexité du dépannage.
- **Sécurité renforcée** : évitez que des appareils inutilisés ou oubliés restent sur le réseau.
- **Supervision simplifiée** : aidez les administrateurs à auditer et à gérer les appareils actifs.

#### Fonctionnement

Une limite d’appareils est attribuée à chaque utilisateur. Une fois cette limite atteinte, l’utilisateur doit supprimer un appareil existant ou demander l’autorisation d’en ajouter un autre.

##### Étapes de configuration
1. Activez la **limite d’appareils** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.
2. Définissez le nombre d’appareils autorisés par utilisateur.
3. Supervisez et ajustez l’utilisation si nécessaire.


### **TOUJOURS ACTIVÉ**
_Garantissez que l’application s’exécute en continu afin d’appliquer les politiques réseau._

#### Présentation

La fonctionnalité **Toujours activé** maintient le ***_<span style="color: darkblue;">service Jimber SASE</span>_*** en cours d’exécution à tout moment afin de garantir l’application cohérente des politiques réseau. Elle propose deux niveaux d’application : le **mode forcé** et le **mode démarrage automatique**, offrant ainsi aux organisations une certaine flexibilité en fonction de leurs besoins de sécurité.

#### Avantages

- **Application continue des politiques** : garantit que les politiques de sécurité sont toujours actives.
- **Conformité renforcée** : aide à satisfaire aux exigences réglementaires et aux exigences internes en matière de sécurité.
- **Contrôle de l’expérience utilisateur** : permet de trouver un équilibre entre application stricte et flexibilité.

#### Fonctionnement

Lorsque la fonctionnalité Toujours activé est activée, l’application démarre avec le système. Selon le mode sélectionné, les utilisateurs peuvent ou non être autorisés à la désactiver.

- **Mode forcé** : l’application démarre avec le système et l’utilisateur ne peut pas l’arrêter.
- **Mode démarrage automatique** : l’application démarre automatiquement, mais les utilisateurs peuvent se déconnecter si nécessaire.

##### Étapes de configuration

1. Activez **Toujours activé** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.
2. Choisissez entre le **mode forcé** et le **mode démarrage automatique**.
3. Déployez les paramètres sur les appareils connectés.

<!-- ### **EDR**

_Les systèmes EDR supervisent en continu l’activité sur les terminaux._

EDR signifie Endpoint Detection and Response. Il s’agit d’une solution de sécurité axée sur la supervision, la détection et la réponse aux menaces sur les terminaux tels que les ordinateurs, les ordinateurs portables et les serveurs. Les solutions EDR contribuent à détecter les cyberattaques à un stade précoce et à réduire les dommages en permettant une réponse rapide aux activités suspectes.

Vous trouverez [ici](/./rules/edrconfiguration/edrconfiguration.md) plus d’informations sur EDR.

##### Étape de configuration

- Activez **EDR** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.

edr_groupconfig.png -->
### **SSL**

_L’inspection SSL intercepte, déchiffre, analyse et chiffre à nouveau en temps réel le trafic web HTTPS chiffré afin de détecter les menaces de sécurité cachées._

##### Étape de configuration

- Activez **SSL** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.


<!-- ### **IDS/IPS**

_Le système IDS (Intrusion Detection System) identifie les intrusions potentielles, les accès non autorisés ou d’autres activités suspectes au sein d’un réseau._

_Le système IPS (Intrusion Prevention System) détecte et empêche les intrusions, les accès non autorisés et d’autres activités suspectes au sein d’un réseau._


Les systèmes IDS et IPS surveillent le trafic réseau pour détecter les activités malveillantes. Un IDS détecte les menaces et génère des alertes, tandis qu’un IPS détecte également les menaces et prend des mesures pour les arrêter. -->


<!-- tabs:end -->
