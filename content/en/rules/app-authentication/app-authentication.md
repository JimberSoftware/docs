# App Authentication (SAML and OIDC)

App Authentication lets the **_<span style="color: darkblue;">Jimber SASE Platform</span>_** act as the identity provider for internal and third-party applications. Users sign in with their Jimber identity while application owners continue to use the standard SAML 2.0 or OpenID Connect (OIDC) integration offered by their application.

## Why use App Authentication?

- **One identity for more applications:** users do not need another application-specific password.
- **Central access control:** grant access to users or groups and remove access from the same place when responsibilities change.
- **Device-aware protection:** optionally require an approved device running the Jimber agent before authentication is allowed.
- **Standards-based integration:** connect SAML service providers and OIDC relying parties without a proprietary authentication protocol.
- **Reduced data exposure:** release only the attributes, scopes, and claims that an application needs.
- **Auditable access:** review user sign-ins and protocol events from the SASE monitoring interface.

> [!NOTE]
> App Authentication controls who can authenticate to an application. If the application is hosted on a private network, configure the required service and firewall policy separately.

## Before you begin

Collect the integration values supplied by the application:

- For SAML: the service provider entity ID, Assertion Consumer Service (ACS) URL, optional Single Logout URL, expected NameID format, and any required attributes.
- For OIDC: the redirect URI, application type, supported token endpoint authentication method, requested scopes, and optional post-logout redirect URI.

Make sure the users who will sign in have the required profile data, such as an email address, first name, last name, and display name.

In the SASE platform, go to **Security > App Authentication**. Select **View IdP details** to obtain the SAML metadata and the OIDC discovery URL. Prefer metadata or discovery over copying individual endpoints, because applications can then discover the correct endpoints and signing keys.

## Create an application

![create_authentication](./screenshots/create_authentication.png ":size=600")

1. Go to **Security > App Authentication**.
2. Select **Create new**.

    ![create_authentication](./screenshots/create_authentication2.png ":size=600")

3. Choose **SAML 2.0** or **OpenID Connect (OIDC)**. The protocol cannot be changed after the application is created.
4. Enter a recognizable service name (required), a short description, and the application URL.
5. Configure the protocol-specific settings described below.
6. Add at least one assignment.
7. Select **Save changes**.

>[!ATTENTION]
>The application URL is the destination opened from the Security Panel. It is not used as a SAML ACS URL or OIDC redirect URI unless the application explicitly documents the same URL for both purposes.

## Configure a SAML application

#### Basic Settings

Enter the values provided by the service provider:

- **SP Entity ID:** the unique identifier of the service provider (required).
- **Primary ACS URL:** the exact endpoint that receives the SAML response (required).
- **SP Single Logout URL:** an optional endpoint for SP-initiated logout responses.
- **NameID source and format:** the user value and identifier format expected by the service provider. A persistent identifier is the most privacy-preserving option when the application supports it.

#### Application Access

Here, you can choose to see a launch tile in your Security Panel, and to refuse sign-in without an approved enrolled device.

#### SAML Security

SAML assertions are signed with RSA-SHA256. Keep **Sign assertion** enabled unless the service provider explicitly requires the complete response to be signed instead. Enable signed authentication requests or assertion encryption only when the service provider supports them, and supply the corresponding service provider certificate.

#### Additional ACS endpoints

Use **Additional ACS endpoints** only for documented failover, regional, or private-connectivity endpoints. SASE accepts only registered endpoints.

#### Attributes

On the **Attributes** tab, map every attribute required by the service provider to the appropriate Jimber user field. Avoid sending attributes the application does not need.

 ![attributes](./screenshots/attributes.png ":size=600")

> [!TIP]
> Import the SASE SAML metadata into the service provider when possible. The metadata contains the entity ID, sign-in endpoint, logout endpoint, and signing certificate.

## Configure an OIDC application

#### Options

Choose the client settings that match the application:

- **Public client:** browser, mobile, desktop, or other software that cannot safely keep a secret. Token endpoint authentication is **None-PKCE only**.
- **Confidential client:** server-side software that can protect a client secret. Select the token endpoint authentication method documented by the application.
- **Application type:** select web or native to match where the client runs.
- **Subject identifier:** use the recommended pairwise subject unless the application has a documented need for another identifier.
- **Redirect URIs:** register every callback exactly. Wildcards are not accepted.
- **Post-logout redirect URIs:** optional exact destinations that may be used after logout.
- **Token lifetime and refresh tokens:** keep access tokens short-lived and enable refresh tokens only when the application needs long-running access.

![OIDC application settings in Jimber SASE](./screenshots/oidc-settings.png ':size=800')

After saving, copy the generated client ID into the application. A confidential client secret is shown only when it is created or regenerated. **Copy it immediately** and store it in the application's secret store.

> [!IMPORTANT]
> Public clients must use the Authorization Code flow with PKCE. Use the `S256` code challenge method and never place a client secret in browser or installed application code.

#### Select scopes and claims

The _**openid**_ scope is always enabled. Enable only the additional data the application requires:

- _**profile**_ supplies _*name*_, _*given_name*_, _*family_name*_, and _*preferred_username*_.
- _**email**_ supplies _email_ and *email_verified*.
- _**groups**_ supplies *directory group memberships*.
- <b>offline_access</b> is enabled when refresh tokens are allowed.

Review the source of each claim. The immutable user ID is always used for `sub`. The remaining claims can be mapped to the corresponding user profile values.

![OIDC scopes and claim mappings in Jimber SASE](./screenshots/scopes-and-claims.png ':size=800')

## Assign access and apply device protection

Open **Assignments**, select **Add Assignments**, and choose the users or groups that may sign in. A user must be covered by an assignment before SASE will authorize the application.

![An assigned user in Jimber SASE](./screenshots/assignments.png ':size=800')

The application options also provide two access controls:

- **Show in security panel:** displays a launch tile to assigned users.
- **Require Jimber agent:** refuses sign-in unless the user is on an approved enrolled device. Use this when application access must be tied to device trust.

## Test sign-in

After saving the application, select **Start test sign-in**. Complete the application's authentication flow and verify the following:

- SAML responses arrive at the registered ACS endpoint, or OIDC authorization returns to the exact redirect URI.
- The application recognizes the expected user identifier.
- Required attributes or claims contain the expected profile values.
- Public OIDC clients exchange the authorization code with the original PKCE verifier and without a client secret.

>[!NOTE]
>Testing proves that the identity exchange works. The application itself remains responsible for creating its local session and applying its own authorization rules.

## Monitor sign-ins

Select **View sign-in activity** from an application, or go to **Monitoring > App Authentication**.

- **Sign-in Activity** shows user-facing sign-in attempts by time, application, protocol, and user.

![OIDC sign-in activity in Jimber SASE](./screenshots/sign-in-activity.png ':size=800')


- **Authentication Events** shows the individual SAML or OIDC protocol events and failures used to troubleshoot an attempt.

![OIDC Authentication Events in Jimber SASE](./screenshots/authentication.png ':size=800')

- **Details**

Clicking on the corresponding strip of a line opens a detailed view with additional information:


![details.png](./screenshots/details.png ':size=600')


## Troubleshooting

| Symptom                                            | What to check                                                                                                               |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| The user is not assigned                           | Assign the user directly or through a group in the same company context.                                                    |
| The application reports a redirect or ACS mismatch | Copy the exact registered URL, including scheme, host, path, port, and trailing slash.                                      |
| An OIDC callback has no authorization code         | Review the authorization failure under **Authentication Events**, the client assignment, redirect URI, and PKCE parameters. |
| A public OIDC client asks for a client secret      | Configure it as a public client and use Authorization Code with PKCE instead of a secret.                                   |
| A claim or SAML attribute is empty                 | Enable the required scope or attribute mapping and verify that the selected source exists on the user's profile.            |
| Sign-in is refused because an agent is required    | Use an approved enrolled device running the Jimber agent, or disable the requirement if device trust is not needed.         |

## Security recommendations

- Use HTTPS callback, ACS, logout, and application URLs in production.
- Prefer SAML metadata and OIDC discovery so endpoints and signing keys stay current.
- Use pairwise OIDC subjects and persistent SAML identifiers where supported.
- Use PKCE with `S256`, especially for public clients.
- Keep confidential client secrets in a server-side secret store and rotate them if exposed.
- Grant access through the smallest appropriate user or group assignment.
- Release only the attributes, scopes, and claims required by the application.
- Review **Authentication Events** after configuration changes and when investigating failed sign-ins.
