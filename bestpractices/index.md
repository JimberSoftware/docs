# Network Isolation - Best practices - 
## Intro
Welcome to the best practices guide for Jimber Network Isolation. In this document, we'll dive into how to get the most out of our product by focusing on key areas: setting up groups, choosing the right IP ranges, and managing user permissions. It's especially important to get familiar with these features now, as we're planning to phase out multiple IP ranges in the future. This guide aims to give you all the tools and knowledge needed to ensure your network is not only effective but also secure and future-ready.


## The general group
As part of our ongoing efforts to streamline 'Network Isolation' and make it more user-friendly, we're moving towards a significant change in how IP ranges are assigned to groups. Currently, each group is associated with a specific IP range. However, this approach will soon be simplified: we're phasing out individual IP ranges for groups. The good news is, this change won't disrupt the functionality of your network - everything will continue to operate as before, albeit with some changes in IP addresses.

To ensure a smooth transition and minimize potential disruptions, we recommend a proactive approach. Start by aligning all devices - including users, servers, and NIACs - within the same IP range. This best practice will pave the way for easier adaptation to future changes.

Looking ahead, the default IP range for new networks or customers will be ***'198.18.0.0/15'***. When setting up a new network or onboarding a new customer, it's advisable to use this range for the primary group, which should be designated as group number ***'0'*** and named ***'General'***. This approach not only aligns with our forthcoming standard but also ensures your network setup is aligned with future configurations.

![general_group.jpg](/networkisolation/general_group.jpg)

## Applying rules
In configuring rules within 'Network Isolation,' focusing on functionality rather than specific user groups is key. This approach emphasizes the purpose or action of the rule, making your network's configuration more intuitive and manageable. For instance, rather than naming a group based on the department or personnel, like 'Sales,' name it in a way that reflects its function. Consider names like 'AllowFileserver' to grant access to a file server.

To illustrate this further, other examples of function-focused group names could include 'ForceWanGateway,' which could be used for directing all traffic through a specific WAN gateway, or 'BlockDangerousWebsites' for a group aimed at enhancing network security by restricting access to potentially harmful online sites. Another example is 'AllowRemoteServerLogin,' a group designated for users who need remote access to servers.

By adopting this functional naming convention, you create a rule structure that is straightforward and self-explanatory. This method simplifies the administration of the network, allowing for quick identification, modification, and understanding of each group's role and permissions. It ensures that as your network grows or changes, you can easily adjust access and permissions without having to overhaul the group structure."

## Azure Groups
When integrating 'Network Isolation' with Azure Entra ID, it's important to note how group synchronization works. For instance, if you have a group named 'AllowFileserver' in Azure and the 'Sales' group is a member of it, all members of 'Sales' will be automatically synced to 'AllowFileserver' in 'Network Isolation.' 

This ensures that your network permissions reflect your organizational structure by leveraging your existing nested groups in Azure. Such integration streamlines access management, as changes in Azure group memberships are automatically updated in 'Network Isolation,' maintaining consistency and efficiency.

![entraid_example.png](/networkisolation/entraid_example.png)
