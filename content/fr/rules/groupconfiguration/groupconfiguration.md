# ![](../../images/menu/menu_groupconfig.png ':size=28') Configuration de groupe

La configuration de groupe permet aux administrateurs de définir et de gérer des politiques qui contrôlent le comportement de différents groupes d’utilisateurs ou d’appareils au sein du réseau. En attribuant des appareils à des groupes, vous pouvez adapter des fonctionnalités spécifiques — telles que le comportement de routage, la résolution DNS, les règles d’intégration des appareils et l’application des applications — aux besoins de l’organisation ou aux exigences de sécurité.

![Capture d’écran de la page Configuration de groupe](./screenshots/groupconfig.png ':size=800')

Cette approche modulaire permet d’appliquer facilement des paramètres cohérents à des utilisateurs ou des services similaires, de faire respecter les normes de conformité et de simplifier la gestion à grande échelle. Chaque onglet ci-dessous correspond à une option configurable qui peut être activée, désactivée ou personnalisée pour chaque groupe.

> [!TIP]
> Vous pouvez télécharger un aperçu de la configuration de groupe en cliquant sur l’icône de téléchargement ![](../../images/icons/icon_download.png ':size=20') située en haut à droite de l’aperçu. L’aperçu sera téléchargé au format CSV. 


### Modifier la configuration de groupe

Vous pouvez modifier la configuration de groupe en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de sa ligne.

![edit_group_configuration.png](./screenshots/edit_group_configuration.png ':size=300')

### Filtrer la configuration de groupe

Vous pouvez rechercher des configurations de groupe dans la liste à l’aide du champ de recherche situé en haut de la page. Cela vous permet de trouver et de gérer rapidement la configuration de groupe recherchée.

- Utilisez le champ de recherche pour saisir des mots-clés et filtrer la liste des configurations de groupe.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Lorsque vous cliquez dessus, elle affiche des options de filtrage avancées qui vous permettent de définir des conditions supplémentaires en fonction des trois éléments suivants :

- **Propriété** : menu déroulant permettant de choisir le champ à filtrer.
- **Type de correspondance** : menu déroulant permettant de sélectionner le mode de correspondance de la valeur (`is` ou `is not`).
- **Valeur** : saisissez ou sélectionnez la valeur à rechercher, selon la propriété sélectionnée.

![filter_groupconfig.png](./screenshots/filter_groupconfig.png ':size=400')

Pour ajouter plusieurs filtres, cliquez de nouveau sur l’icône de filtre ![](../../images/icons/icon_filter.png ':size=20'), puis cliquez sur le bouton `+`.


> [!TIP]
> Vous pouvez actualiser la liste en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

<!-- tabs:start -->

### **PASSERELLE WAN**
_Faites transiter tout le trafic Internet des clients par le routeur cloud ou sur site._

#### Aperçu

En activant cette fonctionnalité, vous pouvez rendre certaines applications accessibles **uniquement** aux utilisateurs connectés de manière sécurisée via la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***.

#### Avantages de la passerelle WAN
- Faites transiter le trafic par votre pare-feu ou proxy existant pour renforcer la sécurité ou la supervision.
- Assurez-vous que tout le trafic Internet semble provenir d’une seule adresse IP cohérente — ce qui est nécessaire pour que certaines applications SaaS (cloud) puissent contrôler les accès.

#### Fonctionnement

Lorsque cette option est activée, tout le trafic Internet des appareils connectés transite par le routeur cloud ou sur site, plutôt que d’utiliser leur propre connexion Internet.

> [!WARNING]
> Les appareils connectés via un client Network Isolation Access Client (NIAC) **ne pourront pas accéder à Internet** s’ils n’appartiennent pas à un groupe pour lequel la **passerelle WAN** est activée.

> [!INFO]
> **Points à prendre en compte lors de l’utilisation de la passerelle WAN :**
> - **Tout le trafic Internet** des clients transitera par le **contrôleur réseau local sur site** ou le **contrôleur réseau cloud**, selon votre configuration.
> - **Les services associés à votre IP WAN locale** peuvent cesser de fonctionner. Par exemple, certains paramètres DNS des fournisseurs d’accès à Internet reposent sur une adresse IP spécifique. Un problème connu concerne les **routeurs Telenet** utilisant `195.130.131.11` comme DNS : cette adresse **ne fonctionne pas** lorsque le trafic transite par le contrôleur cloud. Dans ce cas, utilisez le **remplacement DNS** pour résoudre le problème.
> - Une **légère hausse de la latence** est possible, car le trafic effectue un saut supplémentaire par la passerelle.

##### Étapes de configuration
1. Activez la **passerelle WAN** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.
2. Supervisez et ajustez l’utilisation selon vos besoins.

### **REMPLACEMENT DNS**
_Résolvez les appareils internes à l’aide de leur nom d’hôte ou de leur alias et activez le filtrage web basé sur DNS._

#### Aperçu

La fonctionnalité **Remplacement DNS** améliore le contrôle et la sécurité en vous permettant de personnaliser la résolution des noms de domaine au sein de votre réseau. Elle vous permet de résoudre les appareils internes à l’aide de leur nom d’hôte ou de leur alias, ce qui simplifie la gestion du réseau et améliore la facilité d’utilisation. Le remplacement DNS permet également le filtrage web, qui vous donne la possibilité de bloquer l’accès à certains sites Web pour renforcer la sécurité ou améliorer la productivité.


#### Avantages du remplacement DNS

##### 1. Résoudre les appareils internes à l’aide de leur nom d’hôte ou de leur alias
- **Facilité d’accès** : accédez rapidement et facilement aux appareils internes sans avoir à mémoriser leurs adresses IP.
- **Gestion du réseau simplifiée** : centralisez les enregistrements DNS de tous les appareils internes.
- **Conventions de nommage cohérentes** : réduisez les risques de confusion et d’erreurs.

##### 2. Filtrage web
- **Sécurité renforcée** : bloquez l’accès aux sites Web malveillants connus.
- **Amélioration de la productivité** : empêchez l’accès aux sites Web distrayants.
- **Filtrage personnalisable** : adaptez les politiques de filtrage web à votre organisation.

#### Fonctionnement

La fonctionnalité de remplacement DNS intercepte les requêtes DNS au sein de votre réseau et applique des règles de résolution personnalisées.

> [!IMPORTANT]
> Sous Linux, le remplacement DNS est pris en charge uniquement avec **systemd-resolved**.

##### Étapes de configuration
1. Définissez les noms d’hôte et les alias.
2. Configurez les règles de filtrage web.
3. Activez le **remplacement DNS** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.

#### Exemples de cas d’utilisation

**Résolution des appareils internes :**
- Accédez à un serveur via `server.company.local` ou un alias tel que `fileserver`.

**Filtrage web :**
- Bloquez les sites d’hameçonnage ou les sites chronophages, comme les réseaux sociaux.


### **APPROBATION DES APPAREILS**
_Exigez le consentement d’un administrateur avant d’autoriser les appareils à accéder au réseau._

#### Aperçu

La fonctionnalité **Approbation des appareils** ajoute une couche de sécurité supplémentaire en exigeant l’approbation d’un administrateur avant l’intégration d’un appareil.

#### Avantages de l’approbation des appareils

##### 1. Sécurité renforcée
- **Contrôle des accès** : seuls les appareils approuvés peuvent rejoindre le réseau.
- **Conformité** : contribue au respect des politiques et réglementations internes.
- **Responsabilisation** : fournit une piste d’audit.

##### 2. Supervision administrative
- **Système de notification** : les administrateurs sont alertés (si cette option est activée).
- **Flux de travail d’approbation** : interface simple pour gérer les demandes.
- **Supervision** : suivez tous les appareils connectés.

#### Fonctionnement

Lorsqu’un utilisateur tente d’intégrer un appareil, la fonctionnalité Approbation des appareils exige l’approbation d’un administrateur avant que l’appareil ne puisse accéder au réseau.

##### Étapes de configuration
1. Activez **Approbation des appareils** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.
2. Activez les notifications pour les nouvelles demandes.
3. Les administrateurs examinent et approuvent les appareils depuis le tableau de bord.


### **CONNEXION MOBILE**
_Connectez les appareils mobiles au réseau en toute sécurité._

#### Aperçu

La fonctionnalité **Connexion mobile** permet aux utilisateurs de connecter en toute sécurité leurs appareils mobiles à la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** à l’aide de l’application Jimber Network Isolation. Une fois la fonctionnalité activée, les utilisateurs peuvent enregistrer et associer leurs appareils mobiles selon un processus simple et sécurisé.

#### Avantages

- **Accès mobile sécurisé** : garantit que les appareils mobiles bénéficient des mêmes politiques d’isolation et de sécurité que les ordinateurs de bureau.
- **Configuration conviviale** : les utilisateurs peuvent rapidement associer leur appareil en scannant un code QR, ce qui accélère et facilite l’intégration.
- **Prise en charge du travail à distance** : permet aux utilisateurs mobiles de se connecter en toute sécurité depuis l’extérieur du réseau d’entreprise.
- **Application cohérente des politiques** : tous les appareils mobiles connectés suivent les mêmes configurations de groupe et de sécurité.

#### Fonctionnement

Lorsque la connexion mobile est activée, les utilisateurs peuvent ajouter un appareil mobile depuis le volet Sécurité de la plateforme. Ils sont guidés dans la création d’une entrée pour un nouvel appareil mobile et son association à l’aide d’un code QR. Le code QR est scanné à l’aide de l’application Jimber Network Isolation installée sur l’appareil mobile, qui établit alors une connexion sécurisée à la plateforme.

##### Étapes de configuration

1. Activez **Connexion mobile** dans les paramètres de configuration de groupe de la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_** pour le groupe sélectionné.
2. Créez un nouvel appareil mobile dans le volet Sécurité.
3. Associez l’appareil mobile en scannant le code QR avec l’**_<span style="color: darkblue;">application Jimber SASE</span>_**.
<!-- 3. Link the mobile device by scanning the QR code with the Jimber Network Isolation app. -->


### **LIMITE D’APPAREILS**
_Limitez le nombre d’appareils que chaque utilisateur peut intégrer._

#### Aperçu

La fonctionnalité **Limite d’appareils** permet aux administrateurs de contrôler le nombre d’appareils que chaque utilisateur peut intégrer. Cela permet de s’assurer que seuls les appareils approuvés sont utilisés et d’éviter que d’anciens appareils ou des appareils inutilisés restent connectés.

> [!NOTE]
> La limite d’appareils définie dans la configuration de groupe est prioritaire. La limite de l’entreprise s’applique uniquement si aucune limite n’est définie pour un groupe.

#### Avantages

- **Utilisation d’appareils approuvés** : limitez les utilisateurs aux ordinateurs portables fournis par l’entreprise ou autorisés.
- **Simplification du support informatique** : la standardisation des appareils réduit la complexité du dépannage.
- **Sécurité renforcée** : empêchez les appareils inutilisés ou oubliés de rester sur le réseau.
- **Supervision facilitée** : aidez les administrateurs à auditer et gérer les appareils actifs.

#### Fonctionnement

Une limite d’appareils est attribuée à chaque utilisateur. Une fois cette limite atteinte, l’utilisateur doit supprimer un appareil existant ou demander l’autorisation d’en ajouter un autre.

##### Étapes de configuration
1. Activez **Limite d’appareils** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.
2. Définissez le nombre d’appareils autorisés par utilisateur.
3. Supervisez et ajustez l’utilisation selon vos besoins.


### **TOUJOURS ACTIVÉ**
_Garantissez le fonctionnement continu de l’application pour faire respecter les politiques réseau._

#### Aperçu

La fonctionnalité **Toujours activé** maintient le ***_<span style="color: darkblue;">service Jimber SASE</span>_*** en fonctionnement permanent afin de garantir l’application cohérente des politiques réseau. Elle propose deux niveaux d’application : **Mode forcé** et **Mode démarrage automatique**, afin que les organisations puissent choisir la configuration adaptée à leurs besoins de sécurité.

#### Avantages

- **Application continue des politiques** : garantit que les politiques de sécurité sont toujours actives.
- **Conformité renforcée** : contribue au respect des exigences réglementaires et de sécurité internes.
- **Contrôle de l’expérience utilisateur** : permet de trouver un équilibre entre une application stricte et la flexibilité.

#### Fonctionnement

Lorsque la fonctionnalité Toujours activé est activée, l’application démarre avec le système. Selon le mode sélectionné, les utilisateurs peuvent ou non la désactiver.

- **Mode forcé** : l’application démarre avec le système et l’utilisateur ne peut pas l’arrêter.
- **Mode démarrage automatique** : l’application démarre automatiquement, mais les utilisateurs peuvent se déconnecter si nécessaire.

##### Étapes de configuration

1. Activez **Toujours activé** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.
2. Choisissez entre le **mode forcé** et le **mode démarrage automatique**.
3. Déployez les paramètres sur les appareils connectés.

### **EDR**

_Les systèmes EDR surveillent en permanence l’activité des terminaux._

EDR signifie Endpoint Detection and Response. Il s’agit d’une solution de sécurité axée sur la supervision, la détection et la réponse aux menaces sur les terminaux, tels que les ordinateurs, les ordinateurs portables et les serveurs. Les solutions EDR contribuent à détecter les cyberattaques à un stade précoce et à limiter les dommages en permettant une réponse rapide aux activités suspectes.

Vous trouverez plus d’informations sur l’EDR [ici](/./rules/edrconfiguration/edrconfiguration.md).

##### Étape de configuration

- Activez **EDR** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.

edr_groupconfig.png
### **SSL**

_L’inspection SSL intercepte, déchiffre, analyse et rechiffre en temps réel le trafic Web HTTPS chiffré afin de détecter les menaces de sécurité dissimulées._

##### Étape de configuration

- Activez **SSL** dans les paramètres de configuration de groupe de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** pour le groupe sélectionné.


<!-- ### **IDS/IPS**

_Le système IDS (Intrusion Detection System) détecte les intrusions potentielles, les accès non autorisés ou toute autre activité suspecte sur un réseau._

_Le système IPS (Intrusion Prevention System) détecte et empêche les intrusions, les accès non autorisés et toute autre activité suspecte sur un réseau._


Les systèmes IDS et IPS surveillent le trafic réseau à la recherche d’activités malveillantes. Un IDS détecte les menaces et génère des alertes, tandis qu’un IPS détecte les menaces et prend également des mesures pour les arrêter. -->


<!-- tabs:end -->
