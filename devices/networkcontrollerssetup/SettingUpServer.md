# Installation of the Network Controller

> [!Note]
> If you intend to install this server virtually, please consider the necessary [BIOS settings](/./advanced/hypervisorinstallation/hypervisorinstallation.md) 

<!-- listed at the bottom of this page. -->


Download the latest version for the 'Network Controller' from https://signal.jimber.io/downloads (no need to log in).

Use the downloaded file to install the Network Controller. 

![nc_install_start.png](/nc_install_start.png ':size=600')

Press Enter.

![installation_server_nc_3.png](/installation_server_nc_3.png ':size=600')

In the window "Guided storage configuration", you can hit 'Done'. You will get an overview of the storage configuration. Here and in the next window, you can also hit 'Done'. 

![installation_server_nc_4.png](/installation_server_nc_4.png ':size=600')



![networkconnections.png](/networkconnections.png ':size=600')



<!-- Then you will see a window with the message “Confirm destructive action”. This is a warning that all data on the used disks will be lost. Only in case of starting this process by mistake, you can choose here for “Continue”. -->

In the next window you will be informed that all data on the used disks may be lost. Choose to “Continue”. 

![installation_server_nc.png](/installation_server_nc.png ':size=600')

The installation process will then begin, which can take several minutes.

![installation_server_nc_2.png](/installation_server_nc_2.png ':size=600')

While the installation is in progress, you can create your Network Controller on https://signal.jimber.io. 
Data you need:
- Your Public IP. Use https://whatismyipaddress.com/ if necessary. 
- Token: copy it!
- Endpoint Address: see next step.

> [!INFO]
> Detailed instructions for the creation of an on-prem Network Controller are available [here](/./devices/networkcontrollers/networkcontrollers.md).

> [!Warning]
> After installation is complete, reboot the system.

![nc_reboot.png](/nc_reboot.png ':size=600')

**Continuation of the installation**

You need this data to proceed (hit "Enter" if necessary):
- username: jimber
- password: jimber


![installation_server_nc_5.png](/installation_server_nc_5.png ':size=600')

On the next screen select option 3 to show the IP configuration of the Network Controller.

![menu.png](./menu.png)

Now use a PC that is on the same network as the Network Controller and go to the shown web URL of option 3 which opens an interface to continue the installation of the Network Controller.

> [!Note]
>Use the displayed IP address to complete the installation of the Network Controller on the `Jimber SASE Platform` by filling it in under the endpoint address.

![ip_configuration.png](./ip_configuration.png ':size=600')


Login with `jimber` as password on the web interface.

![web_login](./web_login.png ':size=600')

Set a new password.

>[!Warning] 
>The new password has to be at least **16** characters long!

![web_new_password.png](./web_new_password.png ':size=600')

Select the right network configuration and then click on ![test_connection.png](./test_connection.png ':size=100'). If successful you can go to the next step.

> [!Note]
> If it fails please check that the Network Controller has an active internet connection and the configuration on the web interface is done correctly.

![web_config.png](./web_config.png ':size=600')

Go to the `Jimber SASE Platform` and copy the token of the Network Controller you just created. You can find the token by editing the Network Controller with the yellow pencil.

![signal_token.png](./signal_token.png ':size=500')

Paste this token into the web configuration of the Network Controller. Then hit next.

![web_token.png](./web_token.png ':size=600')

Please wait a moment while the connection is being tested.

![web_wait.png](./web_wait.png ':size=600')

When the connection is established you will get the following screen:

![web_done.png](./web_done.png ':size=600')

Confirm that your Network Controller is now online on the `Jimber SASE Platform` under the Network Controller page.

![signal_nc_online.png](./signal_nc_online.png ':size=600')


### Hypervisor installation

Hypervisor installation is widely used as iy's a very convenient way of working. The major advantage is that the Network Controller Server can be installed on existing hardware. Therefore, there's no need for a physical device. 

> [!INFO]
> Detailed instructions are available in the Advanced section [here](/./advanced/hypervisorinstallation/hypervisorinstallation.md).
