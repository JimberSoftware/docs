# ![](../../images/menu/menu_integrations.png ':size=25') Integrations

<!-- ## Credentials: API Key

API keys are a way to authenticate and grant access to various resources of an application or platform via its API. They are typically used to facilitate the interaction of third-party software with your application, enabling automation, integration, and other advanced functionalities.

![api_key.png](api_key.png) -->


## DNS

A DNS forwarder redirects DNS queries from one server to another. It's useful for managing and speeding up DNS queries by redirecting requests to a faster or more updated DNS server than the one set by default.
To do so, enter the IP address of the DNS server and click on the apply button.

![dns_forwarder.png](./screenshots/dns_forwarder.png ":size=500")



## Microsoft Entra ID

Synchronize your user data seamlessly from Microsoft Entra ID to the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***. This ensures that user information remains consistent across both platforms, providing ease of user management.

> [!INFO]
> Detailed instructions are available in the Advanced section [here](/./advanced/entraid/entraid.md).

![micro_entra_id.png](./screenshots/micro_entra_id.png ":size=500")

<!-- >[!IMPORTANT]
>To activate **Enable Synchronization** in Microsoft Entra ID, you have to disable Active Directory syncing as indicated. -->

> [!CAUTION]
> Ensure that you have appropriate permissions in Microsoft Entra ID to enable synchronization and always backup user data in the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_*** before starting the process.

#### **Steps to enable synchronization**:

1. **SASE Group**: The name of a group on Microsoft Entra ID where all groups that should be synchronized are a member of. All member groups of this group (and their users) will be synced to the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***.

2. **Tenant ID**: A unique identifier that represents your Microsoft Entra ID organization.

3. **Client ID**: Represents the application registration in Microsoft Entra ID.

4. **Client Secret**: A password created for the application registration in Microsoft Entra ID. This is used to authenticate the application during the synchronization process.


>[!TIP]
>The button *Test synchronization* enables you to test whether the authentication with EntraID was successful.
<!-- 

> [!INFO]
> Detailed instructions are available in the Advanced section [here](/./advanced/ad_integration/ad_integration.md).

![integration_ad.png](./screenshots/integration_ad.png ":size=800")

> [!IMPORTANT]
>To activate **Enable Synchronization** in Active Directory, you have to disable Microsoft Entra ID syncing as indicated.
 -->