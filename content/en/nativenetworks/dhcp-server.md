# ![native_networks](../images/menu/menu_dhcpserver.png ':size=25') DHCP Server

Use the *DHCP Server* page to configure DHCP and DNS settings for a native network.

The page lets you select a native network, enable or disable DHCP, define the IP address range for DHCP clients, configure the gateway, and choose between *Jimber* and *Custom* DNS.

### Configure DHCP Server 

![dhcp-server.png](./screenshots/dhcp-server.png ':size=700')

- Choose a **Native Network** from the dropdown at the top left of the page.
- In the **DHCP Configuration** card
  -  Enable the **DHCP Master Toggle** if you want clients on that network to automatically receive IP addresses via DHCP.
  -  Review the *Interface* field. This field is read-only and shows the assigned interface and its CIDR block.
-  Configure the **Range**:
    - Enter the start IP address.
    - Enter the end IP address.
-  Enter the **Gateway IP Address**.
- Configure DNS:
    - Jimber DNS: no further settings needed.
    - Custom DNS:
        - Enter the required DNS server IP address
        - To add another DNS server, click `+ Add IP Address`.

![dhcp-server-custom-dns.png](./screenshots/dhcp-server-custom-dns.png ':size=500')

>[!ATTENTION]
>Don't forget to click `Submit` to implement the changes (button in the upper right corner).


> [!TIP]
> Use an IP range that fits inside the selected network and does not overlap with addresses reserved for gateways, servers, or other statically assigned devices.

<!-- ### Configure DNS

Use the *DNS Configuration* card to choose how DNS should be provided to DHCP clients.



#### Use Jimber DNS

1. Select the required *Native Network*.
2. In the *DNS Configuration* card, choose *Jimber* from the *DNS Selection* dropdown.
3. Review the message shown on the page: *Change DNS to 'Custom' to configure IP Addresses*.
4. Click *Submit*.

#### Use Custom DNS Servers

![dhcp-server-custom-dns.png](./screenshots/dhcp-server-custom-dns.png ':size=500')

1. Select the required *Native Network*.
2. In the *DNS Configuration* card, choose *Custom* from the *DNS Selection* dropdown.
3. In the *IP Addresses* section, enter the required DNS server IP address.
4. To add another DNS server, click *+ Add IP Address*.
5. To remove a DNS server, click the delete icon next to the IP address.
6. Click *Submit*. -->

### Clear or Submit Changes

The top right of the page contains two action buttons:

- Use **Clear changes** if you want to discard edits.
- **Submit** saves the current configuration.

### Disable DHCP

When trying disabling DHCP for one of the Native Networks, you get a warning: 

![disabling_DHCP.png](./screenshots/disabling_DHCP.png ':size=400')

To effectively disable DHCP, enter the name of the Native Network and hit the `Disable` button.

## Summary

Use the *DHCP Server* page to configure IP address assignment and DNS settings for devices connected to a native network.
