# Users

A user is a user on the platform. Users can have roles and be linked to properties of different products.


> [!WARNING]
> In order to create a new user, the company **must** have a domain, so a domain name must be added first. The users email address must use the added domain name.

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
>  Username cannot be changed after creating a user! 

### User Roles and their permissions

- **Admin**:
  - Allows the user to log into the security platform.
  - Grants privileges to manage the company's settings.
  - To promote a user to an administrator, hit the slider.

    ![create_admin.png](/create_admin.png ':size=500x300')


 
- **Enable Network Isolation**:
  - Activating this option will enable `Network Isolation` for the particular user, adding an extra layer of security.
  - To activate Network Isolation, hit the slider.
  
    ![access_control.png](/access_control.png ':size=500x300')

  
<!-- > [!INFO]
>  Before adding a user, a domain name must be added first. The users email address must use the added domain name. -->

  
- **Enable Secure mode**:
  - If Secure mode is turned ON for a device all incoming traffic will be blocked unless it comes from Network Isolation.
  - To turn on Secure mode, hit the slider.

> [!INFO]
>  Secure mode can only be enabled if Network Isolation is also enabled. 

- **Security Consultant**:
   - This option is only available for **partners**.
   - Enables a particular user to manage configurations of customers.
   <!-- - To gain access, the security consultant must be created as an admin. -->

    <!-- ![security_consultant_2.png](/security_consultant_2.png ':size=800') -->

   - **How to add a security consultant:**

      - Go to the partner of the customer where you want to add the security consultant to. In the example, that is **Testpartner**. 

       ![user_in_integrator.png](/user_in_integrator.png ':size=800')

      - Create a new user as Security Consultant by hitting the slider.

        ![create_sec_cons.png](/create_sec_cons.png ':size=500x300')

      -After creating that user (e.g.: ' user3@tel.net') select the correct **Customer** and then the option "Users". Choose 
       ![btn_add_consultant.png](/btn_add_consultant.png ':size=150x25')
      
      
      The email that must provided is the one of the user just created in previous step (' user3@tel.net'). That user becomes a Security Consultant for that company.

      ![add_sec_cons.png](/add_sec_cons.png ':size=500x300')

> [!INFO]
>  You can also use an already existing Security Consultant from the partner. In that case you can skip the first step.      
     

## Edit User
  
 Users can be edited by clicking on the yellow pencil icon next to their name ![pencil_2.png](/icon_edit.png ':size=35').
 
  ![edit_user.png](/edit_user.png ':size=500x350')
  
  The username cannot be changed, of course, but all other options are the same as when creating a user.
  
## Deleting User

 Users can be deleted by clicking on the red trash bin icon next to their name ![recycle_bin.png](/icon_delete.png ':size=35').
 
 You will receive a warning before the user is permanently deleted:
 
 ![deleting_user.png](/deleting_user.png ':size=500x150')


## User properties

 In the overview of the users, you can already see some properties: the role of the user in the company (Admin or User), the platform role that is generally 'User' and whether or not the user and Secure Mode are enabled.

 ![overview_users.png](/overview_users.png ':size=800x150')

 Clicking on the corresponding strip of the user, there appears a window with more details:


![properties_user.png](/properties_user.png ':size=500')


