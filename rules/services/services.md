# Services

Within the *`Jimber SASE Platform`*, a **Service** represents a digital resource that can be made accessible to users. These services can include websites, internal portals, remote desktops, CRMs, or any other network-based application.

To make a service available, it must be assigned to a **group** and a **destination** on the [**Attribute Services**](/./rules/attribute_services/attribute_services.md) page. Once this is configured, the service will appear in the [**Security Panel**](/./rules/security_panel/security_panel.md) for users who are members of the selected group.

Users can open the Security Panel by clicking the **Jimber SASE tray icon** in their taskbar.

![security_panel.png](/security_panel.png ':size=300')

A security panel with multiple services can look like this:

![security_panel_overview.png](/security_panel_overview.png ':size=800')


## Create Service

To create a service into the platform, click on the `Create new` button

![create_new.png](/create_new.png)

prominently located at the upper right corner of the interface.


![create_service.png](/create_service.png ':size=800')

1. **Choose a Name**: Start by giving your service a clear and recognizable name.

2. **Create a New Service Entry**: Click **"Create new service entry"**. This defines how the service behaves.

    - **Description**: Provide a short explanation of the service entry.
    - **Action**: Currently, the only available option is **"Open website"**.
    - **URL/Path**: Enter the web address or internal path the service should open.

3. **Add an Access Rule**: Define how traffic is allowed for the service.

    - **Description**: Briefly describe the purpose of the rule.
    - **Start Port / End Port**: Specify the port range to allow. If left empty, it defaults to `1` and `65535`.
    - **Protocol**: Choose the protocol the service will use (e.g., TCP or UDP).

Repeat these steps to configure additional services as needed.

> [!WARNING]
> Don't forget to submit the service, by clicking on the `Submit service` button.

If there are any unsaved changes, a warning message will appear, so you won’t miss submitting the service.

![unsaved_changes.png](/unsaved_changes.png ':size=400')


After creating the service you can switch to [Attribute Services](/./rules/attribute_services/attribute_services.md) to specify the details of the service.


## Edit Service
Services can be edited by clicking on the yellow pencil icon next to their name 
![icon_edit.png](/icon_edit.png ':size=35').

From here, you can:

- Change the **service name**.
- Add, remove, or modify **service entries**.
- Add, remove, or modify **access rules**.

If you make changes you don’t want to keep, use the `Clear changes` button to revert to the previously saved version.
Don’t forget to save your changes to apply the updates by pressing the `Submit service` button.


## Delete Service

Services can be removed by clicking on the red trash bin icon next to their name 
![icon_delete.png](/icon_delete.png ':size=35').

 You will receive a warning before the service is permanently deleted:
 
![deleting_service.png](/deleting_service.png ':size=500x150')

