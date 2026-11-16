# Zero Trust Outbound

ZTO is a security mode in which outbound connections from agents are restricted by default, necessitating an explicit firewall rule for every permitted connection.

 When Zero Trust Outbound is enabled, three new firewall policies are created in the **_<span style="color: darkblue;">Jimber SASE Platform</span>_**: 

 ![zto_policies.png](./images/zto_policies.png ':size=800') 

1. Standard Internet - NIACs
2. Standard Internet - Servers
3. Standard Internet - Users

All three policies are working with the same principle, namely deny all traffic that is going out. Only specific traffic is allowed.
Only when these policies are enabled, the internet can be used. 

More information about firewall policies, you can find [here](/./rules/firewall-policies/firewall-policies.md).



In [Firewall Services](/./rules/firewall-policies/firewall-policies.md) you can specify the ports and protocol through which the protocol will communicate.

![update_service_internet.png](./images/update_service_internet.png ':size=800') 

>[!WARNING]
>Changing or deleting one of these options can cause a failure of the corresponding service. 

