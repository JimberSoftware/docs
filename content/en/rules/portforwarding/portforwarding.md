# ![](../../images/menu/menu_portforwarding.png ':size=28') Port Forwarding

Port Forwarding allows external users who are not members of the **_<span style="color: darkblue;">Jimber SASE Platform</span>_** to connect to internal services. Access is provided through the public IP of the Cloud Network Controller or the IP address of the On-Premise Network Controller.

![Screenshot of the Port Forward Rules page](./screenshots/portforward.png ':size=700')

### Create Port Forwarding Rule

Click on the `+ Create a new rule` button and follow the steps below:

1. **Description**: Provide a clear description of the rule for future reference.
2. **Network Controller**: Select the controller that receives incoming traffic. The rule applies only to this controller.
3. **Source Port**: Enter the port number that external clients will use to connect.
4. **Destination Port**: Specify the internal port number the traffic should be forwarded to.
5. **Destination**: Choose the internal destination that should receive the forwarded traffic.
6. **Protocol**: Select either TCP or UDP based on your service's requirements.
7. **Enable or Disable**: Use the slider to turn the rule on or off.
8. **Optional: Create a Note** ![](../../images/icons/icon_note.png ':size=20'): If the rule has a specific purpose or context, it’s helpful to include a note for clarity.
9. **Activate Changes**: Once the rule is configured, press the `➢ Submit` button to apply your changes.

You can use the same source port and protocol on different controllers. Active rules on the same controller must use a different source port or protocol.

### Country restrictions

Each rule has one country mode. Existing and new rules use **No country restriction** by default.

- **No country restriction**: The country does not restrict the rule.
- **Allow only selected countries**: Allow a known country only if it is selected. Block an unknown country.
- **Block selected countries**: Block a selected country. Allow an unknown country when the database is usable.

Select countries, read-only preset regions, and company regions. Their countries form one set. Duplicate membership has no extra effect. A restricted mode must have at least one country or region. Use **No country restriction** to remove the restriction.

The controller checks the incoming public source IP before it replaces the source address. VPNs, proxies, and upstream address replacement can change the country that the controller sees. This estimate is not proof of a person's location. It does not replace authentication or other service protection.

Changes apply to new IPv4 TCP and UDP connections. Existing connections can continue until they close or expire. If no usable country database exists, both restricted modes block all new connections and report an error. Unrestricted rules are not affected.

The controller uses a local country database. It checks for an update daily. It validates each replacement and keeps the last valid file if an update fails.

### Regions

Manage regions under **Security → Regions**. Preset regions appear in the table and cannot be changed or deleted. A custom region can contain countries and presets, but not another custom region. Empty regions are not allowed. Edits update all rules that use the region. A custom region cannot be deleted while a rule uses it. Select its rule count to show those rules.

The read-only presets are Africa (UN M49 region 002), Americas (019), Asia (142, including Taiwan), Europe (150), Oceania (009), and Benelux (BE, NL, LU). Their member lists are shown in the country selector.

Company Admins and Security Consultants can manage groups and restrictions. They must have the required role in the target company. Port Forwarding feature access is also required.

Blocked traffic appears under **Monitoring → Port-forward Blocks** with separate columns for the rule ID and name, source country or unknown, and block reason. Search, filters, sorting, packet details, and CSV exports use the same stored events. Packet Inspection still includes these events, with country details in the packet details panel.

Country rejection and unavailable country data are separate reasons. Five-minute groups keep different rules, countries, and reasons separate. Event delivery is not complete under attack or when queues are full. Region changes and rule country changes appear separately in activity history.

Existing rules are copied to each controller during the upgrade. Every company with port-forward rules must have a network controller before the upgrade. The migration fails if this condition is not met. New controllers do not automatically receive existing rules.

> [!TIP]
> You can download an overview of the port forwarding rules associated to a destination by clicking on the download icon ![](../../images/icons/icon_download.png ':size=20') located above the overview on the right next to the `➢ Submit` button.. The overview will be downloaded as a CSV-file.

> [!IMPORTANT]
> Regularly review your port forwarding rules to ensure they meet the current needs and security standards of your organization.

### Filter Port Forwarding Rules

You can filter the list of Port Forwarding rules using the field at the top of the page. This helps you quickly locate and manage specific rules.

### Edit Port Forward Rules

You can freely edit the listed Port Forwarding rules. If you make changes you don’t want to keep, use the `Clear changes` button to revert to the previously saved version.

The notes of Port Forwarding rules can be updated by clicking the update icon ![](../../images/icons/icon_note.png ':size=20') in their row. The following window appears:

![Screenshot of the Update Note window](./screenshots/update_note_rule.png ':size=400')

> [!WARNING]
> Don’t forget to save your changes to apply the updates by using the `➢ Save` button.

If there are any unsaved changes when you leave the page, a warning message will appear, so you won’t miss submitting the rules.
![Screenshot of the unsaved changes warning](../../images/notifications/unsaved_changes.png ':size=400')

### Delete Port Forward Rules

Port Forwarding rules can be removed by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in their row.

> [!WARNING]
> The port forward rule will be deleted without further notice. If by mistake the delete button was hit, you can restore the original settings by clicking `Clear changes` as long as the `Submit` button was not yet hit.
