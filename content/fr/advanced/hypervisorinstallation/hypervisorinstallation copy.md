### Installation de l’hyperviseur

Les paramètres matériels minimum suivants doivent être définis :    
  - 2 cœurs
  - 4 Go de RAM
  - 25 Go d’espace disque
   

#### VMware ESXi

Lors de l’installation du contrôleur réseau sur site sur ESXi, veillez à sélectionner BIOS comme type de micrologiciel :


![esxi_specs.png](esxi_specs.png ':size=700')


#### Hyper-V

Lors de l’installation d’une machine virtuelle sur Hyper-V, vous pouvez choisir une machine virtuelle de première ou de deuxième génération.

##### Création d’un serveur Hyper-V

Ouvrez le Gestionnaire Hyper-V :

![hyperv_manager.png](hyperv_manager.png ':size=500')


Sélectionnez le serveur et, dans le menu Actions, choisissez `New Virtual Machine`. Suivez les étapes de l’Assistant :

![start_wizard.png](start_wizard.png ':size=500')


1. Indiquez le nom et l’emplacement.
2. Indiquez la génération. 
> [!Note]
> Si cette option n’apparaît pas, cela signifie que vous disposez d’une ancienne version d’Hyper-V. Ce n’est pas un problème.

Vous devez choisir entre la génération 1 et la génération 2. Si vous ne savez pas laquelle choisir, vous pouvez consulter cette page : https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/plan/should-i-create-a-generation-1-or-2-virtual-machine-in-hyper-v 

3. Attribuez de la mémoire : 4 Go. Activez l’option « Utiliser la mémoire dynamique pour cette machine virtuelle ».
4. Configurez le réseau : choisissez Nouveau commutateur virtuel.
5. Créez un disque virtuel : au moins 25 Go.
6. Options d’installation : fichier ISO.

![installation_options.png](installation_options.png ':size=500')
7. L’étape suivante présente un récapitulatif des options choisies. Après avoir cliqué sur le bouton « Terminer », l’installation commence comme décrit ci-dessus.

> [!Warning]
> Après l’installation, vous devez redémarrer le serveur et le message d’erreur suivant peut s’afficher :
>![cdrom_mount_failed.png](cdrom_mount_failed.png ':size=500')



<!-- tabs:start -->



###### **Première génération**

Dans la liste des machines virtuelles, choisissez « Paramètres » dans le menu rapide de la machine virtuelle :

![boot_order_gen1.PNG](boot_order_gen1.PNG ':size=500')

Modifiez l’**ordre de démarrage** pour sélectionner IDE. Dans le menu « Action » de la machine virtuelle, choisissez « Réinitialiser ». 
Le contrôleur réseau devrait maintenant démarrer.  

 
###### **Deuxième génération**

Dans la liste des machines virtuelles, choisissez « Paramètres » dans le menu rapide de la machine virtuelle.

1. Choisissez l’option Sécurité et décochez l’option « Activer le démarrage sécurisé ».

![secure_boot.png](secure_boot.png ':size=500')


2. Choisissez l’option Micrologiciel et modifiez l’**ordre de démarrage** pour sélectionner Disque dur. 

![boot_order_gen2.PNG](boot_order_gen2.PNG ':size=500')

Dans le menu « Action » de la machine virtuelle, choisissez « Réinitialiser ». 
Le contrôleur réseau devrait maintenant démarrer.  

<!-- tabs:end -->
