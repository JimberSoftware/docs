# Native Devices

Native Devices can be any network device that is reachable through a Network Controller. Once a Native Device has been created, rules can be applied to the Native Device the same way rules are applied to servers and NIACs. While traffic to Native Devices is not encrypted on the network layer, they can be a safe way to reach devices that are only reachable by the Network Controller by connecting or giving access to the Network Controller to a specific VLAN.

For instance, should an IP camera be situated within the camera VLAN and access by specific users is required, you can register the camera's IP as a Native Device with the on-premises Network Controller. By establishing the appropriate access rules, users will then be able to access the camera from any location through Jimber Network Isolation.

![scheme1.png](scheme1.png)