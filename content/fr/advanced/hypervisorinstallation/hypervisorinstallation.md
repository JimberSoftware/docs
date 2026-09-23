### Installation de l’hyperviseur

L’installation d’un hyperviseur est largement répandue. C’est une méthode de travail très pratique. Son principal avantage est que le serveur du contrôleur réseau peut être installé sur du matériel existant. Il n’est donc pas nécessaire d’avoir un appareil physique. Toutefois, certains paramètres sont à prendre en compte.

Les paramètres matériels minimum suivants doivent être définis :    
  - 2 cœurs
  - 4 Go de RAM
  - 25 Go d’espace disque
   

#### VMware ESXi

Configuration du matériel : 

![virt_hardware esxi.png](./screenshots/virt_hardware_esxi.png ':size=500')


Configuration des options : veillez à sélectionner BIOS comme type de micrologiciel.


![vm_options esxi.png](./screenshots/vm_options_esxi.png ':size=500')


#### Hyper-V

Lors de l’installation d’une machine virtuelle sur Hyper-V, vous pouvez choisir une machine virtuelle de première ou de deuxième génération.

##### Création d’un serveur Hyper-V

Ouvrez le Gestionnaire Hyper-V :

![hyperv_manager.png](./screenshots/hyperv_manager.png ':size=500')


Sélectionnez le serveur, puis, dans le menu Actions, choisissez `New Virtual Machine`. Suivez les étapes de l’assistant :

![start_wizard.png](./screenshots/start_wizard.png ':size=500')


1. Indiquez le nom et l’emplacement.
2. Indiquez la génération. 
> [!Note]
> Si cette option n’apparaît pas, cela signifie que vous utilisez une ancienne version d’Hyper-V. Ce n’est pas un problème.

Vous devez choisir entre la génération 1 et la génération 2. Si vous ne savez pas laquelle choisir, vous pouvez consulter cette page : https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/plan/should-i-create-a-generation-1-or-2-virtual-machine-in-hyper-v 

3. Attribuez de la mémoire : 4 Go. Activez l’option « Utiliser la mémoire dynamique pour cette machine virtuelle ».
4. Configurez le réseau : choisissez Nouveau commutateur virtuel.
5. Créez un disque virtuel : au moins 25 Go.
6. Options d’installation : fichier ISO.

![installation_options.png](./screenshots/installation_options.png ':size=500')

7. L’étape suivante présente un récapitulatif des options choisies. Après avoir cliqué sur le bouton « Terminer », l’installation commence comme indiqué [ici](/./devices/networkcontrollerssetup/SettingUpServer.md).

> [!Warning]
> Après l’installation, vous devez redémarrer le serveur. Le message d’erreur suivant peut alors s’afficher :
>![cdrom_mount_failed.png](cdrom_mount_failed.png ':size=500')



<!-- tabs:start -->



###### **Première génération**

Dans la liste des machines virtuelles, choisissez « Paramètres » dans le menu contextuel de la machine virtuelle :

![boot_order_gen1.PNG](./screenshots/boot_order_gen1.PNG ':size=500')

Modifiez **l’ordre de démarrage** pour sélectionner IDE. Dans le menu « Action » de la machine virtuelle, choisissez « Réinitialiser ». 
Le contrôleur réseau devrait alors démarrer.  

 
###### **Deuxième génération**

Dans la liste des machines virtuelles, choisissez « Paramètres » dans le menu contextuel de la machine virtuelle.

1. Choisissez l’option Sécurité et décochez l’option « Activer le démarrage sécurisé ».

![secure_boot.png](./screenshots/secure_boot.png ':size=500')


2. Choisissez l’option Micrologiciel et modifiez **l’ordre de démarrage** pour sélectionner Disque dur. 

![boot_order_gen2.PNG](./screenshots/boot_order_gen2.PNG ':size=500')

Dans le menu « Action » de la machine virtuelle, choisissez « Réinitialiser ». 
Le contrôleur réseau devrait alors démarrer.  

<!-- tabs:end -->
