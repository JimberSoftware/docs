# ![](../../images/menu/menu_configuration.png ':size=25') Configuration

The **Configuration** section lets you manage essential settings for your company and how user devices interact with your network. It is divided into two main areas:

### Company Settings

These settings define general information about your company within the **_*<span style="color: darkblue;">Jimber SASE Platform</span>*_**.

![Company Configuration](./screenshots/config_company.png ':size=600')

- **Display name**: This is the company name as it will appear throughout the platform for users and administrators.
- **Primary contact email**: Enter a contact email address that can be used for support or administrative purposes.
- **Website URL**: Specify your company’s website.

    > [!INFO]
    > The platform will automatically try to extract the company logo from this URL and display it in the user interface.

### Network Isolation <!--Jimber SASE Licence--> Settings

These settings control how user devices are managed and isolated in your environment.

![Network Isolation Configuration](./screenshots/config_ni.png ':size=600')

- **IP range**: Define the internal IP range used for isolated network segments.

- **User devices expiry time**: Set how many days a user device remains active before it expires (default = 30 days).

- **Amount of devices allowed per user**: Specify the maximum number of devices per user (default = 3).

- **Download Certificate**: Download the company's current Jimber root CA certificate. The issued and expiry dates shown below the buttons identify the certificate you are downloading.

- **Request New Certificate**: Immediately replace the current certificate with a newly generated certificate. The old certificate stops working as soon as you confirm the warning. Devices can lose connectivity until the new certificate is deployed and trusted.

    Use the [Microsoft Intune deployment guide](./root-certificate-intune.md) to install the certificate on managed macOS devices.

### Zero Trust Outbound

Zero Trust Outbound (ZTO) controls internet access through enabled outbound policies. Managed endpoints retain the following built-in exceptions even when their outbound policies are disabled:

| Protocol    | Destination port                                     | Allowed destinations                                                                                          |
| ----------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| TCP and UDP | 53 (DNS)                                             | Any destination                                                                                               |
| TCP and UDP | 51820 (Jimber tunnel connectivity)                   | Any destination                                                                                               |
| TCP         | 80 and 443 (Signal Server and Lifeline connectivity) | IP addresses resolved from the Signal Server URL and configured Lifeline addresses, including its fallback IP |

DNS is allowed by default, so the automatically created **Standard Internet** service does not include port 53. Disabling a Standard Internet policy does not block DNS or Jimber tunnel connectivity.

If a Signal Server or Lifeline hostname lookup fails or returns no IP addresses, TCP ports 80 and 443 are allowed to any destination to preserve platform connectivity. With a successful lookup, ordinary HTTP and HTTPS internet access requires an enabled outbound policy.

> [!IMPORTANT]
> Always remember to click the **_Apply_** button to save your changes after editing any configuration setting.
