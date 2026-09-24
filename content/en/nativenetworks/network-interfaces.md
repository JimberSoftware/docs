# ![native_networks](../images/menu/menu_networkinterfaces.png ':size=25') Network Interfaces

Use the *Network Interfaces* page to connect physical ports and VLANs to your native networks.

### Network Interfaces List

You can search the list of Network Interfaces using the search box at the top of the page.

![network-interfaces.png](./screenshots/network-interfaces.png ':size=700')

The table includes the interface description, WAN or LAN role, port, network controller, address, and addressing mode.

### Filter Network Interfaces

Use the search box to enter keywords and filter the Network Interfaces list.

Next to the search box, there is a filter icon ![](../../images/icons/icon_filter.png ':size=20'). When clicked, it reveals advanced filtering options where you can define additional conditions based on the following three elements:

- **Property**: A dropdown menu where you choose the field to filter on.
- **Match type**: A dropdown that allows you to select how to match the value (`EQUALS`, `CONTAINS`, or `NOT`).
- **Value**: Enter or select the value to match, depending on the selected property.

![filter_native_networks.png](./screenshots/filter_native_networks.png ':size=500')

To add multiple filters you can press the filter icon ![](../../images/icons/icon_filter.png ':size=20') again and then press the `+` button.

Active filters appear at the top of the page:

![active_filters.png](./screenshots/active_filters.png ':size=700')

> [!TIP]
> You can refresh the list of users by pressing the refresh icon ![](../../images/icons/icon_reload.png ':size=20') at the top of the page.


### Create a Network Interface

To create a new Network Interface into the platform, click on the `+ Create new` button located at the upper right corner of the interface.

![create-network-interface.png](./screenshots/create-network-interface.png ':size=700')

On the *Create Network Interface* page, complete the *Interface* section:

- **Description**: Enter a clear label for the interface.
- **VLAN**: Choose *Untagged* for default traffic on the port, or **Tagged** for traffic on a specific VLAN.
    -   If you select *Tagged*, enter the *VLAN ID*.
- **Network Controller**: Select the on-premises Network Controller that will manage the interface.
- **WAN/LAN**: Choose whether the interface is used for WAN or LAN traffic.
- **Port**: Select the physical port on the Network Controller.
- **DHCP/Static**: Choose how the interface gets its IP address.
- If you selected **Static**, complete the *Static* section:
    - **IP Address (CIDR)**: Enter the interface IP address in CIDR format, for example *192.168.1.1/24*.
    - **Gateway IP Address**: Enter the gateway IP address.
- If you selected **DHCP**, the static section is not available:


 ![static_not_available.png](./screenshots/static_not_available.png ':size=700')


> [!NOTE]
> Don't forget to click on **Submit** 



### Update a Network Interface

 Network Interfaces can be edited by clicking on the edit icon ![](../../images/icons/icon_edit.png ':size=20') in their row.

![edit-network-interfaces.png](./screenshots/edit-network-interfaces.png ':size=700')

All options are the same as when creating a Network Interface.


> [!IMPORTANT]
> If you change the *IP Address (CIDR)* or *Gateway IP Address*, the DHCP server for that network will be disabled automatically to prevent an invalid configuration. You can enable it again later from the [DHCP Server](./dhcp-server.md) page.

### Delete a Network Interface

Network Interfaces can be deleted by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in their row.

You will receive a warning before the user is permanently deleted:

![delete-network-interface.png](./screenshots/delete-network-interface.png ':size=400')


> [!IMPORTANT]
> Deleting a network interface also deletes the related network. This action cannot be undone.

> [!WARNING]
> Be careful when changing or removing active interfaces, because these settings affect live network connectivity.


### VLAN and Addressing Guidance

- Use *Untagged* when the interface should carry the default traffic for a port.
- Use *Tagged* when the interface should be attached to a specific VLAN.
- Use *DHCP* when the interface should receive its address automatically.
- Use *Static* when the interface must use a fixed IP configuration.

## Summary

Use the *Network Interfaces* page to define how WAN and LAN traffic enters and leaves the on-premises Network Controller.
