# Groups

Groups in the network setting act as a valuable mechanism for applying uniform network rules across multiple users, servers, and Network Isolation Access Clients (NIACs). An important factor to remember is that all devices allocated under the same PRIMARY group inherently share the same subnet, thereby ensuring a unified network interface.

The concept of groups brings a high level of versatility and control to your network management. For instance, a group named 'Developers' could be set up, with rules allowing them to communicate with the devices in the 'Servers' group. Simultaneously, a separate group such as 'Sales' could be configured to not have this access, thereby segmenting network interactions based on job function or department.

This approach helps create a network landscape that aligns with your organization's unique operational dynamics, managing access, and communication based on the distinct needs and roles of different groups. In essence, the use of groups facilitates a more streamlined, controlled, and secure network environment.


![groups.png](/groups.png ':size=900')

In the overview of the groups, you can see the different entries of a group:

![group-entry.png](/group-entry_2.png ':size=900')




### Primary vs Additional groups

Each user or device on your network can be assigned to one primary group, as well as numerous additional groups.

The primary group not only establishes the subnet for the user or device, but also determines its primary set of network rules. On the other hand, the role of additional groups is to supplement the network rules that are applied to the device; they do not influence its subnet.

For instance, consider a scenario where a user or device is assigned to one primary group and four additional groups. The user or device would obtain its subnet based on the IP range designated by the primary group. Then, the network rules from both the primary and all additional groups are aggregated and enforced on the user or device.

This flexible structure allows for a fine-tuned, layered approach to network management. Users or devices can benefit from a blend of network rules across multiple groups while adhering to clear subnet boundaries defined by their primary group.


![edit-server.png](/edit-server.png ':size=600')


## Create a group

To create a new group into the platform, click on the `Create new` button 

![create_new.png](/create_new.png)

prominently located at the upper right corner of the interface.

> [!WARNING]
> Please ensure to configure the group settings in such a way that there is no overlap with your organization's existing physical network, VPNs, or any other networks accessed by your staff.

Creating a new group requires the following information:

- Group Name: An identifier for the group, which can be updated later as needed.
- Group Number: A numerical value utilized by the Network Controller interface.
- Ip range: The designated private network range assigned to the group.


![create-group.png](/create-group.png ':size=600')


## Group details
Access the details of a specific group by selecting the corresponding strip within the table (avoid clicking on the buttons at the end). This will reveal the network rules associated with the chosen group, along with the devices that fall under this group's purview.


![group-details.png](/group-entry.png ':size=900')


## Edit a group
Groups can be edited by clicking on the yellow pencil icon next to their name ![pencil_2.png](/pencil_2.png).

 You'll then be able to adjust the group name as needed:

![create-group.png](/edit-group.png ':size=600')



## Remove a group
Groups can be removed by clicking on the red trash bin icon next to their name 
![recycle_bin.png](/recycle_bin.png).



![delete-group.png](/delete-group.png ':size=500')



> [!WARNING]
> A group can only be deleted if it has no linked devices or active network rules.

To facilitate the removal process:

1. Refer to the 'Group Details' section to identify any devices associated with the group and its active network rules.
2. Nullify all network rules associated with the group.
3. Reassign any devices within the group to a different group.

> [!INFO]
> After taking these steps, you should be able to successfully delete the group.


