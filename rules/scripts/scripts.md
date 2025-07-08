# ![](../../images/menu/menu_scripts.png ':size=28') User Device Scripts

Within the *`Jimber SASE Platform`*, you can create and manage user device scripts under the **User Device Scripts** section. These scripts are executed on the user's device and support two types of triggers:

- **On Connect** – triggered when the device connects to the *`Jimber SASE Platform`* via the *`Jimber SASE Client`*.  
- **On Disconnect** – triggered when the device disconnects from the platform.

Scripts can be written for a variety of operating systems:

- **Windows**
- **macOS**
- **Linux**
- **Windows Server**
- **Linux Server**

![Screenshot of the User Device Scripts page](./screenshots/scripts.png ':size=800')

This allows for flexible device-side automation based on connection status, for example, applying firewall rules, starting background services, or cleaning up temporary resources.

### Create User Device Scripts

Click on the `+ Create new` button and follow the steps below:

1. **Name**: Enter a descriptive name for the script to help identify its purpose.
2. **Select Group**: Choose the user group this script should apply to. The script will only execute for users who are members of this group.
3. **Occurrence**: Select whether the script should run `On Connect` or `On Disconnect`.
4. **Platform**: Choose the operating system the script is intended for (e.g. Windows, macOS, Linux, etc.).
5. **Enable or Disable**: Use the slider to turn the script on or off.
6. **Script Field**: Write or paste your script content in the provided editor. Make sure it matches the format for the selected platform.
7. **Activate Changes**: Press the `Create User Device Script` button to save and apply the new user device script.

> [!NOTE]  
> Ensure that your script syntax matches the requirements of the target platform:
> - `.bat` or `.ps1` for Windows-based systems  
> - `.sh` (Bash) for Linux/macOS-based systems

![Screenshot of the Create User Device Script window](./screenshots/create_script.png ':size=500')

> [!WARNING]
> It is essential to select the correct **group** when creating the script. The script will only be executed on devices belonging to the specified group when the defined trigger condition is met. Assigning the script to the wrong group may result in it not running on the intended devices.

### Filter User Device Scripts

You can search the list of Scripts using the search box at the top of the page. This helps you quickly find and manage the script you're looking for.

- Use the search box to enter keywords and filter the scripts list.

Next to the search box, there is a filter icon ![](../../images/icons/icon_filter.png ':size=20'). When clicked, it reveals advanced filtering options where you can define additional conditions based on the following three elements:

- **Property**: A dropdown menu where you choose the field to filter on.
- **Match type**: A dropdown that allows you to select how to match the value (`equals` or `contains`).
- **Value**: Enter or select the value to match, depending on the selected property.

![filter_scripts.png](./screenshots/filter_scripts.png ':size=400')

To add multiple filters you can press the filter icon ![](../../images/icons/icon_filter.png ':size=20') again and then press the `+` button.

> [!INFO]
> You can refresh the list of users by pressing the refresh icon ![](../../images/icons/icon_reload.png ':size=20') at the top of the page.


### User Device Scripts Details

To view the details of a specific script, select the row in the table (rather than using the action buttons at the end).

![script_details.png](./screenshots/script_details.png ':size=500')

### Edit User Device Scripts

Scripts can be edited by clicking on the edit icon ![](../../images/icons/icon_edit.png ':size=20') in their row.

![edit_script.png](./screenshots/edit_script.png ':size=500')

### Delete User Device Scripts

Scripts can be removed by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in their row.

You will receive a warning before the user is permanently deleted:

![delete_script.png](./screenshots/delete_script.png ':size=500')

