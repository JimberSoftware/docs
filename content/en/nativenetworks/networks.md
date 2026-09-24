# ![native_networks](../images/menu/menu_nativenetworks.png ':size=25') Networks

Use the *Networks* page to view existing networks and manage both direct and routed native networks.

### Networks List

![networks.png](./screenshots/networks.png ':size=800')

The *Networks* list shows Name, Network Controller, Network Address, DHCP Enabled, and Type.


### Filter Networks

You can search the list of networks using the search box at the top of the page. This helps you quickly find and manage the network you're looking for.

Use the search box to enter keywords and filter the network list.

Next to the search box, there is a filter icon. When clicked, it reveals advanced filtering options where you can define additional conditions based on the following three elements:

- **Property**: A dropdown menu where you choose the field to filter on.
- **Match type**: A dropdown that allows you to select how to match the value (`EQUALS`, `CONTAINS`, or `NOT`).
- **Value**: Enter or select the value to match, depending on the selected property.


<!-- You can use the search field, filter button, refresh button, and pagination controls to find the network you need. -->

![networks-filter.png](./screenshots/networks-filter.png ':size=500')

> [!TIP]
> You can refresh the list of users by pressing the refresh icon ![](../../images/icons/icon_reload.png ':size=20') at the top of the page

## Routed Networks

Clicking `+ Create new` opens the *Create Routed Network* window. 
Choose the type of network you want to create: **native** or **virtual**.

<!-- tabs:start -->

### **Create a Routed Native Network**


>[!NOTE]
>Use this when the network you want to add is reachable through an existing direct native network.

![create-routed-network.png](./screenshots/create-routed-network.png ':size=350')


 In the *Create Routed Network* window, complete the fields:

 - **Name**: Enter a clear name for the network.
 - **Network Controller**: Select the controller that will manage the network.
 - **Native Network (Direct)**: Select the directly connected native network that provides access to this routed network.
 - **Network Address (CIDR)**: Enter the routed network address in CIDR format.
 - **Next Hop**: Enter the gateway IP address that leads to the routed network.

> [!IMPORTANT]
> The *Next Hop* address must be reachable through the selected *Native Network (Direct)*.

> [!WARNING]
> Make sure the network address and next hop match your existing routing design to avoid connectivity issues.


### **Create a Routed Virtual Network**

![create-virtual-network.png](./screenshots/create-virtual_network.png ':size=350')

In the *Create Routed Network* window, complete the fields:

 - **Virtual Interface**: Select the virtual interface that will manage the network.
 - **Network Address (CIDR)**: Enter the routed network address in CIDR format.
 

<!-- tabs:end -->

---

#### Details of a Native Network

 Clicking on the end of the corresponding strip of a native network opens a detailed view with additional information about the installed policies.

![details_native_networks.png](./screenshots/details_native_networks.png ':size=700')


#### Edit a Routed Native Network

Routed Native Networks can be edited by clicking on the edit icon ![](../../images/icons/icon_edit.png ':size=20') in their row.

![edit_routed_native_network.png](./screenshots/edit_routed_native_network.png ':size=600')

All options are the same as when creating a Routed Native Network.


<!-- 1. Open *Networks*.
2. Find the routed native network in the table.
3. Click the edit icon in the *Actions* column.
4. Update the same fields that are available in the create window.
5. Save your changes. -->

#### Delete a Routed Native Network

 Routed Native Networks can be deleted by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in their row.


 > [!WARNING]
> This process is irreversible.
 
 You will receive a warning before the network is permanently deleted:

  ![deleting_routed_network.png](./screenshots/deleting_routed_network.png ':size=300')

### Direct Native Networks

Direct native networks are attached to a network interface and provide the base connectivity that routed native networks can use.

#### Edit a Direct Native Network


Direct Native Networks can be edited by clicking on the edit icon ![](../../images/icons/icon_edit.png ':size=20') in their row.

![edit-network.png](./screenshots/edit-network.png ':size=600')

You can change the name of the Direct Native Network. 

<!-- 1. Open *Networks*.
2. Find the direct native network in the table.
3. Click the edit icon in the *Actions* column.
4. If the direct native network is a *LAN* network, enable or disable internet access using the *Allow Internet* toggle.
5. Save your changes. -->

> [!NOTE]
> If the direct native network is a *LAN* network, you can manage internet access with the *Allow Internet* toggle. For *WAN* direct native networks, this toggle is not shown.

#### Remove a Direct Native Network

To remove a direct native network, delete the related network interface.

## Summary

Use the *Networks* page to manage the logical network segments that the Network Controller should route and maintain, including both **direct** and **routed** Native Networks.
