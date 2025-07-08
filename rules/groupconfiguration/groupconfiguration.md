# ![](../../images/menu/menu_groupconfig.png ':size=28') Group Configuration

Group Configuration allows administrators to define and manage policies that control how different sets of users or devices behave within the network. By assigning devices to groups, you can tailor specific features—such as routing behavior, DNS resolution, device onboarding rules, and application enforcement—to match organizational needs or security requirements.

![Screenshot of the Group Configuration page](./screenshots/groupconfig.png ':size=800')

This modular approach makes it easy to apply consistent settings across similar users or departments, enforce compliance standards, and simplify large-scale management. Each tab below represents a configurable option that can be enabled, disabled, or customized per group.

### Filter Group Configurations

You can search the list of group configurations using the search box at the top of the page. This helps you quickly find and manage the group configuration you're looking for.

- Use the search box to enter keywords and filter the group configuration list.

Next to the search box, there is a filter icon ![](../../images/icons/icon_filter.png ':size=20'). When clicked, it reveals advanced filtering options where you can define additional conditions based on the following three elements:

- **Property**: A dropdown menu where you choose the field to filter on.
- **Match type**: A dropdown that allows you to select how to match the value (only `equals`).
- **Value**: Enter or select the value to match, depending on the selected property.

![filter_groupconfig.png](./screenshots/filter_groupconfig.png ':size=400')

To add multiple filters you can press the filter icon ![](../../images/icons/icon_filter.png ':size=20') again and then press the `+` button.

<!-- Once filters are applied:
- The results are updated to reflect your conditions.
- Active filters appear at the top of the page.
- You can remove filters individually by clicking the `X` next to each, or remove all at once by clicking the `Reset Filters` button. -->

> [!INFO]
> You can refresh the list of users by pressing the refresh icon ![](../../images/icons/icon_reload.png ':size=20') at the top of the page.

<!-- tabs:start -->

### **WAN GATEWAY**
_Force all client internet traffic through the cloud or on-premise router._

#### Overview

By enabling this feature, you can make certain applications accessible **only** to users who are securely connected through the *`Jimber SASE Platform`*.

#### Benefits of WAN Gateway
- Route traffic through your existing firewall or proxy for added security or monitoring.
- Ensure all internet traffic appears to come from a single, consistent IP address — which is required by some SaaS (cloud) applications for access control.

#### How It Works

When this option is enabled, all internet traffic from connected devices will be routed through the cloud or on-premise router, instead of using the device’s own internet connection.

> [!WARNING]
> Devices connected through a Network Isolation Access Client (NIAC) **won’t be able to access the internet** unless they belong to a group where the **WAN Gateway** is enabled.

> [!INFO]
> **Things to keep in mind when using WAN Gateway:**
> - **All internet traffic** from clients will be routed through either the **local on-prem** or **cloud Network Controller**, depending on your setup.
> - **Services tied to your local WAN IP** may stop working. For example, some DNS settings from internet providers rely on a specific IP. A known issue occurs with **Telenet routers** using `195.130.131.11` as their DNS—this address does **not** work when routed through the cloud controller. In such cases, use **DNS Override** to fix it.
> - **Slightly increased latency** is possible, as traffic takes an extra hop through the gateway.

##### Configuration Steps
1. Enable **WAN Gateway** in the *`Jimber SASE Platform`* group settings of the selected group.
2. Monitor and adjust usage as needed.

### **DNS OVERRIDE**
_Resolve internal devices by hostname or alias and enable DNS-based web filtering._

#### Overview

The **DNS Override** feature enhances control and security by allowing you to customize how domain names are resolved within your network. With this feature, you can resolve internal devices by their hostname or alias, which simplifies network management and improves usability. Additionally, DNS override enables web filtering, letting you block access to specific websites for improved security or to increase productivity.


#### Benefits of DNS Override

##### 1. Resolve Internal Devices by Hostname or Alias
- **Ease of Access**: Quickly and easily access internal devices without needing to remember IP addresses.
- **Simplified Network Management**: Centralize DNS records for all internal devices.
- **Consistent Naming Conventions**: Reduce confusion and potential errors.

##### 2. Web Filtering
- **Enhanced Security**: Block access to known malicious websites.
- **Productivity Improvement**: Prevent access to distracting websites.
- **Customizable Filtering**: Tailor web filtering policies to your organization.

#### How It Works

The DNS override feature works by intercepting DNS queries within your network and applying custom resolution rules.

##### Configuration Steps
1. Define hostnames and aliases.
2. Set up web filtering rules.
3. Enable **DNS Override** in the *`Jimber SASE Platform`* group settings of the selected group.

#### Example Use Cases

**Internal Device Resolution:**
- Access a server via `server.company.local` or alias like `fileserver`.

**Web Filtering:**
- Block phishing or time-wasting sites like social media.


### **DEVICE APPROVAL**
_Require administrative consent before devices can access the network._

#### Overview

The **Device Approval** feature introduces an extra layer of security by requiring admin approval before a device can be onboarded.

#### Benefits of Device Approval

##### 1. Enhanced Security
- **Access Control**: Only approved devices can join the network.
- **Compliance**: Helps with internal policies and regulations.
- **Accountability**: Provides an audit trail.

##### 2. Administrative Oversight
- **Notification System**: Admins are alerted (if enabled).
- **Approval Workflow**: Simple UI to manage requests.
- **Monitoring**: Track all connected devices.

#### How It Works

When a user tries to onboard a device, the Device Approval feature requires administrator approval before the device is granted access to the network.

##### Configuration Steps
1. Enable **Device Approval** in the *`Jimber SASE Platform`* group settings of the selected group.
2. Enable notifications for new requests.
3. Admins review/approve devices via dashboard.


### **MOBILE CONNECTION**
_Connect mobile devices to the network securely._

#### Overview

The **Mobile Connection** feature enables users to securely connect their mobile devices to the Jimber SASE Platform using the Jimber Network Isolation app. Once enabled, users can register and link their mobile devices through a simple and secure process.

#### Benefits

- **Secure Mobile Access**: Ensures that mobile devices are protected by the same isolation and security policies as desktops.
- **User-Friendly Setup**: Users can quickly link their device by scanning a QR code, making onboarding fast and easy.
- **Support for Remote Work**: Enables secure connectivity for mobile users outside the corporate network.
- **Consistent Policy Enforcement**: All connected mobile devices follow the same group and security configurations.

#### How it works

When Mobile Connection is enabled, users can add a mobile device via the Security panel on the platform. They are guided through the process of creating a new mobile device entry and linking it using a QR code. The QR code is scanned using the Jimber Network Isolation app installed on the mobile device, which then establishes a secure connection to the platform.

##### Configuration Steps

1. Enable **Mobile Connection** in the *`Jimber SASE Platform`* group settings of the selected group.
2. Create a new mobile device in the Security panel.
3. Link the mobile device by scanning the QR code with the Jimber Network Isolation app.


### **DEVICE LIMIT**
_Restrict how many devices each user can onboard._

#### Overview

The **Device Limit** feature lets administrators control how many devices each user can onboard. This helps ensure only approved hardware is used and prevents old or unused devices from staying connected.

#### Benefits

- **Enforce Approved Devices**: Limit users to company-issued or authorized laptops.
- **Simplify IT Support**: Standardized devices reduce troubleshooting complexity.
- **Improve Security**: Prevent unused or forgotten devices from lingering on the network.
- **Easier Oversight**: Helps admins audit and manage active devices.

#### How it works

Each user is assigned a device limit. Once they reach this limit, they must remove an existing device or request permission to add another.

##### Configuration Steps
1. Enable **Device Limit** in the *`Jimber SASE Platform`* group settings of the selected group.
2. Set the device count per user.
3. Monitor and adjust usage as needed.


### **ALWAYS ON**
_Ensure the application runs continuously to enforce network policies._

#### Overview

The **Always On** feature keeps the *`Jimber SASE Service`* running at all times to ensure that network policies are consistently enforced. It offers two enforcement levels: **Forced Mode** and **Autostart Mode**, giving organizations flexibility based on their security needs.

#### Benefits

- **Continuous Policy Enforcement**: Ensures security policies are always active.
- **Improved Compliance**: Helps meet regulatory and internal security requirements.
- **User Experience Control**: Allows balance between strict enforcement and flexibility.

#### How it works

When Always On is enabled, the application will launch with the system. Depending on the selected mode, users may or may not be able to disable it.

- **Forced Mode**: The app starts with the system and cannot be stopped by the user.
- **Autostart Mode**: The app starts automatically but allows users to disconnect if needed.

##### Configuration Steps

1. Enable **Always On** in the *`Jimber SASE Platform`* group settings of the selected group.
2. Choose between **Forced Mode** or **Autostart Mode**.
3. Deploy the settings to connected devices.

### **EDR**

_EDR systems continuously monitor activity on endpoints._

EDR stands for Endpoint Detection and Response. It is a security solution focused on monitoring, detecting and responding to threats on endpoints such as computers, laptops and servers. EDR solutions help detect cyberattacks at an early stage and minimize damage by enabling a swift response to suspicious activities.

### **IDS/IPS**

_IDS (Intrusion Detection System) identifies potential intrusions, unauthorized access, or other suspicious activities within a network._

_IPS (Intrusion Prevention System) detects and prevents intrusions, unauthorized access, and other suspicious activities within a network._


IDS and IPS are security systems that monitor network traffic for malicious activity. An IDS detects threats and generates alerts, while an IPS not only detects threats but also takes action to stop them.


<!-- tabs:end -->
