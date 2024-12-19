# Allow Custom Ports

This feature is designed for fine-grained control over inter-group communication. It lets you specify which server a group can communicate with, through which port, and using what protocol. It's an ideal solution for groups that don't require unrestricted access to another group.

![allow_custom_ports.png](allow_custom_ports.png ':size=800')

### Configure Custom Ports

Click on `Create New Rule` and follow the steps below:  

1. **Description**: Start by providing a clear description of the rule for future reference.
2. **Select Source Group**: Choose the group for which you're creating the rule.
3. **Specify Destination Port**: Input the port number on the destination server that the source group should access.
4. **Choose Protocol**: Select between TCP and UDP based on the needs of the rule you're granting access to.
5. **Activate Changes**: Once you've configured the rule, press the `Submit Rules` button ![submit_rules.png](/submit_rules.png ':size=100') to apply your changes.

In any case, you will receive a warning if the rule was not submitted:

![unsaved_changes.png](/unsaved_changes.png ':size=400')

> [!INFO] 
> It's essential to periodically review and adjust custom ports rules to ensure they're in line with the security needs of your organization.

This feature is used to give specific groups access to webservers, native devices,...

**For example:** 

You have a webserver running on a server, but you don't want the users to have full access to the server. So this group will not have group traffic rules to the server, but only a specific custom port rule to the webserver.

## Update Custom Ports

Custom Ports can be updated by clicking on the yellow pencil icon next to their name 
![icon_edit.png](/icon_edit.png ':size=35').

The following window appears: 

![update_note_rule.png](/update_note_rule.png ':size=400')

## Delete Custom Ports

Custom ports can be removed by clicking on the red trash bin icon next to their name 
![icon_delete.png](/icon_delete.png ':size=35').

 > [!WARNING] 
>  The rule will be deleted without further notice.
