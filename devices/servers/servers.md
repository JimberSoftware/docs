# Servers

## Create a server

To create a server in the Security platform, click on the `Create new` button

![create_new.png](/create_new.png)

prominently located at the upper right corner of the interface.


![add_server.png](create_server.png 'size:=500x')

 
> [!INFO] 
> Hostname is mandatory must be a lowercase string.


## Server installation


### Platforms 

#### Windows <i class="mdi mdi-microsoft-windows"></i>

Download the latest version for the 'Windows Server' from https://signal.jimber.io/downloads (no need to login).


Once downloaded, decompress the file and initiate the .msi installation file by double-clicking it.

A dialog box will emerge—confirm the process by selecting 'Yes.'

Subsequently, open the file **`settings.json`** located at C:\Program Files\Jimber\ as an **Administrator**. 
In this file, enter the token you were provided upon creating the server within the Network Isolation interface. 
 
  

```json
{
 "publicKey": "l7D1+dm...",
 "privateKey": "ENjN41TJE7WEU76T...",
 "token": "YOUR_TOKEN"
}
```

> [!WARNING] 
**Attention!** Don't forget the comma at the end of lines and the quotation marks!
Ensure to save the changes made to the file.




The required token can be retrieved from the 'Servers' tab within the Signal server interface. Simply select and edit an existing server to find it.


![edit_server.png](/edit_server.png 'size:=500x')


Access the 'services' panel by entering 'services.msc' into the start menu's search bar. Within this panel, find the 'Jimber Network Isolation' service and initiate a restart.


![services_jimber.png](/services_jimber.png 'size:=800x')


Upon successful restart, the server should display a connected status (indicated by a green dot) in the Network Isolation interface. For any necessary troubleshooting, consult the log file at this location: 
`C:\Program Files\Jimber\jimbernetworkisolation.log`


> [!WARNING]
> **Attention!** When installing a server, Jimber Network Isolation might reset the DNS settings. Please add the "nodns" flag to disable this when using static IP/DNS configuration

```json
{
 "publicKey": "l7D1+dm...",
 "privateKey": "ENjN41TJE7WEU76T...",
 "token": "YOUR_TOKEN",
  "nodns" : "true"
}
```
#### Linux <i class="mdi mdi-ubuntu"></i>

> [!INFO] 
> Support is currently provided for the latest LTS versions of Ubuntu and Debian. For other OS distributions, please reach out to our support team.


Download the latest version for the 'Linux Server' from https://signal.jimber.io/downloads (no need to login).

```bash
sudo apt update
sudo apt install wireguard
wget https://signal.jimber.io/clients/linux-server-latest.deb
sudo dpkg -i linux-server-latest.deb
```

Upon completion of the installation, a new `settings.json` file will be automatically created in the `/etc/jimber/`directory.
Open this file using the text editor of your choice. Within this file, you'll notice an empty token along with newly created public and private keys.

In this file, enter the token you were provided upon creating the server within the Network Isolation interface.

The required token can be retrieved from the 'Servers' tab within the Signal server interface. Simply select and edit an existing server to find it.


![edit_server.png](/edit_server.png 'size:=500x')


```json
{
 "publicKey": "l7D1+dm...",
 "privateKey": "ENjN41TJE7WEU76T...",
 "token": "YOUR_TOKEN"
}
```
> [!WARNING]
> **Attention**! Don't forget the comma at the end of lines and the quotation marks!
Ensure to save the changes made to the file.


Restart the service by executing the following command:
```bash
sudo systemctl restart jimbernetworkisolation.service
```

Once successful, the server will display a connected status, indicated by a green dot, within the Network Isolation interface. If needed, refer to the following log files for debugging purposes:

```bash
cat /var/log/jimber/jimbernetworkisolation.log
```

>[!INFO]
> You can see the installed version using `jimberfw -version`

> [!WARNING]
> **Attention**! When installing a server, Jimber Network Isolation might reset the DNS settings. Please add the "nodns" flag to disable this when using static IP/DNS configuration

```json
{
 "publicKey": "l7D1+dm...",
 "privateKey": "ENjN41TJE7WEU76T...",
 "token": "YOUR_TOKEN",
  "nodns" : "true"
}
```


#### Synology <i class="mdi mdi-nas"></i>

>[!INFO]
> Support is currently provided for Synology NAS running DMS 7.2+. If you're using an earlier version, please update or contact our support team for guidance.


##### **1. NAS Reset (Optional):**
> [!INFO]
> **Note:** Only perform if you wish to reset to factory settings.

  1. On the NAS back, locate the reset button.
  2. Press and hold for ~5 seconds until a beep sounds.
  3. Quickly press and hold again until 3 distinct beeps are heard.
  4. Await a final beep signaling the reset completion.


##### **2. Setup**

##### Find synology online
Make sure you are connected to the same network as the synology. Then go to http://find.synology.com/ and search for a nearby synology device.
If you don't find any, check the possible reasons below.
##### Possible reasons
- The synology hasn't started up yet and is not yet discoverable. Refresh the search a few times as it might take some time.
- You are not on the same network as the synology or it is not connected to the internet.
- It is turned off.
- The synology has to be restarted because of some failure. Hold the power button until the blue light blinks, then let go. 
Wait until it is turned off, then press the power button again. Wait until you hear a beep before it can be found on https://find.synology.com (+- 1 minute).

##### Installation
Connect the synology and go through all the steps, most are straight forward.

While you are waiting for the installation process to finish go to https://signal.jimber.io/ and add a new server to the signal interface. 
Check the 'hostname' and 'Token' of the new server by going to the Server tab and clicking on the yellow pencil button of the server.
These will be used later to make a login for the synology interface.

##### Create login
Once the installation is done you need to make a login. Use the following data to make it easy for other company admins to login. But feel free to use another method.
- Device name: Use the server hostname from the signal interface
- Admin account: Company name
- Password: 'hostname of server with capital first letter' + 'token of the server' + '!'

Example Hostname: synology-nas
Example token: 8vfbdrf
Example password: Synology-test8vfbdrf!

##### Synology interface
After the login has been created go through the final steps that will take you to the synology interface.
- Login
- Go to control panel -> Terminal & SNMP
- Enable SSH service on port 22 and click apply. This will make you able to SSH to the synology and no longer need to use the synology interface.

##### SSH
Find the IP of the synology with http://find.synology.com/
- SSH to the synology using its admin account from the login and IP that you just found earlier. (ex: ssh admin@192.168.40.250)
- Delete the previous './jimbernetworkisolation' folder and the zip if they already exist in the home directory.
- Go to https://signal.jimber.io/clients/ for a list of all clients.
- Search for the 'synology' tag and copy the right version url.
- Go back to the SSH terminal and do the following commands using the url from the previous step.
```
wget https://signal.jimber.io/clients/synology-latest.zip
7z x 'synology-latest.zip'
cd ./jimbernetworkisolation
sudo ./install.sh
```

This will install networkisolation on the synology.


Now go to https://signal.jimber.io to find the token at the servers section after login. There click on the yellow edit pencil of the server to see the 'Token' at the bottom. Copy this token to use in the next step.


![edit_server.png](/edit_server.png 'size:=500x')


Add the token from the server in signal interface to the jimber settings file. 
```
vi /etc/jimber/settings.json
```

The file will look like this, change 'YOUR_TOKEN' with the token you copied from the previous step. Don't change anything else!

```json
{
 "publicKey": "l7D1+dm...",
 "privateKey": "ENjN41TJE7WEU76T...",
 "token": "YOUR_TOKEN"
}

```

> [!WARNING]
> **Attention**! Don't forget the comma at the end of lines and the quotation marks!
Ensure to save the changes made to the file.


Reboot after changing and saving the settings file

```
reboot
```

Check the server in the signal interface, it should go online if everthing went well. This can take some time since the synology is still starting up. But it should not take longer than 3 minutes


##### Update version
**Auto update**

SSH to the signal server and change the updates.json file. The synology tag is located at the bottom of the file.

```
sudo nano /var/www/binaries/updates.json
```

After changing and saving the file reboot the synology to auto update.

**Manual update**
- SSH to the synology, check the ['Create Login'](https://github.com/JimberSoftware/jimberfw_server/new/development/platforms/synology#create-login) section above for the password.
- Delete the previous './jimbernetworkisolation' folder and the zip if they exist.
- Go to https://signal.jimber.io/clients/ for a list of all clients.
- Search for the 'synology' tag and copy the right version url.
- Go back to the SSH terminal and do the following commands
```
wget https://signal.jimber.io/clients/synology-latest.zip
7z x 'synology-latest.zip'
cd ./jimbernetworkisolation
sudo ./install.sh
```

##### Check version

SSH to the synology, then use the following command:
```
jimberfw -version
```

##### Debugging
You can see the network isolation logs with the following command:
```
tail -f /var/log/jimber/jimbernetworkisolation.log
```

##### Online interface
If you need to go to the interface of the synology first find the IP of it by going to http://find.synology.com/ .

Then type in that ip in your browser and login with the credentials from the [create login](#create-login)


## Server online/offline

In the overview of the servers, you can see which is online or offline.

A server online will appear in the overview with a green dot:

![server online.png](server_online.png 'size:=800x')


A server offline will appear in the overview with a red dot:

![server offline.png](server_offline.png 'size:=800x')


## Details and firewall rules of a server

By clicking on the server name in the overview, you can view the server details and check the firewall rules.

![server detail.png](server_details.png 'size:=500x')


![server_firewall_rules.png](server_firewall_rules.png 'size:=500x')


## Updating a server

 An update is available when a green icon is visible next to the name  ![deleting_user.png](/icoon_update.png )
.
 
 By hovering over the icon, you can see which update it refers to.
 
![update server.png](updating_server.png 'size:=500x')

 
 Actually updating the server can be done by clicking on the icon.
> [!INFO]
> In case of a successful update, the update icon disappears. 


>[!WARNING]
> The update icon is not visible when the server is offline.


 

 ## Editing a server
  
 Servers can be edited by clicking on the yellow pencil icon next to their name 
![pencil_2.png](/pencil_2.png)
.
  
![edit server.png](/edit_server.png 'size:=500x')

  
  All  options are the same as when creating a server.

## Deleting a server

Servers can be deleted by clicking on the red trash bin icon next to their name 
![recycle_bin.png](/recycle_bin.png)
.


You will receive a warning before the device is permanently deleted:

![deleting_server.png](delete_server.png 'size:=500x')

