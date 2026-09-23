File: devices/userdevices/userdevices.md

# ![](../../images/menu/menu_devices.png ':size=25') Appareils utilisateur

La section *Appareils utilisateur* de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** fournit une vue d’ensemble et une interface de gestion des appareils associés à vos utilisateurs. Les appareils peuvent utiliser différents systèmes d’exploitation, notamment Windows, Mac et Linux, ainsi que des appareils mobiles compatibles.

### Quand les appareils sont-ils visibles ?

Les appareils apparaissent dans la liste *Appareils utilisateur* dès que :

1. Le logiciel client correspondant au système d’exploitation de l’appareil est installé correctement.
2. L’utilisateur se connecte pour la première fois depuis l’appareil.

>[!INFO]
>Si un appareil n’apparaît pas comme prévu après l’installation, vérifiez qu’il dispose d’une connexion Internet active et que l’utilisateur s’est connecté correctement. Vous pouvez également essayer de redémarrer le client ou l’appareil.

### Installation du client de bureau

Ouvrez la page [Téléchargements Jimber SASE](https://sase.jimber.io/downloads) et téléchargez le client correspondant à votre système d’exploitation :

![downloads.png](./screenshots/downloads.png ":size=700")

#### Plateformes

<!-- tabs:start -->

<!-- #### Windows <i class="mdi mdi-microsoft-windows"></i> -->

#### **Windows**

Comme indiqué, téléchargez la dernière version de « Windows Client » depuis la page [Téléchargements Jimber SASE](https://sase.jimber.io/downloads), ou utilisez le lien direct pour télécharger la version la plus récente pour Windows : [dernière version Windows](https://sase.jimber.io/clients/windows-desktop-latest.msi)

> [!INFO]
> Pour télécharger une autre version spécifique, vous pouvez utiliser ce [lien](https://sase.jimber.io/clients).

Ouvrez le fichier téléchargé pour installer le **_Jimber SASE Service_**.
Lorsqu’une boîte de dialogue s’affiche ensuite, sélectionnez « Oui » pour continuer.

![windows-popup2.png](./screenshots/windows-popup2.png ":size=300")

Pour lancer le logiciel, recherchez « Jimber » dans le menu Démarrer de Windows ou cliquez simplement sur la nouvelle icône créée sur le bureau.

![windows-search.png](./screenshots/windows-search.png ":size=600")

Après le lancement du logiciel, l’icône Jimber de la zone de notification apparaît en bas à droite de l’écran, indiquant que le **_Jimber SASE Service_** est en cours d’exécution.

![windows-tray-icon.png](./screenshots/windows-tray-icon.png ":size=400")

> [!TIP]
> L’icône Jimber de la zone de notification peut être masquée. Si nécessaire, cliquez sur l’icône en forme de flèche vers le haut ![](./screenshots/arrow_up.png ":size=30") pour afficher les icônes masquées.

Cliquez sur l’icône Jimber de la zone de notification et sélectionnez `Sign in`. 

![sign_in.png](./screenshots/sign_in.png ":size=200")


Une page s’ouvrira dans votre navigateur pour vous permettre de vous connecter.

![login.png](./screenshots/login.png ":size=300")

Choisissez une méthode de connexion et un compte avec lequel vous connecter.

>[!IMPORTANT]
>Si vous n’avez pas encore de compte, contactez votre administrateur réseau pour qu’il en configure un pour vous.

Une fois connecté et authentifié, vous recevez une notification vous indiquant que vous êtes connecté, et un point vert apparaît sur l’icône Jimber de la zone de notification pour le confirmer.

![logged_in.png](./screenshots/logged_in.png ":size=700")



<!-- #### Mac <i class="mdi mdi-apple"></i> -->

#### **Mac**

> [!ATTENTION]
> Notre client Mac prend actuellement uniquement en charge l’installation sur un système où l’utilisateur dispose de droits sudo/d’administrateur.

Comme indiqué, téléchargez la dernière version de « Mac Client » depuis la page [Téléchargements Jimber SASE](https://sase.jimber.io/downloads), ou utilisez le lien direct pour télécharger la version la plus récente pour Mac : [dernière version Mac](https://sase.jimber.io/clients/mac-x64-latest.dmg)"

Dans le dossier Downloads, vous trouverez le fichier `SASE-Mac-2.XX.0.pkg` (XX correspond au numéro de version).

![mac_version.png](./screenshots/mac_version.png ":size=100")

> [!INFO]
> Pour télécharger une autre version spécifique, vous pouvez utiliser ce [lien](https://sase.jimber.io/clients).

Double-cliquez sur ce fichier et suivez les étapes de l’assistant d’installation pour installer le **_Jimber SASE Service_**.

![mac_download.png](./screenshots/mac_download.png ":size=400") 

Une fenêtre contextuelle peut vous avertir que vous avez téléchargé un fichier depuis Internet et vous demander si vous souhaitez l’ouvrir. Vous pouvez répondre « Ouvrir » sans risque.

![mac_install_1.png](./screenshots/mac_install_1.png ":size=200")

Une fois l’installation terminée, vous trouverez l’icône JimberNetworkIsolation dans votre Launchpad. Recherchez simplement « JimberNetworkIsolation » et appuyez sur `Enter` pour lancer l’application.

![mac-install_2.png](./screenshots/mac_install_2.png ":size=400")

Après le lancement du logiciel, l’icône Jimber de la barre des menus apparaît en haut à droite de l’écran, indiquant que le **_Jimber SASE Service_** est en cours d’exécution.

![mac_launchpad.png](./screenshots/mac_launchpad.png ":size=300")

Cliquez sur l’icône Jimber de la barre des menus et sélectionnez `Sign in`. Une page s’ouvrira dans votre navigateur pour vous permettre de vous connecter.

![mac-offline-tray.png](./screenshots/mac-offline-tray.png ":size=300").

> [!INFO]
> Une fois connecté et authentifié, un point vert apparaît sur l’icône Jimber de la barre des menus pour le confirmer.

![mac-tray-icon-online.png](./screenshots/mac-online-tray.png ":size=300")

Si vous n’avez pas encore de compte, contactez votre administrateur réseau pour qu’il en configure un pour vous.

<!-- #### Linux <i class="mdi mdi-ubuntu"></i> -->

#### **Linux**

> [!ATTENTION]
> La prise en charge est actuellement assurée pour la dernière version LTS d’Ubuntu. Pour les autres distributions de système d’exploitation, veuillez contacter notre équipe d’assistance.

Comme indiqué, téléchargez la dernière version de « Linux Client » depuis la page [Téléchargements Jimber SASE](https://sase.jimber.io/downloads), ou utilisez le lien direct pour télécharger la version la plus récente pour Linux : [dernière version Linux](https://sase.jimber.io/clients/linux-desktop-latest.deb)

> [!INFO]
> Pour télécharger une autre version spécifique, vous pouvez utiliser ce [lien](https://sase.jimber.io/clients).

![linux-open-deb.png](./screenshots/linux-open-deb.png ":size=300")

Si vous utilisez un programme d’installation par défaut, double-cliquez sur le fichier pour installer le programme, puis choisissez *Install Package* :

![package_installer.png](./screenshots/package_installer.png ":size=300")



Si aucun programme d’installation par défaut n’est configuré, la fenêtre suivante s’affiche lorsque vous double-cliquez sur le fichier.

![linux_no_defaultinstaller](./screenshots/linux_no_defaultinstaller.png ":size=700")

Fermez la fenêtre et accédez à `Downloads`. Faites un clic droit sur l’icône, sélectionnez `Open With...`, puis choisissez `Software Install` :

![/linux_open_download](./screenshots/linux_open_download.png ":size=300")


Une authentification est requise : 

![/authentication](./screenshots/authentication.png ":size=300")

Saisissez le mot de passe pour lancer l’installation : 

<!-- Choose `Install` in the next screen: -->

![/linux_install_software](./screenshots/linux_install_software.png ":size=400")

Une fois l’installation terminée, accédez au programme depuis le menu système en recherchant **_Jimber SASE_**.

![linux-search.png](./screenshots/linux-search.png ":size=300")

Après le lancement du logiciel, l’icône Jimber de la zone de notification apparaît en haut à droite de l’écran, indiquant que le **_Jimber SASE Service_** est en cours d’exécution.

![linux-tray-icon.png](./screenshots/linux-tray-icon.png ":size=200")

Cliquez sur l’icône Jimber de la zone de notification et sélectionnez `Sign in`. Une page s’ouvrira dans votre navigateur pour vous permettre de vous connecter.

>[!IMPORTANT]
>Si vous n’avez pas encore de compte, contactez votre administrateur réseau pour qu’il en configure un pour vous.


Une fois connecté et authentifié, un point vert apparaît sur l’icône de la zone de notification pour le confirmer.

![linux-tray-logged-in.png](./screenshots/linux_signed_in.png ":size=200")

.

<!-- tabs:end -->



---

### L’icône Jimber de la zone de notification ![](./screenshots/jimber_icon.png ":size=25")

Après vous être connecté, cliquez sur l’icône pour afficher ce menu :

![jimber_tray.png](./screenshots/jimber_tray.png ":size=250")

- `Security panel` : vous y trouverez une vue d’ensemble des services et de vos appareils. Vous trouverez des informations détaillées sur les services [ici](/./rules/services/services.md).
- Sélectionnez `Sign out` pour vous déconnecter de l’application. L’avertissement suivant s’affiche :

![logout.png](./screenshots/logout.png ":size=300")

- `Stealth mode` garantit que le trafic est envoyé via HTTP chiffré. Cette fonctionnalité est conçue pour permettre les connexions VPN dans des environnements où elles sont normalement bloquées, tels que les points d’accès publics, les aéroports ou les pays où la censure d’Internet est stricte. Elle masque le trafic VPN pour qu’il ressemble à du trafic Internet ordinaire, ce qui vous aide à contourner les restrictions réseau. Le port 51820 est normalement utilisé pour cette fonctionnalité.
>
> [!ATTENTION]
> **Stealth mode** est uniquement disponible dans certaines situations où votre connexion est reconnue comme étant externe à l’environnement cloud Jimber SASE.

- `Disconnect` vous déconnecte de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***, mais vous restez connecté à votre compte.
- `Quit` ferme l’application.

### Détails des appareils utilisateur

La vue d’ensemble des appareils utilisateur affiche déjà certaines propriétés :

- Le système d’exploitation, indiqué par une icône de système d’exploitation rouge ou verte : ![](../../images/icons/icon_windows_os.png ':size=25'), ![](../../images/icons/icon_ubuntu_os.png ':size=20'), ![](../../images/icons/icon_apple_os.png ':size=20').
- Le nom de l’appareil.
- Si le mode sécurisé est actif, désactivé ou non pris en charge.
- L’adresse IP.
- Le statut d’approbation.

>[!NOTE]
>La fonctionnalité « Device Approval » de notre plateforme ajoute une couche supplémentaire de sécurité et de contrôle en exigeant une approbation administrative avant qu’un appareil puisse être ajouté au réseau. Ce processus garantit que seuls les appareils autorisés obtiennent l’accès, contribuant ainsi à préserver l’intégrité et la sécurité du réseau.

![overview_userdevices.png](./screenshots/overview_userdevices.png ":size=800")

La vue d’ensemble permet également de voir quels appareils sont en ligne ou hors ligne :

- Un appareil utilisateur en ligne apparaît en haut de la liste dans la vue d’ensemble, avec une icône de système d’exploitation verte au début de sa ligne.
- Un appareil utilisateur hors ligne apparaît dans la vue d’ensemble avec une icône de système d’exploitation rouge au début de sa ligne.
- Un appareil utilisateur mobile en ligne apparaît dans la vue d’ensemble avec une icône d’appareil mobile verte ![](../../images/icons/icon_mobile.png ':size=20') au début de sa ligne.
- Un appareil utilisateur qui nécessite une mise à jour apparaît dans la vue d’ensemble avec un triangle d’avertissement jaune ![](../../images/icons/icon_deviceupdate.png ':size=20') avant l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20'), à la fin de sa ligne. 

Cliquez sur la ligne correspondante de l’appareil utilisateur pour ouvrir une nouvelle fenêtre contenant plus de détails :

![user_device_info_details.png](./screenshots/user_device_info_details.png ":size=500")

L’onglet des logiciels affiche les logiciels antivirus et le pare-feu installés : 

![user_device_info_software.png](./screenshots/user_device_info_software.png ":size=500")

L’onglet de sécurité affiche les politiques installées :

![user_device_info_security.png](./screenshots/user_device_info_security.png ":size=500")

>[!TIP]
>Vous pouvez copier toutes les informations à l’aide du bouton de copie ![](../../images/buttons/button_copy.png ":size=25") situé dans le coin supérieur droit.

### Filtrer les appareils utilisateur

Vous pouvez rechercher des appareils utilisateur à l’aide du champ de recherche situé en haut de la page. Cela vous aide à trouver et à gérer rapidement l’appareil recherché.

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des appareils.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher des options de filtrage avancées, où vous pouvez définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : menu déroulant permettant de choisir le champ à filtrer.
- **Type de correspondance** : menu déroulant permettant de choisir comment faire correspondre la valeur (`equals`, `contains` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur recherchée, en fonction de la propriété sélectionnée.

![filter_userdevice.png](./screenshots/filter_userdevice.png ':size=400')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

<!-- Once filters are applied:
- The results are updated to reflect your conditions.
- Active filters appear at the top of the page.
- You can remove filters individually by clicking the `X` next to each, or remove all at once by clicking the `Reset Filters` button. -->

> [!TIP]
> Vous pouvez actualiser la liste des appareils utilisateur en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

### Supprimer un appareil utilisateur

Vous pouvez supprimer des appareils utilisateur en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') dans leur ligne.

> [!WARNING]
> La suppression d’un appareil actif le déconnecte immédiatement de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***. Pour ajouter à nouveau l’appareil, l’utilisateur devra s’y connecter et, si cette fonctionnalité est activée, faire approuver l’appareil sur la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***.

Un avertissement s’affiche avant la suppression de l’appareil :

![delete_device.png](./screenshots/delete_device.png ':size=400')
