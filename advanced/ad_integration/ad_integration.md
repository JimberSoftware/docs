# Active Directory Integration

In this section you can see how to integrate users and groups from an Active Directory into the SASE platform.


<!-- UNDER CONSTRUCTION -->

#### In the Active Directory

Create a new user in de AD (e.g. User1) and add the user to the AD group Read-Only Domain Controllers:

![user_in_rodc.png](./screenshots/user_in_rodc.png ':size=500')

Create a new Global Security groups e.g. JimberSASE_Sync and GeneralUsers:

![new_groups.png](./screenshots/new_groups.png ':size=500')


Add your user to the group GeneralUsers. 

Add the group GeneralUsers to the group JimberSASE_Sync. 

![user_in_groups.png](./screenshots/user_in_groups.png ':size=500')


>[!NOTE]
> In the same way, you can add more users and groups that you want to synchronize with the SASE platform.

#### In the SASE platform
 
Open the Jimber SASE platform.

![integrations.png](./screenshots/integrations.png ':size=800')
<!-- 

On the domain controller, open PowerShell and run these two commands: -->

- In the **SASE group field**, enter the Distinguished Name of the group (in this example: CN=JimberSASE_Sync,CN=Users,DC=domainname,DC=be). 
- In the **username field**, enter the Distinguished Name of the user you want to sync (in this example: CN=User1,CN=Users,DC=domainname,DC=be).
- The **password** is the password of the user. 
- Choose the right **network controller**.



Click the Apply button to apply the entered values.

You can check whether the synchronization was successful at the users section.


