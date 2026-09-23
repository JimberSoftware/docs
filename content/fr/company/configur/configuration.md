# ![](../../images/menu/menu_configuration.png ':size=25') Configuration

La section **Configuration** vous permet de gérer les paramètres essentiels de votre entreprise et la façon dont les appareils utilisateur interagissent avec votre réseau. Elle est divisée en deux grandes parties :

### Paramètres de l’entreprise

Ces paramètres définissent les informations générales concernant votre entreprise au sein de la **_*<span style="color: darkblue;">Plateforme Jimber SASE</span>*_**.

![Configuration de l’entreprise](./screenshots/config_company.png ':size=600')

- **Nom d’affichage** : Il s’agit du nom de l’entreprise tel qu’il apparaîtra sur la plateforme pour les utilisateurs et les administrateurs.
- **Adresse e-mail principale de contact** : Saisissez une adresse e-mail de contact qui pourra être utilisée à des fins d’assistance ou d’administration.
- **URL du site web** : Indiquez le site web de votre entreprise.

    > [!INFO]
    > La plateforme tentera automatiquement d’extraire le logo de l’entreprise à partir de cette URL et de l’afficher dans l’interface utilisateur.

### Paramètres d’isolation du réseau <!--Jimber SASE Licence-->

Ces paramètres déterminent la façon dont les appareils utilisateur sont gérés et isolés dans votre environnement.

![Configuration de l’isolation du réseau](./screenshots/config_ni.png ':size=600')

- **Plage d’IP** : Définissez la plage d’IP interne utilisée pour les segments de réseau isolés.

- **Délai d’expiration des appareils utilisateur** : Définissez le nombre de jours pendant lesquels un appareil utilisateur reste actif avant d’expirer (valeur par défaut = 30 jours).

- **Nombre d’appareils autorisés par utilisateur** : Indiquez le nombre maximal d’appareils par utilisateur (valeur par défaut = 3).

- **Télécharger le certificat** : Téléchargez le certificat d’autorité racine Jimber actuel de l’entreprise. Les dates d’émission et d’expiration indiquées sous les boutons identifient le certificat que vous téléchargez.

- **Demander un nouveau certificat** : Remplacez immédiatement le certificat actuel par un certificat nouvellement généré. L’ancien certificat cesse de fonctionner dès que vous confirmez l’avertissement. Les appareils peuvent perdre leur connectivité jusqu’à ce que le nouveau certificat soit déployé et approuvé.

    Utilisez le [guide de déploiement de Microsoft Intune](./root-certificate-intune.md) pour installer le certificat sur les appareils macOS gérés.

> [!IMPORTANT]
> N’oubliez pas de cliquer sur le bouton **_Appliquer_** pour enregistrer vos modifications après avoir modifié un paramètre de configuration.
