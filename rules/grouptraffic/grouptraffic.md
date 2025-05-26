# ![](../../images/menu/menu_grouptraffic.png ':size=28') Group Traffic

The **Group Traffic** feature controls how different groups can communicate with each other across your network setup. On the *`Jimber SASE Platform`*, a **group** is a flexible concept that can represent users, servers, or devices connected via a Network Isolation Access Client (NIAC).

![Screenshot of the Group Trafic page](./screenshots/group_traffic_start.png ':size=800')

Because groups can be applied to various types of endpoints, this feature gives you precise control over traffic flow between these segments. For example, you might:

- Allow a group of **developers (users)** to access a group containing **staging servers**
- Permit **NIAC-connected devices** to communicate with a group of **infrastructure services**
- Enable internal communication between all devices within a **specific department**

> [!WARNING]  
> Group Traffic should be used carefully. For more targeted control over specific services, consider using **Allow Custom Ports**, which offers a more secure and detailed approach.

### Create Group Traffic Rules

Click on the `+ Create a new rule` button and follow the steps below:

1. **Select Source Group**: Choose the group that should be allowed to initiate the connection.
2. **Select Destination Group**: Choose the group that should be allowed to receive the connection.
3. **Start Port / End Port**: Define the allowed port range. If you don’t specify a range, it will default to `1–65535`, allowing all ports.
4. **Enable or Disable**: Use the slider to turn the rule on or off.
5. **Optional Note** ![](../../images/icons/icon_note.png ':size=20'): Add a short explanation to clarify the rule's purpose.
6. **Activate Changes**: Press the `➢ Submit rules` button to save and apply the rule.

For example, to grant the **"Developers"** group access to your **"Servers"**, you would set **"Developers"** as the source group and **"Servers"** as the destination group.

![Screenshot of the configuration of the example scenario](./screenshots/group_traffic.png ':size=800')

If you want members within the same group to communicate with each other, select the same group as both source and destination.

![Screenshot of the configuration of internal traffic](./screenshots/group_traffic_intern.png ':size=800')

### Filter Group Traffic Rules

You can filter the list of Group Traffic rules using the fields at the top of the page. This helps you quickly locate and manage specific rules.

- **Source Group**: Filter rules based on the selected source group using the dropdown menu.
- **Destination**: Narrow down results by selecting a destination from the dropdown menu.

### Edit Group Traffic Rules

You can freely edit the listed Group Traffic rules. If you make changes you don’t want to keep, use the `Clear changes` button to revert to the previously saved version.

The notes of Group Traffic rules can be updated by clicking the update icon ![](../../images/icons/icon_note.png ':size=20') in their row. The following window appears: 

![Screenshot of the Update Note window](./screenshots/update_note_rule.png ':size=400')

> [!WARNING]
> Don’t forget to save your changes to apply the updates by using the `➢ Submit rules` button.

### Delete Group Traffic Rules

Group Traffic rules can be removed by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in their row.

> [!WARNING]
> Don’t forget to save your changes to apply the updates by using the `➢ Submit rules` button.

> [!INFO]
> If there are any unsaved changes when you leave the page, a warning message will appear, so you won’t miss submitting the rules.
>
>![Screenshot of the unsaved changes warning](../../images/notifications/unsaved_changes.png ':size=400')

### Download Group Traffic Rules

You can download all Group Traffic rules as a **.csv file** by clicking the download icon ![](../../images/icons/icon_download.png ':size=20') located next to the `➢ Submit rules` button.




