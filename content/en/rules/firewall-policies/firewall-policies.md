# ![](../../images/menu/menu_policies.png ':size=28') Policies

<br>

<!-- tabs:start -->

## **![](../../images/menu/menu_services.png ':size=28') Firewall Services**

Within the **_<span style="color: darkblue;">Jimber SASE Platform</span>_**, a **Service** represents a digital resource that can be made accessible to users. These services can include websites, internal portals, remote desktops, CRMs, or any other network-based application.

To make a service available, it must be assigned to a **group** and a **destination** on the [**Policies**](/./rules/firewall-policies/firewall-policies.md) page. Once this is configured, the service will appear in the [**Security Panel**](/./rules/security_panel/security_panel.md) for users who are members of the selected group.

Users can open the Security Panel by clicking the **Jimber SASE tray icon** in their taskbar.

![Screenshot of the Jimber Tray Menu](./screenshots/security_panel.png ':size=300')

A security panel with multiple services can look like this:

![Screenshot of the Services tab of the Security Panel](./screenshots/security_panel_overview.png ':size=600')


#### Create Services

To create a service into the platform, click on the `+ Create new` button located at the upper right corner of the interface.

![Screenshot of the Services page](./screenshots/services.png ':size=600')

This will open the following screen where you can enter the specifics of your service:

![Screenshot of the Create Service page](./screenshots/create_service.png ':size=600')

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

    ![Screenshot of the unsaved changes warning](../../images/notifications/unsaved_changes.png ':size=300')

**Repeat these steps** to configure additional access rules as needed. 

After creating the service you can switch to [Policies](/./rules/firewall-policies/firewall-policies.md) to specify the details of the service.

#### Service Template

You can save the configuration of your service by clicking the `📄Save template` button. When prompted, enter a distinctive name and a clear, descriptive summary to make it easy to identify and reuse later. 

![save_template.png](./screenshots/save_template.png ':size=500')

 
 Any saved templates can be used when creating a new service by clicking the `📄Load template` button at the bottom of the page, selecting the appropriate service template and clicking the `➢ Apply template` button.

![load_template.png](./screenshots/load_template.png ':size=500')


#### Search Services

You can search the list of Services using the search box at the top of the page. This helps you quickly find and manage the service you're looking for.

> [!TIP]
> You can refresh the list of services by pressing the refresh icon ![](../../images/icons/icon_reload.png ':size=20') at the top of the page.

#### Update Services
Services can be edited by clicking on the edit icon ![](../../images/icons/icon_edit.png ':size=20') in their row.

![update_service.png](./screenshots/update_service.png ':size=800')

From here, you can:

- Change the **service name**.
- Add, remove, or modify **access rules**.

> [!IMPORTANT]
> Don't forget to submit the service, by clicking on the `➢ Submit` button.

You can use the `Clear changes` button if you decide not to submit the changes.


#### Delete Services

Services can be removed by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in their row.

 You will receive a warning before the service is permanently deleted:
 
![Screenshot of the deletion warning](./screenshots/delete_service.png ':size=400')


## **![](../../images/menu/menu_services.png ':size=28') Firewall Policies**

**Policies** in the **_<span style="color: darkblue;">Jimber SASE Platform</span>_** provide a comprehensive and centralized approach to managing network security rules. Unlike traditional rule-based systems, policies define access permissions by specifying **sources**, **destinations**, and **services** in a unified framework.

Policies offer several advantages over legacy rule configurations:

- **Simplified Management**: Create one policy instead of multiple individual rules
- **Service-Centric Security**: Directly associate services with access permissions
- **Entity-Based Control**: Use groups, devices, users, and networks as policy components
- **Centralized Overview**: View all access rules in a single, organized interface

> [!INFO]
> Policies replace and consolidate functionality from legacy features like Group Traffic, Allow Custom Ports, and Attribute Services, providing a more intuitive and scalable security management approach.

### Prerequisites

Before creating policies, ensure you have the following components configured:

#### 1. Required Dependencies

- **Services**: At least one service must be created to attach to a policy
- **Network Controller**: A cloud controller must be running to enable SASE connectivity

#### 2. Optional Entity Sources

Policies can use any combination of these entity types as sources and destinations:

- **[Groups](/./company/groups/groups.md)**: User or device groups
- **[Servers](/./devices/servers/servers.md)**: Backend servers and infrastructure
- **[NIACs](/./devices/niacs/niacs.md)**: Network Isolation Access Clients
- **[Native Devices](/./devices/nativedevices/nativedevices.md)**: Physical devices on the network
- **[Network Isolation Users](/./company/users/users.md)**: Individual users with network access
- **[User Devices](/./devices/userdevices/userdevices.md)**: End-user devices (laptops, mobiles, etc.)
- **[Native Networks](/./devices/nativenetworks/index.md)**: Physical network segments

### Create Policy

To create a new policy, click the `+ Create new` button in the upper right corner of the Policies page.

![create_policy.png](./screenshots/create_policy.png ':size=500')

##### 1. Basic Settings

 1. **Policy Name**: Provide a clear, descriptive name for the policy
 2. **Enabled**: Use the toggle to activate or deactivate the policy
 3. **Migration Source** (if applicable): Shows the original rule source if this policy was migrated from legacy configurations.
    <!-- Click [here](#policy-migration) for migration overview.  -->

##### 2. Configure Services

Select which services this policy will govern. Services define the applications, websites, or resources that users can access through this policy.

 1. Click `+ Add Services` to select from available services.
 2. Multiple services can be added to a single policy.
<!-- 3. Each service shows its configured access rules and destinations. -->

![add_service.png](./screenshots/add_service.png ':size=500')



##### 3. Define Sources

Sources represent **who** can access the services defined in this policy. As already mentioned, you can add multiple source entities:

 1. Click `+ Add Sources` to open the entity selection dialog
 2. Choose from available entity types:

    - **[Groups](/./company/groups/groups.md)**: Select user or device groups
    - **[Servers](/./devices/servers/servers.md)**: Choose specific servers
    - **[NIACs](/./devices/niacs/niacs.md)**: Pick Network Isolation Access Clients
    - **[Native Devices](/./devices/nativedevices/nativedevices.md)**: Select physical network devices
    - **[Users](/./company/users/users.md)**: Choose individual users
    - **[User Devices](/./devices/userdevices/userdevices.md)**: Pick specific devices of a user
    - **[Native Networks](/./devices/nativenetworks/index.md)**: Select network segments

 3. **Search and Filter**: Use the search function to quickly locate specific entities

![add_source.png](./screenshots/add_source.png ':size=500')

 4. **Multiple Selection**: Add as many source entities as needed for your policy

##### 4. Define Destinations

Destinations represent **where** the sources can connect. This defines the target resources that sources can access:

 1. Click `+ Add Destinations` to select destination entities
 2. Choose from the same entity types available for sources
 3. Destinations typically include:
    - **[Servers](/./devices/servers/servers.md)** hosting the services
    - **[Groups](/./company/groups/groups.md)** containing target resources
    - **[Native Networks](/./devices/nativenetworks/index.md)** with accessible resources
    - **All other entities** providing services


![add_destination.png](./screenshots/add_destination.png ':size=500')

> [!INFO]
> Don't forget to hit the save-button at the bottom of each window. 

##### 5. Service Entries

 1. Click `+ Add Service entry` to enter a service entry.
 2. Choose a name for the entry.
 3. Choose an action.
 4. Enter the correct URL or path the service will need to complete the action.

![service_entry.png](./screenshots/service_entry.png ':size=700')



##### 6. Submit Policy

Once all sections are configured:

 1. Review your policy configuration
 2. Click `➢ Submit` to save and activate the policy
 3. The policy will immediately take effect if enabled

### Manage Existing Policies

##### View Policy List

The main Policies page displays all configured policies in a table format:

**Table Columns:**

- **Name**: Policy identifier
- **Services**: Services governed by this policy
- **Sources**: Entities that can initiate access
- **Destinations**: Target entities for access
- **Enabled**: Current policy status (active/inactive)

![policies_overview.png](./screenshots/policies_overview.png ':size=700')

> [!NOTE]
>If any of the items are left blank, a yellow exclamation mark will appear in the policy row.

###### Enable/Disable Policies

Toggle policy status directly from the main table:

 1. Click the **Enable/Disable toggle** in the policy row
 2. The policy status updates immediately
 3. Disabled policies stop enforcing access rules but remain configured

> [!TIP]
> You can refresh the list of policies by pressing the refresh icon ![](../../images/icons/icon_reload.png ':size=20') at the top of the page.

##### Update Policies

To modify an existing policy:

 1. Click the the edit icon ![](../../images/icons/icon_edit.png ':size=20') in the policy row.
 2. Make necessary changes to any section
 3. Click `➢ Submit` to save updates

![update_policy.png](./screenshots/update_policy.png ':size=500')

##### Delete Policies

Click the delete icon ![](../../images/icons/icon_delete.png ':size=20') in the policy row to remove a policy.

You will receive a warning before the policy is permanently deleted:

![delete_policy.png](./screenshots/delete_policy.png ':size=400')

> [!WARNING]
> Deleting a policy immediately removes permanently all associated access rules. Users may lose access to services if no other policies grant permission.

### Policy Migration

The system automatically migrates legacy rules from previous configurations:

- **Attribute Service rules** → Service-based policies
- **Group Traffic rules** → Group-to-group policies
- **Allow Custom Ports rules** → Port-specific policies

Migrated policies show their original source in the Basic Settings section, helping you understand the rule's history and context.

### Best Practices

#### Policy Organization

- **Use descriptive names** that clearly indicate the policy's purpose
- **Group related services** into single policies when appropriate
- **Separate critical and non-critical** access rules into different policies
- **Use groups** instead of individual entities where possible

#### Security Considerations

- **Apply the principle of least privilege** - grant only necessary access
- **Regularly review policies** to ensure they match current business needs
- **Use groups instead of individual entities** for easier management

> [!INFO]
> Policies provide audit trails and logging capabilities, which makes it easier to monitor usage and fix connection problems.
<!-- making it easier to track access patterns and troubleshoot connectivity issues.-->
### Troubleshooting

#### Common Issues

 **Policy Not Taking Effect**

  - Verify the policy is **enabled**
  - Check that the **Network Controller is running**
  - Ensure **sources and destinations** are correctly configured
  - Confirm **services** are properly defined and active

 **Access Denied Despite Policy**

  - Review **service access rules** for correct port ranges
  - Verify **entity memberships** (users in groups, devices in networks)
  - Ensure **destinations include the target resources**


## **![](../../images/menu/menu_services.png ':size=28') Posture Policies**

A posture policy is a set of rules and automated decision criteria that evaluate whether a system, device, or application meets a required compliance or security standard before it is allowed onto a network or into production.

### Create Posture Policy

To create a posture policy into the platform, click on the `+ Create new` button located at the upper right corner of the interface.

![posture_policy.png](./screenshots/posture_policy.png ':size=600')

![create_posture_policy.png](./screenshots/create_posture_policy.png ':size=400')

1. Select the posture check this policy should evaluate.
2. Select the operating systems where this posture policy will be enabled.
3. Choose your preferred settings.
4. Choose wherefor the policy is required: SASE network connection, and/or cloud authentication.
5. Create the policy, by clicking on the `Create` button.  

![posture_policy_settings.png](./screenshots/posture_policy_settings.png ':size=400')

>[!ATTENTION]
>Before the policy is created you get an important warning!
>
>![warning_posture_policy.png](./screenshots/warning_posture_policy.png ':size=400')

### Enable/Disable Policies

Toggle policy status directly from the main table:

 1. Click the **Enable/Disable toggle** in the policy row.
 2. The policy status updates immediately.
 3. Disabled policies stop enforcing access rules but remain configured.

> [!TIP]
> You can refresh the list of policies by pressing the refresh icon ![](../../images/icons/icon_reload.png ':size=20') at the top of the page.

### Edit Posture Policy

Posture Policies can be edited by clicking on the edit icon ![](../../images/icons/icon_edit.png ':size=20') in their row.

The option are the same as when creating the policy. Naturally, the chosen poster check cannot be changed.

### Delete Posture Policy

Posture Policies can be removed by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in their row.

 You will receive a warning before the policy is permanently deleted:

![Screenshot of the deletion warning](./screenshots/delete_posture_policy.png ':size=400')


## **![](../../images/menu/menu_services.png ':size=28') Agentless Policies**

Agentless policies are rules and governance frameworks applied to systems, cloud workloads, or network devices without requiring a dedicated software agent to be installed directly on each target endpoint.

### Create Agentless Policy

To create a agentless policy into the platform, click on the `+ Create new` button located at the upper right corner of the interface.

![agentless_policy.png](./screenshots/agentless_policies.png ':size=600')

![create_agentless_policy.png](./screenshots/create_agentless_policy.png ':size=300')

1. Choose a name for the policy (required).
2. Select at least one service: SSH and/or RDP. 
3. Add at least one source: group and/or user.
4. Add at least one destination: group, server, native device, and/or NIAC device.
5. Create the policy, by clicking on the `Create` button.  

### Enable/Disable Policies

Toggle policy status directly from the main table:

 1. Click the **Enable/Disable toggle** in the policy row.
 2. The policy status updates immediately.
 3. Disabled policies stop enforcing access rules but remain configured.

> [!TIP]
> You can refresh the list of policies by pressing the refresh icon ![](../../images/icons/icon_reload.png ':size=20') at the top of the page.


### Edit Agentless Policy

Agentless Policies can be edited by clicking on the edit icon ![](../../images/icons/icon_edit.png ':size=20') in their row.

The option are the same as when creating the policy. 

### Delete Agentless Policy

Agentless Policies can be removed by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in their row.

 You will receive a warning before the policy is permanently deleted:

![Screenshot of the deletion warning](./screenshots/delete_agentless_policy.png ':size=400')


<!-- tabs:end -->
