# Allow Custom Ports

This feature is designed for fine-grained control over inter-group communication. It lets you specify which server a group can communicate with, through which port, and using what protocol. It's an ideal solution for groups that don't require unrestricted access to another group.

![allow_custom_ports.png](allow_custom_ports.png ':size=800')

### Configure Custom Ports

Click on `Create New Rule` and follow the steps below:  

1. **Description**: Start by providing a clear description of the service rule for future reference.
2. **Select Source Group**: Choose the group for which you're creating the service rule.
3. **Specify Destination Port**: Input the port number on the destination server that the source group should access.
4. **Choose Protocol**: Select between TCP and UDP based on the needs of the service you're granting access to.
5. **Removing Service Rules**: Should you need to revoke a rule, click on the red trash bin icon next to the service rule![recycle_bin.png](/icon_delete.png ':size=35'). 
6. **Activate Changes**: Once you've configured the service rule, press the `Submit Rules` button ![submit_rules.png](/submit_rules.png ':size=100') to apply your changes.

> [!INFO] 
> It's essential to periodically review and adjust service rules to ensure they're in line with the security needs of your organization.

This feature is used to give specific groups access to webservers, native devices,...

**For example:** 

You have a webserver running on a server, but you don't want the users to have full access to the server.So this group will not have group traffic rules to the server, but only a specific custom port rule to the webserver.