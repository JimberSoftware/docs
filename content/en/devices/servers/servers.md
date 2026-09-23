# ![](../../images/menu/menu_servers.png ':size=25') Servers

### Create Server

To create a server in the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***, click on the `+ Create new` button located at the upper right corner of the interface. This will open following dialog box:

![create_server.png](./screenshots/create_server.png ":size=800")

- Hostname is mandatory and must be a lowercase string. 
- You can create a new tag or use a saved tag.


 
>[!TIP] 
>We advise you to copy the token as you will be needing it for the installation of the server, but you can still access it at any time on the editing screen of the server on the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***.


### Server installation

#### Platforms 

> [!ATTENTION] 
> First create your server on the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_*** (see above).

<!-- tabs:start -->



### **Windows**

Download the latest version of the 'Windows Server' client from https://SASE.jimber.io/downloads (no need to log in).

> [!TIP]
> To download another specific version, you can use this [link](https://SASE.jimber.io/clients).

Once downloaded, initiate the .msi installation file by double-clicking it.

![win_server_msi.png](./screenshots/win_server_msi.png ':size=100')




When starting **_Jimber SASE Client_**, a dialog box will emerge: 

![jimber_server_settings.png](./screenshots/jimber_server_settings.png ':size=500')

The required token was created with the new server. If you did not copy the token in the previous step, it can be retrieved from the 'Servers' tab of the ****_<span style="color: darkblue;">Jimber SASE Platform</span>_***. Simply select and edit the correct server to find it.

![update_server.png](./screenshots/update_server_token.png ':size=800')

<!-- ![token.png](./screenshots/token.png ':size=500') -->

After filling in the token and clicking the submit button, a pop-up appears stating that the server configuration has been submitted and the service will be restarted:


![settings_updated.png](./screenshots/settings_updated.png ':size=400')




<!-- Access the 'services' panel by entering 'services.msc' into the start menu's search bar. Within this panel, find the 'Jimber Network Isolation' service and initiate a restart.


![services_jimber.png](/services_jimber.png ':size=800') -->


Upon successful installation, the server should display a connected status (indicated by a green dot) on the 'Servers' tab of the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***. 

<!-- For any necessary troubleshooting, consult the log file at this location: 
`C:\Program Files\Jimber\jimbernetworkisolation.log` -->

### **Linux**

> [!INFO] 
> Support is currently provided for the latest LTS versions of Ubuntu. For other OS distributions, please reach out to our support team.

Download and install the latest version for the 'Linux Server' client from https://SASE.jimber.io/downloads (no need to log in) by running following commands:

```bash
sudo apt update
sudo apt install wireguard
wget https://SASE.jimber.io/linux-server-latest.deb
sudo dpkg -i linux-server-latest.deb
```
> [!TIP]
> To download another specific version, you can use this [link](https://SASE.jimber.io/clients).

Upon completion of the installation, a new `settings.json` file will be automatically created in the `/etc/jimber/`directory.
This file must be completed with the token you were provided upon creating the server within the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_*** interface. This can be established with the following command:

```bash
sudo jimberfw -config
```
![token_linux_server.png](./screenshots/token_linux_server.png ':size=300') 

If you did not copy the token in the previous step, it can be retrieved from the 'Servers' tab of the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***. Simply select and edit the correct server to find it.


![update_server.png](./screenshots/update_server_token.png ':size=800')


<!-- Restart the service by running the following commandsudo

```bash
sudo systemctl restart jimbernetworkisolation.service
``` -->

Upon successful installation, the server should display a connected status (indicated by a green dot) on the 'Servers' tab of the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***. 
<!-- If needed, refer to the following log files for debugging purposes:

```bash
cat /var/log/jimber/jimbernetworkisolation.log
``` -->

>[!TIP]
> You can see the installed version using *jimberfw version*. You can also see the installed version in the details page of the server in the SASE platform (see below).


### **Synology**

[Click here to see how to setup your Synology NAS](../../advanced/synology/synology.md)

### **Raspberry Pi**

Requirements:
- Default Raspbian installation 

Follow the Linux installation but use the following deb file instead: 
- https://SASE.jimber.io/clients/rpi-latest.deb

> [!TIP]
> To download another specific version, you can use this [link](https://SASE.jimber.io/clients).

All other configuration is identical.

<!-- tabs:end -->

>[!INFO]
>For any necessary troubleshooting, you can consult the log files. Locations of the log files can be found [here](/./advanced/logging/logging.md). 

---
---

### Filter Servers

You can search the list of servers using the search box at the top of the page. This helps you quickly find and manage the server you're looking for.

Next to the search box, there is a filter icon ![](../../images/icons/icon_filter.png ':size=20'). When clicked, it reveals advanced filtering options where you can define additional conditions based on the following three elements:

- **Property**: A dropdown menu where you choose the field to filter on.
- **Match type**: A dropdown that allows you to select how to match the value (`EQUALS`, `CONTAINS`, or `NOT`).
- **Value**: Enter or select the value to match, depending on the selected property.

![filter_server.png](./screenshots/filter_server.png ':size=500')

To add multiple filters you can press the filter icon ![](../../images/icons/icon_filter.png ':size=20') again and then press the `+` button.


> [!TIP]
> You can refresh the list of servers by pressing the refresh icon ![](../../images/icons/icon_reload.png ':size=20') at the top of the page.

### Tags

Tags are added while creating or editing the server.

You can review the used **Tags** by pressing the`Tags`button at the top of the page. Here you can also delete any used tags by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in their row.

![tags.png](./screenshots/tags.png ':size=500')

> [!CAUTION]
> Deleting a tag permanently removes all use of it. You will not receive a warning message before deletion. 

### Server Details

In the overview of the servers you can see which servers are online or offline.

An online server will appear in the overview with a green dot. An offline server will appear in the overview with a red dot. When a server update is available, it will be indicated by the green update icon ![](../../images/icons/icon_update.png ':size=20'). Hover over the icon to see which update it refers to.

![updating_server.png](./screenshots/updating_server.png ':size=800')

Click the update icon ![](../../images/icons/icon_update.png ':size=20') to initiate the update.

> [!INFO]
> In case of a successful update, the update icon disappears. Should the icon remain after several minutes, retry the update by clicking the icon again. 


>[!NOTE]
> The update icon is not visible when the server is offline.


![server online.png](./screenshots/server_online.png ':size=800')

Clicking on the corresponding strip of a specific server opens a new window with more details, installed firewalls or antivirus, installed interfaces, security settings, and secure mode exceptions.

<!-- tabs:start -->

##### **Details**

This window shows general information about the server and  the groups to which the server belongs.

![server_detail.png](./screenshots/server_details.png ':size=500')

##### **Software**

Here you get an overview of the installed antivirus software and firewalls.

![server_software.png](./screenshots/server_software.png ':size=500')


##### **Interfaces**

In this window you can find the network interfaces detected on the server.

![server_interfaces.png](./screenshots/server_interfaces.png ':size=500')

##### **Security**

This window shows the founded policies and port forwarding rules on the server.

![server_firewall_rules.png](./screenshots/server_firewall_rules.png ':size=500')

##### **Secure Mode**

Here you find any secure mode exceptions. Secure mode exceptions allow specific websites, applications, or network traffic to bypass enhanced security restrictions, to ensure daily tasks are not blocked while maintaining high-level defenses. 
 
![server_secure_mode.png](./screenshots/server_secure_mode.png ':size=500')

Secure mode can be enabled when creating the server, or when updating the server: 

![enable_secure_mode.png](./screenshots/enable_secure_mode.png ':size=500')


<!-- tabs:end -->

---

### Edit Server

A server can be edited by clicking on the edit icon ![](../../images/icons/icon_edit.png ':size=20') in its row.

![edit server.png](./screenshots/update_server.png ':size=800')

All options are the same as when creating a server.

### Delete Server

A server can be deleted by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in its row.

You will receive a warning before the device is permanently deleted:

![delete_server.png](./screenshots/delete_server.png ':size=300')

