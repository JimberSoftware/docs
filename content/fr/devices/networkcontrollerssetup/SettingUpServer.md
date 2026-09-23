File: devices/networkcontrollerssetup/SettingUpServer.md

# ![](../../images/menu/menu_networkcontrollers.png ':size=25')Installation du contrôleur réseau

> [!Note]
> Si vous prévoyez d’installer ce serveur virtuellement, veuillez tenir compte des [paramètres du BIOS](/./advanced/hypervisorinstallation/hypervisorinstallation.md) nécessaires. 

<!-- listed at the bottom of this page. -->

Ceci est un test.
Téléchargez la dernière version du « contrôleur réseau » à l’adresse https://sase.jimber.io/downloads 

Utilisez le fichier téléchargé pour installer le contrôleur réseau. 

![nc_install_start.png](./screenshots/nc_install_start.png ':size=600')

Appuyez sur Entrée.

<!-- ![installation_server_nc_3.png](./screenshots/installation_server_nc_3.png ':size=600')

Dans la fenêtre « Configuration guidée du stockage », vous pouvez cliquer sur « Terminé ». Un aperçu de la configuration du stockage s’affiche. Dans cette fenêtre et dans la suivante, vous pouvez également cliquer sur **Terminé**. 

![installation_server_nc_4.png](./screenshots/installation_server_nc_4.png ':size=600') -->



![network_config.png](./screenshots/network_config_.png ':size=600')




Dans la fenêtre suivante, vous serez informé que toutes les données des disques utilisés risquent d’être perdues. Choisissez **Continuer**. 

![installation_server_nc.png](./screenshots/installation_server_nc.png ':size=600')

L’installation va alors commencer. Elle peut prendre plusieurs minutes.

![installation_server_nc_2.png](./screenshots/installation_server_nc_2.png ':size=600')

Pendant l’installation, vous pouvez créer votre contrôleur réseau sur https://signal.jimber.io. 
Vous aurez besoin des données suivantes :
- Token : copiez-le !
- Adresse du point de terminaison : voir l’étape suivante.

> [!INFO]
> Des instructions détaillées pour créer un contrôleur réseau sur site sont disponibles [ici](/./devices/networkcontrollers/networkcontrollers.md).

> [!Warning]
> Une fois l’installation terminée, redémarrez le système.

![nc_reboot.png](./screenshots/nc_reboot.png ':size=600')

**Suite de l’installation**

Vous aurez besoin des données suivantes pour continuer (appuyez sur « Entrée » si nécessaire) :
- username: jimber
- password: jimber


![installation_server_nc_5.png](./screenshots/installation_server_nc_5.png ':size=600')

Sur l’écran suivant, sélectionnez l’option 3 pour afficher la configuration IP du contrôleur réseau.

![menu.png](./screenshots/menu.png)

Utilisez maintenant un PC connecté au même réseau que le contrôleur réseau et accédez à l’URL web affichée pour l’option 3. Une interface s’ouvrira pour poursuivre l’installation du contrôleur réseau.

> [!Note]
>Utilisez l’adresse IP affichée pour terminer l’installation du contrôleur réseau sur la `Jimber SASE Platform` en la renseignant dans le champ « Adresse du point de terminaison ».

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

Accédez à la `Jimber SASE Platform` et copiez le token du contrôleur réseau que vous venez de créer. Vous trouverez le token en modifiant le contrôleur réseau à l’aide du crayon jaune.

![signal_token.png](./screenshots/signal_token.png ':size=500')

Collez ce token dans la configuration web du contrôleur réseau. Cliquez ensuite sur « Suivant ».

![web_token.png](./screenshots/web_token.png ':size=600')

Veuillez patienter quelques instants pendant que la connexion est testée.

![web_wait.png](./screenshots/web_wait.png ':size=600')

Une fois la connexion établie, l’écran suivant s’affichera :

![web_done.png](./screenshots/web_done.png ':size=600')

Vérifiez que votre contrôleur réseau est maintenant en ligne sur la `Jimber SASE Platform`, dans la page « Contrôleur réseau ».

![signal_nc_online.png](./screenshots/signal_nc_online.png ':size=600')


### Installation de l’hyperviseur

L’installation sur un hyperviseur est très répandue, car elle offre une grande facilité d’utilisation. Son principal avantage est que le serveur du contrôleur réseau peut être installé sur du matériel existant. Il n’est donc pas nécessaire d’utiliser un appareil physique. 

> [!INFO]
> Des instructions détaillées sont disponibles dans la section Avancé [ici](/./advanced/hypervisorinstallation/hypervisorinstallation.md).
