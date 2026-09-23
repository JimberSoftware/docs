# ![](../../images/menu/menu_nativedevices.png ':size=25') Native Devices

Native Devices can be any network devices that are reachable through a Network Controller. Once a Native Device has been created, rules can be applied to the Native Device in the same way rules are applied to servers and NIACs. While traffic to Native Devices is not encrypted at the network layer, they can still be a safe way to reach devices that are only accessible through the Network Controller, by assigning the Network Controller access to a specific VLAN.

<!--While traffic to Native Devices is not encrypted on the network layer, they can be a safe way to reach devices that are only reachable by the Network Controller by connecting or giving access to the Network Controller to a specific VLAN.-->

For instance, should an IP camera be situated within the camera VLAN and access by specific users is required, you can register the camera's IP as a Native Device with the on-premises Network Controller. By establishing the appropriate access rules, users will then be able to access the camera from any location through the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***.

![scheme1.png](./screenshots/scheme1.png)



### Create Native Device
To create a new native device into the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***, click on the `+ Create new` button located at the upper right corner of the interface.

![create_native.png](./screenshots/create_native.png ':size=400')
                    
The hostname is mandatory and must be alphanumeric. Also the IP address and the network controller are required.

Select the appropriate network controller and enter the valid IP address.

<!-- > [!IMPORTANT] 
> Once the Native Device is created, the admin needs to add a [Allow Custom Port](/./rules/customports/customports.md) rule that gives specific groups access to the Native Device (under destination). -->
<!-- Now we add a new 'Allow Custom Port' rule where group testers77 can ping the native device called 'Websitetest'. 
 
 ![allow_custom_ports_2.png](./screenshots/allow_custom_ports_2.png ':size=800')
 
 All other groups can't reach the Native Device unless specifically allowed by adding a new 'Allow Custom Port' rule.

> [!INFO] 
> You can also add attribute services. 

Choose the Native Device as 'Destination'.

![add_attr_services.png](./screenshots/add_attr_services.png ':size=800')
 -->

> [!IMPORTANT] 
> Once the Native Device is created, the admin needs to add a [Policy](./rules/firewall-policies/firewall-policies) that gives specific groups access to the Native Device.

 **For example:**

 We create a Native Device 'Websitetest':

![example_native_device.png](./screenshots/example_native_device.png ':size=700')

 Now we add a new [Policy](./rules/firewall-policies/firewall-policies):
 - **Destinations**: name of the native device.
 - **Sources**: groups that you want to grant access to the native device.
 - **Services**: [services](./rules/services/services) that create Access Rules defining start port and end port, and the protocol through which the service will communicate.

 ![policy_for_nd.png](./screenshots/policy_for_nd.png ':size=700')

 ![create_service_for_nd.png](./screenshots/create_service_for_nd.png ':size=700')
 
 >[!ATTENTION]All other groups can't reach the Native Device unless specifically allowed by adding a group as new source.



### Details of a Native Device

Clicking on the corresponding strip of a device opens a detailed view with two tabs: Details and Security.  

Details provides some additional information.
 
![details_native.png](./screenshots/details_native.png ':size=500')

The service tab gives an overview of the attached services.

![services_native.png](./screenshots/services_native.png ':size=500')

### Filter Native Devices

You can search the list of native devices using the search box at the top of the page. This helps you quickly find and manage the native device you're looking for.

Next to the search box, there is a filter icon ![](../../images/icons/icon_filter.png ':size=20'). When clicked, it reveals advanced filtering options where you can define additional conditions based on the following three elements:

- **Property**: A dropdown menu where you choose the field to filter on.
- **Match type**: A dropdown that allows you to select how to match the value (`EQUALS`, `CONTAINS`, or `NOT`).
- **Value**: Enter or select the value to match, depending on the selected property.

![filter_nd.png](./screenshots/filter_nd.png ':size=500')

To add multiple filters you can press the filter icon ![](../../images/icons/icon_filter.png ':size=20') again and then press the `+` button.

> [!TIP]
> You can refresh the list of native devices by pressing the refresh icon ![](../../images/icons/icon_reload.png ':size=20') at the top of the page.


### Edit a Native Device
  
 A native device can be edited by clicking on the edit icon ![](../../images/icons/icon_edit.png ':size=20') in its row.
 
  ![edit_native.png](./screenshots/edit_native.png ':size=400')

   
### Delete a Native Device

 A native device can be deleted by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in its row.
 
 You will receive a warning before the device is permanently deleted:
 
 ![delete_native.png](./screenshots/delete_native.png ':size=400')
  
