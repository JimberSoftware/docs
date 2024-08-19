#### Synology

>[!INFO]
> Support is currently provided for Synology NAS running **DMS 7+**. If you're using an earlier version, please update or contact our support team for guidance.

### Initial setup - `Optional`

> [!WARNING]
> These steps are only required if you need to reset your NAS or if you need to find the IP address. 


<!-- tabs:start -->

#### **Reset Synology NAS**

<!-- > [!INFO]
> **Note:** Only perform if you wish to reset to factory settings. -->

> [!WARNING]
> Only perform if you wish to reset to factory settings.
> This will remove everything!

  1. On the NAS back, locate the reset button.
  2. Press and hold for ~5 seconds until a beep sounds.
  3. Quickly press and hold again until 3 distinct beeps are heard.
  4. Await a final beep signaling the reset completion.

#### **Locate synology nas.**

Make sure you are connected to the same network as the synology.

- Go to http://find.synology.com/ and search for a nearby synology device.
- You can also directly go to the current internal IP address of the NAS. (Example: http://192.168.0.146:5000)

If you don't find any, check the possible reasons below.
#### Possible reasons
- The synology hasn't started up yet and is not yet discoverable. Refresh the search a few times as it might take some time.
- You are not on the same network as the synology or it is not connected to the internet.
- It is turned off.
- The synology has to be restarted because of some failure. Hold the power button until the blue light blinks, then let go. 
Wait until it is turned off, then press the power button again. Wait until you hear a beep before it can be found on https://find.synology.com (+- 1 minute).

<!-- tabs:end -->


#### Preparation
Go to https://signal.jimber.io/ and add a new server to the signal interface. 

![create_synology](create_synology.png ':size=500')

Make sure to copy the **Token** and **Hostname** to a notepad. 

By default you will be able to access the NAS through the hostname. 

>[!INFO]
> On Windows you will have to append **.local**. Any alias you assign to the device will also be resolvable if **DNS Override** is enabled.

##### Create a synology login for network isolation

To make it easier to manage, make a new user on the synology specifically for the installation of Network Isolation. 

Please take note of the chosen **username** and **password**. 

The user will need the following access & permissions: 
- administrator
- ssh 

##### Enable SSH - Only required during the installation. 

![Enable SSH](synology-enable-ssh.png ':size=700')

![Enable SSH](synology-enable-ssh2.png ':size=700')

##### Download the correct package for your synology.

<!-- ![Find the correct synology package](head-to-synology-downloads.png ':size=300x')
![Find the correct synology package](head-to-synology-downloads2.png ':size:700x')
![Find the correct synology package](head-to-synology-downloads3.png ':size=500x')
![Find the correct synology package](find-synology-version.png ':size=800x')
![Find the correct synology package](head-to-synology-downloads4.png ':size=500x') -->

![Find the correct synology package](choose_download_syn.png ':size=200')
![Find the correct synology package](download_synology.png ':size=700')
![Find the correct synology package](download_syn_warning.png ':size=500x250')
![Find the correct synology package](find-synology-version.png ':size=700')
![Find the correct synology package](choose_model.png ':size=500x250')

This will download the latest SPK version for your NAS.

##### Installation

Follow the sequence shown in the screenshots below to properly install the SPK.

![Install the SPK](install-spk.png 'size:=800x')
![Install the SPK](install-spk2.png 'size:=800x')
![Install the SPK](install-spk3.png 'size:=800x')
![Install the SPK](install-spk4.png 'size:=800x')
![Install the SPK](install-spk5.png 'size:=800x')
![Install the SPK](install-spk6.png 'size:=800x')

Wait about 30 to 60 seconds and now you will see that the nas has been successfully added to network isolation. (Indicated by the green circle next to the name.)

![Nas online](nas-online.png 'size:=800x')

##### Most commonly used ports for the synology nas

Ports

- 22
- 80
- 5000
- 445


[Learn how to configure rules.](../../rules/rules.md)

