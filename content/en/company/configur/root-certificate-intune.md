# Deploy the Jimber root certificate to macOS with Microsoft Intune

Use a Microsoft Intune trusted certificate profile to install your company's Jimber root CA certificate on managed macOS devices. This avoids installing and trusting the certificate manually on every device.

## Before you begin

You need permission to manage your company in Jimber SASE and to create configuration profiles in the Microsoft Intune admin center.

1. In Jimber SASE, open **Company**, then **Configuration**.
2. In the **Network Isolation** card, select **Download Certificate**.
3. Confirm that the downloaded file has a `.cer` extension. The file contains the public certificate only. Never upload or distribute a private key.

## Create the trusted certificate profile

1. In the [Microsoft Intune admin center](https://intune.microsoft.com), go to **Devices** > **macOS** > **Configuration**.
2. Select **Create**, then **New policy**.
3. For **Platform**, select **macOS**.
4. For **Profile type**, select **Templates**.
5. For **Template**, select **Trusted certificate**.
6. Enter a recognizable name and description for the profile.
7. Upload the root certificate downloaded from Jimber SASE. Intune accepts `.cer`, `.crt`, and `.der` files containing a DER or Base64-encoded X.509 certificate.
8. Assign the profile to the appropriate device or user groups.
9. Review the profile and select **Create**.

Intune installs the certificate in the macOS System Keychain as a trusted root on assigned devices.

## Verify the deployment

Open the profile in Intune and review **Device status** and **User status**. Resolve any assignment or installation errors before the expiry date shown in Jimber SASE.

When Jimber notifies you about an upcoming expiry, plan the change before selecting **Request New Certificate**. Confirming that action replaces the certificate immediately. Download the new certificate and update the Intune profile right away so managed devices regain or retain connectivity.
