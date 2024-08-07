# Group Traffic

"Group Traffic" functionality ensures specific groups can communicate with each other. It's a crucial feature for enabling inter-group communications without compromising on network security.

![group_traffic_start.png](/group_traffic_start.png ':size=800')

## How to Set Up Group Traffic:

1. **Select Source Group**: Choose the group you wish to create communication rules for.
2. **Select Destination Group**: Pick the group with which the source group should communicate.
3. **Intra-group Communication**: To let a group communicate internally, set both the source and destination groups to be identical. This rule allows members within the same group to interact with each other.

![group_traffic_intern.png](/group_traffic_intern.png ':size=800')


4. **Example**: To grant the "Developers" group access to your servers, select "Developers" as the source group and "Servers" as the destination group.

![group_traffic.png](/group_traffic.png ':size=800')

5. **Activate Changes**: After defining the communication rules, press the `Submit Rules` button ![submit_rules.png](/submit_rules.png ':size=100') to update and apply your configurations.

> [!WARNING]
> This feature should only be used in specific cases, such as allowing developers to access staging environments. Whenever possible, use "Allow Services" for a more granular control, ensuring the highest level of security.

A warning appears for unsaved changes:

![unsaved_changes.png](/unsaved_changes.png ':size=500x175')