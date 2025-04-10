# Servers

## Create Server

To create a server in the Security platform, click on the `Create new` button

![create_new.png](/create_new.png)

prominently located at the upper right corner of the interface.

 
> [!INFO] 
> Hostname is mandatory and must be a lowercase string.


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


Starting Jimber Network Isolation, a dialog box will emerge: 

![jimber_server_settings.png](/jimber_server_settings.png ':size=500')

The required token can be retrieved from the 'Servers' tab within the Signal Server Interface. Simply select and edit the  correct server to find it.

![token.png](/token.png ':size=500')

After filling in the token and pressing the submit button, a pop-up appears stating that the server configuration has been submitted and the service has been restarted:


![settings_updated.png](/settings_updated.png ':size=400')




<!-- Access the 'services' panel by entering 'services.msc' into the start menu's search bar. Within this panel, find the 'Jimber Network Isolation' service and initiate a restart.


![services_jimber.png](/services_jimber.png ':size=800') -->


Upon successful installation, the server should display a connected status (indicated by a green dot) in the Network Isolation Interface. 

For any necessary troubleshooting, consult the log file at this location: 
`C:\Program Files\Jimber\jimbernetworkisolation.log`

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
This file must be completed with the token you were provided upon creating the server within the SASE Platform interface. This can be established with the following command:

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




The required token can be retrieved from the 'Servers' tab within the Signal server interface. Simply select and edit an existing server to find it.


![edit_server.png](/edit_server.png ':size=500')



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


#### **Synology**

[Click here to see how to setup your synology nas](/./devices/synology/synology.md)

#### **Raspberry pi**

Requirements:
- Default raspbian installation 

Follow the Linux installation but use the following deb file instead: 
- https://signal.jimber.io/clients/rpi-latest.deb

> [!INFO]
> To download another specific version, you can use this [link](https://signal.jimber.io/clients).

All other configuration is exactly the same.

<!-- tabs:end -->

## Server online/offline

In the overview of the servers, you can see which is online or offline.

A server online will appear in the overview with a green dot. A server offline will appear in the overview with a red dot.
For a server with an extra green arrow, an update is available.

![server online.png](server_online.png ':size=800')




## Details and firewall rules of a server

Access the details of a specific server and check the firewall rules by selecting the corresponding strip within the table (avoid clicking on the buttons at the end). 

![server detail.png](server_details.png ':size=500')


![server_firewall_rules.png](server_firewall_rules.png ':size=500')

![server_firewall_rules.png](server_firewall_rules.png "size:=500x")

## Updating a server

 An update is available when a green icon is visible next to the name  ![icoon_update.png](/icoon_update.png ':size=35')
.
 
 By hovering over the icon, you can see which update it refers to.
 
![update server.png](updating_server.png ':size=800')

 
 Actually updating the server can be done by clicking on the icon.
> [!INFO]
> In case of a successful update, the update icon disappears. 

![update server.png](updating_server.png "size:=500x")

Actually updating the server can be done by clicking on the icon.

> In case of a successful update, the update icon disappears.

>[!WARNING]
> The update icon is not visible when the server is offline.

## Editing a server

 

 ## Edit Server
  
 Servers can be edited by clicking on the yellow pencil icon next to their name 
![icon_edit.png](/icon_edit.png ':size=35').
  
![edit server.png](/edit_server.png ':size=500')

![edit server.png](/edit_server.png "size:=500x")

All options are the same as when creating a server.

## Deleting Server

Servers can be deleted by clicking on the red trash bin icon next to their name![icon_delete.png](/icon_delete.png ':size=35').

You will receive a warning before the device is permanently deleted:

![deleting_server.png](delete_server.png ':size=400')

