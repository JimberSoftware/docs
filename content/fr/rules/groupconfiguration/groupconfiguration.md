# ![](../../images/menu/menu_groupconfig.png ':size=28') Configuration de groupe

La configuration de groupe permet aux administrateurs de définir et de gérer des politiques qui contrôlent le comportement de différents groupes d’utilisateurs ou d’appareils sur le réseau. En attribuant des appareils à des groupes, vous pouvez adapter des fonctionnalités spécifiques — telles que le comportement de routage, la résolution DNS, les règles d’intégration des appareils et l’application des règles relatives aux applications — aux besoins de l’organisation ou aux exigences de sécurité.

![Capture d’écran de la page Configuration de groupe](./screenshots/groupconfig.png ':size=800')

Cette approche modulaire permet d’appliquer facilement des paramètres cohérents à des utilisateurs ou des services similaires, de faire respecter les normes de conformité et de simplifier la gestion à grande échelle. Chaque onglet ci-dessous correspond à une option configurable qui peut être activée, désactivée ou personnalisée pour chaque groupe.

> [!TIP]
> Vous pouvez télécharger un aperçu de la configuration de groupe en cliquant sur l’icône de téléchargement ![](../../images/icons/icon_download.png ':size=20') située en haut à droite de l’aperçu. L’aperçu sera téléchargé sous forme de fichier CSV.

### Modifier la configuration de groupe

Vous pouvez modifier la configuration de groupe en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de sa ligne.

![edit_group_configuration.png](./screenshots/edit_group_configuration.png ':size=300')

Activez **Connexion automatique** pour un groupe afin que les membres concernés puissent utiliser leur identifiant Windows Entra. Consultez [Connexion automatique Windows avec Microsoft Entra ID](/advanced/entraid/windows-autologin.md) pour connaître les paramètres de l’entreprise et les contrôles des appareils.

### Filtrer la configuration de groupe

Vous pouvez rechercher dans la liste des configurations de groupe à l’aide du champ de recherche situé en haut de la page. Cela vous permet de trouver et de gérer rapidement la configuration de groupe recherchée.

- Utilisez le champ de recherche pour saisir des mots-clés et filtrer la liste des configurations de groupe.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher les options de filtrage avancées, qui vous permettent de définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir la manière dont la valeur doit correspondre (`is` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur recherchée, selon la propriété sélectionnée.

![filter_groupconfig.png](./screenshots/filter_groupconfig.png ':size=400')

Pour ajouter plusieurs filtres, cliquez de nouveau sur l’icône de filtre ![](../../images/icons/icon_filter.png ':size=20'), puis cliquez sur le bouton `+`.

> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

<!-- tabs:start -->

### **PASSERELLE WAN**

_Faites passer tout le trafic Internet des clients par le routeur cloud ou sur site._

#### Présentation

En activant cette fonctionnalité, vous pouvez rendre certaines applications accessibles **uniquement** aux utilisateurs qui sont connectés de manière sécurisée via la **_*<span style="color: darkblue;">Plateforme Jimber SASE</span>*_**.

#### Avantages de la passerelle WAN

- Faites passer le trafic par votre pare-feu ou proxy existant pour renforcer la sécurité ou la supervision.
- Assurez-vous que tout le trafic Internet semble provenir d’une seule adresse IP cohérente — ce qui est nécessaire pour contrôler l’accès à certaines applications SaaS (cloud).

#### Fonctionnement

Lorsque cette option est activée, tout le trafic Internet des appareils connectés passe par le routeur cloud ou sur site, au lieu d’utiliser la connexion Internet propre à l’appareil.

> [!WARNING]
> Les appareils connectés via un client d’accès d’isolation réseau (NIAC) **ne pourront pas accéder à Internet**, sauf s’ils appartiennent à un groupe pour lequel la **passerelle WAN** est activée.

> [!INFO]
> **Points à prendre en compte lors de l’utilisation de la passerelle WAN :**
>
> - **Tout le trafic Internet** des clients passera par le **contrôleur réseau local sur site** ou le **contrôleur réseau cloud**, selon votre configuration.
> - **Les services associés à votre adresse IP WAN locale** peuvent cesser de fonctionner. Par exemple, certains paramètres DNS fournis par des fournisseurs d’accès à Internet dépendent d’une adresse IP spécifique. Un problème connu concerne les **routeurs Telenet** qui utilisent `195.130.131.11` comme DNS : cette adresse ne fonctionne **pas** lorsque le trafic passe par le contrôleur cloud. Dans ce cas, utilisez le **remplacement DNS** pour résoudre le problème.
> - Une **légère augmentation de la latence** est possible, car le trafic effectue un saut supplémentaire par la passerelle.

##### Étapes de configuration

1. Activez **Passerelle WAN** dans les paramètres de configuration de groupe de la **_*<span style="color: darkblue;">Plateforme Jimber SASE</span>*_** pour le groupe sélectionné.
2. Surveillez l’utilisation et ajustez-la au besoin.

### **REMPLACEMENT DNS**

_Résolvez les appareils internes par leur nom d’hôte ou leur alias et activez le filtrage web basé sur DNS._

#### Présentation

La fonctionnalité **Remplacement DNS** renforce le contrôle et la sécurité en vous permettant de personnaliser la résolution des noms de domaine sur votre réseau. Grâce à cette fonctionnalité, vous pouvez résoudre les appareils internes à l’aide de leur nom d’hôte ou de leur alias, ce qui simplifie la gestion du réseau et améliore la facilité d’utilisation. Le remplacement DNS permet également le filtrage web, afin de bloquer l’accès à certains sites web pour renforcer la sécurité ou améliorer la productivité.

#### Avantages du remplacement DNS

##### 1. Résolution des appareils internes par leur nom d’hôte ou leur alias

- **Facilité d’accès** : accédez rapidement et facilement aux appareils internes sans avoir à mémoriser leurs adresses IP.
- **Gestion du réseau simplifiée** : centralisez les enregistrements DNS de tous les appareils internes.
- **Conventions de nommage cohérentes** : réduisez les risques de confusion et d’erreurs.

##### 2. Filtrage DNS

- **Sécurité renforcée** : bloquez l’accès aux sites web malveillants connus.
- **Amélioration de la productivité** : empêchez l’accès aux sites web distrayants.
- **Filtrage personnalisable** : adaptez les politiques de filtrage web à votre organisation.

#### Fonctionnement

La fonctionnalité de remplacement DNS intercepte les requêtes DNS sur votre réseau et applique des règles de résolution personnalisées.

> [!IMPORTANT]
> Sous Linux, le remplacement DNS est pris en charge uniquement avec **systemd-resolved**.

##### Étapes de configuration

1. Définissez les noms d’hôte et les alias.
2. Configurez les règles de filtrage web.
3. Activez **Remplacement DNS** dans les paramètres de configuration de groupe de la **_*<span style="color: darkblue;">Plateforme Jimber SASE</span>*_** pour le groupe sélectionné.

#### Exemples d’utilisation

**Résolution des appareils internes :**

- Accédez à un serveur via `server.company.local` ou via un alias comme `fileserver`.

**Filtrage DNS :**

- Bloquez les sites d’hameçonnage ou les sites chronophages, comme les réseaux sociaux.

### **APPROBATION DES APPAREILS**

_Exigez le consentement d’un administrateur avant que les appareils puissent accéder au réseau._

#### Présentation

La fonctionnalité **Approbation des appareils** ajoute un niveau de sécurité supplémentaire en exigeant l’approbation d’un administrateur avant qu’un appareil puisse être intégré.

#### Avantages de l’approbation des appareils

##### 1. Sécurité renforcée

- **Contrôle d’accès** : seuls les appareils approuvés peuvent rejoindre le réseau.
- **Conformité** : contribue au respect des politiques et réglementations internes.
- **Responsabilisation** : fournit une piste d’audit.

##### 2. Supervision administrative

- **Système de notification** : les administrateurs sont avertis (si cette option est activée).
- **Flux d’approbation** : interface simple pour gérer les demandes.
- **Supervision** : suivez tous les appareils connectés.

#### Fonctionnement

Lorsqu’un utilisateur tente d’intégrer un appareil, la fonctionnalité d’approbation des appareils exige l’approbation d’un administrateur avant que l’appareil puisse accéder au réseau.

##### Étapes de configuration

1. Activez **Approbation des appareils** dans les paramètres de configuration de groupe de la **_*<span style="color: darkblue;">Plateforme Jimber SASE</span>*_** pour le groupe sélectionné.
2. Activez les notifications pour les nouvelles demandes.
3. Les administrateurs examinent et approuvent les appareils depuis le tableau de bord.

### **CONNEXION MOBILE**

_Connectez des appareils mobiles au réseau en toute sécurité._

#### Présentation

La fonctionnalité **Connexion mobile** permet aux utilisateurs de connecter leurs appareils mobiles en toute sécurité à la **_*<span style="color: darkblue;">Plateforme Jimber SASE</span>*_** à l’aide de l’application Jimber Network Isolation. Une fois cette fonctionnalité activée, les utilisateurs peuvent enregistrer et associer leurs appareils mobiles selon un processus simple et sécurisé.

#### Avantages

- **Accès mobile sécurisé** : garantit que les appareils mobiles sont protégés par les mêmes politiques d’isolation et de sécurité que les ordinateurs de bureau.
- **Configuration conviviale** : les utilisateurs peuvent rapidement associer leur appareil en scannant un code QR, ce qui accélère et facilite l’intégration.
- **Prise en charge du travail à distance** : permet aux utilisateurs mobiles de se connecter en toute sécurité depuis l’extérieur du réseau de l’entreprise.
- **Application cohérente des politiques** : tous les appareils mobiles connectés suivent les mêmes configurations de groupe et de sécurité.

#### Fonctionnement

Lorsque la connexion mobile est activée, les utilisateurs peuvent ajouter un appareil mobile depuis le panneau Sécurité de la plateforme. Ils sont guidés dans la création d’une entrée pour un nouvel appareil mobile et son association au moyen d’un code QR. Ce code est scanné à l’aide de l’application Jimber Network Isolation installée sur l’appareil mobile, qui établit alors une connexion sécurisée à la plateforme.

##### Étapes de configuration

1. Activez **Connexion mobile** dans les paramètres de configuration de groupe de la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_** pour le groupe sélectionné.
2. Créez un appareil mobile dans le panneau Sécurité.
3. Associez l’appareil mobile en scannant le code QR avec l’application **_<span style="color: darkblue;">Jimber SASE</span>_**.
 <!-- 3. Link the mobile device by scanning the QR code with the Jimber Network Isolation app. -->

### **LIMITE D’APPAREILS**

_Limitez le nombre d’appareils que chaque utilisateur peut intégrer._

#### Présentation

La fonctionnalité **Limite d’appareils** permet aux administrateurs de contrôler le nombre d’appareils que chaque utilisateur peut intégrer. Cela permet de s’assurer que seuls les équipements approuvés sont utilisés et d’éviter que des appareils anciens ou inutilisés restent connectés.

> [!NOTE]
> La limite d’appareils de la configuration de groupe est prioritaire. La limite de l’entreprise ne s’applique que si aucune limite n’est définie pour un groupe.

#### Avantages

- **Utilisation des appareils approuvés** : limitez les utilisateurs aux ordinateurs portables fournis par l’entreprise ou autorisés.
- **Simplification de l’assistance informatique** : la standardisation des appareils réduit la complexité du dépannage.
- **Sécurité renforcée** : évitez que des appareils inutilisés ou oubliés restent sur le réseau.
- **Supervision facilitée** : aidez les administrateurs à auditer et à gérer les appareils actifs.

#### Fonctionnement

Une limite d’appareils est attribuée à chaque utilisateur. Une fois cette limite atteinte, l’utilisateur doit supprimer un appareil existant ou demander l’autorisation d’en ajouter un autre.

##### Étapes de configuration

1. Activez **Limite d’appareils** dans les paramètres de configuration de groupe de la **_*<span style="color: darkblue;">Plateforme Jimber SASE</span>*_** pour le groupe sélectionné.
2. Définissez le nombre d’appareils autorisés par utilisateur.
3. Surveillez l’utilisation et ajustez-la au besoin.

### **TOUJOURS ACTIVÉ**

_Assurez-vous que l’application fonctionne en continu afin d’appliquer les politiques réseau._

#### Présentation

La fonctionnalité **Toujours activé** maintient le **_*<span style="color: darkblue;">service Jimber SASE</span>*_** en fonctionnement à tout moment afin de garantir l’application constante des politiques réseau. Elle offre deux niveaux d’application : le **mode forcé** et le **mode démarrage automatique**, permettant aux organisations de choisir en fonction de leurs besoins en matière de sécurité.

#### Avantages

- **Application continue des politiques** : garantit que les politiques de sécurité sont toujours actives.
- **Conformité améliorée** : contribue au respect des exigences réglementaires et de sécurité internes.
- **Contrôle de l’expérience utilisateur** : permet de trouver un équilibre entre application stricte et flexibilité.

#### Fonctionnement

Lorsque la fonctionnalité Toujours activé est activée, l’application démarre avec le système. Selon le mode sélectionné, les utilisateurs peuvent ou non la désactiver.

- **Mode forcé** : l’application démarre avec le système et l’utilisateur ne peut pas l’arrêter.
- **Mode démarrage automatique** : l’application démarre automatiquement, mais les utilisateurs peuvent se déconnecter si nécessaire.

##### Étapes de configuration

1. Activez **Toujours activé** dans les paramètres de configuration de groupe de la **_*<span style="color: darkblue;">Plateforme Jimber SASE</span>*_** pour le groupe sélectionné.
2. Choisissez le **mode forcé** ou le **mode démarrage automatique**.
3. Déployez les paramètres sur les appareils connectés.


### **SSL**

_L’inspection SSL intercepte, déchiffre, analyse et chiffre à nouveau en temps réel le trafic web HTTPS chiffré afin de détecter les menaces de sécurité dissimulées._

Activez **SSL** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.


<!-- ### **EDR**

_EDR systems continuously monitor activity on endpoints._

EDR stands for Endpoint Detection and Response. It is a security solution focused on monitoring, detecting and responding to threats on endpoints such as computers, laptops and servers. EDR solutions help detect cyber attacks at an early stage and minimize damage by enabling a swift response to suspicious activities.

More information on EDR is to be find [here](/./rules/edrconfiguration/edrconfiguration.md).

##### Configuration Step

- Enable **EDR** in the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_*** group configuration settings of the selected group.

edr_groupconfig.png -->


<!-- ### **IDS/IPS**

_IDS (Intrusion Detection System) identifies potential intrusions, unauthorized access, or other suspicious activities within a network._

_IPS (Intrusion Prevention System) detects and prevents intrusions, unauthorized access, and other suspicious activities within a network._


IDS and IPS are security systems that monitor network traffic for malicious activity. An IDS detects threats and generates alerts, while an IPS not only detects threats but also takes action to stop them. -->

<!-- tabs:end -->
