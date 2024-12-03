### Hypervisor installation

Hypervisor installation is widely used. It's a very convenient way of working. The major advantage is that the network controller server can be installed on existing hardware. Therefore, there's no need for a physical device. However, there are some settings you need to consider.

The following minimum hardware settings must be set:    
  - 2 cores
  - 4 GB RAM
  - 25 GB of hard disk space
   

#### VMware ESXi

When installing the network controller on-prem on ESXi, you need to make sure to select BIOS as the firmware type:


![esxi_specs.png](esxi_specs.png ':size=700')


#### Hyper-V

When installing a virtual machine on Hyper-V, you can choose for a virtual machine of the first generation or a virtual machine of the second generation.

##### Creating a Hyper-V server

Open the Hyper-V manager:

![hyperv_manager.png](hyperv_manager.png ':size=500')


Select the server and in the menu-item Actions choose `New Virtual Machine`. Follow the steps of the Wizard:

![start_wizard.png](start_wizard.png ':size=500')


1. Specify name and location
2. Specify generation. 
> [!Note]
> If you don't see this option, it means you have an older version of Hyper-V. That is no problem.

Here you have to choose between Generation 1 or Generation 2. If you are not sure which one to choose, you can consult this page: https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/plan/should-i-create-a-generation-1-or-2-virtual-machine-in-hyper-v 

3. Assign memory: 4 GB. Activate the option 'Use Dynamic Memory for this virtual machine'.
4. Configure network: choose for New Virtual Switch.
5. Create virtual disk: at least 25 GB.
6. Installation options: iso-file.

![installation_options.png](installation_options.png ':size=500')

7. Next step is a summary of the chosen options. After hitting the 'Finish'-button the installation begins as described above.

> [!Warning]
> After installation you have to restart the server and you could face this error message:
>![cdrom_mount_failed.png](cdrom_mount_failed.png ':size=500')



<!-- tabs:start -->



###### **First generation**

In the list of Virtual Machines, choose in the quick menu of the virtual machine 'Settings':

![boot_order_gen1.PNG](boot_order_gen1.PNG ':size=500')

Change the **startup order** to IDE. In the 'Action'-menu of the virtual machine choose 'Reset'. 
Now the Network Controller should start.  

 
###### **Second generation**

In the list of Virtual Machines, choose in the quick menu of the virtual machine 'Settings'.

1. Choose the option Security and  uncheck the option 'Enable Secure Boot'.

![secure_boot.png](secure_boot.png ':size=500')


2. Choose the option Firmware and change the **boot order** to Hard Drive. 

![boot_order_gen2.PNG](boot_order_gen2.PNG ':size=500')

In the 'Action'-menu of the virtual machine choose 'Reset'. 
Now the Network Controller should start.  

<!-- tabs:end -->