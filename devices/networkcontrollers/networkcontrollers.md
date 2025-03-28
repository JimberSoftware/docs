# Network Controllers
> [!INFO]
> Network Controllers can either be cloud or on-premise.



A network controller is a networking device that forwards data packets between the network. Network controllers play a crucial role in Network Isolation. Isolating a network means restricting its accessibility to only trusted entities and ensuring unauthorized access is prevented. 

> [!INFO]
> It ensures that each part of your network, whether it's a device, user, or application, cannot access any other part without explicit permission.



## Cloud Network Controller (default)

Every company that uses Network Isolation will have a cloud network controller **added by default**. This network controller ensures that all the company's devices and users, both external and internal, can access the network securely and consistently. The cloud network controller acts as an entry and exit point for network traffic, ensuring everyone can log in and access the necessary resources.


![network controllers.png](/networkcontrollers.png ':size=800')


### On-Premise Network Controller (optional)

However, there is a potential challenge with the cloud-only approach. Without an on-premise network controller, internal or on-premise traffic will be routed through the internet, which can lead to unnecessary latency.

To address this concern, companies have the option to add an on-premise network controller to their setup. 

> [!INFO]
> This ensures that local traffic remains local and does not get routed to the internet, thereby ensuring faster response times for internal network operations.



### On-Premise Network Controller Types:
1. **Virtual Appliance**: This is a software-based network controller that can be installed on virtualized infrastructure, making it easier to deploy, scale and manage.
2. **Physical Appliance**: This is a tangible hardware device that is installed in the company's data center or networking closet.

## Create on-premise Network Controller

To add a network controller into the platform, click on the `Create new` button

![create_new.png](/create_new.png)

prominently located at the upper right corner of the interface.


![create_networkcontroller.png](/create_networkcontroller.png ':size=500')

> [!WARNING]
> Hostname, Endpoint Address and Public IP are mandatory.


## Edit on-premise Network Controller

 Network Controllers can be edited by clicking on the yellow pencil icon next to their name 
![icon_edit.png](/icon_edit.png ':size=35').


![edit_networkcontroller.png](/edit_networkcontroller.png ':size=500')


## Delete on-premise Network Controller

 Network Controllers can be removed by clicking on the red trash bin icon next to their name 
![icon_delete.png](/icon_delete.png ':size=35').

 
 

![delete_networkcontroller.png](/delete_networkcontroller.png ':size=500')


## On-premise Network Controller minimum specifications

**General**:
- 25GB hard disk

**For each 50 users:**
- 2 CPU
- 4GB RAM

