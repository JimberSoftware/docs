# Installation of the Network Controller Server

**Start of the installation**

Download the latest version for the 'Network Controller Server' from https://signal.jimber.io/downloads (no need to login).

Use the downloaded file to install the Network Controller Server. 
In the next window, click on Enter.

![networkconnections.png](/networkconnections.png ':size=500')

Then you will see a window with the message “Confirm destructive action”. This is a warning that all data on the used disks will be lost. Only in case of starting this process by mistake, you can choose here for “Continue”.

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
- jimbernc login
- The associated password

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


