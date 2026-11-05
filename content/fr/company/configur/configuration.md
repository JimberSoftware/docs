# ![](../../images/menu/menu_configuration.png ':size=25') Configuration

La section **Configuration** vous permet de gérer les paramètres essentiels de votre entreprise et la manière dont les appareils utilisateur interagissent avec votre réseau. Elle est divisée en trois parties : Paramètres de l’entreprise, Authentification et Divers :

![Configuration](./screenshots/configuration.png ':size=600')

<!-- tabs:start -->

### **Paramètres de l’entreprise**

Ces paramètres définissent les informations générales relatives à votre entreprise dans la **_*<span style="color: darkblue;">Plateforme Jimber SASE</span>*_**.

![Configuration de l’entreprise](./screenshots/config_company.png ':size=600')

- **Nom d’affichage** : il s’agit du nom de l’entreprise tel qu’il apparaîtra sur la plateforme pour les utilisateurs et les administrateurs.
- **E-mail du contact principal** : saisissez une adresse e-mail de contact qui pourra être utilisée à des fins d’assistance ou d’administration.
- **URL du site web** : indiquez le site web de votre entreprise.

    > [!INFO]
    > La plateforme tentera automatiquement d’extraire le logo de l’entreprise à partir de cette URL et de l’afficher dans l’interface utilisateur.

### **Authentification**

Pour vous connecter, vous pouvez choisir parmi trois méthodes d’authentification. Sélectionnez la ou les méthodes que vous souhaitez utiliser ou mettre à disposition.

![Authentification de la configuration](./screenshots/config_auth.png ':size=600')

#### Fournisseur OIDC

##### Ajouter un fournisseur OIDC

Vous pouvez également ajouter un fournisseur OIDC :

![add_oidc_provider](./screenshots/add_oidc_provider.png ':size=300')

##### Modifier un fournisseur OIDC

Vous pouvez modifier un fournisseur OIDC en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') dans sa ligne.

![edit_oidc_provider](./screenshots/edit_oidc_provider.png ':size=300')

##### Supprimer un fournisseur OIDC

Vous pouvez supprimer un fournisseur OIDC en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') dans sa ligne :

![delete_oidc_provider](./screenshots/delete_oidc_provider.png ':size=300')

>[!Attention]
>Le fournisseur OIDC sera supprimé sans autre avertissement.

<!-- ### Network Isolation Settings -->
### **Divers**

Ces paramètres contrôlent la gestion et l’isolation des appareils utilisateur dans votre environnement.

![Configuration de l’isolation réseau](./screenshots/config_ni.png ':size=600')

- **Plage IP** : définissez la plage IP interne utilisée pour les segments réseau isolés.

- **Durée d’expiration des appareils utilisateur** : définissez le nombre de jours pendant lesquels un appareil utilisateur reste actif avant d’expirer (valeur par défaut = 30 jours).

- **Nombre d’appareils autorisés par utilisateur** : indiquez le nombre maximal d’appareils par utilisateur (valeur par défaut = 3).

- **Télécharger le certificat** : téléchargez le certificat d’autorité de certification racine Jimber actuellement utilisé par l’entreprise. Les dates d’émission et d’expiration affichées sous les boutons indiquent le certificat que vous téléchargez.

- **Demander un nouveau certificat** (![](../../images/icons/icon_reload.png ':size=15')) : remplacez immédiatement le certificat actuel par un certificat nouvellement généré. L’ancien certificat cesse de fonctionner dès que vous confirmez l’avertissement. Les appareils peuvent perdre leur connectivité jusqu’à ce que le nouveau certificat soit déployé et approuvé.

    Utilisez le [guide de déploiement de Microsoft Intune](./company/configur/root-certificate-intune.md) pour installer le certificat sur les appareils macOS gérés.


- **Sortie Zero Trust**

    La sortie Zero Trust (ZTO) contrôle l’accès à Internet par l’intermédiaire des politiques de sortie activées. Les terminaux gérés conservent les exceptions intégrées suivantes, même lorsque leurs politiques de sortie sont désactivées :

    | Protocole    | Port de destination                                    | Destinations autorisées                                                                                           |
| ----------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
    | TCP et UDP | 53 (DNS)                                             | Toute destination                                                                                               |
    | TCP et UDP | 51820 (connectivité du tunnel Jimber)                | Toute destination                                                                                               |
    | TCP         | 80 et 443 (connectivité du serveur Signal et de Lifeline) | Adresses IP résolues à partir de l’URL du serveur Signal et des adresses Lifeline configurées, y compris son IP de secours |

    Le DNS est autorisé par défaut ; le service **Internet standard** créé automatiquement n’inclut donc pas le port 53. La désactivation d’une politique Internet standard ne bloque ni le DNS ni la connectivité du tunnel Jimber.

    Si la recherche du nom d’hôte du serveur Signal ou de Lifeline échoue ou ne renvoie aucune adresse IP, les ports TCP 80 et 443 sont autorisés vers toute destination afin de préserver la connectivité à la plateforme. Si la recherche aboutit, l’accès Internet HTTP et HTTPS ordinaire nécessite une politique de sortie activée.

<!-- tabs:end -->

> [!IMPORTANT]
> N’oubliez pas de cliquer sur le bouton **_Appliquer_** pour enregistrer vos modifications après avoir modifié un paramètre de configuration. **Aucun avertissement ne s’affiche si vous ne le faites pas**.
