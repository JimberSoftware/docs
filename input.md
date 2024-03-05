# Network Controllers
> Network Controllers can either be cloud or on-premise.
{.is-info}


A network controller is a networking device that forwards data packets between the network. Network controllers play a crucial role in Network Isolation. Isolating a network means restricting its accessibility to only trusted entities and ensuring unauthorized access is prevented. 
> It ensures that each part of your network, whether it's a device, user, or application, cannot access any other part without explicit permission.
{.is-success}


## Cloud Network Controller (default)

Every company that uses Network Isolation will have a cloud network controller **added by default**. This network controller ensures that all the company's devices and users, both external and internal, can access the network securely and consistently. The cloud network controller acts as an entry and exit point for network traffic, ensuring everyone can log in and access the necessary resources.

![networkcontrollers.png](/networkisolation/networkcontrollers.png =800x){.decor-shadow .radius-5}

### On-Premise Network Controller (optional)

However, there is a potential challenge with the cloud-only approach. Without an on-premise network controller, internal or on-premise traffic will be routed through the internet, which can lead to unnecessary latency.

To address this concern, companies have the option to add an on-premise network controller to their setup. 
> This ensures that local traffic remains local and does not get routed to the internet, thereby ensuring faster response times for internal network operations.
{.is-success}


### On-Premise Network controller Types:
1. **Virtual Appliance**: This is a software-based network controller that can be installed on virtualized infrastructure, making it easier to deploy, scale and manage.
2. **Physical Appliance**: This is a tangible hardware device that is installed in the company's data center or networking closet.

## Create on-premise Network Controller

To add a network controller into the platform, click on the `Create new` button
![create_new.png](/create_new.png){ .radius-5}
prominently located at the upper right corner of the interface.

![create_networkcontroller.png](/networkisolation/create_networkcontroller.png =800x){.decor-shadow .radius-5}

> Hostname, Endpoint Address and Public IP are mandatory.
{.is-info}

## Edit on-premise Network Controller

 Network Controllers can be edited by clicking on the yellow pencil icon next to their name ![pencil_2.png](/pencil_2.png){.radius-5}.

![edit_networkcontroller.png](/networkisolation/edit_networkcontroller.png =800x){.decor-shadow .radius-5}

## Delete on-premise Network Controller

 Network Controllers can be removed by clicking on the red trash bin icon next to their name. ![recycle_bin.png](/recycle_bin.png){.radius-5}
 
 

![delete_networkcontroller.png](/networkisolation/delete_networkcontroller.png =600x){.decor-shadow .radius-5}

## On-premise Network Controller minimum specifications

**General**:
- 20GB hard disk

**For each 50 users:**
- 1 CPU
- 1024MB RAM,

