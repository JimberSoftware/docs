# ![](../../images/menu/menu_networkcontrollers.png ':size=25') Network Controllers
> [!INFO]
> Network Controllers can either be cloud or on-premise.

A network controller is a networking device that forwards data packets between the network. Network controllers play a crucial role in the `Jimber SASE Platform`. Isolating a network means restricting its accessibility to only trusted entities and ensuring unauthorized access is prevented. 

> [!INFO]
> It ensures that each part of your network, whether it's a device, user, or application, cannot access any other part without explicit permission.


![network controllers.png](./screenshots/networkcontrollers.png ':size=800')

### Cloud Network Controller (default)

Every company that uses the `Jimber SASE Platform` will have a cloud network controller **added by default**. This network controller ensures that all the company's devices and users, both external and internal, can access the network securely and consistently. The cloud network controller acts as an entry and exit point for network traffic, ensuring everyone can log in and access the necessary resources.

### On-Premise Network Controller (optional)

However, there is a potential challenge with the cloud-only approach. Without an on-premise network controller, internal or on-premise traffic will be routed through the internet, which can lead to unnecessary latency.

To address this concern, companies have the option to add an on-premise network controller to their setup. 

> [!INFO]
> This ensures that local traffic remains local and does not get routed to the internet, thereby ensuring faster response times for internal network operations.

### On-Premise Network Controller Types:
1. **Virtual Appliance**: This is a software-based network controller that can be installed on virtualized infrastructure, making it easier to deploy, scale and manage.
2. **Physical Appliance**: This is a tangible hardware device that is installed in the company's data center or network closet.

> [!INFO]
> When an update for a Network Controller is available, a green update icon ![](../../images/icons/icon_update.png ':size=20') will appear. Click the icon to initiate the update.
>
> ![nc_onpremise_update.png](./screenshots/nc_onpremise_update.png ':size=800')

## Create on-premise Network Controllers

To add a network controller into the `Jimber SASE Platform`, click on the `+ Create new` button located at the upper right corner of the interface.

![create_networkcontroller.png](./screenshots/create_networkcontroller.png ':size=500')

> [!WARNING]
> Hostname, Endpoint Address and Public IP are mandatory.

> [!INFO]
> Detailed instructions for the installation of an on-prem Network Controller are available [here](../../advanced/networkcontrollerssetup/SettingUpServer.md). 
> The minimum specifications for on-prem Network Controllers are:
> 
> **General**:
> - 25GB hard disk
> **For every 50 users:**
> - 2 CPU
> - 4GB RAM

### Edit on-premise Network Controllers

 Network Controllers can be edited by clicking on the edit icon ![](../../images/icons/icon_edit.png ':size=20') in their row.

![edit_networkcontroller.png](./screenshots/edit_networkcontroller.png ':size=500')


### Delete on-premise Network Controllers

 Network Controllers can be removed by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in their row.

 You will receive a warning before the device is permanently deleted:

![delete_networkcontroller.png](./screenshots/delete_networkcontroller.png ':size=500')

