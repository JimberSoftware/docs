# ![native_networks](../images/menu/menu_wanloadbalance.png ':size=25') WAN Load Balance

Use the *WAN Load Balance* page to decide which WAN interfaces are used during normal operation and which interfaces are kept for failover.

- *Primary Interfaces* are the preferred WAN connections for links that should carry traffic during normal operation.
- *Failover Interfaces* are backup WAN connections that are used when primary connectivity is unavailable.

![wan-load-balance.png](./screenshots/wan-load-balance.png ':size=800')

### Configure WAN Load Balancing


- Open **Native Networks**.
- Select **WAN Load Balance**.
- Select the correct **Network Controller** from the dropdown at the top left of the page.
- In the *Primary Interfaces* section, click **Add WAN Interfaces**.

![add-wan-interface.png](./screenshots/add-wan-interface.png ':size=500')

- Select one or more WAN interfaces with the checkboxes.
- Click *Save*.
- Follow the same procedure for the **Failover Interfaces**

>[!Attention]
>Don't forget to click *Submit* on the main page!

### Update WAN Interfaces

Updating WAN Interfaces is done in the same way as configuring: 

- Open **Native Networks**.
- Select **WAN Load Balance**.
- Select the correct **Network Controller** from the dropdown at the top left of the page.
- Adjust the selected interfaces by opening the *Add WAN Interfaces* window in either section.

>[!Attention]
>Don't forget to click *Save* in the current window and *Submit* on the main page!

<!-- 1. Return to *WAN Load Balance*.
2. Select the same *Network Controller*.
3. Open the *Add WAN Interfaces* window in either section.
4. Adjust the selected interfaces.
5. Click *Save*.
6. Click *Submit*. -->

### Remove WAN Interfaces

To remove a WAN Interface 

- Open **Native Networks**.
- Select **WAN Load Balance**.
- Select the correct **Network Controller** from the dropdown at the top left of the page.
- Open the *Add WAN Interfaces* window in either section.
- Click the *X* button next to the interface name

![remove-wan-interface.png](./screenshots/remove-wan-interface.png ':size=500')

>[!Attention]
>Don't forget to click *Save* in the current window and *Submit* on the main page!


<!-- 1. Return to *WAN Load Balance*.
2. Select the same *Network Controller*.
3. Click the *X* button next to the interface name in the *Primary Interfaces* or *Failover Interfaces* section.
4. Click *Submit*. -->

> [!IMPORTANT]
> At least one primary interface is required before you can submit the changes.

![one_primary_interface.png](./screenshots/one_primary_interface.png ':size=500')


> [!NOTE]
> The default WAN for your Network Controller is automatically selected as the first primary WAN interface. 
<!-- You can change it by clicking the edit icon in the *Primary Interfaces* section. -->

## Summary

Use *WAN Load Balance* to improve availability and distribute outbound traffic across the WAN interfaces assigned to an on-premises Network Controller.
