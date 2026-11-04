# ![](../../images/menu/menu_groupconfig.png ':size=28') Configuration de groupe

La configuration de groupe permet aux administrateurs de définir et de gérer des politiques qui contrôlent le comportement de différents ensembles d’utilisateurs ou d’appareils au sein du réseau. En attribuant des appareils à des groupes, vous pouvez adapter certaines fonctionnalités — comme le comportement du routage, la résolution DNS, les règles d’intégration des appareils et l’application des politiques relatives aux applications — aux besoins de l’organisation ou aux exigences de sécurité.

![Capture d’écran de la page Configuration de groupe](./screenshots/groupconfig.png ':size=800')

Cette approche modulaire permet d’appliquer facilement des paramètres cohérents à des utilisateurs ou à des services similaires, de faire respecter les normes de conformité et de simplifier la gestion à grande échelle. Chaque onglet ci-dessous correspond à une option configurable qui peut être activée, désactivée ou personnalisée pour chaque groupe.

> [!TIP]
> Vous pouvez télécharger un aperçu de la configuration de groupe en cliquant sur l’icône de téléchargement ![](../../images/icons/icon_download.png ':size=20') située en haut à droite de l’aperçu. L’aperçu sera téléchargé sous forme de fichier CSV.

### Modifier la configuration de groupe

Vous pouvez modifier la configuration de groupe en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') sur sa ligne.

![edit_group_configuration.png](./screenshots/edit_group_configuration.png ':size=300')

### Filtrer la configuration de groupe

Vous pouvez rechercher dans la liste des configurations de groupe à l’aide du champ de recherche situé en haut de la page. Cela vous permet de trouver et de gérer rapidement la configuration de groupe recherchée.

- Utilisez le champ de recherche pour saisir des mots-clés et filtrer la liste des configurations de groupe.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Lorsque vous cliquez dessus, des options de filtrage avancées s’affichent. Elles permettent de définir des conditions supplémentaires selon les trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ sur lequel appliquer le filtre.
- **Type de correspondance** : menu déroulant qui vous permet de choisir comment faire correspondre la valeur (`is` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur à rechercher, selon la propriété sélectionnée.

![filter_groupconfig.png](./screenshots/filter_groupconfig.png ':size=400')

Pour ajouter plusieurs filtres, cliquez de nouveau sur l’icône de filtre ![](../../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

<!-- tabs:start -->

### **PASSERELLE WAN**

_Faites passer tout le trafic Internet des clients par le routeur cloud ou sur site._

#### Présentation

En activant cette fonctionnalité, vous pouvez rendre certaines applications accessibles **uniquement** aux utilisateurs connectés de manière sécurisée via la **_*<span style="color: darkblue;">Plateforme Jimber SASE</span>*_**.

#### Avantages de la passerelle WAN

- Faites passer le trafic par votre pare-feu ou proxy existant pour renforcer la sécurité ou la supervision.
- Assurez-vous que tout le trafic Internet semble provenir d’une seule adresse IP cohérente — une exigence de certaines applications SaaS (cloud) pour contrôler les accès.

#### Fonctionnement

Lorsque cette option est activée, tout le trafic Internet des appareils connectés est acheminé par le routeur cloud ou sur site, au lieu d’utiliser la propre connexion Internet de l’appareil.

> [!WARNING]
> Les appareils connectés via un client d’accès à l’isolation réseau (NIAC) **ne pourront pas accéder à Internet**, sauf s’ils appartiennent à un groupe pour lequel la **Passerelle WAN** est activée.

> [!INFO]
> **Points à garder à l’esprit lors de l’utilisation de la passerelle WAN :**
>
> - **Tout le trafic Internet** des clients sera acheminé par le **contrôleur réseau local sur site** ou le **contrôleur réseau cloud**, selon votre configuration.
> - **Les services associés à votre adresse IP WAN locale** peuvent cesser de fonctionner. Par exemple, certains paramètres DNS des fournisseurs d’accès à Internet dépendent d’une adresse IP spécifique. Un problème connu concerne les **routeurs Telenet** utilisant `195.130.131.11` comme DNS : cette adresse **ne fonctionne pas** lorsque le trafic passe par le contrôleur cloud. Dans ce cas, utilisez le **Remplacement DNS** pour résoudre le problème.
> - **La latence peut légèrement augmenter**, car le trafic effectue un saut supplémentaire par la passerelle.

##### Étapes de configuration

1. Activez la **Passerelle WAN** dans les paramètres de configuration de groupe de la **_*<span style="color: darkblue;">Plateforme Jimber SASE</span>*_** pour le groupe sélectionné.
2. Supervisez l’utilisation et ajustez-la si nécessaire.

### **REMPLACEMENT DNS**

_Résolvez les appareils internes par nom d’hôte ou alias et activez le filtrage web basé sur DNS._

#### Présentation

La fonctionnalité **Remplacement DNS** renforce le contrôle et la sécurité en vous permettant de personnaliser la résolution des noms de domaine au sein de votre réseau. Elle vous permet de résoudre les appareils internes par leur nom d’hôte ou leur alias, ce qui simplifie la gestion du réseau et améliore la facilité d’utilisation. De plus, le remplacement DNS active le filtrage web, qui vous permet de bloquer l’accès à certains sites web pour renforcer la sécurité ou améliorer la productivité.

#### Avantages du remplacement DNS

##### 1. Résoudre les appareils internes par nom d’hôte ou alias

- **Facilité d’accès** : accédez rapidement et facilement aux appareils internes sans avoir à mémoriser leurs adresses IP.
- **Gestion simplifiée du réseau** : centralisez les enregistrements DNS de tous les appareils internes.
- **Conventions de nommage cohérentes** : réduisez la confusion et les erreurs potentielles.

##### 2. Filtrage DNS

- **Sécurité renforcée** : bloquez l’accès aux sites web malveillants connus.
- **Amélioration de la productivité** : empêchez l’accès aux sites web qui détournent l’attention.
- **Filtrage personnalisable** : adaptez les politiques de filtrage web à votre organisation.

#### Fonctionnement

La fonctionnalité de remplacement DNS intercepte les requêtes DNS au sein de votre réseau et applique des règles de résolution personnalisées.

> [!IMPORTANT]
> Sous Linux, le remplacement DNS est pris en charge uniquement avec **systemd-resolved**.

##### Étapes de configuration

1. Définissez les noms d’hôte et les alias.
2. Configurez les règles de filtrage web.
3. Activez le **Remplacement DNS** dans les paramètres de configuration de groupe de la **_*<span style="color: darkblue;">Plateforme Jimber SASE</span>*_** pour le groupe sélectionné.

#### Exemples de cas d’utilisation

**Résolution des appareils internes :**

- Accédez à un serveur via `server.company.local` ou via un alias comme `fileserver`.

**Filtrage DNS :**

- Bloquez les sites d’hameçonnage ou les sites chronophages, comme les réseaux sociaux.

### **APPROBATION DES APPAREILS**

_Exigez le consentement d’un administrateur avant que des appareils puissent accéder au réseau._

#### Présentation

La fonctionnalité **Approbation des appareils** ajoute une couche de sécurité supplémentaire en exigeant l’approbation d’un administrateur avant qu’un appareil puisse être intégré.

#### Avantages de l’approbation des appareils

##### 1. Sécurité renforcée

- **Contrôle des accès** : seuls les appareils approuvés peuvent rejoindre le réseau.
- **Conformité** : contribue au respect des politiques et des réglementations internes.
- **Responsabilisation** : fournit une piste d’audit.

##### 2. Supervision administrative

- **Système de notification** : les administrateurs sont avertis (si cette option est activée).
- **Flux d’approbation** : interface simple pour gérer les demandes.
- **Supervision** : suivez tous les appareils connectés.

#### Fonctionnement

Lorsqu’un utilisateur tente d’intégrer un appareil, la fonctionnalité Approbation des appareils exige l’approbation d’un administrateur avant que l’appareil soit autorisé à accéder au réseau.

##### Étapes de configuration

1. Activez **Approbation des appareils** dans les paramètres de configuration de groupe de la **_*<span style="color: darkblue;">Plateforme Jimber SASE</span>*_** pour le groupe sélectionné.
2. Activez les notifications pour les nouvelles demandes.
3. Les administrateurs examinent et approuvent les appareils depuis le tableau de bord.

### **CONNEXION MOBILE**

_Connectez les appareils mobiles au réseau de manière sécurisée._

#### Présentation

La fonctionnalité **Connexion mobile** permet aux utilisateurs de connecter leurs appareils mobiles en toute sécurité à la **_*<span style="color: darkblue;">Plateforme Jimber SASE</span>*_** à l’aide de l’application Jimber Network Isolation. Une fois la fonctionnalité activée, les utilisateurs peuvent enregistrer et associer leurs appareils mobiles en suivant un processus simple et sécurisé.

#### Avantages

- **Accès mobile sécurisé** : garantit que les appareils mobiles bénéficient des mêmes politiques d’isolation et de sécurité que les ordinateurs de bureau.
- **Configuration conviviale** : les utilisateurs peuvent rapidement associer leur appareil en scannant un code QR, ce qui rend l’intégration rapide et facile.
- **Prise en charge du travail à distance** : permet aux utilisateurs mobiles de se connecter de manière sécurisée depuis l’extérieur du réseau de l’entreprise.
- **Application cohérente des politiques** : tous les appareils mobiles connectés suivent les mêmes configurations de groupe et de sécurité.

#### Fonctionnement

Lorsque la Connexion mobile est activée, les utilisateurs peuvent ajouter un appareil mobile depuis le panneau Sécurité de la plateforme. Ils sont guidés pour créer une nouvelle entrée d’appareil mobile et l’associer à l’aide d’un code QR. Le code QR est scanné avec l’application Jimber Network Isolation installée sur l’appareil mobile, qui établit alors une connexion sécurisée à la plateforme.

##### Étapes de configuration

1. Activez **Connexion mobile** dans les paramètres de configuration de groupe de la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_** pour le groupe sélectionné.
2. Créez un nouvel appareil mobile dans le panneau Sécurité.
3. Associez l’appareil mobile en scannant le code QR avec l’**_<span style="color: darkblue;">application Jimber SASE</span>_**.
 <!-- 3. Link the mobile device by scanning the QR code with the Jimber Network Isolation app. -->

### **LIMITE D’APPAREILS**

_Limitez le nombre d’appareils que chaque utilisateur peut intégrer._

#### Présentation

La fonctionnalité **Limite d’appareils** permet aux administrateurs de contrôler le nombre d’appareils que chaque utilisateur peut intégrer. Cela permet de garantir que seuls les appareils autorisés sont utilisés et d’éviter que des appareils anciens ou inutilisés restent connectés.

> [!NOTE]
> La limite d’appareils définie dans la configuration de groupe est prioritaire. La limite de l’entreprise s’applique uniquement si aucune limite n’est définie pour un groupe.

#### Avantages

- **Utilisation d’appareils approuvés** : limitez les utilisateurs aux ordinateurs portables fournis par l’entreprise ou autorisés.
- **Simplification de l’assistance informatique** : des appareils standardisés réduisent la complexité du dépannage.
- **Sécurité renforcée** : évitez que des appareils inutilisés ou oubliés restent sur le réseau.
- **Supervision simplifiée** : aidez les administrateurs à auditer et à gérer les appareils actifs.

#### Fonctionnement

Une limite d’appareils est attribuée à chaque utilisateur. Une fois cette limite atteinte, l’utilisateur doit supprimer un appareil existant ou demander l’autorisation d’en ajouter un autre.

##### Étapes de configuration

1. Activez **Limite d’appareils** dans les paramètres de configuration de groupe de la **_*<span style="color: darkblue;">Plateforme Jimber SASE</span>*_** pour le groupe sélectionné.
2. Définissez le nombre d’appareils par utilisateur.
3. Supervisez l’utilisation et ajustez-la si nécessaire.

### **TOUJOURS ACTIVÉ**

_Garantissez que l’application fonctionne en permanence afin d’appliquer les politiques réseau._

#### Présentation

La fonctionnalité **Toujours activé** maintient le **_*<span style="color: darkblue;">service Jimber SASE</span>*_** en fonctionnement permanent afin de garantir l’application constante des politiques réseau. Elle propose deux niveaux d’application : le **Mode forcé** et le **Mode démarrage automatique**, offrant aux organisations une certaine flexibilité en fonction de leurs besoins en matière de sécurité.

#### Avantages

- **Application continue des politiques** : garantit que les politiques de sécurité sont toujours actives.
- **Amélioration de la conformité** : contribue au respect des exigences réglementaires et des exigences de sécurité internes.
- **Contrôle de l’expérience utilisateur** : permet de trouver un équilibre entre une application stricte et la flexibilité.

#### Fonctionnement

Lorsque la fonctionnalité Toujours activé est activée, l’application démarre avec le système. Selon le mode sélectionné, les utilisateurs peuvent ou non être autorisés à la désactiver.

- **Mode forcé** : l’application démarre avec le système et l’utilisateur ne peut pas l’arrêter.
- **Mode démarrage automatique** : l’application démarre automatiquement, mais les utilisateurs peuvent se déconnecter si nécessaire.

##### Étapes de configuration

1. Activez **Toujours activé** dans les paramètres de configuration de groupe de la **_*<span style="color: darkblue;">Plateforme Jimber SASE</span>*_** pour le groupe sélectionné.
2. Choisissez entre le **Mode forcé** et le **Mode démarrage automatique**.
3. Déployez les paramètres sur les appareils connectés.

<!-- ### **EDR**

_EDR systems continuously monitor activity on endpoints._

EDR stands for Endpoint Detection and Response. It is a security solution focused on monitoring, detecting and responding to threats on endpoints such as computers, laptops and servers. EDR solutions help detect cyber attacks at an early stage and minimize damage by enabling a swift response to suspicious activities.

More information on EDR is to be find [here](/./rules/edrconfiguration/edrconfiguration.md).

##### Configuration Step

- Enable **EDR** in the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_*** group configuration settings of the selected group.

edr_groupconfig.png -->

### **SSL**

_L’inspection SSL intercepte, déchiffre, analyse et rechiffre en temps réel le trafic web HTTPS chiffré afin de détecter les menaces de sécurité dissimulées._

##### Étape de configuration

- Activez **SSL** dans les paramètres de configuration de groupe de la **_*<span style="color: darkblue;">Plateforme Jimber SASE</span>*_** pour le groupe sélectionné.

<!-- ### **IDS/IPS**

_IDS (Intrusion Detection System) identifies potential intrusions, unauthorized access, or other suspicious activities within a network._

_IPS (Intrusion Prevention System) detects and prevents intrusions, unauthorized access, and other suspicious activities within a network._


IDS and IPS are security systems that monitor network traffic for malicious activity. An IDS detects threats and generates alerts, while an IPS not only detects threats but also takes action to stop them. -->

<!-- tabs:end -->
