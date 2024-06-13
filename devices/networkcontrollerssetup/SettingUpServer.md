# Installation of the Network Controller

> [!Note]
> If you intend to install this server virtually, please consider the necessary BIOS settings listed at the bottom of this page.


**Start of the installation**

Download the latest version for the 'Network Controller' from https://signal.jimber.io/downloads (no need to login).

Use the downloaded file to install the Network Controller. 
In the next window, click on Enter.

![networkconnections.png](/networkconnections.png ':size=500')

<!-- Then you will see a window with the message “Confirm destructive action”. This is a warning that all data on the used disks will be lost. Only in case of starting this process by mistake, you can choose here for “Continue”. -->

In the next window you have to confirm that all data on the used disks may be lost. You can choose here for “Continue”. 

![installation_server_nc.png](/installation_server_nc.png ':size=500')

The installation process will then begin and can take several minutes.

![installation_server_nc_2.png](/installation_server_nc_2.png ':size=500')

While Network Isolation is installing,  you can create your Network Controller on https://signal.jimber.io.  You can find more explanation on how to do so at https://docs.jimber.io/#/./devices/networkcontrollers/networkcontrollers.

Data you need:
- Your Public IP. Use https://whatismyipaddress.com/ if necessary. 
- Token: copy it!
- Endpoint Address: see next step.

> [!WARNING]
> After installation is complete, reboot the system.

**Continuation of the installation**

You need this data to proceed:
- username: jimber
- password: jimber

Now, you get the message “Welcome to Jimber NC”.

![welcome_to_jimber_nc.png](/welcome_to_jimber_nc.png ':size=500')

Choose the second option: “Configure Network Controller” and enter the name of your company. 

Attention, this data is case-sensitive. 

Then, you have to fill in your Network Controller **token** you had to copy in a previous stage and hit Enter.
In the next window you can also hit Enter. 

![select_wan.png](/select_wan.png ':size=500')


Check your WAN IP address. It should be correct!

![check_wan.png](/check_wan.png ':size=500')

**Completing the installation**

The service needs to be restarted now:

![restart_service.png](restart_service.png ':size=500')

![endpoint_address.png](endpoint_address.png ':size=500')


Endpoint Address: choose shell, and in the started console, you enter: ip a

Then Exit to leave the console and restart service. 

>[!NOTE]
>Now you can complete the creation of the Network Controller. 

Shortly after, there should be a green dot visible next to the created network controller.
![success.png](success.png ':size=800')

### Hypervisor installation

Hypervisor installation is widely used. It's a very convenient way of working. The major advantage is that the network controller server can be installed on existing hardware. Therefore, there's no need for a physical device. However, there are some settings you need to consider.

 
#### VMware ESXi

When installing the network controller on-prem on ESXi, you need to make sure to select BIOS as the firmware type:


![esxi_specs.png](esxi_specs.png ':size=700')


#### Hyper-V

When installing the network controller on-prem on Hyper-V, you need to choose legacy boot mode instead of EFI mode.This can be done in the settings of the virtual machine.

##### Installing Hyper-V on a server (standard installation)

In the Server Manager, choose Add Roles and Features on the tab Manage. 

![server_manager.png](server_manager_2.png ':size=500')

In the next screen 'Before you begin' click Next.
Then you have to select the installation type. Here you can choose Role-based or feature installation. 
In the following step you have to choose the destination server, mostly that will be a server from te server pool. Choose the right server. 

Choose the Server Role Hyper-V in the next step, add the required features. That will include .Net Framework 4.8 Features, if not already installed. 
After that you can choose next until you have to confirm installation selection. By clicking on Install Hyper-V will install on your server.  
After installation a restart is required. 

##### Creating a Hyper-V server

Open the Hyper-V manager:

![hyperv_manager.png](hyperv_manager.png ':size=500')

Select the server and in the column Actions choose `New Virtual Machine`. 

