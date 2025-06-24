# ![](../../images/menu/menu_niacs.png ':size=25') Network Isolation Access Client - NIAC

A Network Isolation Access Client (NIAC) is a specialized hardware device engineered to enable secure network connections. It can be integrated with a broad range of devices, including printers, IP cameras, hard drives and industrial machinery. By serving as a distinct gateway for these devices, NIACs enhance accessibility, ensuring that all data in transit remains encrypted for utmost security.


![niacs.png](./screenshots/niacfront.png ':size=300')
 

![niacs.png](./screenshots/niacback.png ':size=300')


A NIAC has four available ports: one WAN port for internet connection, two LAN ports and one USB port. The USB port is currently not supported, so only network devices can be connected.
A LAN port is typically used to connect local devices within a network. Typical devices that can be connected to a LAN port include:
- Computers (desktops, laptops)
- Smart TVs
- Network storage devices (NAS)
- Network printers
- ...

Once a device is connected, you can see the via DHCP assigned IP address of the device in the overview of the NIAC. In this overview you can also remove a device and activate or deactivate secure mode. 


![niac_overview.png](./screenshots/niac_overview.png ':size=800')

> [!INFO]
> If you're an end customer interested in integrating NIACs with your devices, please get in touch with your assigned integrator. 

> [!INFO]
> If you're an integrator in need of NIACs, you can either contact your distributor or reach out directly to Jimber via email at security@jimber.io.

### Create NIAC
> [!WARNING]
> Creating a NIAC can only be done by super admins of Jimber.

To create a NIAC into the platform, click on the `+ Create new` button located at the upper right corner of the interface.


![create_niac.png](./screenshots/create_niac.png ':size=500')

> [!INFO]
> The hostname must be a lowercase string.

<!-- > [!WARNING]
> A device that is connected to a NIAC will not be able to reach the internet unless the NIAC is member of a group of which the Wan Gateway is enabled. For instance: if a NIAC is member of the group WanGateway and in Group Details is Wan Configuration enabled for that group, the connected device will be able to reach the internet. -->

> [!WARNING]
> A device that is connected to a NIAC will not be able to reach the internet unless the NIAC is a member of a group for which the WAN Gateway is enabled. For instance: if a NIAC is a member of the group WanGateway and WAN GATEWAY is enabled for that group in Group Configuration, then the connected device will be able to reach the internet.

![group_config.png](./screenshots/group_config.png ':size=800')

<!-- ![group_details_niac.png](/group_details_niac.png ':size=600') -->

### Inspect NIAC

Clicking on the corresponding strip of the NIAC opens a new window with more details:

![niac_details.png](./screenshots/niac_details.png ':size=600')

You can release one of the devices connected to the NIAC by clicking on the red padlock icon ![](../../images/icons/icon_lock.png ':size=20') in their row.

### Edit NIAC

NIACs can be edited by clicking on the edit icon ![](../../images/icons/icon_edit.png ':size=20') in their row.

![edit_niac.png](./screenshots/edit_niac.png ':size=600x')

### Delete NIAC

NIACs can be deleted by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in their row.

You will receive a warning before the NIAC is permanently deleted:
 
![delete_niac.png](./screenshots/delete_niac.png ':size=500x')
