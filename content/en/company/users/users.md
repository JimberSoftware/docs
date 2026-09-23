# ![](../../images/menu/menu_users.png ':size=25') Users

A user refers to an individual account within the platform. Users can have roles and be linked to properties of different products.


> [!IMPORTANT]
> Managing users efficiently is crucial for maintaining the security and integrity of your platform. 


### Create User
To create a new User into the platform, click on the `+ Create new` button located at the upper right corner of the interface.

> [!WARNING]
> To create a new user, the company **must** first add a domain. The user's email address must correspond to the added domain. You can find more information on Domains [here](/company/domains/domains.md).

**Email** is used as the primary identifier for a user. It is essential for authentication purposes. Ensure that the provided email is valid and accessible by the user. 

![create_user.png](./screenshots/create_user.png ':size=400')


<!-- > [!WARNING]
>  Be aware that the username cannot be changed after creating a user. -->

#### User Roles and their permissions

- **Admin**:
  - Toggle this option to promote a user to an administrator.
  - Allows the user to log into the security platform.
  - Grants privileges to manage the company's settings.
 
<!-- - **Network Isolation** 
  - Toggle this option to enable `Network Isolation` for this particular user, adding an extra layer of security.
  - When Network Isolation is enabled, groups can be selected. For more information on groups, you can find [here](/./company/groups/groups.md). -->

- **Enable Secure Mode**:
  - Toggle this option to enable Secure mode.
  - If Secure mode is turned ON for a device all incoming traffic will be blocked unless it comes from the **_Jimber SASE Platform_**:

  ![secure_mode_warning.png](./screenshots/secure_mode_warning.png ':size=400')



### Create Security Consultants

To create a new Security Consultant into the platform, follow the steps below. 
A Security Consultant can manage configurations of its customer.


> [!CAUTION] This option is only available for **partners**.

- Navigate to the partner **associated** with the customer where you want to add the security consultant. In this example, the partner of Space Odyssey is **Space Partner**:

![customer_partner.png](./screenshots/customer_partner.png ':size=800')

![user_in_integrator.png](./screenshots/user_in_integrator.png ':size=800x200')

- There are two ways to proceed: **create** a new user with the Security Consultant role,
or **edit** and promote an existing user by toggling the option.

<!-- tabs:start -->
#### **New user**

Navigate to the section `Users` from the partner, click on the `+ Create new` button to create a new user, and toggle the `Security Consultant` button: 

![create_sec_cons.png](./screenshots/create_sec_cons.png ':size=350')

#### **Promote an existing user**

Navigate to the section `Users` from the partner, click on the `+ Add Security Consultant` button to promote a existing user:

 ![promote_sec_consult.png](./screenshots/promote_sec_consult.png ':size=350')

Provide the email of the user to be promoted.


<!-- tabs:end -->

    
 

### Filter Users

You can search the list of users using the search box at the top of the page. This helps you quickly find and manage the user you're looking for.

Use the search box to enter keywords and filter the user list.

Next to the search box, there is a filter icon ![](../../images/icons/icon_filter.png ':size=20'). When clicked, it reveals advanced filtering options where you can define additional conditions based on the following three elements:

- **Property**: A dropdown menu where you choose the field to filter on.
- **Match type**: A dropdown that allows you to select how to match the value (`equals`, `contains`, or `NOT`).
- **Value**: Enter or select the value to match, depending on the selected property.

![filter_user.png](./screenshots/filter_user.png ':size=500')

To add multiple filters you can press the filter icon ![](../../images/icons/icon_filter.png ':size=20') again and then press the `+` button.

Active filters appear at the top of the page:

![active_filters.png](./screenshots/active_filters.png ':size=600')

<!-- Once filters are applied:
- The results are updated to reflect your conditions.
- Active filters appear at the top of the page.
- You can remove filters individually by clicking the `X` next to each, or remove all at once by clicking the `Reset Filters` button. -->

> [!TIP]
> You can refresh the list of users by pressing the refresh icon ![](../../images/icons/icon_reload.png ':size=20') at the top of the page.

### User Details

In the user overview, several key properties are immediately visible: the user's role within the company (e.g., Admin or User), their platform role (typically 'User'), the status of the user account (enabled or not) and Secure Mode (activated or not).

 ![overview_users.png](./screenshots/overview_users.png ':size=800')

 Clicking on the corresponding strip of a user opens a detailed view with additional information, a tab with some details and a tab with security settings. 

![properties_user.png](./screenshots/properties_user.png ':size=500')

![security_user.png](./screenshots/security_user.png ':size=500')



<!-- > [!INFO] 
> There is no additional info for Security Consultants. -->

### Edit User
  
 Users can be edited by clicking on the edit icon ![](../../images/icons/icon_edit.png ':size=20') in their row.
 
  ![edit_user.png](./screenshots/edit_user.png ':size=400')
  
All options are the same as when creating a user.
  
### Delete User

 Users can be deleted by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in their row.

> [!WARNING]
> This process is irreversible.
 
 You will receive a warning before the user is permanently deleted:
 
 ![delete_user.png](./screenshots/delete_user.png ':size=350')


