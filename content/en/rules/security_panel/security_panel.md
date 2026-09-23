# Security Panel

When you click on the Jimber tray icon, a menu appears with several available options. Here you can select `Security Panel`:

![Screenshot of the Jimber Tray Menu](./screenshots/jimber_tray.png ':size=300')


Aside from the Security Panel, the menu offers other information about your connection to the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***, such as your login status, user details, the company you are connected to, and your ***_<span style="color: darkblue;">Jimber SASE Platform</span>_*** IP address.


Here you can either quit the application, disconnect (and reconnect) to the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***, or log out from the platform. Note that you will need to log back in with your credentials if you choose this option.

Finally, the menu allows you to toggle **Stealth mode** for your session. Stealth mode ensures that traffic is sent via encrypted HTTP and is designed to make VPN connections possible in environments that would normally block them, such as public hotspots, airports, or countries with strict internet censorship. It works by disguising VPN traffic to look like regular internet traffic, helping you bypass network restrictions.
**Stealth mode** is only available in certain situations where your connection is recognized as external to the Jimber SASE cloud environment, so you have to be connected to the **cloud network controller**. 

> [!IMPORTANT]
> To be able to use **Stealth mode** the user has to be member of a group that 'Allow Mobile connection' to be set in Group Configuration.

![group_configuration.png](./screenshots/group_configuration_2.png ':size=800')


> [!WARNING]
> **Stealth mode** is not available when you are connected to on-premises network controller(s).



Clicking **Security Panel** opens a new browser tab. By default, the Services tab is shown, and depending on the configured services, the screen you see may vary.

![Screenshot of the Services tab of the Security Panel](./screenshots/secure_panel.png ':size=700')

The services listed on this page depend on the configurations set under Services in the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_*** and are specific to the group the user belongs to. Clicking the `Open →` link launches the selected service, for example opening the company wiki page.

> [!INFO]
> More information on configuring services can be found [here](/./rules/services/services.md).

Selecting the second option in the sidebar, Devices, displays a screen where you can inspect all your devices.

![Screenshot of the Devices tab of the Security Panel](./screenshots/sec_pan_devices.png ':size=700')

> [!NOTE]
> All devices will appear in the list after installing the **_Jimber SASE Client_** and running it on the device to sign in to the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***.
<!-- >
>The `+ Create new` button will only be visible if the Group Configuration **MOBILE CONNECTION** is enabled for the group the user belongs to. 
>
> More information on Group Configuration can be found [here](/./rules/groupconfiguration/groupconfiguration.md). -->


<!-- You can add a new mobile device by clicking on the `+ Create new` button located at the upper right corner of the interface.  -->

## Installing Jimber SASE on a mobile device

**Step 1**

Search in the Play Store or in the App Store for ***_<span style="color: darkblue;">Jimber SASE</span>_*** and install the app.   

<!-- ![Screenshot of step 1 of adding a User Device](./screenshots/scan_device.png ':size=500') -->

**Step 2** 

Open the app and sign in to your account: 

![log_in](./screenshots/sign_in.png ':size=300')

> [!NOTE]
> If you don't have a login yet, please reach out to your network administrator to set up an account for you.

**Step 3**

You wil be asked to enter a verification code.

![verification_code](./screenshots/verification_code.jpg ':size=150')

Follow the instructions and enter the code. Click *Verify*.

**Step 4**

Choose a name for your added mobile device and hit *Submit*

![choose_name](./screenshots/choose_name.jpg ':size=150')

You will get a message that **_Jimber SASE_** will establish a VPN-connection. You can click *OK*.

![VPN_connection.jpg](./screenshots/VPN_connection.jpg ':size=150')

**Step 5**

In the next screen, toggle the switch to turn on **_Jimber SASE_**.  

![turn_on](./screenshots/turn_on_jimber.jpg ':size=150')

<!-- In Step 3, you are provided with a different QR code to connect the mobile device to your user account on the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***. Follow the instructions in this step to scan the code using the application.

![Screenshot of step 3 of adding a User Device](./screenshots/add_user_device_2.png ':size=500')

After confirming the installation by clicking `I have configured my device`, your mobile device will be added to the list.  -->
The mobile device can now be found in the list of devices. 

>[!Warning]
> The user will not be able to add a new mobile device if the Group Configuration **DEVICE LIMIT** is enabled and the maximum number of allowed devices has already been reached.