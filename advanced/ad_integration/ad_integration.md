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


##### 1. Create a new group with the same name as in the Active Directory, in this example GeneralUsers. 

![same_group.png](./screenshots/same_group.png ':size=500')

##### 2. Configure the DNS forwarder
   - Go to Company > Integrations
   - At the top of the page, you can find the configuration setting.
   - Add the Network Isolation IP of the Domain Controller here.


   ![dnsforwarding.png](./screenshots/dnsforwarding.png ':size=500')

>[!NOTE]
> Clients with DNS override enabled are filtered through our DNS service.
>
> Domain-specific queries are still resolved by the server you specify in this field.

##### 3. Sync
- Go to Company > Integrations

![integrations.png](./screenshots/integrations.png ':size=600')
<!-- 

On the domain controller, open PowerShell and run these two commands: -->

- In the **SASE Group field**, enter the Distinguished Name of the group (in this example: CN=JimberSASE_Sync,CN=Users,DC=domainname,DC=be). 
- In the **Username field**, enter the Distinguished Name of the user you want to sync (in this example: CN=User1,CN=Users,DC=domainname,DC=be).
- The **Password** is the password of the user. 
- Choose the right **Network Controller**.

>[!WARNING]
> Don't forget to click the`Apply`button to apply the entered values.

##### 4. Group Domain Controllers

- Go to Company > Groups
- Create a new group **Domain Controllers**

![create_group_dc.png](./screenshots/create_group_dc.png ':size=500')

- Add the domain controller to this new group 
    - Go to Company > Devices > Servers
    - Edit the domain controller

![edit_server_dc.png](./screenshots/edit_server_dc.png ':size=500')

![update_dc.png](./screenshots/update_dc.png ':size=500')

>[!WARNING]
> Don't forget to click the`Submit server`button to apply the changes.

##### 5. Ports

- Go to Security > Services
- Click on the`+ Create new`button located at the upper right corner of the interface.
- Click on the`Load template`button at the bottom of the page.

![template_for_ad.png](./screenshots/template_for_ad.png ':size=500')

- Use the existing **Active Directory** template.

![choose_template.png](./screenshots/choose_template.png ':size=500')

>[!WARNING]
> Don't forget to click the`Apply template`button to apply the template.

##### 6. Attribute Services

- Go to Security > Attribute Services
- Choose `Add service`:
    - Group: Domain Controllers
    - Service: Domain controller service
    - Destination: domain controller 

![attribute_service.png](./screenshots/attribute_service.png ':size=500')

>[!WARNING]
> Don't forget to click the`Submit service`button to submit the service.


<!-- You can check whether the synchronization was successful at the users section. -->


