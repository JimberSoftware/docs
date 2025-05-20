# User Device Scripts

Within the *`Jimber SASE Platform`*, you can create and manage user device scripts under the **User Device Scripts** section. These scripts are executed on the user's device and support two types of triggers:

- **On Connect** – triggered when the device connects to the *`Jimber SASE Platform`* via the *`Jimber SASE Client`*.  
- **On Disconnect** – triggered when the device disconnects from the platform.

Scripts can be written for a variety of operating systems:

- **Windows**
- **macOS**
- **Linux**
- **Windows Server**
- **Linux Server**

> [!NOTE]  
> The script format must match the target operating system:
> - **Windows** and **Windows Server**: use `.bat` or `.ps1` (PowerShell) scripts.  
> - **macOS** and **Linux-based systems**: use standard shell scripts (`.sh`), written in Bash or another supported shell.

This allows for flexible device-side automation based on connection status, for example, applying firewall rules, starting background services, or cleaning up temporary resources.

## Create User Device Script 
To create a new script into the platform, click on the `+ Create new` button located at the upper right corner of the interface.

![create_script.png](create_script.png ':size=500')

All fields in the script creation form are mandatory. Ensure that the script content is written in the correct format for the selected platform.

> [!WARNING]
> It is essential to select the correct **group** when creating the script. The script will only be executed on devices belonging to the specified group when the defined trigger condition is met. Assigning the script to the wrong group may result in it not running on the intended devices.

## User Device Script Details

To view the details of a specific script, select the row in the table (rather than using the action buttons at the end).

![overview_scripts.png](overview_scripts.png ':size=800')

![script_details.png](script_details.png ':size=500')

## Edit User Device Script

Scripts can be edited by clicking on the yellow pencil icon next to their name ![icon_edit.png](/icon_edit.png ':size=35').


![edit_script.png](edit_script.png ':size=500')

## Delete User Device Script

Scripts can be deleted by clicking on the red trash bin icon next to their name ![recycle_bin.png](/icon_delete.png ':size=35').

You will receive a warning before the user is permanently deleted:

![delete_script.png](delete_script.png ':size=500')

