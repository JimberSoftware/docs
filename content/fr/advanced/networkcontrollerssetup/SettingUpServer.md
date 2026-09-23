File: advanced/networkcontrollerssetup/SettingUpServer.md

# ![](../../images/menu/menu_networkcontrollers.png ':size=25') Installation d’un contrôleur réseau

> [!Note]
> Si vous prévoyez d’installer ce serveur virtuellement, veuillez tenir compte des [paramètres BIOS](/./advanced/hypervisorinstallation/hypervisorinstallation.md) nécessaires.

> [!Note]
> La configuration minimale requise pour un contrôleur réseau sur site est la suivante :
> 
> **Général** :
> - Disque dur de 25 Go
> **Pour 50 utilisateurs :**
> - 2 CPU
> - 4 Go de RAM

Téléchargez la dernière version du « Network Controller » depuis https://SASE.jimber.io/downloads (aucune connexion n’est nécessaire).

Utilisez le fichier téléchargé pour installer le contrôleur réseau.

![nc_install_start.png](./screenshots/nc_install_start.png ':size=600')

Appuyez sur Entrée, puis sélectionnez **Terminé** dans l’écran suivant.

![installation_server_nc_3.png](./screenshots/installation_server_nc_3.png ':size=600')

Dans la fenêtre « Guided storage configuration », sélectionnez **Terminé**. Un aperçu de la configuration du stockage s’affichera. Ici et dans la fenêtre suivante, vous pouvez également sélectionner **Terminé**.

![installation_server_nc_4.png](./screenshots/installation_server_nc_4.png ':size=600')

<!-- In the window "Network configuration", you can hit **Done**. -->

![network_config.png](./screenshots/network_config.png ':size=600')



<!-- Then you will see a window with the message “Confirm destructive action”. This is a warning that all data on the used disks will be lost. Only in case of starting this process by mistake, you can choose here for “Continue”. -->

Dans la fenêtre suivante, vous serez informé que toutes les données des disques utilisés risquent d’être perdues. Sélectionnez **Continuer**.

![install_system.png](./screenshots/install_system.png ':size=600')

L’installation démarre alors. Elle peut prendre plusieurs minutes.

![installation_server_nc_2.png](./screenshots/installation_server_nc_2.png ':size=600')

Pendant l’installation, vous pouvez créer votre contrôleur réseau sur https://signal.jimber.io.
Données nécessaires :
- Jeton : copiez-le !
- Adresse du point de terminaison : voir l’étape suivante.

> [!INFO]
> Vous trouverez [ici](/./devices/networkcontrollers/networkcontrollers.md) des instructions détaillées pour créer un contrôleur réseau sur site.

> [!Warning]
> Une fois l’installation terminée, redémarrez le système.

![nc_reboot.png](./screenshots/nc_reboot.png ':size=600')

**Suite de l’installation**

Vous aurez besoin des informations suivantes pour continuer (appuyez sur « Entrée » si nécessaire) :
- nom d’utilisateur : jimber
- mot de passe : jimber


![installation_server_nc_5.png](./screenshots/installation_server_nc_5.png ':size=600')

Dans l’écran suivant, sélectionnez l’option **3** pour afficher la configuration IP du contrôleur réseau.

![menu.png](./screenshots/menu.png)

Utilisez ensuite un PC connecté au même réseau que le contrôleur réseau et accédez à l’URL web affichée pour l’option 3. Une interface s’ouvrira pour poursuivre l’installation du contrôleur réseau.

> [!Note]
>Utilisez l’adresse IP affichée pour terminer l’installation du contrôleur réseau sur la `Jimber SASE Platform` en la saisissant dans le champ « Adresse du point de terminaison ».

![ip_configuration.png](./screenshots/ip_configuration.png ':size=600')


Connectez-vous à l’interface web avec `jimber` comme mot de passe.

![web_login](./screenshots/web_login.png ':size=600')

Définissez un nouveau mot de passe.

>[!Warning] 
>Le nouveau mot de passe doit comporter au moins **16** caractères !

![web_new_password.png](./screenshots/web_new_password.png ':size=600')

Sélectionnez la configuration réseau appropriée, puis cliquez sur ![test_connection.png](./screenshots/test_connection.png ':size=100'). Si le test réussit, vous pouvez passer à l’étape suivante.

> [!Note]
> En cas d’échec, vérifiez que le contrôleur réseau dispose d’une connexion Internet active et que la configuration de l’interface web est correcte.

![web_config.png](./screenshots/web_config.png ':size=600')

Accédez à la `Jimber SASE Platform` et copiez le jeton du contrôleur réseau que vous venez de créer. Pour trouver le jeton, modifiez le contrôleur réseau à l’aide du crayon jaune.

![signal_token.png](./screenshots/signal_token.png ':size=500')

Collez ce jeton dans la configuration web du contrôleur réseau. Cliquez ensuite sur Suivant.

![web_token.png](./screenshots/web_token.png ':size=600')

Veuillez patienter pendant que la connexion est testée.

![web_wait.png](./screenshots/web_wait.png ':size=600')

Une fois la connexion établie, l’écran suivant s’affiche :

![web_done.png](./screenshots/web_done.png ':size=600')

Vérifiez que votre contrôleur réseau est maintenant en ligne sur la `Jimber SASE Platform`, dans la page Network Controller.

![signal_nc_online.png](./screenshots/signal_nc_online.png ':size=600')


### Installation sur un hyperviseur

L’installation sur un hyperviseur est très répandue et constitue une méthode de travail très pratique. Son principal avantage est qu’elle permet d’installer le serveur du contrôleur réseau sur du matériel existant. Il n’est donc pas nécessaire de disposer d’un appareil physique.

> [!INFO]
> Vous trouverez des instructions détaillées [ici](/./advanced/hypervisorinstallation/hypervisorinstallation.md).
