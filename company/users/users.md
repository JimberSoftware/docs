# Users

A user refers to an individual account within the platform. Users can have roles and be linked to properties of different products.


> [!WARNING]
> To create a new user, the company **must** first add a domain. The user's email address must correspond to the added domain.

> [!WARNING]
> Managing users efficiently is crucial for maintaining the security and integrity of your platform. 


## Create User
To create a new user into the platform, click on the `Create new`  button

![create_new.png](/create_new.png)

prominently located at the upper right corner of the interface.

> [!INFO]
> **Email** is used as the primary identifier for a user. It is essential for authentication purposes. Ensure that the provided email is valid and accessible by the user. 

![create_user.png](create_user.png ':size=500x300 :border-radius=10px')


> [!WARNING]
>  Be aware that the username cannot be changed after creating a user.

### User Roles and their permissions

- **Admin**:
  - Toggle this option to promote a user to an administrator.
  - Allows the user to log into the security platform.
  - Grants privileges to manage the company's settings.

    ![create_admin.png](/create_admin.png ':size=500x300')

 
- **Network Isolation** <!--Jimber SASE Licence-->:
  - Toggle this option to enable `Network Isolation` <!--`Jimber SASE Licence`--> for this particular user, adding an extra layer of security.
  
    ![access_control.png](/access_control.png ':size=500x300')

  
<!-- > [!INFO]
>  Before adding a user, a domain name must be added first. The users email address must use the added domain name. -->

  
- **Enable Secure mode**:
  - Toggle this option to enable Secure mode.
  - If Secure mode is turned ON for a device all incoming traffic will be blocked unless it comes from the `Jimber SASE Platform`.
  

> [!INFO]
>  Secure mode can only be enabled if Network Isolation is also enabled. 

- **Security Consultant**:
   - This option is only available for **partners**.
   - Enables a particular user to manage configurations of customers.
   <!-- - To gain access, the security consultant must be created as an admin. -->

    <!-- ![security_consultant_2.png](/security_consultant_2.png ':size=800') -->

   - **How to add a security consultant:**

      - Navigate to the partner associated with the customer where you want to add the security consultant. In this example, the partner is **Testpartner**. 

       ![user_in_integrator.png](/user_in_integrator.png ':size=800')

      - Create a new user with the Security Consultant role by toggling the option.

        ![create_sec_cons.png](/create_sec_cons.png ':size=500x300')

      - Return to the Users page of customer where you want to add the security consultant and add the user you created in the previous step (e.g.: 'user3@tel.net') by choosing

       ![btn_add_consultant.png](/btn_add_consultant.png ':size=150x25')
      
      Provide the email address of the user you created ('user3@tel.net') and click 'Add Security Consultant' for this user to become security consultant for that company. 

      ![add_sec_cons.png](/add_sec_cons.png ':size=500x300')

> [!INFO]
>  You can also use an already existing Security Consultant from the partner. In that case you can skip the first step.      
     

## Edit User
  
 Users can be edited by clicking on the![pencil_2.png](/icon_edit.png ':size=35') icon next to their name.
 
  ![edit_user.png](/edit_user.png ':size=500x350')
  
  The username cannot be changed, as stated earlier, but all other options are the same as when creating a user.
  
## Deleting User

 Users can be deleted by clicking on the![recycle_bin.png](/icon_delete.png ':size=35') icon next to their name.
 
 You will receive a warning before the user is permanently deleted:
 
 ![deleting_user.png](/deleting_user.png ':size=500x150')


## User properties

In the user overview, several key properties are immediately visible: the user's role within the company (e.g., Admin or User), their platform role (typically 'User'), and the status of both the user account and Secure Mode.

 ![overview_users.png](/overview_users.png ':size=800x150')

 Clicking on the corresponding strip of a user opens a detailed view with additional information.  

> [!INFO] 
> Avoid using the action buttons at the end of the row (e.g. edit or delete).


![properties_user.png](/properties_user.png ':size=500')


