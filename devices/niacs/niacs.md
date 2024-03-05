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

Once a device is connected, you can see the assigned IP address of the device in the overview of the NIACs. In this overview, you can also remove a device and activate or deactivate secure mode.


![niac_overview.png](/niac_overview.png ':size=920x')


> [!INFO]
> If you're an end customer interested in integrating NIACs with your devices, please get in touch with your assigned integrator. 


> [!INFO]
> If you're an integrator in need of NIACs, you can either contact your distributor or reach out directly to Jimber via email at security@jimber.io.




## Create a NIAC
> Creating a NIAC can only be done by super admins of Jimber.



To create a NIAC into the platform, click on the `Create new` button

![create_new.png](/create_new.png)

prominently located at the upper right corner of the interface.


![create_niac.png](/create_niac.png ':size=600x')


You can choose a hostname. The initial selected primary group is 'Servers' and 'Secure mode' is selected. Both can be changed. 

> [!WARNING]
> A device that is connected to a NIAC will not be able to reach the internet unless "Allow WAN" is enabled for the NIAC.


## Edit a NIAC
NIACs can be edited by clicking on the yellow pencil icon next to their name 
![pencil_2.png](/pencil_2.png)
.


![edit_niac.png](/edit_niac.png ':size=600x')


## Remove a NIAC

NIACs can be removed by clicking on the red trash bin icon next to their name 
![recycle_bin.png](/recycle_bin.png)
.

 You will receive a warning before the NIAC is permanently deleted:
 
![delete_niac.png](/delete_niac.png ':size=500x')
