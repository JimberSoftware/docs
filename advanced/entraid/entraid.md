# How to setup Microsoft Entra ID

## Create an account

Go to https://azure.microsoft.com/ and create an Azure Account if you don't already have one.

After creating an account you can go to the [azure portal](https://portal.azure.com/#home).

## Create app registration

On the Azure portal go to App registrations, this is located under 'Azure services'

![azure_portal.png](/azure_portal.png ":size=900")

Register a new application by clicking on “New registration” found on the top left

![azure_new_registration.png](/azure_new_registration.png ":size=900")

Choose a name (eg. JimberNetworkIsolation) and your scope, mostly “Single tenant” will suffice.
You don’t need a redirect URI.
Then click on ‘Register’ at the bottom left of your screen.

![azure_registration_info.png](/azure_registration_info.png ":size=900")

## Permissions

Go to your newly created app registration, and choose 'API Permissions' in the right menu panel.

![apipermissions.png](/apipermissions.png ":size=900")

Following permissions from the Microsoft Graph API are needed:

- Group.Read.All (Application)
- User.Read (Delegated) -> this one should already be created by default
- User.Read.All (Application)

To grant new permissions you can click on 'Add a permission' which is located just above the existing permissions.
Here you can click on the 'Microsoft Graph' button.

![azure_microsoft_graph.png](/request_api.png ":size=900")

As said before you will need to add Group.Read.All and User.Read.All, both are **Application permissions**.

> [!WARNING]
> Make sure to click on the right type of permissions!

![microsoft_graph_type_permissions.png](/request_api_2.png ":size=900")

This will give you a whole list of different permissions where you can search for the right ones: 'Group.Read.All' and 'User.Read.All'.

![permission_group.png](/permission_group.png ":size=500")

![permission_user.png](/permission_user.png ":size=500")

After this is done your permission list should look like this:

![azure_permissions_list.png](/azure_permissions_list.png ":size=900")

Admin consent is required and must be granted for your base directory in Azure. The base directory in our example is 'Standaardmap'.

To do this click on 'Grand admin consent for Standaardmap' which is next to 'Add a permission'. This will change the status for each permission to 'granted'.

![grand_admin_consent.png](/grant_admin_consent.png ":size=900")

> [!NOTE]
> If you cannot grand admin consent this is because your user does not have administrator rights. Please contact the admin of your Azure portal to grant admin consent.

Eventually your permission list should look like this:

![grand_admin_consent.png](/configured_permissions.png ":size=900")

## Client credentials

Go to 'Overview' in the left menu panel to get a list of the essential info.

Here you need to add client credentials:

![azure_credentials.png](/azure_credentials.png ":size=900")

In the next screen, click on 'New client secret'. Choose a description and an expiration date:

![new_client_secret.png](/new_client_secret.png ":size=900")

> [!WARNING]
> When the token expires, manual action is needed to ensure that Entra ID Sync keeps working.

Following information is needed for setup in Jimber Network Isolation:

- The client secret you just created (Value)
- The client ID of your registered application (Found in overview)
- The Tenant ID of your directory (Found in overview)

![new_client_secret.png](/secret_id.png ":size=900")

![needed_info.png](/needed_info.png ":size=900")

To finish setup with Network Isolation go to the following [documentation page](/company/integrations/integrations.md)
