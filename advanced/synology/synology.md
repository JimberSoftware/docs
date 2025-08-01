# Synology  

>[!INFO]
> Support is currently provided for Synology NAS running **DMS 7+**. If you're using an earlier version, please update or contact our support team for guidance.

### Initial setup - `Optional`

> [!INFO]
> These steps are only required if you need to reset your NAS or if you need to find the IP address. 



##### **Reset Synology NAS**

<!-- > [!INFO]
> **Note:** Only perform if you wish to reset to factory settings. -->

> [!WARNING]
> Only perform if you wish to reset to factory settings.
> This will remove everything!

  1. Locate the reset button on the back of the NAS.
  2. Press and hold for approximately 5 seconds until you hear a beep sound. Usually you need a sharp pin to press the reset button.

  ![reset_synology](./screenshots/reset_synology.png ':size=100')

  3. Release then quickly press and hold again until 3 distinct beeps are heard.
  4. Await a final beep signaling the reset completion.

  > [!Warning]
  > After a complete reset of the Synology, you need to reinstall the operating system.

##### **Locate Synology NAS**

Make sure you are connected to the same network as the Synology.

- Go to http://find.synology.com/ and search for a nearby Synology device.

![search_synology](./screenshots/search_synology.png ':size=500')

>[!INFO]
> If you can't locate the Synology NAS, check following reasons: 
> - The Synology isn't turned on or hasn't started up and is not yet discoverable. Make sure the device is turned on and refresh the search a few times as it might take some time.
> - You are not on the same network as the Synology or it is not connected to the internet.
> - The Synology has to be restarted because of some failure. Hold the power button until the blue light blinks, then let go. Wait until it is turned off, then press the power button again. Wait until you hear a beep before it can be found on https://find.synology.com (+- 1 minute).
- You can also directly go to the current internal IP address of the NAS. (Example: http://192.168.0.146:5000)

After locating the Synology, you will see the following screen:

![find_synology](./screenshots/find_synology.png ':size=500')


Select the correct device, click 'Connect', and accept the EULA. 

![synology_eula.png](./screenshots/synology_eula.png ':size=500')

Click 'Next' to start the software installation.

![connecting_synology](./screenshots/connecting_synology.png ':size=500')



### Preparation
Go to https://signal.jimber.io/ and add a new server to the `Jimber SASE Platform`. 

![create_synology](./screenshots/create_synology.png ':size=500')

Make sure to copy the **Token** and **Hostname** to a notepad. 

By default you will be able to access the NAS through the hostname. 

>[!INFO]
> On Windows you will have to append **.local**. Any alias you assign to the device will also be resolvable if **DNS Override** is enabled.

##### Create a Synology login for Jimber SASE Client

To make it easier to manage, make a new user on the Synology specifically for the installation of the `Jimber SASE Client`. 

The user will need the following access & permissions: 
  - administrator
  - ssh 

**Creating a new user** can be realized in 'Control Panel', 'User & Group':

![control_panel](./screenshots/control_panel.png ':size=500') 

Please take note of the chosen **username** and **password**. 

**Enable SSH** - Only required during the installation.

Enable SSH can be realized in 'Control Panel', 'Terminal & SNMP':

![control_panel_ssh](./screenshots/control_panel_ssh.png ':size=500') 

![ssh_settings](./screenshots/ssh_settings.png ':size=500')


### Installing Jimber SASE Client on your Synology

Download the latest version for your Synology from [downloads](https://signal.jimber.io/downloads) (no need to log in).

> [!INFO]
> To download another specific version, you can use this [link](https://signal.jimber.io/clients).


<!-- ![Find the correct synology package](head-to-synology-downloads.png ':size=300x')
![Find the correct synology package](head-to-synology-downloads2.png ':size:700x')
![Find the correct synology package](head-to-synology-downloads3.png ':size=500x')
![Find the correct synology package](find-synology-version.png ':size=800x')
![Find the correct synology package](head-to-synology-downloads4.png ':size=500x') -->

![Find the correct synology package](./screenshots/choose_download_syn.png ':size=200')
![Find the correct synology package](./screenshots/downloads.png ':size=700') 

![Find the correct synology package](./screenshots/download_syn_warning.png ':size=500x250') 

![Find the correct synology package](./screenshots/info_center.png ':size=500') 

![Find the correct synology package](./screenshots/choose_model.png ':size=500x250') 

This will download the latest SPK version for your NAS.

##### Installation

Choose Package Center in the taskbar and then Manual Install in the right upper corner.

![Install the SPK](./screenshots/install-spk.png ':size=500')

Follow the sequence shown in the screenshots below to properly install the SPK.

![Install the SPK](./screenshots/install-spk2.png ':size=500')
![Install the SPK](./screenshots/install-spk3.png ':size=500')

![Install the SPK](./screenshots/install-spk5.png ':size=500')
![Install the SPK](./screenshots/install-spk6.png ':size=500')

You will receive a confirmation that the installation was successful.

![Install the SPK](./screenshots/install_syn_succes.png ':size=500')


In about 30 to 60 seconds you should be able to see that the NAS has been successfully added to the `Jimber SASE Platform`, as indicated by the green dot next to the hostname.

![NAS online](./screenshots/nas-online.png ':size=500')

##### Most commonly used ports for the Synology NAS

Ports

- 22
- 80
- 5000
- 445


>[!INFO]
>Configuring rules can be found in the [SECURITY](/security.md) section of the sidebar.


