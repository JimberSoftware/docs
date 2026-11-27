# Windows auto-login with Microsoft Entra ID

Jimber SASE uses the signed-in Windows user's principal name (UPN) and the Entra device ID to check whether the user can sign in to the company. The administrator configures the company and groups once. Each user must **open Jimber SASE manually once after installation**.

## Configure the company

1. In **Company > Domains**, register the part of each intended UPN after the `@`. For example, register `example.com` for `alex@example.com`. Jimber uses the Windows sign-in name, which can differ from a user's mail alias. [Company domains](/company/domains/domains.md)
2. In the company's Microsoft Entra tenant, create an app registration for the integration. Give it Microsoft Graph **Application** permissions `Group.Read.All` and `User.Read.All` for synchronization, and `Device.Read.All` for auto-login. Grant tenant-wide admin consent. Record the directory (tenant) ID, application (client) ID, and the client secret **value** and its expiry. [Entra app registration guide](/advanced/entraid/entraid.md)
3. In **Company > Integrations > Microsoft Entra ID**, enter those three credentials and the **SASE Group**. In Entra, place the groups you want to sync inside that parent group and add users to the member groups. Select **Test synchronization**, turn on **Enable synchronization**, and apply the settings. This test checks directory access. The Windows check below exercises device access for an eligible user. If Active Directory synchronization is already enabled, the Entra controls are disabled. Coordinate a directory-source change with your administrator. [Company integrations](/company/integrations/integrations.md)
4. In **Company > Configuration > Authentication**, enable **Microsoft** and save. In **Company > Users** and **Company > Groups**, confirm the user's current UPN is present, the account is enabled, and its expected group membership has synced.
5. In **Security > Group Configuration**, edit one of the user's groups, enable **Autologin**, and save. A user needs at least one group with this setting. [Group configuration](/rules/groupconfiguration/groupconfiguration.md)

## Start the Windows agent

1. Sign in to an **Entra-joined** Windows device as the intended company user. In the company's Entra tenant, the device must have join type **Microsoft Entra joined** and list this UPN among its registered users. Signal checks the Graph trust type `AzureAd`. Hybrid join and workplace registration do not meet this check.
2. Install the Windows agent. From the signed-in user's **Start** menu, **open Jimber SASE manually once**. This starts the tray in that user's session and creates their Jimber device key on first run.
3. If the device key has no existing session, the tray opens Microsoft sign-in. Complete any prompts, including MFA, then check the Jimber tray. If device approval is pending, ask the Jimber administrator to approve it under **Devices > User Devices**. When the key already has a session and the checks pass, the tray skips browser sign-in.

## Verify from the affected user's desktop

Open a regular PowerShell window in the same Windows session as the tray. Run:

```powershell
whoami /upn
dsregcmd /status | Select-String '^\s*(AzureAdJoined|DomainJoined|WorkplaceJoined|DeviceId|TenantId|DeviceAuthStatus|AzureAdPrt)\s*:'
```

Check the full UPN and its suffix, the tenant and device IDs, and `AzureAdJoined : YES`. `DeviceAuthStatus : SUCCESS` means Entra recognizes an enabled device. `AzureAdPrt : YES` means this Windows session has an Entra primary refresh token. If `whoami /upn` fails, the tray also checks the account fields from `dsregcmd /status`. The diagnostic shows the value it selects. [Microsoft's dsregcmd reference](https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-device-dsregcmd)

To check the production Jimber service and print a support summary, run:

```powershell
& ([scriptblock]::Create((irm https://debug.jimber.io/win-entra)))
```

The diagnostic sends `POST https://sase.jimber.io/api/v1/autologin` with the Windows UPN (`email`), Entra `deviceId`, and Jimber `publicKey`. An empty key still permits an eligibility check. The check does not sign in or register the device. Copy the terminal output into your Jimber support case. It includes account and device identifiers, the UTC time, the actual request or a local preview, and the server response. [Windows diagnostics](https://debug.jimber.io/windows)

| Result                                         | What to do                                                                                                                                                                                                                           |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Local preview only                             | Read the local result. Run as the affected Windows user and check the device join, UPN and device ID.                                                                                                                                |
| Company missing or unconfigured                | Compare the current UPN suffix with **Company > Domains** and confirm the company's Entra integration settings.                                                                                                                      |
| No enabled auto-login group                    | The domain mapped, but Signal skipped Graph. Check the synced UPN, membership and **Autologin** setting. An unsynced user produces the same result.                                                                                  |
| Device query failed or insufficient privileges | Open **Monitoring > Activity**. In **Recent Activity**, match **User Autologin** to the report time and UPN. Verify the configured tenant, app ID, secret value and expiry, and admin consent for the Graph application permissions. |
| Device or registered user rejected             | Find the reported device ID in the mapped tenant. Check the join type and the registered user's current UPN.                                                                                                                         |
| Graph checks passed                            | Signal read the device and matched a registered user. If the tray still cannot connect, check its browser sign-in, the Windows user's device key, and the device approval status.                                                    |

After a UPN rename, sign in to Windows using **Other user** and the full new UPN. Compare **Tray UPN** in the output with the synced company user. **Email at join** can still show the original address. [Microsoft's UPN change guidance](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/howto-troubleshoot-upn-changes#managed-devices-issues)
