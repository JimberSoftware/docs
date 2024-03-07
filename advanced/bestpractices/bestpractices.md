# Network Isolation - Best practices
## Intro
Welcome to the best practices guide for Jimber Network Isolation. In this document, we'll dive into how to get the most out of our product by focusing on key areas: setting up groups, choosing the right IP ranges, and managing user permissions. It's especially important to get familiar with these features now, as we're planning to phase out multiple IP ranges in the future. This guide aims to give you all the tools and knowledge needed to ensure your network is not only effective but also secure and future-ready.

## Applying rules
In configuring rules within 'Network Isolation,' focusing on functionality rather than specific user groups is key. This approach emphasizes the purpose or action of the rule, making your network's configuration more intuitive and manageable. For instance, rather than naming a group based on the department or personnel, like 'Sales,' name it in a way that reflects its function. Consider names like 'AllowFileserver' to grant access to a file server.

To illustrate this further, other examples of function-focused group names could include 'ForceWanGateway,' which could be used for directing all traffic through a specific WAN gateway, or 'BlockDangerousWebsites' for a group aimed at enhancing network security by restricting access to potentially harmful online sites. Another example is 'AllowRemoteServerLogin,' a group designated for users who need remote access to servers.

By adopting this functional naming convention, you create a rule structure that is straightforward and self-explanatory. This method simplifies the administration of the network, allowing for quick identification, modification, and understanding of each group's role and permissions. It ensures that as your network grows or changes, you can easily adjust access and permissions without having to overhaul the group structure."

## Azure Groups
When integrating 'Network Isolation' with Azure Entra ID, it's important to note how group synchronization works. For instance, if you have a group named 'AllowFileserver' in Azure and the 'Sales' group is a member of it, all members of 'Sales' will be automatically synced to 'AllowFileserver' in 'Network Isolation.' 

This ensures that your network permissions reflect your organizational structure by leveraging your existing nested groups in Azure. Such integration streamlines access management, as changes in Azure group memberships are automatically updated in 'Network Isolation,' maintaining consistency and efficiency.


![entraid_example.png](/entraid_example.png)
