# Synology  

>[!INFO]
> La prise en charge est actuellement assurée pour les NAS Synology exécutant **DMS 7+**. Si vous utilisez une version antérieure, veuillez la mettre à jour ou contacter notre équipe d’assistance pour obtenir des conseils.

### Configuration initiale - `Optional`

> [!INFO]
> Ces étapes ne sont nécessaires que si vous devez réinitialiser votre NAS ou trouver son adresse IP. 



##### Réinitialiser le NAS Synology

<!-- > [!INFO]
> **Remarque :** À effectuer uniquement si vous souhaitez rétablir les paramètres d’usine. -->

> [!WARNING]
> À effectuer uniquement si vous souhaitez rétablir les paramètres d’usine.
> Toutes les données seront supprimées !

  1. Repérez le bouton de réinitialisation à l’arrière du NAS.
  2. Maintenez-le enfoncé pendant environ 5 secondes, jusqu’à entendre un bip. Vous aurez généralement besoin d’une épingle pointue pour appuyer sur le bouton de réinitialisation.

  ![réinitialiser_synology](./screenshots/reset_synology.png ':size=100')

  3. Relâchez le bouton, puis appuyez rapidement de nouveau dessus et maintenez-le enfoncé jusqu’à entendre 3 bips distincts.
  4. Attendez le dernier bip indiquant que la réinitialisation est terminée.

  > [!Warning]
  > Après une réinitialisation complète du Synology, vous devez réinstaller le système d’exploitation.

##### Localiser le NAS Synology

Assurez-vous d’être connecté au même réseau que le Synology.

- Accédez à http://find.synology.com/ et recherchez un appareil Synology à proximité.

![rechercher_synology](./screenshots/search_synology.png ':size=500')

>[!INFO]
> Si vous ne parvenez pas à localiser le NAS Synology, vérifiez les points suivants : 
> - Le Synology n’est pas allumé ou n’a pas démarré et n’est pas encore détectable. Assurez-vous que l’appareil est allumé et actualisez la recherche plusieurs fois, car cela peut prendre un certain temps.
> - Vous n’êtes pas sur le même réseau que le Synology, ou celui-ci n’est pas connecté à Internet.
> - Le Synology doit être redémarré en raison d’une défaillance. Maintenez le bouton d’alimentation enfoncé jusqu’à ce que le voyant bleu clignote, puis relâchez-le. Attendez que l’appareil s’éteigne, puis appuyez de nouveau sur le bouton d’alimentation. Attendez d’entendre un bip avant de pouvoir le trouver sur https://find.synology.com (+- 1 minute).
- Vous pouvez également accéder directement à l’adresse IP interne actuelle du NAS. (Exemple : http://192.168.0.146:5000)

Après avoir localisé le Synology, l’écran suivant s’affiche :

![trouver_synology](./screenshots/find_synology.png ':size=500')


Sélectionnez le bon appareil, cliquez sur « Connecter » et acceptez le contrat de licence utilisateur final (EULA). 

![synology_eula.png](./screenshots/synology_eula.png ':size=500')

Cliquez sur « Suivant » pour lancer l’installation du logiciel.

![connexion_synology](./screenshots/connecting_synology.png ':size=500')

##### Installer DiskStation Manager

Installez enfin le logiciel sur le NAS Synology.

![installer_synology_manager](./screenshots/install_synology_manager.png ':size=500')

![installation_synology](./screenshots/installing_synology.png ':size=500')

Une fois le logiciel installé, le Synology redémarre. Cette opération prend environ 10 minutes.

![redémarrer_synology](./screenshots/restart_synology.png ':size=500')

Après le redémarrage, vous pouvez commencer à gérer le Synology.

![bienvenue_sur_synology](./screenshots/welcome_to_synology.png ':size=500')

Dans la fenêtre suivante, vous pouvez choisir un nom d’appareil, un administrateur et un mot de passe. 

![commencer](./screenshots/getstarted.png ':size=500')

Dans la fenêtre suivante, choisissez une option de mise à jour du Synology.

![options_mise_a_jour](./screenshots/update_options.png ':size=500')

Dans la fenêtre suivante, créez un compte Synology. 

![compte_synology](./screenshots/synology_account.png ':size=500')

À ce stade, vous pouvez créer un compte Synology.

![compte_synology](./screenshots/account_synology.png ':size=300')


### Préparation

Accédez à https://signal.jimber.io/ et ajoutez un nouveau serveur à la `Jimber SASE Platform`. 

![créer_synology](./screenshots/create_synology.png ':size=500')

Veillez à copier le **Token** et le **Hostname** dans un bloc-notes. 

Par défaut, vous pourrez accéder au NAS à l’aide du nom d’hôte. 

>[!INFO]
> Sous Windows, vous devrez ajouter **.local**. Tout alias attribué à l’appareil pourra également être résolu si **DNS Override** est activé.

##### Créer un identifiant Synology pour Jimber SASE Client

Pour faciliter la gestion, créez un nouvel utilisateur sur le Synology spécifiquement pour l’installation de `Jimber SASE Client`. 

L’utilisateur doit disposer des accès et autorisations suivants : 
  - administrateur
  - ssh 

**La création d’un nouvel utilisateur** peut se faire dans « Panneau de configuration », « Utilisateur et groupe » :

![panneau_de_configuration](./screenshots/control_panel.png ':size=500') 

![nouvel_utilisateur](./screenshots/new_user.png ':size=500') 

![rejoindre_groupe](./screenshots/join_group.png ':size=500') 

Vous pouvez ignorer les fenêtres suivantes jusqu’à la fin de l’opération. 

>[!NOTE]
>Veuillez noter le **nom d’utilisateur** et le **mot de passe** choisis. 

**Activer SSH** - Nécessaire uniquement pendant l’installation.

Vous pouvez activer SSH dans « Panneau de configuration », « Terminal et SNMP » :

![panneau_de_configuration_ssh](./screenshots/control_panel_ssh.png ':size=500') 

![paramètres_ssh](./screenshots/ssh_settings.png ':size=500')


### Installer Jimber SASE Client sur votre Synology

Téléchargez la dernière version pour votre Synology depuis la page [téléchargements](https://signal.jimber.io/downloads) (aucune connexion n’est nécessaire).

> [!INFO]
> Pour télécharger une autre version précise, vous pouvez utiliser ce [lien](https://signal.jimber.io/clients).


<!-- ![Find the correct synology package](head-to-synology-downloads.png ':size=300x')
![Find the correct synology package](head-to-synology-downloads2.png ':size:700x')
![Find the correct synology package](head-to-synology-downloads3.png ':size=500x')
![Find the correct synology package](find-synology-version.png ':size=800x')
![Find the correct synology package](head-to-synology-downloads4.png ':size=500x') -->

![Trouver le bon paquet Synology](./screenshots/choose_download_syn.png ':size=200')
![Trouver le bon paquet Synology](./screenshots/downloads.png ':size=700') 

Vous trouverez le nom du modèle de votre Synology dans le Centre d’informations du panneau de configuration. 

![Trouver le bon paquet Synology](./screenshots/download_syn_warning.png ':size=500x250') 

![Trouver le bon paquet Synology](./screenshots/info_center.png ':size=500') 

![Trouver le bon paquet Synology](./screenshots/choose_model.png ':size=500x250') 

La dernière version SPK pour votre NAS sera téléchargée.

##### Installation

Dans la barre des tâches, choisissez Centre de paquets, puis **Installation manuelle** dans le coin supérieur droit.

![Installer le SPK](./screenshots/install-spk.png ':size=500')

Suivez les étapes présentées dans les captures d’écran ci-dessous pour installer correctement le SPK.

![Installer le SPK](./screenshots/install-spk2.png ':size=500')

Dans la fenêtre suivante, vous pouvez choisir `Agree`.

![tiers](./screenshots/third_party.png ':size=500')


![Installer le SPK](./screenshots/install-spk3.png ':size=500')

![Installer le SPK](./screenshots/install-spk5.png ':size=500')
![Installer le SPK](./screenshots/install-spk6.png ':size=500')

Un message vous confirmera que l’installation a réussi.

![Installer le SPK](./screenshots/install_syn_succes.png ':size=500')


Après environ 30 à 60 secondes, le NAS devrait apparaître comme ajouté à la `Jimber SASE Platform`, comme l’indique le point vert à côté du nom d’hôte.

![NAS en ligne](./screenshots/nas-online.png ':size=500')

##### Ports les plus couramment utilisés pour le NAS Synology

Ports

- 22
- 80
- 5000
- 445


>[!INFO]
>Vous trouverez des informations sur la configuration des règles dans la section [SÉCURITÉ](/security.md) de la barre latérale.
