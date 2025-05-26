# ![](../../images/menu/menu_groups.png ':size=25') Groups

Groups in the network setting act as a valuable mechanism for applying uniform network rules across multiple users, servers, and Network Isolation Access Clients (NIACs).

The concept of groups brings a high level of versatility and control to your network management. As mentioned in [Best Practices](/./advanced/bestpractices/bestpractices.md) it is better to choose group names that reflects its function, such as 'AllowFileServer', 'ForceOneGateway'...

For instance, a group named 'AllowServerAccess' could be set up with rules allowing members of that group to access with the devices in the group 'Servers'. Simultaneously, a separate group such as 'NoServerAccess' could be configured not to have this access. 

<!-- A further segmentation of these groups can be made based on job function or department. -->

<!-- For instance, a group named 'Developers' could be set up with rules allowing members of that group to communicate with the devices in the group 'Servers'. Simultaneously, a separate group such as 'Sales' could be configured not to have this access, thereby segmenting network interactions based on job function or department. -->

This approach helps create a network landscape that aligns with your organization's unique operational dynamics, managing access, and communication based on the distinct needs and roles of different groups. In essence, the use of groups facilitates a more streamlined, controlled and secure network environment.


![groups.png](./screenshots/groups.png ':size=800')

In the overview of the groups, you can see the different entries of a group:

![group_entry.png](./screenshots/group_entry_2.png ':size=800')

<!-- ### Primary vs Additional groups

Each user or device on your network can be assigned to one primary group, as well as numerous additional groups.

The primary group not only establishes the subnet for the user or device, but also determines its primary set of network rules. On the other hand, the role of additional groups is to supplement the network rules that are applied to the device; they do not influence its subnet.

For instance, consider a scenario where a user or device is assigned to one primary group and four additional groups. The user or device would obtain its subnet based on the IP range designated by the primary group. Then, the network rules from both the primary and all additional groups are aggregated and enforced on the user or device.

This flexible structure allows for a fine-tuned, layered approach to network management. Users or devices can benefit from a blend of network rules across multiple groups while adhering to clear subnet boundaries defined by their primary group. -->


<!-- ![edit-server.png](/edit-server.png ':size=600') -->

### Create Groups

To create a new group into the platform, click on the `+ Create new` button located at the upper right corner of the interface.

> [!WARNING]
> Please ensure to configure the group settings in such a way that there is no overlap with your organization's existing physical network, VPNs or any other networks accessed by your staff.

Creating a new group requires a group name that can be updated later as needed.


![create_group.png](./screenshots/create_group.png ':size=500')

### Filter Groups

You can search the list of Groups using the search box at the top of the page. This helps you quickly find and manage the group you're looking for.

- Use the search box to enter keywords and filter the group list.

> [!INFO]
> You can refresh the list of groups by pressing the refresh icon ![](../../images/icons/icon_reload.png ':size=20') at the top of the page.


### Group Details

Access the details of a specific group by selecting the corresponding row within the table (avoid clicking on the buttons at the end). This will reveal the network rules associated with the chosen group, along with the devices that fall under this group's purview.


![group_details.png](./screenshots/group_details.png ':size=800')

> [!NOTE]
> Devices and users can only be added to the group from their own page:
>
>    - Comprehensive information on Group Traffic Rules, Attribute Services and Custom Ports Rules can be found in the [**SECURITY**](/security.md) section of the sidebar.
>    - Comprehensive information on Group Configuration can be found [here](/./rules/groupconfiguration/groupconfiguration.md)
>    - Comprehensive information on how to add users can be found [here](/./company/users/users.md).
>    - Comprehensive information on how to add devices can be found in the [**DEVICES**](/devices.md) section of the sidebar.




### Edit Groups
Groups can be edited by clicking on the edit icon ![](../../images/icons/icon_edit.png ':size=20') in their row.

 You'll then be able to adjust the group name as needed:

![edit_group.png](./screenshots/edit_group.png ':size=500')


### Copy Groups
Groups can be copied by clicking on the copy icon ![](../../images/icons/icon_copy.png ':size=20') in their row.

 You'll then be able to choose a name for the new group:

![copy_group.png](./screenshots/copy_group.png ':size=500')

The new group will show the same details as the original group: firewall rules, group traffic rules, port rules and attributed services.




### Delete Groups
Groups can be deleted by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in their row.

> [!WARNING]
> This process is irreversible.

You will receive a warning before the group is permanently deleted:

![delete_group.png](./screenshots/delete_group.png ':size=500')





<!-- [devices]: /./devices -->