# ![](../../images/menu/menu_edr.png ':size=50') EDR Configuration

Endpoint Detection and Response (EDR) monitors Windows endpoints for suspicious activity and can respond automatically when a threat is detected. Configure EDR per group so that the response matches the severity of the detection.

> [!IMPORTANT]
> EDR must be available for your company and enabled for the selected group under **Security > Group Configuration**. Only groups with EDR enabled appear on this page.

## Configure EDR for a group

1. Go to **Security > EDR > EDR Configuration**.
2. Select the group you want to configure.
3. Use the switch on a detection card to enable or disable that detection.
4. For each enabled detection, choose the automatic response for each severity level: **Low**, **Medium**, **High**, or **Critical**.
5. Select **Submit** to apply the configuration.

![EDR Configuration with malicious file detection settings](./screenshots/edrconfiguration.png ':size=1000')

> [!NOTE]
> Enabling a detection without selecting a response action still records detections in the relevant EDR monitoring page. It does not take an automatic response action.

> [!TIP]
> Start with monitoring or less disruptive responses, review the detections, and then enable stronger responses for higher severity levels. This helps reduce disruption from false positives.

### Response actions

| Action | Result |
|---|---|
| **Quarantine** | Quarantines the detected file on the endpoint. |
| **Disable SASE** | Removes the affected device's SASE access. Administrator action may be required before the device can connect again. |
| **Lockdown** | Locks down networking on the endpoint. An administrator must restore the Windows network connection. |

You can select more than one available response action for the same severity level.

> [!WARNING]
> **Disable SASE** interrupts access through Jimber SASE, while **Lockdown** interrupts all networking on the endpoint. Test these responses with a limited group before enabling them broadly.

## Detection types

### Malicious File Detection

Scans files for malicious content. Select a sensitivity level, then configure the response for each severity.

- **Standard** provides the baseline level of detection.
- **Extended** performs broader detection.
- **High** provides the broadest detection and can produce more false positives.

Available responses: **Quarantine**, **Disable SASE**, and **Lockdown**.

### Network Anomaly Detection

Detects suspicious network behavior on the endpoint. Configure **Disable SASE** and **Lockdown** independently for each severity level.

![Network anomaly detection settings](./screenshots/network-anomaly-detection.png ':size=1000')

### Unsigned Binaries

Detects executable files and libraries that do not have a trusted digital signature. Configure **Quarantine** independently for each severity level.

![Unsigned binary and file anomaly detection settings](./screenshots/unsigned-binaries-file-anomaly.png ':size=1000')

### File Anomaly Detection

Detects unusual file activity and records it for review. This detection has no configurable automatic response actions.

### Windows Defender

Monitors supported Microsoft Defender Antivirus events. Configure **Disable SASE** and **Lockdown** independently for each severity level.

![Windows Defender settings](./screenshots/windows-defender.png ':size=1000')

> [!NOTE]
> If an endpoint belongs to multiple groups, its EDR configuration combines the enabled detections and response actions from those groups. Malicious File Detection uses the highest configured sensitivity.

## Review detections

Open the relevant page under **Monitoring > EDR** to review detections, severity, affected device, and the action taken. See the [Monitoring documentation](/./monitoring/monitoring.md) for more information.

## EDR Whitelist

The EDR whitelist prevents a trusted file from triggering Malicious File Detection. A whitelist entry applies to the file's SHA-256 hash, so a changed version of the file requires a new entry.

> [!WARNING]
> Only whitelist files that you have verified and trust. A whitelisted file is excluded from malicious file detection.

### Create a whitelist entry

1. Go to **Security > EDR > EDR Whitelist**.
2. Select **+ Create new**.
3. Enter a recognizable filename.
4. Enter the file's SHA-256 hash.
5. Save the entry.

![Create an EDR whitelist entry](./screenshots/create_whitelist.png ':size=500')

On Windows, you can calculate the hash in PowerShell:

```powershell
Get-FileHash -Algorithm SHA256 "C:\path\to\file.exe"