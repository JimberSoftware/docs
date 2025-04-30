# Servers

## Create Server

To create a server in the `Jimber SASE Platform`, click on the `Create new` button

![create_new.png](/create_new.png)

prominently located at the upper right corner of the interface. This will open following dialog box:

![create_server.png](/create_server.png)
 
> [!INFO] 
> Hostname is mandatory and must be a lowercase string. We advise you to copy the token as you will be needing it for the installation of the server, but you can still access it at any time on the editing screen of the server on the `Jimber SASE Platform`.


## Server installation

### Platforms 

<!-- tabs:start -->



#### **Windows**

> [!INFO] 
> First create your server (see above).

Download the latest version for the 'Windows Server' from https://signal.jimber.io/downloads (no need to login).

> [!INFO]
> To download another specific version, you can use this [link](https://signal.jimber.io/clients).

Once downloaded, decompress the file and initiate the .msi installation file by double-clicking it.

<!-- A dialog box will emerge—confirm the process by selecting 'Yes.' -->

<!-- Subsequently, open the file **`settings.json`** located at C:\Program Files\Jimber\ as an **Administrator**. 
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
Ensure to save the changes made to the file. -->


When starting `Jimber SASE Platform`, a dialog box will emerge: 

![jimber_server_settings.png](/jimber_server_settings.png ':size=500')

The required token was created with the new server. If you did not copy the token in the previous step, it can be retrieved from the 'Servers' tab within the `Jimber SASE Platform`. Simply select and edit the correct server to find it.

![token.png](/token.png ':size=500')

After filling in the token and pressing the submit button, a pop-up appears stating that the server configuration has been submitted and the service has been restarted:


![settings_updated.png](/settings_updated.png ':size=400')




<!-- Access the 'services' panel by entering 'services.msc' into the start menu's search bar. Within this panel, find the 'Jimber Network Isolation' service and initiate a restart.


![services_jimber.png](/services_jimber.png ':size=800') -->


Upon successful installation, the server should display a connected status (indicated by a green dot) in the `Jimber SASE Platform`. 

<!-- For any necessary troubleshooting, consult the log file at this location: 
`C:\Program Files\Jimber\jimbernetworkisolation.log` -->

#### **Linux**

> [!INFO] 
> Support is currently provided for the latest LTS versions of Ubuntu. For other OS distributions, please reach out to our support team.

Download the latest version for the 'Linux Server' from https://signal.jimber.io/downloads (no need to login).

> [!INFO]
> To download another specific version, you can use this [link](https://signal.jimber.io/clients).

```bash
sudo apt update
sudo apt install wireguard
wget https://signal.jimber.io/clients/linux-server-latest.deb
sudo dpkg -i linux-server-latest.deb
```

Upon completion of the installation, a new `settings.json` file will be automatically created in the `/etc/jimber/`directory.
This file must be completed with the token you were provided upon creating the server within the `Jimber SASE Platform` interface. This can be established with the following command:

```bash
sudo jimberfw -config
```
![token_linux_server.png](/token_linux_server.png ':size=300') 

<!-- Open this file using the text editor of your choice. Within this file, you'll notice an empty token along with newly created public and private keys.

In this file, enter the token you were provided upon creating the server within the SASE Platform interface.

```json
{
  "publicKey": "l7D1+dm...",
  "privateKey": "ENjN41TJE7WEU76T...",
  "token": "YOUR_TOKEN"
}
```
> [!WARNING]
> **Attention**! Don't forget the comma at the end of lines and the quotation marks!
Ensure to save the changes made to the file. -->




If you did not copy the token in the previous step, it can be retrieved from the 'Servers' tab within the `Jimber SASE Platform`. Simply select and edit the correct server to find it.


![edit_server.png](/edit_server.png ':size=500')



Restart the service by executing the following command:

```bash
sudo systemctl restart jimbernetworkisolation.service
```

Upon successful installation, the server should display a connected status (indicated by a green dot) in the `Jimber SASE Platform`. 
<!-- If needed, refer to the following log files for debugging purposes:

```bash
cat /var/log/jimber/jimbernetworkisolation.log
``` -->

>[!INFO]
> You can see the installed version using `jimberfw -version`


#### **Synology**

[Click here to see how to setup your Synology NAS](/./devices/synology/synology.md)

#### **Raspberry Pi**

Requirements:
- Default Raspbian installation 

Follow the Linux installation but use the following deb file instead: 
- https://signal.jimber.io/clients/rpi-latest.deb

> [!INFO]
> To download another specific version, you can use this [link](https://signal.jimber.io/clients).

All other configuration is exactly the same.

<!-- tabs:end -->

>[!INFO]
>For any necessary troubleshooting, you can consult the log files. Locations of the log files van be found [here](/./advanced/logging/logging.md). 

---
## Server online/offline

In the overview of the servers you can see which is online or offline.

An online server will appear in the overview with a green dot. An offline server will appear in the overview with a red dot. When a server upgrade is available, it will be indicated by a green circle with an upward-pointing arrow.

![server online.png](server_online.png ':size=800')




## Details and firewall rules of a server

To view the details of a specific server and inspect its firewall rules, select the corresponding row in the table.

> [!INFO] 
> Avoid using the action buttons at the end of the row (e.g. edit or delete).

![server detail.png](server_details.png ':size=500')


![server_firewall_rules.png](server_firewall_rules.png ':size=500')


## Updating a server

 An update is available when indicated by a green circle with an upward-pointing arrow ![icoon_update.png](/icoon_update.png ':size=35')
.
 
 By hovering over the icon you can see which update it refers to.
 
![update server.png](updating_server.png ':size=700')

 
 Execute the update by clicking on the icon.

> [!INFO]
> In case of a successful update, the update icon disappears. 


>[!WARNING]
> The update icon is not visible when the server is offline.

 

 ## Edit Server
  
 Servers can be edited by clicking on the![icon_edit.png](/icon_edit.png ':size=35') icon next to their name.
  
![edit server.png](/edit_server.png ':size=500')


All options are the same as when creating a server.

## Deleting Server

Servers can be deleted by clicking on the![icon_delete.png](/icon_delete.png ':size=35') icon next to their name.

You will receive a warning before the device is permanently deleted:

![deleting_server.png](delete_server.png ':size=400')

