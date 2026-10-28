File: company/configur/configuration.md

# ![](../../images/menu/menu_configuration.png ':size=25') Configuration

La section **Configuration** vous permet de gérer les paramètres essentiels de votre entreprise et la manière dont les appareils utilisateurs interagissent avec votre réseau. Elle est divisée en deux sections principales :

### Paramètres de l’entreprise

Ces paramètres définissent les informations générales concernant votre entreprise au sein de la **_*<span style="color: darkblue;">Plateforme Jimber SASE</span>*_**.

![Configuration de l’entreprise](./screenshots/config_company.png ':size=600')

- **Nom d’affichage** : Il s’agit du nom de l’entreprise tel qu’il apparaîtra sur la plateforme pour les utilisateurs et les administrateurs.
- **Adresse e-mail du contact principal** : Saisissez une adresse e-mail de contact pouvant être utilisée à des fins d’assistance ou d’administration.
- **URL du site web** : Indiquez le site web de votre entreprise.

    > [!INFO]
    > La plateforme tentera automatiquement d’extraire le logo de l’entreprise à partir de cette URL et de l’afficher dans l’interface utilisateur.

### Authentification

La section **Authentification** contrôle la manière dont les utilisateurs se connectent à l’entreprise. Les options d’authentification intégrées peuvent être activées en complément d’un ou plusieurs fournisseurs OpenID Connect.

Consultez [Connexion OIDC](./oidc-login.md) pour connecter un fournisseur d’identité conforme aux normes, comprendre comment SASE valide et associe les utilisateurs, et tester le flux de connexion complet.

### Paramètres d’isolation du réseau <!--Jimber SASE Licence-->

Ces paramètres contrôlent la gestion et l’isolation des appareils utilisateurs dans votre environnement.

![Configuration de l’isolation du réseau](./screenshots/config_ni.png ':size=600')

- **Plage d’adresses IP** : Définissez la plage d’adresses IP interne utilisée pour les segments de réseau isolés.

- **Durée d’expiration des appareils utilisateurs** : Définissez le nombre de jours pendant lesquels un appareil utilisateur reste actif avant d’expirer (30 jours par défaut).

- **Nombre d’appareils autorisés par utilisateur** : Indiquez le nombre maximal d’appareils par utilisateur (3 par défaut).

- **Télécharger le certificat** : Téléchargez le certificat d’AC racine Jimber actuel de l’entreprise. Les dates d’émission et d’expiration affichées sous les boutons identifient le certificat que vous téléchargez.

- **Demander un nouveau certificat** : Remplacez immédiatement le certificat actuel par un nouveau certificat généré. L’ancien certificat cesse de fonctionner dès que vous confirmez l’avertissement. Les appareils peuvent perdre leur connectivité jusqu’à ce que le nouveau certificat soit déployé et approuvé.

    Consultez le [guide de déploiement Microsoft Intune](./root-certificate-intune.md) pour installer le certificat sur les appareils macOS gérés.

### Sortie Zero Trust

Zero Trust Outbound (ZTO) contrôle l’accès à Internet par le biais de politiques de trafic sortant activées. Les points de terminaison gérés conservent les exceptions intégrées suivantes, même lorsque leurs politiques de trafic sortant sont désactivées :

| Protocole    | Port de destination                                    | Destinations autorisées                                                                                       |
| ----------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| TCP et UDP | 53 (DNS)                                             | Toute destination                                                                                             |
| TCP et UDP | 51820 (connectivité du tunnel Jimber)                 | Toute destination                                                                                             |
| TCP         | 80 et 443 (connectivité Signal Server et Lifeline) | Adresses IP résolues à partir de l’URL Signal Server et des adresses Lifeline configurées, y compris son IP de secours |

DNS est autorisé par défaut ; le service **Standard Internet** créé automatiquement n’inclut donc pas le port 53. La désactivation d’une politique Standard Internet ne bloque ni DNS ni la connectivité du tunnel Jimber.

Si la recherche du nom d’hôte Signal Server ou Lifeline échoue ou ne renvoie aucune adresse IP, les ports TCP 80 et 443 sont autorisés vers toute destination afin de préserver la connectivité de la plateforme. Si la recherche aboutit, l’accès Internet HTTP et HTTPS ordinaire nécessite une politique de trafic sortant activée.

> [!IMPORTANT]
> N’oubliez pas de cliquer sur le bouton **_Appliquer_** pour enregistrer vos modifications après avoir modifié un paramètre de configuration.
