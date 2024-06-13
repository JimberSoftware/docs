# Port Forwarding

Port Forwarding allows external users, which are not enabled for Network Isolation, to connect to internal services. This can be achieved using the public IP of the cloud network controller or the IP of the on-premise network controller.

## How to Set Up Port Forwarding:

1. **Description**: Begin by entering a clear description for the port forwarding rule to help in future references.
2. **Select Source Port**: Specify the port number through which external clients will initiate the connection.
3. **Specify Destination Port**: Determine the internal port number to which the traffic should be forwarded.
4. **Choose Protocol**: Depending on your service's requirements, select either the TCP or UDP protocol.
5. **Specify Destination**: Define the endpoint or service within your network to which the traffic should be directed.
6. **Removing Port Forwarding Rules**: If you need to revoke or adjust a rule, simply click on the garbage bin icon next to the relevant rule.
7. **Activate Changes**: After configuring your port forwarding rule, ensure you press the `Submit Rules` button to save and implement your changes.

> [!INFO] 
>  Regularly review your port forwarding rules to ensure they meet the current needs and security standards of your organization.