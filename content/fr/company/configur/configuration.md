# ![](../../images/menu/menu_configuration.png ':size=25') Configuration

La section **Configuration** vous permet de gérer les paramètres essentiels de votre entreprise et la manière dont les appareils utilisateur interagissent avec votre réseau. Elle est divisée en deux zones principales :

### Paramètres de l’entreprise

Ces paramètres définissent les informations générales de votre entreprise dans la **_*<span style="color: darkblue;">Plateforme Jimber SASE</span>*_**.

![Configuration de l’entreprise](./screenshots/config_company.png ':size=600')

- **Nom d’affichage** : Nom de l’entreprise tel qu’il apparaîtra sur la plateforme pour les utilisateurs et les administrateurs.
- **Adresse e-mail du contact principal** : Saisissez une adresse e-mail de contact pouvant être utilisée à des fins d’assistance ou d’administration.
- **URL du site web** : Indiquez le site web de votre entreprise.

    > [!INFO]
    > La plateforme essaiera automatiquement d’extraire le logo de l’entreprise à partir de cette URL et de l’afficher dans l’interface utilisateur.

### Paramètres d’isolation réseau <!--Jimber SASE Licence-->

Ces paramètres contrôlent la gestion et l’isolation des appareils utilisateur dans votre environnement.

![Configuration de l’isolation réseau](./screenshots/config_ni.png ':size=600')

- **Plage d’adresses IP** : Définissez la plage d’adresses IP interne utilisée pour les segments réseau isolés.

- **Délai d’expiration des appareils utilisateur** : Définissez le nombre de jours pendant lesquels un appareil utilisateur reste actif avant son expiration (par défaut = 30 jours).

- **Nombre d’appareils autorisés par utilisateur** : Indiquez le nombre maximal d’appareils par utilisateur (par défaut = 3).

- **Télécharger le certificat** : Téléchargez le certificat CA racine Jimber actuellement utilisé par l’entreprise. Les dates d’émission et d’expiration affichées sous les boutons indiquent le certificat que vous téléchargez.

- **Demander un nouveau certificat** : Remplacez immédiatement le certificat actuel par un certificat nouvellement généré. L’ancien certificat cesse de fonctionner dès que vous confirmez l’avertissement. Les appareils peuvent perdre leur connectivité jusqu’à ce que le nouveau certificat soit déployé et approuvé.

    Consultez le [guide de déploiement Microsoft Intune](./root-certificate-intune.md) pour installer le certificat sur les appareils macOS gérés.

### Trafic sortant Zero Trust

Le trafic sortant Zero Trust (ZTO) contrôle l’accès à Internet au moyen de politiques de trafic sortant activées. Les terminaux gérés conservent les exceptions intégrées suivantes, même lorsque leurs politiques de trafic sortant sont désactivées :

| Protocole    | Port de destination                                  | Destinations autorisées                                                                                       |
| ----------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| TCP et UDP  | 53 (DNS)                                             | Toute destination                                                                                             |
| TCP et UDP  | 51820 (connectivité du tunnel Jimber)                | Toute destination                                                                                             |
| TCP         | 80 et 443 (connectivité du Signal Server et de Lifeline) | Adresses IP résolues à partir de l’URL du Signal Server et des adresses Lifeline configurées, y compris son IP de secours |

Le DNS est autorisé par défaut ; le service **Internet standard** créé automatiquement n’inclut donc pas le port 53. La désactivation d’une politique Internet standard ne bloque ni le DNS ni la connectivité du tunnel Jimber.

Si la recherche du nom d’hôte du Signal Server ou de Lifeline échoue ou ne renvoie aucune adresse IP, les ports TCP 80 et 443 sont autorisés vers toute destination afin de préserver la connectivité à la plateforme. Si la recherche aboutit, l’accès HTTP et HTTPS ordinaire à Internet nécessite une politique de trafic sortant activée.

> [!IMPORTANT]
> N’oubliez pas de cliquer sur le bouton **_Appliquer_** pour enregistrer vos modifications après avoir modifié un paramètre de configuration.
