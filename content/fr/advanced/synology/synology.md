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
> Cela supprimera tout le contenu !

  1. Repérez le bouton de réinitialisation à l’arrière du NAS.
  2. Maintenez-le enfoncé pendant environ 5 secondes, jusqu’à ce que vous entendiez un bip. Vous aurez généralement besoin d’une épingle pointue pour appuyer sur le bouton de réinitialisation.

  ![reset_synology](./screenshots/reset_synology.png ':size=100')

  3. Relâchez le bouton, puis appuyez rapidement dessus et maintenez-le à nouveau enfoncé jusqu’à entendre 3 bips distincts.
  4. Attendez le bip final signalant la fin de la réinitialisation.

  > [!Warning]
  > Après une réinitialisation complète du Synology, vous devez réinstaller le système d’exploitation.

##### Localiser le NAS Synology

Assurez-vous d’être connecté au même réseau que le Synology.

- Rendez-vous sur http://find.synology.com/ et recherchez un appareil Synology à proximité.

![search_synology](./screenshots/search_synology.png ':size=500')

>[!INFO]
> Si vous ne parvenez pas à localiser le NAS Synology, vérifiez les raisons suivantes : 
> - Le Synology n’est pas allumé ou n’a pas démarré et n’est donc pas encore détectable. Assurez-vous que l’appareil est allumé et relancez la recherche plusieurs fois, car cela peut prendre un certain temps.
> - Vous n’êtes pas sur le même réseau que le Synology ou celui-ci n’est pas connecté à Internet.
> - Le Synology doit être redémarré en raison d’une défaillance. Maintenez le bouton d’alimentation enfoncé jusqu’à ce que le voyant bleu clignote, puis relâchez-le. Attendez que l’appareil soit éteint, puis appuyez à nouveau sur le bouton d’alimentation. Attendez d’entendre un bip avant de le rechercher sur https://find.synology.com (+- 1 minute).
- Vous pouvez également accéder directement à l’adresse IP interne actuelle du NAS. (Exemple : http://192.168.0.146:5000)

Une fois le Synology localisé, l’écran suivant s’affiche :

![find_synology](./screenshots/find_synology.png ':size=500')


Sélectionnez le bon appareil, cliquez sur « Connect » et acceptez le contrat de licence utilisateur final (EULA). 

![synology_eula.png](./screenshots/synology_eula.png ':size=500')

Cliquez sur « Next » pour lancer l’installation du logiciel.

![connecting_synology](./screenshots/connecting_synology.png ':size=500')

##### Installer DiskStation Manager

Installez ensuite le logiciel du NAS Synology.

![install_synology_manager](./screenshots/install_synology_manager.png ':size=500')

![installing_synology](./screenshots/installing_synology.png ':size=500')

Après l’installation du logiciel, le Synology redémarre. Cela prend environ 10 minutes.

![restart_synology](./screenshots/restart_synology.png ':size=500')

Après le redémarrage, vous pouvez commencer à gérer le Synology.

![welcome_to_synology](./screenshots/welcome_to_synology.png ':size=500')

Dans la fenêtre suivante, vous pouvez choisir un nom d’appareil, un administrateur et un mot de passe. 

![get started](./screenshots/getstarted.png ':size=500')

Dans la fenêtre suivante, choisissez une option de mise à jour du Synology.

![update_options](./screenshots/update_options.png ':size=500')

Dans la fenêtre suivante, créez un compte Synology. 

![synology_account](./screenshots/synology_account.png ':size=500')

À ce stade, vous pouvez créer un compte Synology.

![account_synology](./screenshots/account_synology.png ':size=300')


### Préparation

Rendez-vous sur https://sase.jimber.io/ et ajoutez un nouveau serveur à la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_**. 

![create_synology](./screenshots/create_synology.png ':size=500')

Veillez à copier le **Token** et le **Hostname** dans un bloc-notes. 

Par défaut, vous pourrez accéder au NAS via le nom d’hôte. 

>[!INFO]
> Sous Windows, vous devrez ajouter **.local**. Tout alias attribué à l’appareil pourra également être résolu si le **remplacement DNS** est activé.

##### Créer une connexion Synology pour Jimber SASE Client

Pour faciliter la gestion, créez un nouvel utilisateur sur le Synology spécifiquement pour l’installation de **_<span style="color: darkblue;">Jimber SASE Client</span>_**. 

L’utilisateur devra disposer des accès et autorisations suivants : 
  - administrateur
  - ssh 

**La création d’un nouvel utilisateur** peut se faire dans « Control Panel », « User & Group » :

![control_panel](./screenshots/control_panel.png ':size=500') 

![new_user](./screenshots/new_user.png ':size=500') 

![join_group](./screenshots/join_group.png ':size=500') 

Vous pouvez ignorer les fenêtres suivantes jusqu’à la fin de l’opération. 

>[!NOTE]
>Veuillez noter le **nom d’utilisateur** et le **mot de passe** choisis. 

**Activer SSH** - Uniquement nécessaire pendant l’installation.

L’activation de SSH peut se faire dans « Control Panel », « Terminal & SNMP » :

![control_panel_ssh](./screenshots/control_panel_ssh.png ':size=500') 

![ssh_settings](./screenshots/ssh_settings.png ':size=500')


### Installer Jimber SASE Client sur votre Synology

Téléchargez la dernière version pour votre Synology depuis la page [téléchargements](https://sase.jimber.io/downloads) (aucune connexion n’est nécessaire).

> [!INFO]
> Pour télécharger une autre version spécifique, vous pouvez utiliser ce [lien](https://sase.jimber.io/clients).


<!-- ![Trouver le paquet Synology adapté](head-to-synology-downloads.png ':size=300x')
![Trouver le paquet Synology adapté](head-to-synology-downloads2.png ':size:700x')
![Trouver le paquet Synology adapté](head-to-synology-downloads3.png ':size:500x')
![Trouver le paquet Synology adapté](find-synology-version.png ':size=800x')
![Trouver le paquet Synology adapté](head-to-synology-downloads4.png ':size:500x') -->

![Trouver le paquet Synology adapté](./screenshots/choose_download_syn.png ':size=200')
![Trouver le paquet Synology adapté](./screenshots/downloads.png ':size=300') 

Vous trouverez le nom du modèle de votre Synology dans le Centre d’information du panneau de configuration. 

![Trouver le paquet Synology adapté](./screenshots/download_syn_warning.png ':size=300') 

![Trouver le paquet Synology adapté](./screenshots/info_center.png ':size=500') 

![Trouver le paquet Synology adapté](./screenshots/choose_model.png ':size=300') 

La dernière version SPK pour votre NAS sera alors téléchargée.

##### Installation

Sélectionnez Package Center dans la barre des tâches, puis **Manual Install** dans le coin supérieur droit.

![Installer le SPK](./screenshots/install-spk.png ':size=500')

Suivez la séquence présentée dans les captures d’écran ci-dessous pour installer correctement le SPK.

![Installer le SPK](./screenshots/install-spk2.png ':size=500')

Dans la fenêtre suivante, vous pouvez choisir `Agree`.

![third_party](./screenshots/third_party.png ':size=500')


![Installer le SPK](./screenshots/install-spk3.png ':size=500')

![Installer le SPK](./screenshots/install-spk5.png ':size=500')
![Installer le SPK](./screenshots/install-spk6.png ':size=500')

Vous recevrez une confirmation indiquant que l’installation a réussi.

![Installer le SPK](./screenshots/install_syn_succes.png ':size=300')


Dans un délai de 30 à 60 secondes, le NAS devrait apparaître comme ajouté avec succès à la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_**, comme l’indique le point vert à côté du nom d’hôte.

![NAS en ligne](./screenshots/nas-online.png ':size=300')

##### Ports les plus fréquemment utilisés pour le NAS Synology

Ports

- 22
- 80
- 5000
- 445


>[!INFO]
>La configuration des règles est décrite dans la section [SÉCURITÉ](/security.md) de la barre latérale.
