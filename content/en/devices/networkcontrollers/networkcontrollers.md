# ![](../../images/menu/menu_networkcontrollers.png ':size=25') Network Controllers
> [!INFO]
> Network Controllers can either be cloud or on-premise.

A network controller is a networking device that forwards data packets between the network. Network controllers play a crucial role in the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***. Isolating a network means restricting its accessibility to only trusted entities and ensuring unauthorized access is prevented. 

> [!INFO]
> A network controller ensures that each part of your network, whether it's a device, a user, or an application cannot access any other part without explicit permission.


![network controllers.png](./screenshots/networkcontrollers.png ':size=800')

### Filter Network Controllers

You can search the list of networkcontrollers using the search box at the top of the page. This helps you quickly find and manage the networkcontroller you're looking for.

Use the search box to enter keywords and filter the networkcontroller list.

Next to the search box, there is a filter icon ![](../../images/icons/icon_filter.png ':size=20'). When clicked, it reveals advanced filtering options where you can define additional conditions based on the following three elements:

- **Property**: A dropdown menu where you choose the field to filter on.
- **Match type**: A dropdown that allows you to select how to match the value (`EQUALS`,`CONTAINS`, or `NOT`).
- **Value**: Enter or select the value to match, depending on the selected property.

![filter_nc.png](./screenshots/filter_nc.png ':size=400')

To add multiple filters you can press the filter icon ![](../../images/icons/icon_filter.png ':size=20') again and then press the `+` button.


> [!TIP]
> You can refresh the list of networkcontrollers by pressing the refresh icon ![](../../images/icons/icon_reload.png ':size=20') at the top of the page.

### Cloud Network Controller (default)

Every company that uses the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_*** will have a cloud network controller **added by default**. This network controller ensures that all the company's devices and users, both external and internal, can access the network securely and consistently. The cloud network controller acts as an entry and exit point for network traffic, ensuring everyone can log in, and access the necessary resources.

### On-Premises Network Controller (optional)

However, there is a potential challenge with the cloud-only approach. Without an on-premise network controller, internal or on-premise traffic will be routed through the internet, which can lead to unnecessary latency.

To address this concern, companies have the option to add an on-premise network controller to their setup. 

> [!INFO]
> This ensures that local traffic remains local and does not get routed to the internet, thereby ensuring faster response times for internal network operations.

##### On-Premises Network Controller Types:
1. **Virtual Appliance**: This is a software-based network controller that can be installed on virtualized infrastructure, making it easier to deploy, scale and manage.
2. **Physical Appliance**: This is a tangible hardware device that is installed in the company's data center or network cabinet.

> [!INFO]
> When an update for a Network Controller is available, a green update icon ![](../../images/icons/icon_update.png ':size=20') will appear. Click the icon to initiate the update.
>
> ![nc_onpremise_update.png](./screenshots/nc_onpremise_update.png ':size=800')

<!-- ## Create on-premise Network Controllers -->
### Create Network Controller

To add a network controller into the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***, click on the `+ Create new` button located at the upper right corner of the interface.

![create_networkcontroller.png](./screenshots/create_networkcontroller.png ':size=400')


Hostname and Endpoint Address are mandatory. The hostname must contain only letters, numbers, and optional hyphens.

> [!INFO]
> Detailed instructions for the installation of an on-prem Network Controller are available [here](/./advanced/networkcontrollerssetup/SettingUpServer.md). 
> The minimum specifications for on-prem Network Controller are:
> 
> **General**:
> - 25GB hard disk
> **For every 50 users:**
> - 2 CPU
> - 4GB RAM

### SSH connection with a Network Controller

![network controllers_1.png](./screenshots/networkcontrollers_1.png ':size=700x40')


By clicking on the padlock icon, you can establish an SSH connection to the network controller. You will then receive a TOTP code, which you can enter in the SSH session.

![totp_nc.png](./screenshots/totp_nc.png ':size=500')


<!-- ### Edit on-premise Network Controller -->
### Edit Network Controller

 A Network Controller can be edited by clicking on the edit icon ![](../../images/icons/icon_edit.png ':size=20') in its row.

![edit_networkcontroller.png](./screenshots/edit_networkcontroller.png ':size=400') 


<!-- ### Delete on-premise Network Controllers -->
### Delete Network Controller

 Network Controllers can be removed by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in their row.

 You will receive a warning before the device is permanently deleted:

![delete_networkcontroller.png](./screenshots/delete_networkcontroller.png ':size=350')
