# Active Directory Integration

In this section you can see how to integrate users and groups from an Active Directory into the SASE platform.

>[!WARNING]
>To enable Active Directory Integration you need at least one on-premise network controller.

![no_on_premise.png](./screenshots/no_on_premise.png ':size=500')


How to setup a network controller you can [here](/./advanced/networkcontrollerssetup/SettingUpServer.md).



#### In the Active Directory

Create a new user in de AD (e.g. **User1**) and add the user to the AD group **Read-Only Domain Controllers**:

![user_in_rodc.png](./screenshots/user_in_rodc.png ':size=500')

> [!IMPORTANT]
> The readonly user, user1, is used for SASE to be able to read the active directory from the domain controller.

Assign the 'Read-Only Domain Controllers' group as the user's primary group.
- Select the properties of the group.

![properties_user.png](./screenshots/properties_user.png ':size=300')

  - Open the **Member of** tab.
  - Select the **Read-Only Domain Controllers** group.
  - Click **Set Primary Group**.

![primary_group.png](./screenshots/primary_group.png ':size=300')

Create new Global Security groups e.g. **JimberSASE_Sync** and **GeneralUsers**:

![new_groups.png](./screenshots/new_groups.png ':size=500')


Add the AD-user to be synchronized (e.g. Jack) to the group GeneralUsers. 

Add the group GeneralUsers to the group JimberSASE_Sync. 

![user_in_groups.png](./screenshots/user_in_groups.png ':size=500')


>[!IMPORTANT]
> Any other user or group you want to synchronize with the SASE platform you have to add to the group GeneralUsers.


#### In the SASE platform
 
Open the Jimber SASE platform.


##### 1. Create a new group with the same name as in the Active Directory, in this example GeneralUsers. 

![same_group.png](./screenshots/same_group.png ':size=500')

##### 2. Configure the DNS forwarder
   - Go to Company > Integrations
   - At the top of the page, you can find the configuration setting.
   - Add the Network Isolation IP of the Domain Controller here.


   ![dnsforwarding.png](./screenshots/dnsforwarding.png ':size=600')

>[!NOTE]
> Clients with DNS override enabled are filtered through our DNS service.
>
> Domain-specific queries are still resolved by the server specified in this field.

##### 3. Sync
- Go to Company > Integrations

![integrations.png](./screenshots/integrations.png ':size=600')
<!-- 

On the domain controller, open PowerShell and run these two commands: -->

- In the **SASE Group field**, enter the Distinguished Name of the group (in this example: CN=JimberSASE_Sync,CN=Users,DC=domainname,DC=be). 
- In the **Username field**, enter the Distinguished Name of the readonly user that was created earlier (in this example: CN=User1,CN=Users,DC=domainname,DC=be).
- The **Password** is the password of the user (in this example the password of User1). 
- Choose the right **Network Controller**.
- Click the **Apply** button to apply the entered values.

>[!TIP]
>To identify the correct distinguished names, you can execute the following commands in PowerShell:
>
>```bash
>   dsquery group -name JimberSASE_Sync
>```
>```bash
>   dsquery user -name user1
>```



##### 4. Group Domain Controllers

- Go to Company > Groups
- Create a new group **Domain Controllers**

![create_group_dc.png](./screenshots/create_group_dc.png ':size=500')

- Add the domain controller to this new group:
    - Go to Company > Devices > Servers
    - Edit the domain controller
    - Add the group **Domain Controllers** to the list of groups via the dropdown list.
    - Click the **Submit** button to apply the changes.

![edit_server_dc.png](./screenshots/edit_server_dc.png ':size=600')

![update_dc.png](./screenshots/update_dc.png ':size=600')


##### 5. Ports

- Go to Security > Services
- Click on the`+ Create new`button located at the upper right corner of the interface.
- Click on the`Load template`button at the bottom of the page.

![template_for_ad.png](./screenshots/template_for_ad.png ':size=600')

- Use the existing **Active Directory** template:
  - Select the correct template.
  - Click the`Apply template`button to apply the template.


![choose_template.png](./screenshots/choose_template.png ':size=500')



##### 6. Service-based policy

- Go to Security > Policies
- Choose `Create new`:


![create_policy_dc.png](./screenshots/create_policy_dc.png ':size=600')

Follow these steps:
- Choose a name for the policy.
- Choose `Add Services` and select the correct service:

![choose_service.png](./screenshots/choose_service.png ':size=500')

- Choose `Add sources` and select the group **Domain Controllers**

![choose_source.png](./screenshots/choose_source.png ':size=500')

  - Choose `Add Destinations`. Select the domain controller.  

![choose_destination.png](./screenshots/choose_destination.png ':size=500')




>[!IMPORTANT]
> Don't forget to click the`Save`button after each step.

>[!TIP]
> To easily find the correct components, you can use the search box and/or the type dropdown list 
>
>![se_type_box.png](./screenshots/se_type_box.png ':size=400').





<!-- You can check whether the synchronization was successful at the users section. -->


After selecting the different components, you need to click the `Submit` button to apply the changes:

![result_attribute.png](./screenshots/result_attribute.png ':size=600')

After submitting the policy, you should find it in the overview of the `policies`.

![overview_att_policy.png](./screenshots/overview_att_policy.png ':size=800').



