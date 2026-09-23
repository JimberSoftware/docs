# Deploy Network Controller in Azure

This guide walks you through deploying a Jimber SASE Network Controller on Microsoft Azure.

## Prerequisites

Obtain the following prerequisite items:

- A subscription to Azure.
- A Jimber SASE Network Controller VHD

> [!Note]
> The minimum specifications for Network Controller are:
> 
> - 25GB hard disk
> - 2 CPU
> - 4GB RAM
> 
> **Recommended VM sizes in Azure:**
> - Standard_B2s (2 vCPUs, 4GB RAM)
> - Standard_B2ms (2 vCPUs, 8GB RAM)
> - Standard_D2s_v3 (2 vCPUs, 8GB RAM)

## Download the Network Controller VHD

Before creating resources in Azure, you need to download the Jimber SASE Network Controller VHD file.

1. Navigate to [https://sase.jimber.io/downloads](https://sase.jimber.io/downloads) in your web browser.

![download-vhd.png](./screenshots/download-vhd.png ':size=600')

2. Download the Azure VHD file for the Network Controller.

3. Save the VHD file to a location on your local machine where you can easily access it for upload to Azure in the next steps.

## Create a Resource Group

In Azure, a Resource Group is a logical folder for all the resources you create, including Disks, Storage Accounts, VMs, and Network Security Groups. If your organization limits the ability to manage Resource Groups, reach out to your Azure Administration Team for assistance.

To create a Resource Group, follow these steps:

1. Log into Azure with an account with permission to create a Resource Group.

2. In the Azure UI, select **Resource Groups** from the Azure services menu at the top of the screen.

![resource_group.png](./screenshots/resource_group.png ':size=600')

3. Select the **+ Create** button in the top left of the Resource Groups screen.

![create_resource_group.png](./screenshots/create_resource_group.png ':size=600')

4. Complete the fields on the Create a resource group screen that opens.

![resource_group_fields.png](./screenshots/resource_group_fields.png ':size=600')

5. Select **Review and create**.

6. Verify that the resource group information is correct and select **Create**.

## Create a Storage Account

To create a Storage Account, follow these steps:

1. Return to the Azure home screen and select **Storage Accounts** from the Azure services menu at the top of the screen.

2. Select the **+ Create** button in the top left of the Storage accounts screen that opens.

3. On the Create Storage Account screen, provide the following information:

   - For **Resource group**, select the drop-down menu and select the resource group that you created in the previous procedure.
   
   > [!Note]
   > If you do not see your resource group, you can search for it by typing in the Select existing field at the top of the list of existing resource groups.

   - The **Storage account name**, which must be 3 to 24 characters long and contain only lowercase letters and numbers.

   - (Optional) Specify the **Location** of the storage account, which can be different from the location of the resource group.

4. Select **Review and create**.

5. Verify that the storage information is correct and select **Create**.

   The storage account is deployed and added to the list on the Home, Storage Accounts screen.

6. Select your new storage account from the list. You must select the **Refresh** button.

7. Select **Containers** from the Data Storage section in the navigation rail to the left. The Containers pane opens.

8. Select **+ Container** to create a storage container in the storage account. A New Container panel opens on the right of the screen.

9. In the New Container panel, enter a **Name** for the new container and select **Create**.

   > [!Note]
   > The container name can only contain lowercase letters, numbers, and hyphens, and must begin with a letter or a number. Each hyphen must be preceded and followed by a non-hyphen character. The name must also be from 3 through 63 characters long.

10. On the Containers panel, locate your new container and select its name (not the checkbox to its left).

11. In the panel that opens, select the **Upload** icon in the upper left then select the Jimber SASE Network Controller VHD image to upload it to Azure.

## Create a Managed Disk

Next, create a disk in Azure.

Follow these steps:

1. Enter "disks" in the search field at the top of the Azure portal.

2. Select **Disks** from the search results.

3. On the Disks page, select the **+ Create** button to add a new disk.

![create-disk-1.png](./screenshots/create-disk-1.png ':size=600')

4. Under **Project Details**, select an existing Resource Group from the drop-down menu.

5. Under **Disk Details**, provide the following information:

   - The **Disk Name**.

   - For **Region**, select the same location as your Storage Account. You must create a disk in the same location as the storage account where you uploaded your VHD.

6. To specify the disk source type and properties, follow these steps:

   - Select **"Storage blob"** from the Source Type drop-down menu. More context-sensitive controls appear.

   - In the **Source blob** field, use the Browse link to select the VHD. Select the Storage Account, then the Container, then the VHD, and finally select **Select**.

![create-disk-select-blob1.png](./screenshots/create-disk-select-blob1.png ':size=600')

![create-disk-select-blob-2.png](./screenshots/create-disk-select-blob-2.png ':size=600')

![create-disk-select-blob-3.png](./screenshots/create-disk-select-blob-3.png ':size=600')

![create-disk-select-blob-4.png](./screenshots/create-disk-select-blob-4.png ':size=600')

   - For **OS type**, select **"Linux."**

   - Verify that the value of the VM generation control (which appeared when you select Linux in the previous step) is **"Gen 1."**

7. To change the default Size (1024 GiB) of the disk, do the following steps:

   - Select the **Change Size** link. The Select a disk size page opens.

   - Verify that the value that is specified in the Disk SKU drop-down menu is **"Premium SSD"**.

   - Select a listed disk size or specify a Custom disk size of at least **80 GiB**.

   - Select **OK**

![create-disk-4.png](./screenshots/create-disk-4.png ':size=600')

8. Select **Review and Create**.

![create-disk-5.png](./screenshots/create-disk-5.png ':size=600')

9. Verify that your settings are correct and, if so, select **Create**. Otherwise, select the **Previous** button to go back and make any necessary changes.

## Create the Virtual Machine

To create a Network Controller VM in Azure, follow these steps:

1. Return to the Disks page and select your disk. A new pane appears with **+ Create VM**.

![create-vm-1.png](./screenshots/create-vm-1.png ':size=600')

2. Select **+ Create VM**. The Create Virtual Machine panel appears.

![create-vm-2.png](./screenshots/create-vm-2.png ':size=600')

3. In the **Basics** tab, enter a **Name** for your VM.

![create-vm-3.png](./screenshots/create-vm-3.png ':size=600')

4. For **Resource Group**, select **"Use Existing"** and select your Resource Group.

5. **Location** is disabled because it is determined by the disk Storage Account location.

6. Select a size. See Installation Requirements for more information. Select the size and then select the **Select** button at the bottom.

7. Select **Review + Create**.

![create-vm-4.png](./screenshots/create-vm-4.png ':size=600')

8. Verify the settings on the Summary page, then select **Create** to commit your changes.

   Deployment begins. To monitor its progress, select the **Notifications** bell icon in the upper right.

## Configure Port Rules

To allow network traffic to the Network Controller, configure Network Security Group (NSG) rules for ports 8080 and 38250.

1. Navigate to your VM in the Azure portal and select **Networking** from the left navigation menu.

2. Select the **Network Security Group** name associated with your VM.

3. Select **Inbound security rules** from the Settings section.

![add-port-rules-1.png](./screenshots/add-port-rules-1.png ':size=600')

4. Select **+ Add** to create a new inbound rule for port 8080:

![add-port-rules-2.png](./screenshots/add-port-rules-2.png ':size=600')

   - **Source**: **"Any"**
   - **Source port ranges**: **"*"**
   - **Destination**: **"Any"**
   - **Destination port ranges**: **"8080"**
   - **Protocol**: **"TCP"**
   - **Action**: **"Allow"**
   - **Priority**: Enter a unique number (e.g., **1000**)
   - **Name**: Enter a descriptive name (e.g., **"Allow-HTTP-8080"**)

5. Select **Add** to create the rule.

6. Repeat steps 4-5 to create a second rule for port 38250 with the following settings:

   - **Destination port ranges**: **"38250"**
   - **Priority**: Enter a different number (e.g., **1010**)
   - **Name**: Enter a descriptive name (e.g., **"Allow-NetworkController-38250"**)

7. Verify that both rules appear in the Inbound security rules list with status "Succeeded".

![add-port-rules-3.png](./screenshots/add-port-rules-3.png ':size=600')

## Network Controller Installation

After the VM is deployed and the port rules are configured, complete the Network Controller installation:

1. Obtain the public IP address of your VM from the Azure portal:

   - Navigate to your Virtual Machine in the Azure portal by searching for your VM name in the search bar at the top, or by going to **Virtual machines** from the Azure services menu.

   - Select your VM from the list to open its Overview page.

   - On the VM's Overview page, locate the **Public IP address** field in the **Essentials** section. This is the IP address you will use to access the Network Controller web interface.

   - Copy this IP address for use in the next steps.

2. Use the displayed IP address to complete the installation of the Network Controller on the Jimber SASE Platform by filling it in under the endpoint address.

   > [!Note]
   > Detailed instructions for the creation of an on-prem Network Controller are available [here](/./devices/networkcontrollers/networkcontrollers.md).

3. Access the Network Controller web interface by navigating to `http://<your-vm-public-ip>:8080` in your web browser.

![nc-setup-1.png](./screenshots/nc-setup-1.png ':size=600')

4. Login with `jimber` as password on the web interface.

![nc-setup-2.png](./screenshots/nc-setup-2.png ':size=600')

5. Set a new password.

   > [!Warning]
   > The new password has to be at least **16** characters long!

![nc-setup-3.png](./screenshots/nc-setup-3.png ':size=600')

6. Select the right network configuration and then click on the test connection button. If successful you can go to the next step.

   > [!Note]
   > If it fails please check that the Network Controller has an active internet connection and the configuration on the web interface is done correctly. Also verify that the port rules (8080 and 38250) are correctly configured in the Network Security Group.

![nc-setup-4.png](./screenshots/nc-setup-4.png ':size=600')

7. Go to the Jimber SASE Platform and copy the token of the Network Controller you just created. You can find the token by editing the Network Controller with the yellow pencil.

8. Paste this token into the web configuration of the Network Controller. Then hit next.

9. Please wait a moment while the connection is being tested.

![nc-setup-5.png](./screenshots/nc-setup-5.png ':size=600')

10. When the connection is established you will get a confirmation screen.

11. Confirm that your Network Controller is now online on the Jimber SASE Platform under the Network Controller page.
