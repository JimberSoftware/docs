# ![](../../images/menu/menu_services.png ':size=28') Services

Within the **_Jimber SASE Platform_**, a **Service** represents a digital resource that can be made accessible to users. These services can include websites, internal portals, remote desktops, CRMs, or any other network-based application.

To make a service available, it must be assigned to a **group** and a **destination** on the [**Policies**](/./rules/firewall-policies/firewall-policies.md) page. Once this is configured, the service will appear in the [**Security Panel**](/./rules/security_panel/security_panel.md) for users who are members of the selected group.

Users can open the Security Panel by clicking the **Jimber SASE tray icon** in their taskbar.

![Screenshot of the Jimber Tray Menu](./screenshots/security_panel.png ':size=300')

A security panel with multiple services can look like this:

![Screenshot of the Services tab of the Security Panel](./screenshots/security_panel_overview.png ':size=800')


### Create Services

To create a service into the platform, click on the `+ Create new` button located at the upper right corner of the interface.

![Screenshot of the Services page](./screenshots/services.png ':size=800')

This will open the following screen where you can enter the specifics of your service:

![Screenshot of the Create Service page](./screenshots/create_service.png ':size=800')

1. **Choose a Name**: Start by giving your service a clear and recognizable name.

> [!NOTE]
> You can start with a template (see below), or you can create a completely new service. 


<!-- 2. **Create a New Service Entry**: Click `+ Create new service entry`. This defines how the service behaves.

    - **Name**: Provide a recognizable name to the service entry.
    - **Action**: Currently, the only available option is **"Open website"**.
    - **URL/Path**: Enter the web address or internal path the service should open. -->

2. **Add Access Rule**: Click `+ Add Access Rule`. This defines how traffic is allowed for the service.

    - **Description**: Briefly describe the purpose of the rule.
    - **Start Port / End Port**: Specify the port range to allow. If left empty, it defaults to `1` and `65535`.
    - **Protocol**: Choose the protocol the service will use (TCP, UDP, or ICMP).
    
    ![add_access_rule.png](./screenshots/add_access_rule.png ':size=500')

3. **Submit the service**, by clicking on the `➢ Submit` button. 
If you leave the page with any unsaved changes, a warning message will appear:

    ![Screenshot of the unsaved changes warning](../../images/notifications/unsaved_changes.png ':size=400')

**Repeat these steps** to configure additional access rules as needed. 

After creating the service you can switch to [Policies](/./rules/firewall-policies/firewall-policies.md) to specify the details of the service.

### Service template

You can save the configuration of your service by clicking the `📄Save template` button. When prompted, enter a distinctive name and a clear, descriptive summary to make it easy to identify and reuse later. 

![save_template.png](./screenshots/save_template.png ':size=500')

 
 Any saved templates can be used when creating a new service by clicking the `📄Load template` button at the bottom of the page, selecting the appropriate service template and clicking the `➢ Apply template` button.

![load_template.png](./screenshots/load_template.png ':size=500')


### Search Services

You can search the list of Services using the search box at the top of the page. This helps you quickly find and manage the service you're looking for.

### Update Services
Services can be edited by clicking on the edit icon ![](../../images/icons/icon_edit.png ':size=20') in their row.

![update_service.png](./screenshots/update_service.png ':size=800')

From here, you can:

- Change the **service name**.
- Add, remove, or modify **access rules**.

> [!IMPORTANT]
> Don't forget to submit the service, by clicking on the `➢ Submit` button.

You can use the `Clear changes` button if you decide not to submit the changes.


### Delete Services

Services can be removed by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in their row.

 You will receive a warning before the service is permanently deleted:
 
![Screenshot of the deletion warning](./screenshots/delete_service.png ':size=300')

