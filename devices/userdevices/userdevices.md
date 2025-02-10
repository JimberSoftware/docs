# User Devices

The "User Devices" section in our security platform provides an overview and management interface for devices associated with your users. Devices can range across various operating systems including Windows, Mac and Linux.

### When are devices visible?

Devices will appear in the "User Devices" list as soon as:

1. The client software corresponding to the device's OS is successfully installed.
2. The user logs in for the first time from the device.

> [!INFO]
> If a device doesn't appear as expected after installation, ensure the device has an active internet connection, the user has logged in successfully, and consider restarting the client or the device.

## Desktop Client installation
Open the page [Jimber SASE downloads](https://signal.jimber.io/downloads) and download the client that matches your operating system:

<!-- ![windows-popup1.png](/start.png ':size=800x') -->
![downloads.png](/downloads.png ':size=600')


### Platforms 

<!-- tabs:start -->

<!-- #### Windows <i class="mdi mdi-microsoft-windows"></i> -->

#### **Windows**
As mentioned, download the latest 'Windows Client' from [Jimber SASE downloads](https://signal.jimber.io/downloads), or use the direct link to access the most recent version for Windows : [latest windows version](https://signal.jimber.io/clients/windows-desktop-latest.msi)

> [!INFO]
> To download another specific version, you can use this [link](https://signal.jimber.io/clients).


Open the downloaded file to install the 'Windows Client'.
When a subsequent dialogue box emerges, please select 'Yes' to proceed.

![windows-popup2.png](/windows-popup2.png ':size=300')

To launch the software, either search for 'Jimber' using the Windows start menu or simply click on the newly created desktop icon.

![windows-search.png](/windows-search.png ':size=600')

Upon launching the software, the Jimber icon will become visible at the bottom right of your screen, indicating that the Network Isolation service is now running. 

> [!INFO]
> The Network Isolation icon  can be hidden. Use the up arrow icon ![arrow_up.png](/arrow_up.png ':size=30') if necessary to view hidden icons.

![windows-tray-icon.png](/windows-tray-icon.png ':size=400')

Click on the Jimber icon and select 'Sign in'. This will launch a browser page for you to sign in.

> [!INFO]
> Once successfully logged in, a green dot will appear on the tray icon as confirmation.




![windows-tray-logged-in.png](/windows-tray-logged-in.png ':size=400')





If you don't have a login yet, please reach out to your network administrator to set up an account for you.

<!-- #### Mac <i class="mdi mdi-apple"></i> -->
#### **Mac**
As mentioned, download the latest 'Mac Client' from [Jimber SASE downloads](https://signal.jimber.io/downloads), or use the direct link to access the most recent version for Mac : [latest mac version](https://signal.jimber.io/clients/mac-x64-latest.dmg)"

In the Downloads folder, you will find the file `SASE-Mac-1.XX.0.dmg`(XX stands for the version number).


![mac_version.png](/mac_version.png ':size=100')

> [!INFO]
> To download another specific version, you can use this [link](https://signal.jimber.io/clients).

Double-click on this file and install the Network Isolation Client by dragging the 'JimberNetworkIsolation' icon into your 'Applications' folder.

![mac_download.png](/mac_download.png ':size=500')

 A pop-up may appear to alert you that you have downloaded a file from the internet, asking if you indeed want to open the file. You can safely answer 'Open' to this prompt.

![mac_install_1.png](/mac_install_1.png ':size=250' )

Following the installation, you'll find the JimberNetworkIsolation icon in your Launchpad. Simply search for 'JimberNetworkIsolation' and press 'Enter' to launch the application.

![mac-install_2.png](/mac_install_2.png ':size=400')

Upon launching the software, the Jimber icon will become visible at the top right of your screen, indicating that the Network Isolation service is now running.

![mac_launchpad.png](/mac_launchpad.png)

Click on the Jimber icon and select 'Sign in'. This will launch a browser page for you to sign in.

![mac-offline-tray.png](/mac-offline-tray.png ':size=300'). 

> [!INFO]
> Once successfully signed in, a green dot will appear on the tray icon as confirmation.


![mac-tray-icon-online.png](/mac-online-tray.png ':size=300')

If you're yet to have a login, please reach out to your network administrator to set up an account for you.


<!-- #### Linux <i class="mdi mdi-ubuntu"></i> -->
#### **Linux**

> [!WARNING]
> Support is currently provided for the latest LTS versions of Ubuntu. For other OS distributions, please reach out to our support team.

As mentioned, download the latest 'Linux Client' from [Jimber SASE downloads](https://signal.jimber.io/downloads), or use the direct link to access the most recent version for Linux : [latest Linux version](https://signal.jimber.io/clients/linux-desktop-latest.deb)

> [!INFO]
> To download another specific version, you can use this [link](https://signal.jimber.io/clients).

![linux-open-deb.png](linux-open-deb.png ':size=300')

In case you're using a default installer, simply double-clicking the file will install the program. 
Without a default installer, you'll encounter the following window by double-clicking.

![linux_no_defaultinstaller](linux_no_defaultinstaller.png ':size=800')

Close the window and browse to Downloads. Right-click on the icon and select 'Open With Other Application'. 

![/linux_open_download](linux_open_download.png ':size=300')

Choose 'Software Install': 

![/linux_chose_software](linux_chose_software.png ':size=300')

Choose 'Install' in the next screen:

![/linux_install_software](linux_install_software.png ':size=300')

Finally, access the program from your system menu by searching for 'Jimber Network Isolation'.

![linux-search.png](/linux-search.png ':size=300')

Upon launching the software, the Jimber icon will become visible at the top right of your screen, indicating that the Network Isolation service is now running.

![linux-tray-icon.png](/linux-tray-icon.png ':size=200')

Click on the Jimber icon and select 'Sign in'. This will launch a browser page for you to sign in. 

> [!INFO]
> Once successfully logged in, a green dot will appear on the tray icon as confirmation.


![linux-tray-logged-in.png](/linux_signed_in.png ':size=200')

If you're yet to have a login, please reach out to your network administrator to set up an account for you.

<!-- tabs:end -->

## User device online/offline

In the overview of user devices, you can see which ones are online or offline:

- A user device online will appear at the top of the list in the overview with a green pc icon.
- A user device offline will appear in the overview with a red pc icon.
- A mobile user device online will appear in the overview with a green mobile device icon. 
- A user device that requires an update will appear in the overview with a yellow warning triangle.

![overview userdevices.png](overviewuserdevices.png ':size=800')


## User device Info

In the overview of the user devices, you can already see some properties: 

- Name of the device.
- Operating System.
- Client Version of the SASE platform.
- Whether Secure Mode is active, disabled, unsupported.
- IP-address.
- Approval status which is normally 'Approved'.


Clicking on the corresponding strip of the user device, there appears a window with more details:

![user_device_info_details.png](user_device_info_details.png ':size=500')

The software tab shows the installed antivirus software:

![user_device_info_software.png](user_device_info_software.png ':size=500')

The info can be copied by using the copy icon ![copy_icon.png](copy_icon.png ':size=25') in the right upper corner.




## Delete user device

Offline user devices can be deleted by clicking on the red trash bin icon next to their name ![icon_delete.png](/icon_delete.png ':size=35').


You will receive a warning before the device is permanently deleted:

![deleting_device.png](deleting_device.png ':size=500')





