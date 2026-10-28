# How to setup Microsoft Entra ID

### Create an account

Go to https://azure.microsoft.com/ and create an Azure Account if you don't already have one.

After creating an account you can go to the [azure portal](https://portal.azure.com/#home).

### Create app registration

On the Azure portal go to App registrations, this is located under 'Azure services'

![azure_portal.png](./screenshots/azure_portal.png ":size=700")

Register a new application by clicking on “New registration” found on the top left

![azure_new_registration.png](./screenshots/azure_new_registration.png ":size=700")

Choose a name (eg. JimberNetworkIsolation) and your scope, mostly “Single tenant” will suffice.
You don’t need a redirect URI.
Then click on ‘Register’ at the bottom left of your screen.

![azure_registration_info.png](./screenshots/azure_registration_info.png ":size=700")

### Permissions

Go to your newly created app registration, and choose 'API Permissions' in the right menu panel.

![apipermissions.png](./screenshots/apipermissions.png ":size=700")

Following permissions from the Microsoft Graph API are needed:

- Group.Read.All (Application)
- User.Read (Delegated) -> this one should already be created by default
- User.Read.All (Application)
- Device.Read.All (Application) -> required for **auto-login**, see [Auto-login](#auto-login-microsoft-entra-id-sso-on-windows)

To grant new permissions you can click on 'Add a permission' which is located just above the existing permissions.
Here you can click on the 'Microsoft Graph' button.

![azure_microsoft_graph.png](./screenshots/request_api.png ":size=700")

As said before you will need to add Group.Read.All, User.Read.All and Device.Read.All, all three are **Application permissions**.

> [!WARNING]
> Make sure to click on the right type of permissions!

![microsoft_graph_type_permissions.png](./screenshots/request_api_2.png ":size=700")

This will give you a whole list of different permissions where you can search for the right ones: 'Group.Read.All', 'User.Read.All' and 'Device.Read.All'.

![permission_group.png](./screenshots/permission_group.png ":size=500")

![permission_user.png](./screenshots/permission_user.png ":size=500")

After this is done your permission list should look like this (your list will show one extra row, `Device.Read.All`, compared to the screenshot):

![azure_permissions_list.png](./screenshots/azure_permissions_list.png ":size=700")

Admin consent is required and must be granted for your base directory in Azure. The base directory in our example is 'Standaardmap'.

To do this click on 'Grand admin consent for Standaardmap' which is next to 'Add a permission'. This will change the status for each permission to 'granted'.

![grand_admin_consent.png](./screenshots/grant_admin_consent.png ":size=700")

> [!NOTE]
> If you cannot grand admin consent this is because your user does not have administrator rights. Please contact the admin of your Azure portal to grant admin consent.

Eventually your permission list should look like this:

![grand_admin_consent.png](./screenshots/configured_permissions.png ":size=700")

### Auto-login (Microsoft Entra ID SSO on Windows)

The Jimber SASE client on Windows can sign a user in automatically with their Microsoft Entra ID identity instead of showing the browser login. Before the client skips the browser login, the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_*** verifies through Microsoft Graph that the device is Entra-joined and that the signed-in user is registered to that device.

That check uses the `/devices` Graph endpoints, which is why the **Device.Read.All** application permission is required in addition to `Group.Read.All` and `User.Read.All`. It must be added as an **Application permission** and admin consent must be granted for it, just like the other two.

> [!NOTE]
> Auto-login is also a per-group setting in the group configuration. When it is not enabled for a group, the platform does not query Microsoft Graph for that user at all.

> [!WARNING]
> If `Device.Read.All` is missing, was added as a *Delegated* permission, or admin consent was not granted for it, Microsoft Graph replies with *Insufficient privileges to complete the operation*. The platform records this as `Device query failed: Insufficient privileges to complete the operation.` in **Recent Activity**, and affected users fall back to the interactive browser login.

### Client credentials

Go to 'Overview' in the left menu panel to get a list of the essential info.

Here you need to add client credentials:

![azure_credentials.png](./screenshots/azure_credentials.png ":size=700")

In the next screen, click on 'New client secret'. Choose a description and an expiration date:

![new_client_secret.png](./screenshots/new_client_secret.png ":size=700")

> [!WARNING]
> When the token expires, manual action is needed to ensure that Entra ID Sync keeps working.

Following information is needed for setup in Jimber Network Isolation:

- The client secret you just created (Value)
- The client ID of your registered application (Found in overview)
- The Tenant ID of your directory (Found in overview)

![new_client_secret.png](./screenshots/secret_id.png ":size=700")

![needed_info.png](./screenshots/needed_info.png ":size=700")

To finish setup with Network Isolation go to the following [documentation page](/company/integrations/integrations.md).
