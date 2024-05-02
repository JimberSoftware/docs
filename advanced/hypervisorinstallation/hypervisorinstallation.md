# Hypervisor installation

In many cases, a hypervisor is used. That is indeed a convenient and economical way of working, as there is there is no need for an (expensive) physical device.

Your hardware must meet the following specifications:

Below are the settings that need to be considered.

### VMWARE (ESXI)

> [!INFO]
> When installing the network controller on prem. We need to make sure when installing on ESXI we select BIOS as the firmware type.


![settings-VMWARE.png](settings-VMWARE.png ':size=500')

### Hyper-V

In Hyper-V you have to disable secure boot and choose Legacy instead of EFI.  

![hyperv-secureboot.png](hyperv-secureboot.png ':size=500')



