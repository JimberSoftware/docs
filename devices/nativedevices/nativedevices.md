# ![](../../images/menu/menu_nativedevices.png ':size=25') Native Devices

Native Devices can be any network devices that are reachable through a Network Controller. Once a Native Device has been created, rules can be applied to the Native Device in the same way rules are applied to servers and NIACs. While traffic to Native Devices is not encrypted at the network layer, they can still be a safe way to reach devices that are only accessible through the Network Controller, by assigning the Network Controller access to a specific VLAN.

<!--While traffic to Native Devices is not encrypted on the network layer, they can be a safe way to reach devices that are only reachable by the Network Controller by connecting or giving access to the Network Controller to a specific VLAN.-->

For instance, should an IP camera be situated within the camera VLAN and access by specific users is required, you can register the camera's IP as a Native Device with the on-premises Network Controller. By establishing the appropriate access rules, users will then be able to access the camera from any location through the `Jimber SASE Platform`.

![scheme1.png](./screenshots/scheme1.png)



### Create Native Device
To create a new native device into the `Jimber SASE Platform`, click on the `+ Create new` button located at the upper right corner of the interface.

![create_native.png](./screenshots/create_native.png ':size=500x350')
                    
The hostname is mandatory and must be alphanumeric. Select the appropriate network controller and enter the valid IP address.

> [!INFO] 
> Once the Native Device is created, the admin needs to add a [Allow Custom Port](/./rules/customports/customports.md).rule that gives specific groups access to the Native Device (under destination).

 **For example:**

 We create a Native Device 'Websitetest':

![example_native_device.png](./screenshots/example_native_device.png ':size=800')

 Now we add a new 'Allow Custom Port' rule where group testers77 can ping the Native Device called 'Websitetest'. 
 
 ![allow_custom_ports_2.png](./screenshots/allow_custom_ports_2.png ':size=800')
 
 All other groups can't reach the Native Device unless specifically allowed by adding a new 'Allow Custom Port' rule.

> [!INFO] 
> You can also add attribute services. 

Choose the Native Device as 'Destination'.

![add_attr_services.png](./screenshots/add_attr_services.png ':size=800')


### Details of a Native Device

Clicking on the corresponding strip of a device opens a detailed view with additional information.

![details_native.png](./screenshots/details_native.png ':size=800')

### Filter Native Devices

You can search the list of native devices using the search box at the top of the page. This helps you quickly find and manage the native device you're looking for.

- Use the search box to enter keywords and filter the native device list.

Next to the search box, there is a filter icon ![](../../images/icons/icon_filter.png ':size=20'). When clicked, it reveals advanced filtering options where you can define additional conditions based on the following three elements:

- **Property**: A dropdown menu where you choose the field to filter on.
- **Match type**: A dropdown that allows you to select how to match the value (`equals`or `contains`).
- **Value**: Enter or select the value to match, depending on the selected property.

![filter_nd.png](./screenshots/filter_nd.png ':size=400')

To add multiple filters you can press the filter icon ![](../../images/icons/icon_filter.png ':size=20') again and then press the `+` button.

> [!INFO]
> You can refresh the list of native devices by pressing the refresh icon ![](../../images/icons/icon_reload.png ':size=20') at the top of the page.


### Edit a Native Device
  
 A native device can be edited by clicking on the edit icon ![](../../images/icons/icon_edit.png ':size=20') in its row.
 
  ![edit_native.png](./screenshots/edit_native.png ':size=500x350')

   
### Delete a Native Device

 A native device can be deleted by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in its row.
 
 You will receive a warning before the device is permanently deleted:
 
 ![delete_native.png](./screenshots/delete_native.png ':size=500')
  