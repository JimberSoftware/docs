# Port Forwarding

Port Forwarding allows external users who are not members of the *`Jimber SASE Platform`* to connect to internal services. Access is provided through the public IP of the Cloud Network Controller or the IP address of the On-Premise Network Controller.


![portforward.png](/portforward.png ':size=800')

### Create Port Forwarding Rule

Click on the `+ Create a new rule` button and follow the steps below:

1. **Description**: Provide a clear description of the rule for future reference.
2. **Source Port**: Enter the port number that external clients will use to connect.
3. **Destination Port**: Specify the internal port number the traffic should be forwarded to.
4. **Destination**: Choose the internal destination that should receive the forwarded traffic.
5. **Protocol**: Select either TCP or UDP based on your service's requirements.
6. **Enable or Disable**: Use the slider to turn the rule on or off.
7. **Optional: Create a Note** ![icon_note.png](/icon_note.png ':size=20'): If the rule has a specific purpose or context, it’s helpful to include a note for clarity.
8. **Activate Changes**: Once the rule is configured, press the `➢ Submit rules` button to apply your changes.

> [!INFO] 
>  Regularly review your port forwarding rules to ensure they meet the current needs and security standards of your organization.

### Filter Port Forwarding Rules

You can filter the list of Port Forwarding rules using the field at the top of the page. This helps you quickly locate and manage specific rules.

- **Destination**: Narrow down results by selecting a destination from the dropdown menu.

### Edit Port Forward Rules

You can freely edit the listed Port Forwarding rules. If you make changes you don’t want to keep, use the `Clear changes` button to revert to the previously saved version.

The notes of Port Forwarding rules can be updated by clicking the update icon ![icon_note.png](/icon_note.png ':size=20') in their row. The following window appears: 

![update_note_rule.png](/update_note_rule.png ':size=400')

> [!WARNING]
> Don’t forget to save your changes to apply the updates by using the `➢ Submit rules` button.

### Delete Port Forward Rules

Port Forwarding rules can be removed by clicking on the delete icon![icon_delete.png](/icon_delete.png ':size=35')in their row.

> [!WARNING]
> Don’t forget to save your changes to apply the updates by using the `➢ Submit rules` button.

> [!INFO]
> If there are any unsaved changes when you leave the page, a warning message will appear, so you won’t miss submitting the rules.
>
>![unsaved_changes.png](/unsaved_changes.png ':size=400')

### Download Port Forwarding Ruless

You can download all Port Forwarding rules as a **.csv file** by clicking the download icon ![icon_download.png](/icon_download.png ':size=20') located next to the `➢ Submit rules` button.