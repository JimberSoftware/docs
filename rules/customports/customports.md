# Allow Custom Ports

This feature is designed for fine-grained control over inter-group communication. It lets you specify which server a group can communicate with, through which port, and using what protocol. It's an ideal solution for groups that don't require unrestricted access to another group.

![Screenshot of the Allow Custom Ports page](./screenshots/allow_custom_ports.png ':size=800')

**For example:** 

You have a webserver running on a server, but you don't want the users to have full access to the server. So this group will not have group traffic rules to the server, but only a specific custom port rule to the webserver.

### Create Custom Ports Rule

Click on the `+ Create a new rule` button and follow the steps below:

1. **Description**: Enter a clear description to identify the rule later.
2. **Select Source Group**: Choose the group that should be allowed to initiate the connection.
3. **Start Port / End Port**: Define the range of destination ports to be accessed. For a single port, use the same value in both fields.
4. **Protocol**: Select the appropriate protocol.
5. **Enable or Disable**: Use the slider to turn the rule on or off.
6. **Optional Note** ![](../../images/icons/icon_note.png ':size=20'): Add a short explanation to clarify the rule's purpose.
7. **Activate Changes**: Press the `➢ Submit rules` button to save and apply the rule.

> [!INFO] 
> It's essential to periodically review and adjust Custom Ports rules to ensure they're in line with the security needs of your organization.

### Filter Custom Port Rules

You can filter the list of Custom Port rules using the fields at the top of the page. This helps you quickly locate and manage specific rules.

- **Search**: Use this text field to search by description.
- **Source Group**: Filter rules based on the selected source group using the dropdown menu.
- **Destination**: Narrow down results by selecting a destination from the dropdown menu.

### Edit Custom Ports Rules

You can freely edit the listed Custom Ports rules. If you make changes you don’t want to keep, use the `Clear changes` button to revert to the previously saved version.

The notes of Custom Ports rules can be updated by clicking the update icon ![](../../images/icons/icon_note.png ':size=20') in their row. The following window appears:

![Screenshot of the Update Note window](./screenshots/update_note_rule.png ':size=400')

> [!WARNING]
> Don’t forget to save your changes to apply the updates by using the `➢ Submit rules` button.

### Delete Custom Ports Rules

Custom Ports rules can be removed by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in their row.

> [!WARNING]
> Don’t forget to save your changes to apply the updates by using the `➢ Submit rules` button.


> [!INFO]
> If there are any unsaved changes when you leave the page, a warning message will appear, so you won’t miss submitting the rules.
>
>![Screenshot of the unsaved changes warning](../../images/notifications/unsaved_changes.png ':size=400')

### Download Custom Ports Rules

You can download all Custom Ports rules as a **.csv file** by clicking the download icon ![](../../images/icons/icon_download.png ':size=20') located next to the `➢ Submit rules` button.
