# Native Devices

Native Devices can be any network devices that are reachable through a Network Controller. Once a Native Device has been created, rules can be applied to the Native Device in the same way rules are applied to servers and NIACs. While traffic to Native Devices is not encrypted at the network layer, they can still be a safe way to reach devices that are only accessible through the Network Controller, by assigning the Network Controller access to a specific VLAN.

<!--While traffic to Native Devices is not encrypted on the network layer, they can be a safe way to reach devices that are only reachable by the Network Controller by connecting or giving access to the Network Controller to a specific VLAN.-->

For instance, should an IP camera be situated within the camera VLAN and access by specific users is required, you can register the camera's IP as a Native Device with the on-premises Network Controller. By establishing the appropriate access rules, users will then be able to access the camera from any location through the `Jimber SASE Platform`.

![scheme1.png](scheme1.png)



## Create Native Device
To create a new native device into the `Jimber SASE Platform`, click on the `Create new`  button

![create_new.png](/create_new.png)

prominently located at the upper right corner of the interface.


![create_native.png](/create_native.png ':size=500x350')
                    
The hostname is mandatory and must be alphanumeric. Select the appropriate network controller and enter the valid IP address.

> [!INFO] 
> Once the Native Device is created, the admin needs to add a [Allow Custom Port](/./rules/customports/customports.md).rule that gives specific groups access to the Native Device (under destination).

 **For example:**

 We create a Native Device 'Websitetest':

![example_native_device.png](/example_native_device.png ':size=800')

 Now we add a new 'Allow Custom Port' rule where group testers77 can ping the Native Device called 'Websitetest'. 
 
 ![allow_custom_ports_2.png](/allow_custom_ports_2.png ':size=800')
 
 All other groups can't reach the Native Device unless specifically allowed by adding a new 'Allow Custom Port' rule.

> [!INFO] 
> You can also add attribute services. 

Choose the Native Device as 'Destination'.

![add_attr_services.png](/add_attr_services.png ':size=800')


## Details of a Native Device

To view the details of a specific Native Device, select its row in the table (rather than using the action buttons at the end). This will reveal any additional information, such as the optional alias.

![details_native.png](details_native.png ':size=800')


## Edit Native Device
  
 A native device can be edited by clicking on the yellow pencil icon next to its name ![icon_edit.png](/icon_edit.png ':size=35').
 
  ![edit_native.png](/edit_native.png ':size=500x350')

   
  
  ## Delete Native Device

 A native device can be deleted by clicking on the red trash bin icon next to its name ![icon_delete.png](/icon_delete.png ':size=35').
 
 You will receive a warning before the device is permanently deleted:
 
 ![delete_native.png](/delete_native.png ':size=500')
  