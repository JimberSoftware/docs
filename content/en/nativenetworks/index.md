# ![native_networks](../../images/menu/menu_nativenetworks.png ':size=25') Native Networks

Use **Native Networks** to manage local network segments through an on-premises Jimber Network Controller.

## What Is a Native Network?

A **Native Network** is a network segment that is managed by an on-premises Jimber Network Controller in your local environment. It extends Jimber connectivity, routing, DNS, DHCP, and filtering controls to devices on your physical network, including devices that cannot run the *Jimber SASE Client*.

Native Networks are useful for devices such as printers, cameras, servers, IoT devices, and other unmanaged endpoints that still need controlled network access and consistent policy enforcement.

## Key Features & Capabilities

The Native Networks module includes the following capabilities:

- **Network management** for local network segments.
- **Network interface management** for physical ports and VLAN-based interfaces.
- **Routed network support** for networks that are reachable through another local network.
- **DHCP services** for automatic IP address assignment.
- **Jimber DNS integration** for DNS management on native networks.
- **WAN load balancing and failover** across multiple WAN interfaces.
- **Web filtering** by category and by custom allowlists or blocklists.

## Navigating the Interface

Open *Native Networks* from the left-hand sidebar menu.

The module contains these pages:

- [Networks](./devices/nativenetworks/networks.md) for viewing and managing native networks.
- [Network Interfaces](./devices/nativenetworks/network-interfaces.md) for configuring physical and VLAN-based interfaces.
- [WAN Load Balance](./devices/nativenetworks/wan-load-balance.md) for assigning primary and failover WAN interfaces.
- [DHCP Server](./devices/nativenetworks/dhcp-server.md) for enabling DHCP and setting address ranges per network.
- [Web Filtering](./devices/nativenetworks/web-filtering.md) for applying filtering categories and custom domain rules.

Most list pages include:

- A *Search* field to quickly find items.
- A *Filter* button for advanced filtering.
- A *Refresh* button to reload the page data.
- Pagination controls at the bottom of the table.

## Recommended Setup Order

For a new setup, use this order:

1. Configure [Network Interfaces](./devices/nativenetworks/network-interfaces.md).
2. Create or review [Networks](./devices/nativenetworks/networks.md).
3. Configure [WAN Load Balance](./devices/nativenetworks/wan-load-balance.md) if multiple WAN links are available.
4. Configure [DHCP Server](./devices/nativenetworks/dhcp-server.md) for the required native networks.
5. Apply [Web Filtering](./devices/nativenetworks/web-filtering.md) where needed.

## Summary

Use Native Networks to bring unmanaged or non-client devices under the same Jimber-controlled networking model as the rest of your environment.
