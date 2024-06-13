# Group configuration
In the group configuration you can define different behavior per group. Options can be enabled or disabled, or custom properties for specific options can be set.

## WAN
To configure WAN settings:

1. **WAN Gateway**

When enabled, it forces clients to navigate the internet via the cloud or on-premise router. If this option is turned off, clients will access the internet using their own internet connection. 

This feature can be turned on to chain the networkcontroller to existing firewall / proxy infrastructure or to be sure that all SaaS applications are accessed from the same IP. SaaS applications can be configured to only allow SaaS from one IP, this way you can make these applications only accessible for users connected to Network Isolation.

> [!WARNING]
> A device that is connected to a NIAC will not be able to reach the internet unless the NIAC is member of a group of which the Wan Gateway is enabled.
   
2. **DNS Override**

This option enables the use of the Jimber Network Isolation DNS server. It facilitates easy host resolution within the Network Isolation environment.

3. **Always On**
4. **Device Approval**
5. **Device Limit**