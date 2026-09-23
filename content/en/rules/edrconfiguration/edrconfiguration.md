# ![](../../images/menu/menu_edr.png ':size=50') EDR

EDR (Endpoint Detection and Response) configuration involves setting up policies and settings to monitor, detect, and respond to threats on endpoints.
The EDR process involves constant monitoring and data gathering from endpoints to identify and address threats in real time and provides information about actions at the endpoints, including details about attempted cyber attacks. 


> [!IMPORTANT]
> This feature must be activated by a company administrator.
  
### EDR CONFIGURATION

![edrconfiguration.png](./screenshots/edrconfiguration.png ':size=800')


> [!WARNING]
> Choosing a higher level of sensitivity for the malicious file detection could resolve in more false positives. 

> [!NOTE]
> If EDR is set, you can use the [monitoring page](/./monitoring/monitoring.md) to inspect recorded activities and threats.  

> [!IMPORTANT]
> If 'Lockdown device network' is enabled and an issue was occurred, an administrator has to unlock the device network again using one of the standard Windows procedures, for instance via Device Manager.

### EDR Whitelist

An EDR whitelist (or allowlist) configures an Endpoint Detection and Response platform to ignore specific files, folders, processes, or scripts. This prevents legitimate administrative tools or business-critical software from triggering false-positive alerts, blocking execution, or consuming resources.

Use whitelists in EDR to:
-  Stop security agents from mistakenly killing vital applications or proprietary software and in this way secure business continuity.
-  Cut down on false positives, saving security teams time and so reduce alert fatigue.

#### Create a whitelist entry

To create a new whitelist entry, click on the `+ Create new` button located at the upper right corner of the interface.

![create_whitelist.png](./screenshots/create_whitelist.png ':size=500')

- Enter the filename.
- Enter the hash. Calculate the hash e.g., by using a browser-based tool like [SHA256 Online Calculator](https://emn178.github.io/online-tools/sha256.html).


#### Edit a whitelist entry

Whitelist Entries can be edited by clicking on the edit icon  in their row.

![edit_whitelist.png](./screenshots/edit_whitelist.png ':size=500')

You can change the name of the file. No need to recalculate the hash.