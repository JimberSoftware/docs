# Network Isolation - NIAC

Network Isolation Access Client (NIAC) is a specialized hardware device engineered to enable secure network connections. It can be integrated with a broad range of devices, including printers, IP cameras, hard drives, and industrial machinery. By serving as a distinct gateway for these devices, NIACs enhance accessibility, ensuring that all data in transit remains encrypted for utmost security.


![niacs.png](/niacfront.png ':size=300')
 

![niacs.png](/niacback.png ':size=300')


At the NIAC, there are 4 ports available: one WAN port for internet connection, two LAN ports, and one USB port. The USB port is currently not supported, so network devices can be connected.
A LAN port is typically used to connect local devices within a network. Typical devices that can be connected to a LAN port include:
- Computers (desktops, laptops)
- Smartphones
- Smart TVs
- Network storage devices (NAS)
- Network printer
- ...

Once a device is connected, you can see the assigned IP address of the device in the overview of the NIACs. In this overview, you can also remove a device and activate or deactivate secure mode. The IP address is assigned via DHCP. 


![niac_overview.png](/niac_overview.png ':size=800')


> [!INFO]
> If you're an end customer interested in integrating NIACs with your devices, please get in touch with your assigned integrator. 


> [!INFO]
> If you're an integrator in need of NIACs, you can either contact your distributor or reach out directly to Jimber via email at security@jimber.io.




## Create NIAC
> [!WARNING]
> Creating a NIAC can only be done by super admins of Jimber.



To create a NIAC into the platform, click on the `Create new` button

![create_new.png](/create_new.png)

prominently located at the upper right corner of the interface.


![create_niac.png](/create_niac.png ':size=500')


You can choose a hostname and it must be a lowercase string. 

<!-- > [!WARNING]
> A device that is connected to a NIAC will not be able to reach the internet unless the NIAC is member of a group of which the Wan Gateway is enabled. For instance: if a NIAC is member of the group WanGateway and in Group Details is Wan Configuration enabled for that group, the connected device will be able to reach the internet. -->

> [!WARNING]
> A device that is connected to a NIAC will not be able to reach the internet unless the NIAC is member of a group of which the Wan Gateway is enabled. For instance: if a NIAC is member of the group WanGateway and in Group Configuration is Wan Gateway enabled for that group, the connected device will be able to reach the internet. -->

![group_config.png](/group_config.png ':size=800')

<!-- ![group_details_niac.png](/group_details_niac.png ':size=600') -->

In the overview, you can find more details about the NIAC by clicking on the corresponding strip.

![niac_details.png](/niac_details.png ':size=600')

By clicking on the red padlock icon you can release one of the devices connected to the NIAC. 

## Edit NIAC
NIACs can be edited by clicking on the yellow pencil icon next to their name 
![icon_edit.png](/icon_edit.png ':size=35').


![edit_niac.png](/edit_niac.png ':size=600x')


## Delete NIAC

NIACs can be deleted by clicking on the red trash bin icon next to their name 
![icon_delete.png](/icon_delete.png ':size=35').

 You will receive a warning before the NIAC is permanently deleted:
 
![delete_niac.png](/delete_niac.png ':size=500x')
