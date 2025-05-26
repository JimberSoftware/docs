# Active Directory Integration

In this section you can see how to integrate users and groups from an Active Directory into the SASE platform.


<!-- UNDER CONSTRUCTION -->

<!-- I try this in Windows for the screenshots and to adapt the text -->

Create a new user in de AD and add the user to the AD group Read-Only Domain Controllers

Create a new Global Security groups e.g. JimberSASE_Sync and GeneralUsers

Add your users to the group GeneralUsers.

Add the group GeneralUsers to the group JimberSASE_Sync. Also other groups you want to sync with the SASE platform you can add.

Open the Jimber SASE platform

![integrations.png](./screenshots/integrations.png ':size=800')


On the domain controller, open PowerShell and run these two commands:

- In the SASE group field, enter the Distinguished Name of the group (in this example: CN=JimberSASE_Sync,CN=Users,DC=domainname,DC=be). 
- In the username field, enter the Distinguished Name of the user you want to sync. 
- The password is the password of the user. 
- Choose the right network controller.



Click the Apply button to apply the entered values.

You can check whether the synchronization was successful at the users section.

<!-- I try this in Windows for the screenshots and to adapt the text -->

