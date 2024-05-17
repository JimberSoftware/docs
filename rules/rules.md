# Rules

Network Isolation rules determine which connections are allowed within a network. These rules work in tandem with optional firewall settings, allowing administrators to control traffic flow and specify which services or endpoints are accessible. You have the flexibility to add firewall rules for various groups, ensuring a tailored approach to network security.

## WAN

To configure WAN settings:

1. **Allow WAN / WAN Gateway**

When enabled, it forces clients to navigate the internet via the cloud or on-premise router. If this option is turned off, clients will access the internet using their own internet connection. 

This feature can be turned on to chain the networkcontroller to existing firewall / proxy infrastructure or to be sure that all SaaS applications are accessed from the same IP. SaaS applications can be configured to only allow SaaS from one IP, this way you can make these applications only accessible for users connected to Network Isolation.

> [!WARNING]
> A device that is connected to a NIAC will not be able to reach the internet unless the NIAC is member of a group of which the Wan Gateway is enabled.
   
2. **DNS Override**

This option enables the use of the Jimber Network Isolation DNS server. It facilitates easy host resolution within the Network Isolation environment.

## DNS Filtering

DNS Filtering allows you to control and manage which websites a specific group can access. Here's how to configure it:

1. **Select a Group**: Begin by choosing the group for which you want to set filtering rules.

2. **Block Categories**: Identify and block specific categories to prevent the selected group from accessing them.

3. **Manage Websites**:
   - **Blocklist & Allowlist**: Add specific websites to a blocklist to prevent access or to an allowlist to ensure access. 
   - **Remove Websites**: To remove a website from either list, click on the garbage bin icon next to the website name.

4. **Time-based Rules**: If you wish to restrict access based on specific times, press the clock icon to set a time slot.

5. **Activate Changes**: After making your desired configurations, ensure you click the `Submit Rules` button to update and apply the rules.

> [!INFO] 
> Always review and confirm the rules before submission to ensure accurate configuration.

## Allow Groups

"Allow Groups" functionality ensures specific groups can communicate with each other. It's a crucial feature for enabling inter-group communications without compromising on network security.

### How to Set Up Allow Groups:

1. **Select Source Group**: Choose the group you wish to create communication rules for.
2. **Select Destination Group**: Pick the group with which the source group should communicate.
3. **Intra-group Communication**: To let a group communicate internally, set both the source and destination groups to be identical. This rule allows members within the same group to interact with each other.
4. **Example**: To grant the "Developers" group access to your servers, select "Developers" as the source group and "Servers" as the destination group.
5. **Activate Changes**: After defining the communication rules, press the `Submit Rules` button to update and apply your configurations.

> [!WARNING]
> This feature should only be used in specific cases, such as allowing developers to access staging environments. Whenever possible, use "Allow Services" for a more granular control, ensuring the highest level of security.

## Allow Services

This feature is designed for fine-grained control over inter-group communication. It lets you specify which server a group can communicate with, through which port, and using what protocol. It's an ideal solution for groups that don't require unrestricted access to another group.

### How to Configure Allow Services:

1. **Description**: Start by providing a clear description of the service rule for future reference.
2. **Select Source Group**: Choose the group for which you're creating the service rule.
3. **Specify Destination Port**: Input the port number on the destination server that the source group should access.
4. **Choose Protocol**: Select between TCP and UDP based on the needs of the service you're granting access to.
5. **Removing Service Rules**: Should you need to revoke a rule, click on the garbage bin icon next to the service rule.
6. **Activate Changes**: Once you've configured the service rule, press the `Submit Rules` button to apply your changes.

> [!INFO] 
> It's essential to periodically review and adjust service rules to ensure they're in line with the security needs of your organization.


## Port Forwarding

Port Forwarding allows external users, which are not enabled for Network Isolation, to connect to internal services. This can be achieved using the public IP of the cloud network controller or the IP of the on-premise network controller.

### How to Set Up Port Forwarding:

1. **Description**: Begin by entering a clear description for the port forwarding rule to help in future references.
2. **Select Source Port**: Specify the port number through which external clients will initiate the connection.
3. **Specify Destination Port**: Determine the internal port number to which the traffic should be forwarded.
4. **Choose Protocol**: Depending on your service's requirements, select either the TCP or UDP protocol.
5. **Specify Destination**: Define the endpoint or service within your network to which the traffic should be directed.
6. **Removing Port Forwarding Rules**: If you need to revoke or adjust a rule, simply click on the garbage bin icon next to the relevant rule.
7. **Activate Changes**: After configuring your port forwarding rule, ensure you press the `Submit Rules` button to save and implement your changes.

> [!INFO] 
>  Regularly review your port forwarding rules to ensure they meet the current needs and security standards of your organization.