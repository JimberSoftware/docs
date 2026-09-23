File: rules/security_panel/security_panel.md

# Panneau de sécurité

Lorsque vous cliquez sur l’icône Jimber dans la barre d’état système, un menu comportant plusieurs options s’affiche. Vous pouvez y sélectionner `Security Panel` :

![Capture d’écran du menu Jimber dans la barre d’état système](./screenshots/jimber_tray.png ':size=300')


Outre le panneau de sécurité, le menu fournit d’autres informations sur votre connexion à la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***, telles que votre état de connexion, les détails de votre compte, l’entreprise à laquelle vous êtes connecté et votre adresse IP sur la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***.


Vous pouvez quitter l’application, vous déconnecter de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** (et vous y reconnecter) ou vous déconnecter de la plateforme. Notez que si vous choisissez cette dernière option, vous devrez vous reconnecter à l’aide de vos identifiants.

Enfin, le menu vous permet d’activer ou de désactiver le **mode furtif** pour votre session. Le mode furtif garantit que le trafic est envoyé via HTTP chiffré. Il est conçu pour permettre les connexions VPN dans des environnements qui les bloqueraient normalement, comme les points d’accès publics, les aéroports ou les pays soumis à une stricte censure d’Internet. Il masque le trafic VPN pour qu’il ressemble à du trafic Internet ordinaire, ce qui vous aide à contourner les restrictions réseau.
Le **mode furtif** n’est disponible que dans certaines situations, lorsque votre connexion est reconnue comme externe à l’environnement cloud Jimber SASE. Vous devez donc être connecté au **contrôleur réseau cloud**.

> [!IMPORTANT]
> Pour pouvoir utiliser le **mode furtif**, l’utilisateur doit appartenir à un groupe pour lequel l’option « Autoriser la connexion mobile » est activée dans la configuration de groupe.

![group_configuration.png](./screenshots/group_configuration_2.png ':size=800')


> [!WARNING]
> Le **mode furtif** n’est pas disponible lorsque vous êtes connecté à un ou plusieurs contrôleurs réseau sur site.



Un clic sur **Security Panel** ouvre un nouvel onglet du navigateur. Par défaut, l’onglet Services s’affiche. L’écran que vous voyez peut varier en fonction des services configurés.

![Capture d’écran de l’onglet Services du panneau de sécurité](./screenshots/secure_panel.png ':size=700')

Les services répertoriés sur cette page dépendent des configurations définies sous Services dans la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** et sont propres au groupe auquel appartient l’utilisateur. Cliquer sur le lien `Open →` lance le service sélectionné, par exemple en ouvrant la page wiki de l’entreprise.

> [!INFO]
> Vous trouverez [ici](/./rules/services/services.md) plus d’informations sur la configuration des services.

En sélectionnant la deuxième option dans la barre latérale, Devices, un écran s’affiche où vous pouvez consulter tous vos appareils.

![Capture d’écran de l’onglet Devices du panneau de sécurité](./screenshots/sec_pan_devices.png ':size=700')

> [!NOTE]
> Tous les appareils apparaîtront dans la liste après l’installation du **_client Jimber SASE_** et son lancement sur l’appareil pour se connecter à la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***.
<!-- >
>Le bouton `+ Create new` ne sera visible que si l’option **MOBILE CONNECTION** de la configuration de groupe est activée pour le groupe auquel appartient l’utilisateur. 
>
> Vous trouverez [ici](/./rules/groupconfiguration/groupconfiguration.md) plus d’informations sur la configuration de groupe. -->


<!-- Vous pouvez ajouter un nouvel appareil mobile en cliquant sur le bouton `+ Create new` situé dans le coin supérieur droit de l’interface.  -->

## Installer Jimber SASE sur un appareil mobile

**Étape 1**

Recherchez ***_<span style="color: darkblue;">Jimber SASE</span>_*** dans le Play Store ou l’App Store et installez l’application.   

<!-- ![Capture d’écran de l’étape 1 de l’ajout d’un appareil utilisateur](./screenshots/scan_device.png ':size=500') -->

**Étape 2** 

Ouvrez l’application et connectez-vous à votre compte : 

![log_in](./screenshots/sign_in.png ':size=300')

> [!NOTE]
> Si vous n’avez pas encore de compte, contactez votre administrateur réseau pour qu’il en crée un pour vous.

**Étape 3**

Vous devrez saisir un code de vérification.

![verification_code](./screenshots/verification_code.jpg ':size=150')

Suivez les instructions et saisissez le code. Cliquez sur *Verify*.

**Étape 4**

Choisissez un nom pour l’appareil mobile que vous ajoutez, puis cliquez sur *Submit*.

![choose_name](./screenshots/choose_name.jpg ':size=150')

Un message vous indiquera que **_Jimber SASE_** va établir une connexion VPN. Vous pouvez cliquer sur *OK*.

![VPN_connection.jpg](./screenshots/VPN_connection.jpg ':size=150')

**Étape 5**

Sur l’écran suivant, activez l’interrupteur pour mettre **_Jimber SASE_** en marche.  

![turn_on](./screenshots/turn_on_jimber.jpg ':size=150')

<!-- À l’étape 3, un autre code QR vous est fourni pour connecter l’appareil mobile à votre compte utilisateur sur la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***. Suivez les instructions de cette étape pour scanner le code à l’aide de l’application.

![Capture d’écran de l’étape 3 de l’ajout d’un appareil utilisateur](./screenshots/add_user_device_2.png ':size=500')

Après avoir confirmé l’installation en cliquant sur `I have configured my device`, votre appareil mobile sera ajouté à la liste.  -->
L’appareil mobile apparaît désormais dans la liste des appareils. 

>[!Warning]
> L’utilisateur ne pourra pas ajouter de nouvel appareil mobile si l’option **DEVICE LIMIT** de la configuration de groupe est activée et que le nombre maximal d’appareils autorisés a déjà été atteint.
