# Group configuration
In the group configuration you can define different behavior per group. Options can be enabled or disabled, or custom properties for specific options can be set.

## WAN Gateway

When enabled, it forces clients to navigate the internet via the cloud or on-premise router. If this option is turned off, clients will access the internet using their own internet connection. 

This feature can be turned on to chain the networkcontroller to existing firewall / proxy infrastructure or to be sure that all SaaS applications are accessed from the same IP. SaaS applications can be configured to only allow SaaS from one IP, this way you can make these applications only accessible for users connected to Network Isolation.

> [!WARNING]
> A device that is connected to a NIAC will not be able to reach the internet unless the NIAC is member of a group of which the Wan Gateway is enabled.

Some considerations in using WAN Gateway:
- All public internet traffic will be routed through either the local on-premise Network Controller or the cloud Network Controller
- Services that are whitelisted for your local WAN IP might stop working. This might include provider specific DNS settings. This is a known issue with Telenet routers that use 195.130.131.11 as their DNS, which is not usable from the cloud network controller. Use DNS override to keep your DNS working in this case.
- WAN Gateway might increase latency slightly


## DNS Override
### Overview

The DNS override function on our platform provides enhanced control and security over how domain names are resolved within your network. This feature allows you to customize DNS resolution behavior, providing two significant benefits: resolving internal devices by hostname or alias and enabling web filtering to block access to specific websites.

### Benefits of DNS Override

#### 1. Resolve Internal Devices by Hostname or Alias

One of the key advantages of the DNS override feature is its ability to resolve all servers, Network Isolation Access Clients (NIACs), and native devices on their hostnames or aliases. This simplifies network management and enhances usability by allowing administrators and users to access devices using easily recognizable and memorable names.

**Key Points:**
- **Ease of Access**: Quickly and easily access internal devices without needing to remember IP addresses.
- **Simplified Network Management**: Centralize DNS records for all internal devices, making it easier to manage and update them.
- **Consistent Naming Conventions**: Ensure consistent and clear naming conventions for all devices, reducing confusion and potential errors.

#### 2. Web Filtering

The DNS override feature also plays a crucial role in web filtering, allowing you to block access to specific malicious or distracting websites. By intercepting DNS queries for certain domains and redirecting or blocking them, you can protect your network from harmful content and improve productivity by limiting access to non-essential sites.

**Key Points:**
- **Enhanced Security**: Block access to known malicious websites, protecting your network from potential threats such as malware, phishing, and other cyber attacks.
- **Productivity Improvement**: Prevent access to distracting websites, helping to maintain focus and productivity within your organization.
- **Customizable Filtering**: Easily configure which websites to block, allowing you to tailor the web filtering policies to meet your organization's specific needs.

### How It Works

The DNS override feature works by intercepting DNS queries within your network and applying custom resolution rules. When a query matches a configured override rule, the platform either resolves the query to the specified internal device or blocks/redirects the query as per the web filtering settings.

**Configuration Steps:**
1. **Define Hostnames and Aliases**: Configure the platform to resolve internal devices by their hostnames or aliases.
2. **Set Up Web Filtering Rules**: Specify the domains to be blocked or redirected for web filtering purposes.
3. **Apply DNS Override Policies**: Implement the override rules across your network to ensure consistent behavior.

### Example Use Cases

**Internal Device Resolution:**
- An employee needs to access the company’s internal server. Instead of using an IP address, they can simply enter `server.company.local` or an alias like `fileserver`, making it easier to connect.

**Web Filtering:**
- To enhance security, you configure the platform to block access to known phishing websites. Additionally, to boost productivity, you block access to social media sites during work hours.

## Always On

### Overview

The "Always On" feature in our platform is designed to enforce network policies strictly by ensuring the application is running continuously. This feature provides two modes: Forced and Autostart, each catering to different levels of policy enforcement.

### Modes of Always On

#### 1. Forced Mode

In Forced Mode, the application is integrated with the system startup process to ensure that network policies are always enforced. This mode is intended for environments where strict compliance with network policies is essential.

**Key Points:**
- **System Startup Integration**: The application starts automatically with the system, ensuring that it is always running and enforcing network policies from the moment the device is powered on.
- **Non-Disabling**: The user cannot disable or terminate the application, ensuring that all network policies are continuously enforced without interruption or user intervention.
- **Policy Enforcement**: By preventing users from closing the application, Forced Mode guarantees that all predefined network policies are adhered to at all times, providing a high level of security and compliance.

#### 2. Autostart Mode

In Autostart Mode, the application also starts automatically with the system but offers more flexibility for the user. This mode is suitable for environments where some user control over network policies is permissible.

**Key Points:**
- **Automatic Startup**: The application starts with the system, ensuring that network policies are enforced immediately upon device startup.
- **User Control**: Unlike Forced Mode, users can disconnect from the network or disable the application if necessary. This allows for a balance between policy enforcement and user flexibility.
- **Flexible Enforcement**: Ideal for environments where strict policy enforcement is not as critical, and users may need the option to manage their connectivity based on specific situations.

### Use Cases

**Forced Mode:**
- **High-Security Environments**: Ensuring that users comply with all network policies without exception, such as in financial institutions, government agencies, and other security-sensitive areas.
- **Strict Compliance Requirements**: Situations where regulatory compliance requires uninterrupted enforcement of network policies, preventing any possibility of bypassing security measures.

**Autostart Mode:**
- **Standard Office Environments**: Providing automatic policy enforcement while allowing users the flexibility to manage their connectivity as needed.
- **Remote and Home Offices**: Balancing policy enforcement with user convenience, ensuring that policies are applied on startup but can be temporarily bypassed if necessary.

### Conclusion

The "Always On" feature is crucial for maintaining strict enforcement of network policies, with Forced and Autostart modes catering to different operational needs. By using Forced Mode, organizations can ensure that all network policies are adhered to without any user intervention, while Autostart Mode provides a balanced approach for environments where user flexibility is acceptable.

## Device Approval

### Overview

The "Device Approval" feature on our platform introduces an extra layer of security and control by requiring administrative consent before a device can be onboarded onto the network. This process ensures that only authorized devices gain access, helping to maintain the integrity and security of the network.

### How It Works

When a user attempts to onboard a new device onto the network, the Device Approval feature intercepts the process and requires administrative approval before the device is granted access. Administrators receive notifications (if enabled) about pending approval requests and can review and approve or deny the onboarding of the device.

### Benefits of Device Approval

#### 1. Enhanced Security

Requiring administrative approval before devices can join the network significantly enhances security. It prevents unauthorized devices from accessing network resources and ensures that all connected devices comply with organizational policies.

**Key Points:**
- **Access Control**: Ensures that only devices approved by administrators can join the network, reducing the risk of unauthorized access.
- **Compliance**: Helps maintain compliance with internal security policies and regulatory requirements by enforcing a controlled onboarding process.
- **Accountability**: Tracks device approvals, creating an audit trail that can be reviewed for security purposes.

#### 2. Administrative Oversight

The Device Approval feature gives administrators greater control and oversight over the devices that are allowed to connect to the network. Notifications about pending approvals ensure that administrators can promptly review and manage device access requests.

**Key Points:**
- **Notification System**: Administrators receive notifications about new device approval requests (notification feature must be enabled), ensuring timely review and action.
- **Approval Workflow**: Provides a clear and manageable workflow for approving or denying device access, making the process efficient and organized.
- **Monitoring**: Allows administrators to monitor and manage the devices on the network actively, ensuring all connected devices are accounted for and compliant.

### Configuration Steps

1. **Enable Device Approval**: Activate the Device Approval feature in the platform settings.
2. **Configure Notifications**: Ensure that administrator notifications for device approval requests are enabled.
3. **Review and Approve Devices**: Administrators receive notifications and can review pending device requests. Approvals or denials are managed through the administrative dashboard.

## Device Limit

### Overview

The "Device Limit" feature on our platform allows administrators to restrict the number of devices each user can onboard onto the network. This is primarily to ensure that users only onboard company-approved laptops and to minimize the chances of old, unused devices lingering on the network.

### How It Works

When the Device Limit feature is enabled, each user is assigned a specific limit on the number of devices they can onboard. Once a user reaches this limit, they will be unable to add additional devices until they remove an existing one or receive administrative permission to exceed the limit. This helps ensure that only approved devices are used and reduces the risk of outdated or unauthorized devices remaining connected.

### Benefits of Device Limit

#### 1. Enforcing Use of Company Laptops

By limiting the number of devices, administrators can ensure that users are primarily using company-approved laptops. This helps maintain control over the types of devices that access the network, ensuring they meet company standards and security policies.

**Key Points:**
- **Standardized Devices**: Ensures that only company-issued or approved laptops are used, which are configured to meet organizational standards and security requirements.
- **Reduced IT Support Complexity**: Simplifies IT support and troubleshooting by ensuring that all devices adhere to company specifications.

#### 2. Reducing Risk of Dangling Devices

The Device Limit feature also helps minimize the risk of old, unused devices remaining logged in and potentially posing security risks. By controlling the number of devices each user can have onboarded, administrators can more easily manage and audit connected devices.

**Key Points:**
- **Enhanced Security**: Reduces the chances of outdated or compromised devices remaining connected to the network, thereby enhancing overall security.
- **Simplified Device Management**: Makes it easier for administrators to keep track of active devices and ensures that old devices are promptly removed from the network.

### Configuration Steps

1. **Enable Device Limit**: Activate the Device Limit feature in the platform settings.
2. **Set Device Limits**: Define the maximum number of devices each user is allowed to onboard, typically aligning with the number of company-issued laptops.
3. **Monitor Device Usage**: Use the administrative dashboard to monitor device usage and manage requests for additional devices if necessary.
