File: devices/userdevices/userdevices.md

# ![](../../images/menu/menu_devices.png ':size=25') Appareils utilisateur

La section *Appareils utilisateur* de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** fournit une interface de présentation et de gestion des appareils associés à vos utilisateurs. Les appareils peuvent fonctionner sous différents systèmes d’exploitation, notamment Windows, Mac et Linux, ainsi que sur des appareils mobiles compatibles.

### Quand les appareils sont-ils visibles ?

Les appareils apparaissent dans la liste *Appareils utilisateur* dès que :

1. Le logiciel client correspondant au système d’exploitation de l’appareil est correctement installé.
2. L’utilisateur se connecte pour la première fois depuis l’appareil.

>[!INFO]
>Si un appareil n’apparaît pas comme prévu après l’installation, vérifiez qu’il dispose d’une connexion Internet active et que l’utilisateur s’est connecté correctement. Pensez également à redémarrer le client ou l’appareil.

### Installation du client de bureau

Ouvrez la page [Téléchargements Jimber SASE](https://sase.jimber.io/downloads) et téléchargez le client correspondant à votre système d’exploitation :

![downloads.png](./screenshots/downloads.png ":size=700")

#### Plateformes

<!-- tabs:start -->

<!-- #### Windows <i class="mdi mdi-microsoft-windows"></i> -->

#### **Windows**

Comme indiqué, téléchargez la dernière version du « client Windows » depuis [Téléchargements Jimber SASE](https://sase.jimber.io/downloads), ou utilisez le lien direct pour accéder à la version la plus récente pour Windows : [dernière version Windows](https://sase.jimber.io/clients/windows-desktop-latest.msi)

> [!INFO]
> Pour télécharger une autre version spécifique, vous pouvez utiliser ce [lien](https://sase.jimber.io/clients).

Ouvrez le fichier téléchargé pour installer le **_service Jimber SASE_**.
Lorsqu’une boîte de dialogue s’affiche, sélectionnez « Oui » pour continuer.

![windows-popup2.png](./screenshots/windows-popup2.png ":size=300")

Pour lancer le logiciel, recherchez « Jimber » dans le menu Démarrer de Windows ou cliquez simplement sur la nouvelle icône créée sur le bureau.

![windows-search.png](./screenshots/windows-search.png ":size=600")

Au lancement du logiciel, l’icône Jimber dans la zone de notification apparaît en bas à droite de votre écran, indiquant que le **_service Jimber SASE_** est en cours d’exécution.

![windows-tray-icon.png](./screenshots/windows-tray-icon.png ":size=400")

> [!TIP]
> L’icône Jimber dans la zone de notification peut être masquée. Si nécessaire, cliquez sur la flèche vers le haut ![](./screenshots/arrow_up.png ":size=30") pour afficher les icônes masquées.

Cliquez sur l’icône Jimber dans la zone de notification et sélectionnez `Sign in`. 

![sign_in.png](./screenshots/sign_in.png ":size=200")


Une page s’ouvrira dans votre navigateur pour vous permettre de vous connecter.

![login.png](./screenshots/login.png ":size=300")

Choisissez une méthode de connexion et un compte.

>[!IMPORTANT]
>Si vous n’avez pas encore de compte, contactez votre administrateur réseau pour qu’il vous en crée un.

Une fois connecté et en ligne, vous recevrez une notification confirmant votre connexion, et un point vert apparaîtra sur l’icône Jimber dans la zone de notification.

![logged_in.png](./screenshots/logged_in.png ":size=700")



<!-- #### Mac <i class="mdi mdi-apple"></i> -->

#### **Mac**

> [!ATTENTION]
> Notre client Mac ne peut actuellement être installé que sur un système où l’utilisateur dispose de droits sudo/d’administrateur.

Comme indiqué, téléchargez la dernière version du « client Mac » depuis [Téléchargements Jimber SASE](https://sase.jimber.io/downloads), ou utilisez le lien direct pour accéder à la version la plus récente pour Mac : [dernière version Mac](https://sase.jimber.io/clients/mac-x64-latest.dmg)"

Dans le dossier Téléchargements, vous trouverez le fichier `SASE-Mac-2.XX.0.pkg` (XX correspond au numéro de version).

![mac_version.png](./screenshots/mac_version.png ":size=100")

> [!INFO]
> Pour télécharger une autre version spécifique, vous pouvez utiliser ce [lien](https://sase.jimber.io/clients).

Double-cliquez sur ce fichier et suivez les étapes de l’assistant d’installation pour installer le **_service Jimber SASE_**.

![mac_download.png](./screenshots/mac_download.png ":size=400") 

Une fenêtre contextuelle peut vous avertir que vous avez téléchargé un fichier depuis Internet et vous demander si vous souhaitez vraiment l’ouvrir. Vous pouvez répondre « Ouvrir » sans risque.

![mac_install_1.png](./screenshots/mac_install_1.png ":size=200")

Une fois l’installation terminée, vous trouverez l’icône JimberNetworkIsolation dans votre Launchpad. Recherchez simplement « JimberNetworkIsolation » et appuyez sur `Enter` pour lancer l’application.

![mac-install_2.png](./screenshots/mac_install_2.png ":size=400")

Au lancement du logiciel, l’icône Jimber dans la barre de menus apparaît en haut à droite de votre écran, indiquant que le **_service Jimber SASE_** est en cours d’exécution.

![mac_launchpad.png](./screenshots/mac_launchpad.png ":size=300")

Cliquez sur l’icône Jimber dans la barre de menus et sélectionnez `Sign in`. Une page s’ouvrira dans votre navigateur pour vous permettre de vous connecter.

![mac-offline-tray.png](./screenshots/mac-offline-tray.png ":size=300").

> [!INFO]
> Une fois connecté et en ligne, un point vert apparaîtra sur l’icône Jimber dans la barre de menus.

![mac-tray-icon-online.png](./screenshots/mac-online-tray.png ":size=300")

Si vous n’avez pas encore de compte, contactez votre administrateur réseau pour qu’il vous en crée un.

<!-- #### Linux <i class="mdi mdi-ubuntu"></i> -->

#### **Linux**

> [!IMPORTANT]
> Sous Linux, le remplacement DNS est pris en charge uniquement avec **systemd-resolved**.

> [!ATTENTION]
> La prise en charge est actuellement assurée pour la dernière version LTS d’Ubuntu. Pour les autres distributions de système d’exploitation, veuillez contacter notre équipe d’assistance.

Comme indiqué, téléchargez la dernière version du « client Linux » depuis [Téléchargements Jimber SASE](https://sase.jimber.io/downloads), ou utilisez le lien direct pour accéder à la version la plus récente pour Linux : [dernière version Linux](https://sase.jimber.io/clients/linux-desktop-latest.deb)

> [!INFO]
> Pour télécharger une autre version spécifique, vous pouvez utiliser ce [lien](https://sase.jimber.io/clients).

![linux-open-deb.png](./screenshots/linux-open-deb.png ":size=300")

Si vous utilisez un programme d’installation par défaut, double-cliquez sur le fichier pour installer le programme, puis choisissez *Installer le paquet* :

![package_installer.png](./screenshots/package_installer.png ":size=300")



Si aucun programme d’installation par défaut n’est disponible, la fenêtre suivante s’affichera après un double-clic.

![linux_no_defaultinstaller](./screenshots/linux_no_defaultinstaller.png ":size=700")

Fermez la fenêtre et accédez au dossier `Downloads`. Faites un clic droit sur l’icône, sélectionnez `Open With...`, puis choisissez `Software Install` :

![/linux_open_download](./screenshots/linux_open_download.png ":size=300")


Une authentification est requise : 

![/authentication](./screenshots/authentication.png ":size=300")

Saisissez le mot de passe pour lancer l’installation : 

<!-- Choose `Install` in the next screen: -->

![/linux_install_software](./screenshots/linux_install_software.png ":size=400")

Une fois l’installation terminée, accédez au programme depuis le menu système en recherchant **_Jimber SASE_**.

![linux-search.png](./screenshots/linux-search.png ":size=300")

Au lancement du logiciel, l’icône Jimber dans la zone de notification apparaît en haut à droite de votre écran, indiquant que le **_service Jimber SASE_** est en cours d’exécution.

![linux-tray-icon.png](./screenshots/linux-tray-icon.png ":size=200")

Cliquez sur l’icône Jimber dans la zone de notification et sélectionnez `Sign in`. Une page s’ouvrira dans votre navigateur pour vous permettre de vous connecter.

>[!IMPORTANT]
>Si vous n’avez pas encore de compte, contactez votre administrateur réseau pour qu’il vous en crée un.


Une fois connecté et en ligne, un point vert apparaîtra sur l’icône dans la zone de notification.

![linux-tray-logged-in.png](./screenshots/linux_signed_in.png ":size=200")

.

<!-- tabs:end -->



---

### L’icône Jimber dans la zone de notification ![](./screenshots/jimber_icon.png ":size=25")

Après vous être connecté, cliquez sur l’icône pour afficher ce menu :

![jimber_tray.png](./screenshots/jimber_tray.png ":size=250")

- `Security panel` : vous obtenez ici un aperçu des services et de vos appareils. Vous trouverez [ici](/./rules/services/services.md) des informations détaillées sur les services.
- Choisissez `Sign out` pour vous déconnecter de l’application. L’avertissement suivant s’affiche :

![logout.png](./screenshots/logout.png ":size=300")

- `Stealth mode` garantit que le trafic est envoyé via HTTP chiffré et permet d’établir des connexions VPN dans des environnements où elles seraient normalement bloquées, tels que les points d’accès publics, les aéroports ou les pays soumis à une censure stricte d’Internet. Cette fonctionnalité masque le trafic VPN en le faisant passer pour du trafic Internet ordinaire, ce qui vous aide à contourner les restrictions réseau. Le port 51820 est généralement utilisé pour cette fonctionnalité.
>
> [!ATTENTION]
> Le **mode furtif** est disponible uniquement dans certaines situations où votre connexion est reconnue comme externe à l’environnement cloud Jimber SASE.

- `Disconnect` vous déconnecte de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***, mais vous restez connecté à votre compte.
- `Quit` ferme l’application.

### Détails de l’appareil utilisateur

L’aperçu des appareils utilisateur présente déjà certaines propriétés :

- Système d’exploitation, indiqué par une icône de système d’exploitation rouge ou verte : ![](../../images/icons/icon_windows_os.png ':size=25'), ![](../../images/icons/icon_ubuntu_os.png ':size=20'), ![](../../images/icons/icon_apple_os.png ':size=20').
- Nom de l’appareil.
- Indique si le mode sécurisé est actif, désactivé ou non pris en charge.
- Adresse IP.
- État de l’approbation.

>[!NOTE]
>La fonctionnalité « Approbation des appareils » de notre plateforme ajoute un niveau supplémentaire de sécurité et de contrôle en exigeant une approbation administrative avant qu’un appareil puisse être ajouté au réseau. Cette procédure garantit que seuls les appareils autorisés obtiennent un accès, contribuant ainsi à préserver l’intégrité et la sécurité du réseau.

![overview_userdevices.png](./screenshots/overview_userdevices.png ":size=800")

L’aperçu vous permet également de voir quels appareils sont en ligne ou hors ligne :

- Un appareil utilisateur en ligne apparaît en haut de la liste de l’aperçu, avec une icône de système d’exploitation verte au début de sa ligne.
- Un appareil utilisateur hors ligne apparaît dans l’aperçu avec une icône de système d’exploitation rouge au début de sa ligne.
- Un appareil mobile utilisateur en ligne apparaît dans l’aperçu avec une icône d’appareil mobile verte ![](../../images/icons/icon_mobile.png ':size=20') au début de sa ligne.
- Un appareil utilisateur nécessitant une mise à jour apparaît dans l’aperçu avec un triangle d’avertissement jaune ![](../../images/icons/icon_deviceupdate.png ':size=20') avant l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') à la fin de sa ligne. 

Cliquez sur la ligne correspondante de l’appareil utilisateur pour ouvrir une nouvelle fenêtre contenant plus de détails :

![user_device_info_details.png](./screenshots/user_device_info_details.png ":size=500")

L’onglet logiciel affiche les antivirus et le pare-feu installés : 

![user_device_info_software.png](./screenshots/user_device_info_software.png ":size=500")

L’onglet sécurité affiche les politiques installées :

![user_device_info_security.png](./screenshots/user_device_info_security.png ":size=500")

>[!TIP]
>Toutes les informations peuvent être copiées à l’aide du bouton de copie ![](../../images/buttons/button_copy.png ":size=25") situé dans le coin supérieur droit.

### Filtrer les appareils utilisateur

Vous pouvez rechercher dans la liste des appareils utilisateur à l’aide du champ de recherche situé en haut de la page. Cela vous aide à trouver et à gérer rapidement l’appareil recherché.

Saisissez des mots-clés dans le champ de recherche pour filtrer la liste des appareils.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Lorsque vous cliquez dessus, des options de filtrage avancées s’affichent. Vous pouvez définir des conditions supplémentaires à partir des trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir le mode de correspondance de la valeur (`equals`, `contains` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à rechercher, selon la propriété sélectionnée.

![filter_userdevice.png](./screenshots/filter_userdevice.png ':size=400')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.

<!-- Once filters are applied:
- The results are updated to reflect your conditions.
- Active filters appear at the top of the page.
- You can remove filters individually by clicking the `X` next to each, or remove all at once by clicking the `Reset Filters` button. -->

> [!TIP]
> Vous pouvez actualiser la liste des appareils utilisateur en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

### Supprimer un appareil utilisateur

Vous pouvez supprimer un appareil utilisateur en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') dans sa ligne.

> [!WARNING]
> La suppression d’un appareil actif le déconnecte immédiatement de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***. Pour ajouter à nouveau l’appareil, l’utilisateur devra s’y connecter et, si cette fonctionnalité est activée, faire approuver l’appareil sur la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***.

Un avertissement s’affichera avant la suppression de l’appareil :

![delete_device.png](./screenshots/delete_device.png ':size=400')
