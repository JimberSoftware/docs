# Installation of the Network Controller

> [!Note]
> If you intend to install this server virtually, please consider the necessary BIOS settings listed at the bottom of this page.


**Start of the installation**

Download the latest version for the 'Network Controller' from https://signal.jimber.io/downloads (no need to login).

Use the downloaded file to install the Network Controller. 

![nc_install_start.png](/nc_install_start.png ':size=500')

Click on Enter.

![installation_server_nc_3.png](/installation_server_nc_3.png ':size=500')

In the window "Guided storage configuration", you can hit 'Done'. You get an overview of the storage configuration. Here and in the next window, you can also choose for 'Done'. 

![installation_server_nc_4.png](/installation_server_nc_4.png ':size=500')


![networkconnections.png](/networkconnections.png ':size=500')



<!-- Then you will see a window with the message “Confirm destructive action”. This is a warning that all data on the used disks will be lost. Only in case of starting this process by mistake, you can choose here for “Continue”. -->

In the next window you have to confirm that all data on the used disks may be lost. Choose here for “Continue”. 

![installation_server_nc.png](/installation_server_nc.png ':size=500')

The installation process will then begin and can take several minutes.

![installation_server_nc_2.png](/installation_server_nc_2.png ':size=500')

While Network Isolation is installing,  you can create your Network Controller on https://signal.jimber.io.  You can find more explanation on how to do so [here](https://docs.jimber.io/#/./devices/networkcontrollers/networkcontrollers).

Data you need:
- Your Public IP. Use https://whatismyipaddress.com/ if necessary. 
- Token: copy it!
- Endpoint Address: see next step.

> [!Warning]
> After installation is complete, reboot the system.

![nc_reboot.png](/nc_reboot.png ':size=500')

**Continuation of the installation**

You need this data to proceed (hit "Enter" if necessary):
- username: jimber
- password: jimber


![installation_server_nc_5.png](/installation_server_nc_5.png ':size=500')

<!-- Now, you get the message “Welcome to Jimber NC”.

![welcome_to_jimber_nc.png](/welcome_to_jimber_nc.png ':size=500')
Choose the second option: “Configure Network Controller” and enter the name of your company. 

Attention, this data is case-sensitive.  -->

After a few minutes you have to enter and re-enter the password for the Jimber-user. This is a password of your choice.

![password_nc.png](/password_nc.png ':size=300')

![nc_success.png](/nc_success.png ':size=300')

Eventually, you will get the screen below.

![nc_start.png](/nc_start.png ':size=500')

Click on the Network Isolation icon in the bottom left corner and choose Network Controller Configuration.

![nc_configuration_2.png](/nc_configuration_2.png ':size=500')


Then, you have to fill in your Network Controller **token** you had to copy in a previous stage, choose your WAN-interface and hit Submit.

The following message will appear:

![settings_update_nc.png](/settings_update_nc.png ':size=300')

Hit the OK button. 

<!-- ![nc_settings_updated.png](/nc_settings_updated.png ':size=400') -->

Click on ![2_computers.png](/2_computers.png ':size=50') in the bottom right corner (next to the date and time display) and choose Connection Information.


![nc_info.png](/nc_info.png ':size=500')

The displayed IP address must be entered as the endpoint address for the on-premise Network Controller. 
 
![nc_endpoint.png](/nc_endpoint.png ':size=500')

Restart the server to complete the installation. You need to re-enter the login and the chosen password.

![re_enter_password.png](re_enter_password.png ':size=500')

Shortly after, there should be a green dot visible next to the created network controller.
![success.png](success.png ':size=500')

### Hypervisor installation

Hypervisor installation is widely used. It's a very convenient way of working. The major advantage is that the network controller server can be installed on existing hardware. Therefore, there's no need for a physical device. 

> [!INFO]
> Comprehensive information can be found [here](/./advanced/hypervisorinstallation/hypervisorinstallation.md).
