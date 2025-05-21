# Security Panel

<!-- ## **Under construction...** -->

When you click on the Jimber tray icon, a menu appears with several available options. Here you can select `Security Panel`:

![Screenshot of the Jimber Tray Menu](./screenshots/jimber_tray.png ':size=300')

Clicking this option opens the Security Panel in a new browser tab. By default, the Services tab is shown, depending on the configured services, the screen you see may vary.

![Screenshot of the Services tab of the Security Panel](./screenshots/secure_panel.png ':size=700')

The services listed on this page depend on the configurations set under Services in the *`Jimber SASE Platform`* and are specific to the group the user belongs to. Clicking the `Open →` link launches the selected service, for example opening the company wiki page.

> [!INFO]
> More information on configuring services can be found [here](/./rules/services/services.md).

Selecting the second option in the sidebar, Devices, displays a screen where you can inspect and add your mobile devices.

![Screenshot of the Devices tab of the Security Panel](./screenshots/sec_pan_devices.png ':size=700')

> [!WARNING]
> Users can only create new mobile devices on this page. Other devices like laptops, PCs and servers will appear in the list after installing the *`Jimber SASE Client`* and running it on the device to sign in to the *`Jimber SASE Platform`*.
>
>The `+ Create new` button will only be visible if the Group Configuration **MOBILE CONNECTION** is enabled for the group the user belongs to. 
>
> More information on Group Configuration can be found [here](/./rules/groupconfiguration/groupconfiguration.md).


You can add a new mobile device by clicking on the `+ Create new` button located at the upper right corner of the interface. 

In step 1, you are provided with a QR code to install the Jimber Network Isolation application.<!--Jimber SASE Application--> If you have already installed the application, you may skip this step.

![Screenshot of step 1 of adding a User Device](./screenshots/scan_device.png ':size=500')

In step 2, you can choose a name for your new mobile device.

![Screenshot of step 2 of adding a User Device](./screenshots/add_user_device.png ':size=500')

In Step 3, you are provided with a different QR code to connect the mobile device to your user account on the *`Jimber SASE Platform`*. Follow the instructions in this step to scan the code using the application.

![Screenshot of step 3 of adding a User Device](./screenshots/add_user_device_2.png ':size=500')

After confirming the installation by clicking `I have configured my device`, your mobile device will be added to the list. 

>[!Warning]
> The user will not be able to add a new mobile device if the Group Configuration **DEVICE LIMIT** is enabled and the maximum number of allowed devices has already been reached.