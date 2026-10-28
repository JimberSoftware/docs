# OIDC Login

OpenID Connect (OIDC) lets users sign in to the Jimber SASE Platform through an external identity provider, such as Okta, Keycloak, Auth0, or ZITADEL.

OIDC is an identity layer built on OAuth 2.0. In this integration:

- The Jimber SASE Platform is the relying party, sometimes called the service provider.
- Your identity provider authenticates the user and applies its own security policies.
- The identity provider returns signed identity claims to SASE.
- SASE matches the verified e-mail claim to an existing user in the selected company and creates the SASE session.

The SASE Platform uses the authorization code flow with PKCE. The user's identity-provider password is entered only at the identity provider and is not stored by Jimber.

## Why OIDC login is included

OIDC allows an organization to use its existing identity platform as the central place for authentication. This provides several benefits:

- **One organizational identity:** Users can access SASE with the same account they use for other company applications.
- **Central security controls:** The identity provider can enforce multi-factor authentication, conditional access, password policies, and account lockout.
- **Faster account lifecycle changes:** Disabling an identity-provider account prevents new OIDC sign-ins without managing another SASE password.
- **Fewer passwords:** SASE does not need a separate password for users who authenticate through OIDC.
- **Vendor-neutral integration:** Any standards-compliant OIDC provider can be used.

OIDC login authenticates users but does not provision them. Create or synchronize the user in SASE before the first OIDC sign-in. The SASE user and the identity-provider account must have the same verified e-mail address.

## Prerequisites

Before configuring OIDC, make sure that:

- The OIDC integration is included in the company's SASE plan.
- You have permission to manage the company's SASE configuration.
- You can create a confidential web application at the identity provider.
- Every user who will sign in already exists in the SASE company.
- The identity provider exposes its issuer and discovery endpoints over public HTTPS.
- The identity provider returns a verified `email` claim.

Keep at least one existing administrator login method enabled while configuring and testing OIDC.

## 1. Create the identity-provider application

Create a confidential web application at the identity provider with these settings:

| Setting                       | Value                                              |
| ----------------------------- | -------------------------------------------------- |
| Application type              | Web                                                |
| Flow                          | Authorization code with PKCE (`S256`)              |
| Redirect URI                  | `https://sase.jimber.io/api/v1/auth/oidc/callback` |
| Token endpoint authentication | `client_secret_post`                               |
| Scopes                        | `openid profile email`                             |

The redirect URI is also displayed in the SASE provider form. Copy it exactly, including the scheme and path.

After creating the application, copy its client ID and client secret. Store the secret securely because it may be shown only once.

> [!NOTE]
> Provider consoles use different labels for token endpoint authentication. For example, ZITADEL calls `client_secret_post` simply **Post**.

## 2. Add the provider in SASE

1. Open **Company > Configuration**.
2. In **Authentication**, select **Add OIDC provider**.
3. Complete the provider form.

![Add an OIDC provider in the Jimber SASE Platform](./screenshots/oidc-provider-form.png ':size=360')

Use the following values:

- **Provider name:** The name shown on the company sign-in page, for example `Company SSO`.
- **Issuer URL:** The exact issuer value from the provider's discovery document.
- **Discovery URL:** Usually `<issuer>/.well-known/openid-configuration`. SASE derives this URL automatically and allows it to be changed for providers that publish metadata elsewhere.
- **Client ID:** The client ID of the application created at the identity provider.
- **Client secret:** The application's client secret.
- **Scopes:** Use `openid profile email` unless the provider requires additional scopes.
- **Email claim:** Use `email` unless the provider exposes the verified user address under another claim name.

Select **Add provider** to save the configuration.

## 3. Test the sign-in flow

1. Open the company-specific sign-in URL in a private browser window:

    ```text
    https://sase.jimber.io/login/<company-name>
    ```

2. Select the configured OIDC provider.

![Select the OIDC provider on the company sign-in page](./screenshots/oidc-login-screen.jpg ':size=480')

3. Authenticate at the identity provider.
4. Confirm that the browser returns to the SASE dashboard.

The provider button uses the configured provider name. A company can configure multiple OIDC providers when different user groups authenticate through different identity systems.

## How SASE matches a user

After the identity provider returns the authorization response, SASE validates the state, nonce, PKCE verifier, token signature, issuer, and subject. SASE then reads the configured e-mail claim.

For a user's first sign-in through a provider:

- The claim must contain an e-mail address.
- The provider must mark the standard `email` claim as verified.
- The verified address must match an existing user in the same SASE company.

After a successful match, SASE links the provider subject to that user. Future sign-ins use this provider-specific subject link while preserving the company boundary.

## Troubleshooting

If SASE displays **OIDC sign-in failed**, verify the following:

- The issuer URL exactly matches the `issuer` value in the discovery document.
- The discovery URL is reachable through public HTTPS.
- The redirect URI at the identity provider exactly matches the URI displayed by SASE.
- The client ID and client secret are current.
- The identity provider accepts `client_secret_post` at its token endpoint.
- The authorization code flow and PKCE `S256` are enabled.
- The requested scopes include `openid` and the provider returns the configured e-mail claim.
- The provider returns `email_verified: true` for a first-time link.
- A SASE user with the same e-mail address exists in the selected company and is enabled.

Administrators can review **Monitoring > Activity** for an OIDC login failure entry. If the issue persists, copy the SASE debug information and include it in a support request. Never include the client secret in screenshots, tickets, or logs.

## Updating or removing a provider

Use **Edit** next to the provider to change its display name, endpoints, credentials, scopes, or e-mail claim. When rotating the client secret, update the identity provider and SASE together, then run another private-window sign-in test.

Before disabling or removing a provider, confirm that another sign-in method remains available. This prevents administrators from being locked out of the company.
