# Native Devices

Native Devices can be any network device that is reachable through a Network Controller. Once a Native Device has been created, rules can be applied to the Native Device the same way rules are applied to servers and NIACs. While traffic to Native Devices is not encrypted on the network layer, they can be a safe way to reach devices that are only reachable by the Network Controller by connecting or giving access to the Network Controller to a specific VLAN.

For instance, should an IP camera be situated within the camera VLAN and access by specific users is required, you can register the camera's IP as a Native Device with the on-premises Network Controller. By establishing the appropriate access rules, users will then be able to access the camera from any location through Jimber Network Isolation.

![scheme1.png](scheme1.png)



## Create a new Native Device
To create a new user into the platform, click on the `Create new`  button

![create_new.png](/create_new.png)

prominently located at the upper right corner of the interface.


![create_native.png](/create_native.png ':size=500x350')
                    
The hostname is mandatory and must be alphanumeric. Select the appropriate network controller and enter the valid IP address.

## Editing a Native Device
  
 A native device can be edited by clicking on the yellow pencil icon next to its name ![pencil_2.png](/pencil_2.png).
 
  ![edit_native.png](/edit_native.png ':size=500x350')
  
  
  ## Deleting a Native Device

 A native device can be deleted by clicking on the red trash bin icon next to its name ![recycle_bin.png](/recycle_bin.png).
 
 You will receive a warning before the device is permanently deleted:
 
 ![delete_native.png](/delete_native.png ':size=500')
  