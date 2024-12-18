# Groups

Groups in the network setting act as a valuable mechanism for applying uniform network rules across multiple users, servers, and Network Isolation Access Clients (NIACs).

The concept of groups brings a high level of versatility and control to your network management. For instance, a group named 'Developers' could be set up, with rules allowing them to communicate with the devices in the 'Servers' group. Simultaneously, a separate group such as 'Sales' could be configured to not have this access, thereby segmenting network interactions based on job function or department.

This approach helps create a network landscape that aligns with your organization's unique operational dynamics, managing access, and communication based on the distinct needs and roles of different groups. In essence, the use of groups facilitates a more streamlined, controlled, and secure network environment.


![groups.png](/groups.png ':size=800')

In the overview of the groups, you can see the different entries of a group:

![group_entry.png](/group_entry_2.png ':size=800')




<!-- ### Primary vs Additional groups

Each user or device on your network can be assigned to one primary group, as well as numerous additional groups.

The primary group not only establishes the subnet for the user or device, but also determines its primary set of network rules. On the other hand, the role of additional groups is to supplement the network rules that are applied to the device; they do not influence its subnet.

For instance, consider a scenario where a user or device is assigned to one primary group and four additional groups. The user or device would obtain its subnet based on the IP range designated by the primary group. Then, the network rules from both the primary and all additional groups are aggregated and enforced on the user or device.

This flexible structure allows for a fine-tuned, layered approach to network management. Users or devices can benefit from a blend of network rules across multiple groups while adhering to clear subnet boundaries defined by their primary group. -->


<!-- ![edit-server.png](/edit-server.png ':size=600') -->


## Create Group

To create a new group into the platform, click on the `Create new` button 

![create_new.png](/create_new.png)

prominently located at the upper right corner of the interface.

> [!WARNING]
> Please ensure to configure the group settings in such a way that there is no overlap with your organization's existing physical network, VPNs, or any other networks accessed by your staff.

Creating a new group requires a group name that can be updated later as needed.
Creating a new group requires a group name that can be updated later as needed.

![create_group.png](/create_group.png ':size=500')


## Group Details

Access the details of a specific group by selecting the corresponding strip within the table (avoid clicking on the buttons at the end). This will reveal the network rules associated with the chosen group, along with the devices that fall under this group's purview.


![group_details.png](/group_details.png ':size=800')

> [!NOTE]
> Devices and users can only be added to the group from their own page:
>
>    - Comprehensive information on Group Traffic Rules, Attribute Services and Custom Ports Rules can be found in the SECURITY section of the sidebar.
>    - Comprehensive information on Group Configuration can be found [here](/./rules/groupconfiguration/groupconfiguration.md)
>    - Comprehensive information on how to add users can be found [here](/./company/users/users.md).
>    - Comprehensive information on how to add devices can be found in the DEVICES section of the sidebar.




## Edit Group
Groups can be edited by clicking on the yellow pencil icon next to their name ![icon_edit.png](/icon_edit.png ':size=35').

 You'll then be able to adjust the group name as needed:

![edit_group.png](/edit_group.png ':size=500')


## Copy Group
Groups can be copied by clicking on the copy icon next to their name ![icon_copy_group.png](/icon_copy_group.png ':size=35').

 You'll then be able to choose a name for the new group:

![copy_group.png](/copy_group.png ':size=500')

The new group will show the same details as the original group: firewall rules, group traffic rules, port rules and attributed services.




## Deleting Group
Groups can be deleted by clicking on the red trash bin icon next to their name 
![icon_delete.png](/icon_delete.png ':size=35').



![delete_group.png](/delete_group.png ':size=500')


> [!WARNING]
> The group will be removed without further notice.



<!-- [devices]: /./devices -->