# ![](../../images/menu/menu_policies.png ':size=28') Policies

**Policies** in the **_Jimber SASE Platform_** provide a comprehensive and centralized approach to managing network security rules. Unlike traditional rule-based systems, policies define access permissions by specifying **sources**, **destinations**, and **services** in a unified framework.

Policies offer several advantages over legacy rule configurations:

- **Simplified Management**: Create one policy instead of multiple individual rules
- **Service-Centric Security**: Directly associate services with access permissions
- **Entity-Based Control**: Use groups, devices, users, and networks as policy components
- **Centralized Overview**: View all access rules in a single, organized interface

> [!INFO]
> Policies replace and consolidate functionality from legacy features like Group Traffic, Allow Custom Ports, and Attribute Services, providing a more intuitive and scalable security management approach.

## Prerequisites

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

## Create Policy

To create a new policy, click the `+ Create new` button in the upper right corner of the Policies page.

![create_policy.png](./screenshots/create_policy.png ':size=500')

#### Basic Settings

1. **Policy Name**: Provide a clear, descriptive name for the policy
2. **Enabled**: Use the toggle to activate or deactivate the policy
3. **Migration Source** (if applicable): Shows the original rule source if this policy was migrated from legacy configurations

#### Configure Services

Select which services this policy will govern. Services define the applications, websites, or resources that users can access through this policy.

1. Click `+ Add Service` to select from available services.
2. Multiple services can be added to a single policy.
<!-- 3. Each service shows its configured access rules and destinations. -->

![add_service.png](./screenshots/add_service.png ':size=500')



#### Define Sources

Sources represent **who** can access the services defined in this policy. You can add multiple source entities:

1. Click `+ Add Source` to open the entity selection dialog
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

#### Define Destinations

Destinations represent **where** the sources can connect. This defines the target resources that sources can access:

1. Click `+ Add Destination` to select destination entities
2. Choose from the same entity types available for sources
3. Destinations typically include:
    - **[Servers](/./devices/servers/servers.md)** hosting the services
    - **[Groups](/./company/groups/groups.md)** containing target resources
    - **[Native Networks](/./devices/nativenetworks/index.md)** with accessible resources
    - **All other entities** providing services


![add_destination.png](./screenshots/add_destination.png ':size=500')

> [!INFO]
> Don't forget to hit the save-button at the bottom of each window. 

#### Service Entries

1. Click `+ Add Service entry` to enter a service entry.
2. Choose a name for the entry.
3. Choose an action.
4. Enter the correct URL or path the service will need to complete the action.

![service_entry.png](./screenshots/service_entry.png ':size=800')


<!-- #### Service Actions

Configure how the policy handles service access:

- **Allow**: Permit access to the specified services
- **Monitor**: Log access attempts for auditing (if available)
- **Custom Rules**: Define specific port ranges or protocols if needed -->

#### Submit Policy

Once all sections are configured:

1. Review your policy configuration
2. Click `➢ Submit` to save and activate the policy
3. The policy will immediately take effect if enabled

## Manage Existing Policies

#### View Policy List

The main Policies page displays all configured policies in a table format:

**Table Columns:**

- **Name**: Policy identifier
- **Services**: Services governed by this policy
- **Sources**: Entities that can initiate access
- **Destinations**: Target entities for access
- **Enabled**: Current policy status (active/inactive)

![policies_overview.png](./screenshots/policies_overview.png ':size=800')

##### Enable/Disable Policies

Toggle policy status directly from the main table:

1. Click the **Enable/Disable toggle** in the policy row
2. The policy status updates immediately
3. Disabled policies stop enforcing access rules but remain configured


#### Update Policies

To modify an existing policy:

1. Click the the edit icon ![](../../images/icons/icon_edit.png ':size=20') in the policy row
2. Make necessary changes to any section
3. Click `➢ Submit` to save updates

![update_policy.png](./screenshots/update_policy.png ':size=800')

#### Delete Policies

Click the delete icon ![](../../images/icons/icon_delete.png ':size=20') in the policy row to remove a policy.

You will receive a warning before the policy is permanently deleted:

![delete_policy.png](./screenshots/delete_policy.png ':size=300')

> [!WARNING]
> Deleting a policy immediately removes permanently all associated access rules. Users may lose access to services if no other policies grant permission.

## Policy Migration

The system automatically migrates legacy rules from previous configurations:

- **Attribute Service rules** → Service-based policies
- **Group Traffic rules** → Group-to-group policies
- **Allow Custom Ports rules** → Port-specific policies

Migrated policies show their original source in the Basic Settings section, helping you understand the rule's history and context.

## Best Practices

### Policy Organization

- **Use descriptive names** that clearly indicate the policy's purpose
- **Group related services** into single policies when appropriate
- **Separate critical and non-critical** access rules into different policies
- **Use groups** instead of individual entities where possible

### Security Considerations

- **Apply the principle of least privilege** - grant only necessary access
- **Regularly review policies** to ensure they match current business needs
- **Use groups instead of individual entities** for easier management

> [!INFO]
> Policies provide audit trails and logging capabilities, which makes it easier to monitor usage and fix connection problems.
<!-- making it easier to track access patterns and troubleshoot connectivity issues.-->
## Troubleshooting

### Common Issues

**Policy Not Taking Effect**

- Verify the policy is **enabled**
- Check that the **Network Controller is running**
- Ensure **sources and destinations** are correctly configured
- Confirm **services** are properly defined and active

**Access Denied Despite Policy**

- Review **service access rules** for correct port ranges
- Verify **entity memberships** (users in groups, devices in networks)
- Ensure **destinations include the target resources**
