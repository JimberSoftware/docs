# ![](../../images/menu/menu_users.png ':size=25') Users

A user refers to an individual account within the platform. Users can have roles and be linked to properties of different products.

> [!INFO]
> Managing users efficiently is crucial for maintaining the security and integrity of your platform. 


### Create Users
To create a new User into the platform, click on the `+ Create new` button located at the upper right corner of the interface.

> [!WARNING]
> To create a new user, the company **must** first add a domain. The user's email address must correspond to the added domain. You can find more information on Domains [here](/company/domains/domains.md).

**Email** is used as the primary identifier for a user. It is essential for authentication purposes. Ensure that the provided email is valid and accessible by the user. 

![create_user.png](./screenshots/create_user.png ':size=500x300 :border-radius=10px')


> [!WARNING]
>  Be aware that the username cannot be changed after creating a user.

#### User Roles and their permissions

- **Admin**:
  - Toggle this option to promote a user to an administrator.
  - Allows the user to log into the security platform.
  - Grants privileges to manage the company's settings.
 
- **Network Isolation** <!--Jimber SASE Licence-->:
  - Toggle this option to enable `Network Isolation` <!--`Jimber SASE Licence`--> for this particular user, adding an extra layer of security.

- **Enable Secure mode**:
  - Toggle this option to enable Secure mode.
  - If Secure mode is turned ON for a device all incoming traffic will be blocked unless it comes from the `Jimber SASE Platform`.

> [!INFO]
>  Secure mode can only be enabled if Network Isolation <!--`Jimber SASE Licence`--> is also enabled. 

### Create Security Consultants

To create a new Security Consultant into the platform, follow the steps below. This enables that user to manage configurations of customers.

> [!INFO] This option is only available for **partners**.

- Navigate to the partner associated with the customer where you want to add the security consultant. In this example, the partner is **Space Partner**. 

	![user_in_integrator.png](./screenshots/user_in_integrator.png ':size=800')

- Create a new user with the Security Consultant role, or edit an existing user by toggling the option.

    ![create_sec_cons.png](./screenshots/create_sec_cons.png ':size=500x300')

- Return to the Users page of customer where you want to add the security consultant and add the user you created in the previous step by pressing `+ Add Security Consultant`.

- Provide the email address of the user you created (e.g.: 'frimaut@spacepartner.io') and click `+ Add Security Consultant` for this user to become security consultant for that company. 

    ![add_sec_cons.png](./screenshots/add_sec_cons.png ':size=500x300')

> [!INFO]
>  You can also use an already existing Security Consultant from the partner. In that case you can skip the first step.      

### Filter Users

You can search the list of Users using the search box at the top of the page. This helps you quickly find and manage the user you're looking for.

- Use the search box to enter keywords and filter the user list.

Next to the search box, there is a filter icon ![](../../images/icons/icon_filter.png ':size=20'). When clicked, it reveals advanced filtering options where you can define additional conditions based on the following three elements:

- **Property**: A dropdown menu where you choose the field to filter on.
- **Match type**: A dropdown that allows you to select how to match the value (e.g. `equals`, `contains`, etc.).
- **Value**: Enter or select the value to match, depending on the selected property.

You can press the `+` button to add multiple filters.

Once filters are applied:
- The results are updated to reflect your conditions.
- Active filters appear at the top of the page.
- You can remove filters individually by clicking the `X` next to each, or remove all at once by clicking the `Reset Filters` button.

> [!INFO]
> You can refresh the list of users by pressing the refresh icon ![](../../images/icons/icon_reload.png ':size=20') at the top of the page.

### User Details

In the user overview, several key properties are immediately visible: the user's role within the company (e.g., Admin or User), their platform role (typically 'User'), and the status of both the user account and Secure Mode.

 ![overview_users.png](./screenshots/overview_users.png ':size=800x150')

 Clicking on the corresponding row of a user opens a detailed view with additional information.  

> [!INFO] 
> Avoid using the action buttons at the end of the row (e.g. edit or delete).


![properties_user.png](./screenshots/properties_user.png ':size=500')

### Edit Users
  
 Users can be edited by clicking on the edit icon ![](../../images/icons/icon_edit.png ':size=20') in their row.
 
  ![edit_user.png](./screenshots/edit_user.png ':size=500x350')
  
> [!WARNING]
> The username cannot be changed. All other options are the same as when creating a user.
  
### Delete Users

 Users can be deleted by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in their row.

> [!WARNING]
> This process is irreversible.
 
 You will receive a warning before the user is permanently deleted:
 
 ![delete_user.png](./screenshots/delete_user.png ':size=500x150')


