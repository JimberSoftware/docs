# ![](../../images/menu/menu_configuration.png ':size=25') Configuration

The **Configuration** section lets you manage essential settings for your company and how user devices interact with your network. It is divided into three areas: Company Settings, Authentication, Misc(ellaneous):

![Configuration](./screenshots/configuration.png ':size=600')

<!-- tabs:start -->

### **Company Settings**

These settings define general information about your company within the **_*<span style="color: darkblue;">Jimber SASE Platform</span>*_**.

![Company Configuration](./screenshots/config_company.png ':size=600')

- **Display name**: This is the company name as it will appear throughout the platform for users and administrators.
- **Primary contact email**: Enter a contact email address that can be used for support or administrative purposes.
- **Website URL**: Specify your company’s website.

    > [!INFO]
    > The platform will automatically try to extract the company logo from this URL and display it in the user interface.

### **Authentication**

To sign in, you can choose from three authentication methods. Select the method(s) you want to use or make available.

![Configuration authentication](./screenshots/config_auth.png ':size=600')

#### OIDC provider

##### Add an OIDC provider

In addition, you can add an OIDC provider: 

![add_oidc_provider](./screenshots/add_oidc_provider.png ':size=300')

##### Edit an OIDC provider

OIDC provider can be edited by clicking on the edit icon ![](../../images/icons/icon_edit.png ':size=20') in its row.

![edit_oidc_provider](./screenshots/edit_oidc_provider.png ':size=300')

##### Delete an OIDC provider

An OIDC provider can be deleted by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in its row:

![delete_oidc_provider](./screenshots/delete_oidc_provider.png ':size=300')

>[!Attention]
>The OIDC provider will be removed without further notice.

<!-- ### Network Isolation Settings -->
### **Misc(ellaneous)**

These settings control how user devices are managed and isolated in your environment.

![Network Isolation Configuration](./screenshots/config_ni.png ':size=600')

- **IP range**: Define the internal IP range used for isolated network segments.

- **User devices expiry time**: Set how many days a user device remains active before it expires (default = 30 days).

- **Amount of devices allowed per user**: Specify the maximum number of devices per user (default = 3).

- **Download Certificate**: Download the company's current Jimber root CA certificate. The issued and expiry dates shown below the buttons identify the certificate you are downloading.

- **Request New Certificate** (![](../../images/icons/icon_reload.png ':size=15')): Immediately replace the current certificate with a newly generated certificate. The old certificate stops working as soon as you confirm the warning. Devices can lose connectivity until the new certificate is deployed and trusted.

    Use the [Microsoft Intune deployment guide](./company/configur/root-certificate-intune.md) to install the certificate on managed macOS devices.


- **Zero Trust Outbound**

    Zero Trust Outbound (ZTO) controls internet access through enabled outbound policies. Managed endpoints retain the following built-in exceptions even when their outbound policies are disabled:

    | Protocol    | Destination port                                     | Allowed destinations                                                                                          |
| ----------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
    | TCP and UDP | 53 (DNS)                                             | Any destination                                                                                               |
    | TCP and UDP | 51820 (Jimber tunnel connectivity)                   | Any destination                                                                                               |
    | TCP         | 80 and 443 (Signal Server and Lifeline connectivity) | IP addresses resolved from the Signal Server URL and configured Lifeline addresses, including its fallback IP |

    DNS is allowed by default, so the automatically created **Standard Internet** service does not include port 53. Disabling a Standard Internet policy does not block DNS or Jimber tunnel connectivity.

    If a Signal Server or Lifeline hostname lookup fails or returns no IP addresses, TCP ports 80 and 443 are allowed to any destination to preserve platform connectivity. With a successful lookup, ordinary HTTP and HTTPS internet access requires an enabled outbound policy.

<!-- tabs:end -->

> [!IMPORTANT]
> Always remember to click the **_Apply_** button to save your changes after editing any configuration setting.  **You don't get a warning if not done**.
