# Port Forwarding

Port Forwarding allows external users, which are not enabled for Network Isolation, to connect to internal services. This can be achieved using the public IP of the cloud network controller or the IP of the on-premise network controller.

![portforward.png](/portforward.png ':size=800')

## Set Up Port Forwarding:

To set up Port Forwarding follow the steps below: 

1. **Description**: Begin by entering a clear description for the port forwarding rule to help in future references.
2. **Select Source Port**: Specify the port number through which external clients will initiate the connection.
3. **Specify Destination Port**: Determine the internal port number to which the traffic should be forwarded.
4. **Choose Protocol**: Depending on your service's requirements, select either the TCP or UDP protocol.
5. **Specify Destination**: Define the endpoint or service within your network to which the traffic should be directed.
6. **Activate Changes**: After configuring your port forwarding rule, ensure you press the `Submit Rules` button ![submit_rules.png](/submit_rules.png ':size=100') to save and implement your changes.

In any case, you will receive a warning if the service was not submitted:

![unsaved_changes.png](/unsaved_changes.png ':size=400')

> [!INFO] 
>  Regularly review your port forwarding rules to ensure they meet the current needs and security standards of your organization.

## Update Port Forward Rules

Rules can be updated by clicking on the yellow pencil icon next to their name 
![icon_edit.png](/icon_edit.png ':size=35').

The following window appears: 

![update_note_rule.png](/update_note_rule.png ':size=400')

## Delete Port Forward Rules

Rules can be removed by clicking on the red trash bin icon next to their name 
![icon_delete.png](/icon_delete.png ':size=35').

 > [!WARNING] 
>  The rule will be deleted without further notice.