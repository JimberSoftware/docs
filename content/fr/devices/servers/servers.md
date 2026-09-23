# ![](../../images/menu/menu_servers.png ':size=25') Serveurs

### Créer un serveur

Pour créer un serveur dans la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***, cliquez sur le bouton `+ Create new` situé dans le coin supérieur droit de l’interface. La boîte de dialogue suivante s’ouvre :

![create_server.png](./screenshots/create_server.png ":size=800")

- Le nom d’hôte est obligatoire et doit être une chaîne en minuscules. 
- Vous pouvez créer une nouvelle étiquette ou utiliser une étiquette enregistrée.


 
>[!TIP] 
>Nous vous conseillons de copier le jeton, car vous en aurez besoin pour installer le serveur. Vous pourrez toutefois y accéder à tout moment depuis l’écran de modification du serveur dans la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***.


### Installation du serveur

#### Plateformes 

> [!ATTENTION] 
> Créez d’abord votre serveur dans la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** (voir ci-dessus).

<!-- tabs:start -->



### **Windows**

Téléchargez la dernière version du client « Windows Server » depuis https://SASE.jimber.io/downloads (aucune connexion n’est nécessaire).

> [!TIP]
> Pour télécharger une autre version spécifique, vous pouvez utiliser ce [lien](https://SASE.jimber.io/clients).

Une fois le fichier téléchargé, lancez l’installation du fichier .msi en double-cliquant dessus.

![win_server_msi.png](./screenshots/win_server_msi.png ':size=100')




Au démarrage du **_Jimber SASE Client_**, une boîte de dialogue s’affiche : 

![jimber_server_settings.png](./screenshots/jimber_server_settings.png ':size=500')

Le jeton requis a été créé avec le nouveau serveur. Si vous ne l’avez pas copié à l’étape précédente, vous pouvez le récupérer dans l’onglet « Servers » de la ****_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***. Sélectionnez et modifiez simplement le serveur concerné pour le trouver.

![update_server.png](./screenshots/update_server_token.png ':size=800')

<!-- ![token.png](./screenshots/token.png ':size=500') -->

Après avoir renseigné le jeton et cliqué sur le bouton d’envoi, une fenêtre contextuelle indique que la configuration du serveur a été envoyée et que le service va être redémarré :


![settings_updated.png](./screenshots/settings_updated.png ':size=400')




<!-- Access the 'services' panel by entering 'services.msc' into the start menu's search bar. Within this panel, find the 'Jimber Network Isolation' service and initiate a restart.


![services_jimber.png](/services_jimber.png ':size=800') -->


Une fois l’installation terminée, le serveur doit apparaître comme connecté (indiqué par un point vert) dans l’onglet « Servers » de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***. 

<!-- For any necessary troubleshooting, consult the log file at this location: 
`C:\Program Files\Jimber\jimbernetworkisolation.log` -->

### **Linux**

> [!INFO] 
> La prise en charge est actuellement assurée pour les dernières versions LTS d’Ubuntu. Pour les autres distributions de système d’exploitation, veuillez contacter notre équipe d’assistance.

Téléchargez et installez la dernière version du client « Linux Server » depuis https://SASE.jimber.io/downloads (aucune connexion n’est nécessaire) en exécutant les commandes suivantes :

```bash
sudo apt update
sudo apt install wireguard
wget https://SASE.jimber.io/linux-server-latest.deb
sudo dpkg -i linux-server-latest.deb
```
> [!TIP]
> Pour télécharger une autre version spécifique, vous pouvez utiliser ce [lien](https://SASE.jimber.io/clients).

Une fois l’installation terminée, un nouveau fichier `settings.json` est automatiquement créé dans le répertoire `/etc/jimber/`.
Ce fichier doit être renseigné avec le jeton qui vous a été fourni lors de la création du serveur dans l’interface de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***. Pour ce faire, exécutez la commande suivante :

```bash
sudo jimberfw -config
```
![token_linux_server.png](./screenshots/token_linux_server.png ':size=300') 

Si vous ne l’avez pas copié à l’étape précédente, vous pouvez récupérer le jeton dans l’onglet « Servers » de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***. Sélectionnez et modifiez simplement le serveur concerné pour le trouver.


![update_server.png](./screenshots/update_server_token.png ':size=800')


<!-- Restart the service by running the following commandsudo

```bash
sudo systemctl restart jimbernetworkisolation.service
``` -->

Une fois l’installation terminée, le serveur doit apparaître comme connecté (indiqué par un point vert) dans l’onglet « Servers » de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***. 
<!-- If needed, refer to the following log files for debugging purposes:

```bash
cat /var/log/jimber/jimbernetworkisolation.log
``` -->

>[!TIP]
> Vous pouvez afficher la version installée à l’aide de *jimberfw version*. Vous pouvez également la consulter dans la page des détails du serveur sur la plateforme SASE (voir ci-dessous).


### **Synology**

[Cliquez ici pour découvrir comment configurer votre NAS Synology](../../advanced/synology/synology.md)

### **Raspberry Pi**

Configuration requise :
- Installation Raspbian par défaut 

Suivez la procédure d’installation Linux, mais utilisez le fichier deb suivant : 
- https://SASE.jimber.io/clients/rpi-latest.deb

> [!TIP]
> Pour télécharger une autre version spécifique, vous pouvez utiliser ce [lien](https://SASE.jimber.io/clients).

Toute autre configuration est identique.

<!-- tabs:end -->

>[!INFO]
>Pour tout dépannage éventuel, vous pouvez consulter les fichiers journaux. Vous trouverez [ici](/./advanced/logging/logging.md) l’emplacement de ces fichiers. 

---
---

### Filtrer les serveurs

Vous pouvez rechercher des serveurs dans la liste à l’aide du champ de recherche situé en haut de la page. Cela vous permet de trouver et de gérer rapidement le serveur recherché.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher les options de filtrage avancées et définir des conditions supplémentaires selon les trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ à filtrer.
- **Type de correspondance** : menu déroulant qui vous permet de choisir la façon de faire correspondre la valeur (`EQUALS`, `CONTAINS` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à rechercher, selon la propriété choisie.

![filter_server.png](./screenshots/filter_server.png ':size=500')

Pour ajouter plusieurs filtres, cliquez à nouveau sur l’icône de filtre ![](../../images/icons/icon_filter.png ':size=20'), puis sur le bouton `+`.


> [!TIP]
> Vous pouvez actualiser la liste des serveurs en cliquant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

### Étiquettes

Les étiquettes sont ajoutées lors de la création ou de la modification du serveur.

Vous pouvez consulter les **étiquettes** utilisées en cliquant sur le bouton `Tags` en haut de la page. Vous pouvez également supprimer les étiquettes utilisées en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') dans leur ligne.

![tags.png](./screenshots/tags.png ':size=500')

> [!CAUTION]
> La suppression d’une étiquette supprime définitivement toutes ses utilisations. Vous ne recevrez aucun avertissement avant sa suppression. 

### Détails du serveur

Dans la vue d’ensemble des serveurs, vous pouvez voir lesquels sont en ligne ou hors ligne.

Un serveur en ligne apparaît dans la vue d’ensemble avec un point vert. Un serveur hors ligne apparaît avec un point rouge. Lorsqu’une mise à jour du serveur est disponible, l’icône de mise à jour verte ![](../../images/icons/icon_update.png ':size=20') l’indique. Survolez l’icône pour voir à quelle mise à jour elle correspond.

![updating_server.png](./screenshots/updating_server.png ':size=800')

Cliquez sur l’icône de mise à jour ![](../../images/icons/icon_update.png ':size=20') pour lancer la mise à jour.

> [!INFO]
> Si la mise à jour réussit, l’icône de mise à jour disparaît. Si elle reste affichée après plusieurs minutes, relancez la mise à jour en cliquant à nouveau sur l’icône. 


>[!NOTE]
> L’icône de mise à jour n’est pas visible lorsque le serveur est hors ligne.


![server online.png](./screenshots/server_online.png ':size=800')

Cliquez sur la ligne correspondant à un serveur pour ouvrir une nouvelle fenêtre contenant plus de détails : les pare-feu ou antivirus installés, les interfaces installées, les paramètres de sécurité et les exceptions du mode sécurisé.

<!-- tabs:start -->

##### **Détails**

Cette fenêtre présente des informations générales sur le serveur et les groupes auxquels il appartient.

![server_detail.png](./screenshots/server_details.png ':size=500')

##### **Logiciels**

Cette section présente un aperçu des logiciels antivirus et des pare-feu installés.

![server_software.png](./screenshots/server_software.png ':size=500')


##### **Interfaces**

Cette fenêtre présente les interfaces réseau détectées sur le serveur.

![server_interfaces.png](./screenshots/server_interfaces.png ':size=500')

##### **Sécurité**

Cette fenêtre affiche les politiques détectées et les règles de redirection de port sur le serveur.

![server_firewall_rules.png](./screenshots/server_firewall_rules.png ':size=500')

##### **Mode sécurisé**

Cette section répertorie les exceptions du mode sécurisé. Celles-ci permettent à certains sites web, applications ou trafics réseau d’ignorer les restrictions de sécurité renforcées, afin que les tâches quotidiennes ne soient pas bloquées tout en maintenant un niveau élevé de protection. 
 
![server_secure_mode.png](./screenshots/server_secure_mode.png ':size=500')

Le mode sécurisé peut être activé lors de la création du serveur ou de sa mise à jour : 

![enable_secure_mode.png](./screenshots/enable_secure_mode.png ':size=500')


<!-- tabs:end -->

---

### Modifier un serveur

Vous pouvez modifier un serveur en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') dans sa ligne.

![edit server.png](./screenshots/update_server.png ':size=800')

Toutes les options sont les mêmes que lors de la création d’un serveur.

### Supprimer un serveur

Vous pouvez supprimer un serveur en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') dans sa ligne.

Un avertissement s’affichera avant la suppression définitive de l’appareil :

![delete_server.png](./screenshots/delete_server.png ':size=300')
