### Synology

>[!INFO]
> Support is currently provided for Synology NAS running **DMS 7+**. If you're using an earlier version, please update or contact our support team for guidance.

#### Initial setup - `Optional`

> [!WARNING]
> These steps are only required if you need to reset your NAS or if you need to find the IP address. 



##### **Reset Synology NAS**

<!-- > [!INFO]
> **Note:** Only perform if you wish to reset to factory settings. -->

> [!WARNING]
> Only perform if you wish to reset to factory settings.
> This will remove everything!

  1. Locate the reset button on the back of the NAS.
  2. Press and hold for ~5 seconds until a beep sounds. Usually you need a sharp pin.

  ![reset_synology](reset_synology.png ':size=100')

  3. Quickly press and hold again until 3 distinct beeps are heard.
  4. Await a final beep signaling the reset completion.

  > [!Warning]
  > After a complete reset of the Synology, you need to reinstall the operating system.

##### **Locate synology NAS**

Make sure you are connected to the same network as the Synology.

- Go to http://find.synology.com/ and search for a nearby synology device.
- You can also directly go to the current internal IP address of the NAS. (Example: http://192.168.0.146:5000)

After locating the Synology, you will see the following screen:

![find_synology](find_synology.png ':size=500')

Click on 'Connect' to start the installation off the software.  

>[!INFO]
> If you don't find any, check the possible reasons below. 

###### Possible reasons
- The synology hasn't started up yet and is not yet discoverable. Refresh the search a few times as it might take some time.
- You are not on the same network as the synology or it is not connected to the internet.
- It is turned off.
- The synology has to be restarted because of some failure. Hold the power button until the blue light blinks, then let go. 
Wait until it is turned off, then press the power button again. Wait until you hear a beep before it can be found on https://find.synology.com (+- 1 minute).


#### Preparation
Go to https://signal.jimber.io/ and add a new server to the signal interface. 

![create_synology](create_synology.png ':size=500')

Make sure to copy the **Token** and **Hostname** to a notepad. 

By default you will be able to access the NAS through the hostname. 

>[!INFO]
> On Windows you will have to append **.local**. Any alias you assign to the device will also be resolvable if **DNS Override** is enabled.

##### Create a synology login for network isolation

To make it easier to manage, make a new user on the Synology specifically for the installation of Network Isolation. 

The user will need the following access & permissions: 
  - administrator
  - ssh 

**Creating a new user** can be realized in 'Control Panel', 'User & Group':

![control_panel](control_panel.png ':size=500') 

Please take note of the chosen **username** and **password**. 

**Enable SSH** - Only required during the installation.

Enable SSH can be realized in 'Control Panel', 'Terminal & SNMP':

![control_panel_ssh](control_panel_ssh.png ':size=500') 

![ssh_settings](ssh_settings.png ':size=500')


#### Installing Network Isolation on your Synology

Download the latest version for your Synology from [downloads](https://signal.jimber.io/downloads) (no need to login) or use the link in the sidebar.

> [!INFO]
> To download another specific version, you can use this [link](https://signal.jimber.io/clients).


<!-- ![Find the correct synology package](head-to-synology-downloads.png ':size=300x')
![Find the correct synology package](head-to-synology-downloads2.png ':size:700x')
![Find the correct synology package](head-to-synology-downloads3.png ':size=500x')
![Find the correct synology package](find-synology-version.png ':size=800x')
![Find the correct synology package](head-to-synology-downloads4.png ':size=500x') -->

![Find the correct synology package](choose_download_syn.png ':size=200')
![Find the correct synology package](download_synology.png ':size=700') 

![Find the correct synology package](download_syn_warning.png ':size=500x250') 

![Find the correct synology package](info_center.png ':size=500') 

![Find the correct synology package](choose_model.png ':size=500x250') 

This will download the latest SPK version for your NAS.

##### Installation

Choose Package Center in the taskbar and then Manuel Install in the right upper corner.

![Install the SPK](install-spk.png ':size=700')

Follow the sequence shown in the screenshots below to properly install the SPK.

![Install the SPK](install-spk2.png ':size=700')
![Install the SPK](install-spk3.png ':size=700')

![Install the SPK](install-spk5.png ':size=700')
![Install the SPK](install-spk6.png ':size=700')

After installation you get the message that the installation was successful.

![Install the SPK](install_syn_succes.png ':size=500')


Wait about 30 to 60 seconds and now you will see that the NAS has been successfully added to Network Isolation, indicated by the green dot next to the name.

![NAS online](nas-online.png ':size=500')

##### Most commonly used ports for the Synology NAS

Ports

- 22
- 80
- 5000
- 445


**Configuring rules** to be found in the SECURITY section of the sidebar.

