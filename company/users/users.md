# Users

A user is a user on the platform. Users can have roles and be linked to properties of different products.


> [!WARNING]
> In order to create a new user, the company **must** have a domain.

> [!WARNING]
> Managing users efficiently is crucial for maintaining the security and integrity of your platform. 


## Create a New User
To create a new user into the platform, click on the `Create new`  button

![create_new.png](/create_new.png)

prominently located at the upper right corner of the interface.

> [!INFO]
> **Email** is used as the primary identifier for a user. It is essential for authentication purposes. Ensure that the provided email is valid and accessible by the user. 

![newuser_2.png](newuser_2.png)

 Groups are optional. 

### User Roles and their permissions

- **Admin**:
  - Allows the user to log into the security platform.
  - Grants privileges to manage the company's settings.
  - To promote a user to an administrator, hit the slider.

    ![create_admin.png](/create_admin.png ':size=500x350')


 
- **Enable Network Isolation**:
  - Activating this option will enable `Network Isolation` for the particular user, adding an extra layer of security.
  - To activate Network Isolation, hit the slider.
  
    ![access_control.png](/access_control.png ':size=500x350')
  

> [!INFO]
>  Before adding a user, a domain name must be added first. The users email address must use the added domain name.

  
- **Enable Secure mode**:
  - If Secure mode is turned ON for a device all incoming traffic will be blocked unless it comes from Network Isolation.
  - To turn on Secure mode, hit the slider.

- **Security Consultant**:
   - This option is only available for **integrators**.
   - Enables a user to manage configurations of customers.
   <!-- - To gain access, the security consultant must be created as an admin. -->

    ![security_consultant_2.png](/security_consultant_2.png ':size=800')

   - **How to add security consultant:**

      - Go to the integrator of the customer where you want to add the security consultant to. In the example, that is 'User2'. 

       ![user_in_integrator.png](/user_in_integrator.png ':size=800')

      - Create a new user as Security Consult by hitting the slider.

        ![create_sec_cons.png](/create_sec_cons.png ':size=800')

      -After creating that user (e.g.: ' user_sec_cons@testdomein2.be') select the correct customer and then the option "Users". Create a new user, using the user just created in previous step (' user_sec_cons@testdomein2.be').

      ![add_sec_cons.png](/add_sec_cons.png ':size=800')
      
     

## Editing a User
  
 Users can be edited by clicking on the yellow pencil icon next to their name ![pencil_2.png](/pencil_2.png).
 
  ![edit_user.png](/edit_user.png ':size=500x350')
  
  The username cannot be changed, of course, but all other options are the same as when creating a user.
  
## Deleting a User

 Users can be deleted by clicking on the red trash bin icon next to their name ![recycle_bin.png](/recycle_bin.png).
 
 You will receive a warning before the user is permanently deleted:
 
 ![deleting_user.png](/deleting_user.png ':size=500')


 