# Logging

This section provides an overview of where you can find Jimber SASE log files on user devices and servers, across different platforms. Proper access to these logs is essential for troubleshooting and monitoring the behavior of the application.

### Overview of Log Types

- **Client Logs:** Capture information about the startup and operation of the `Jimber SASE Client` application on user devices.
- **Server Logs:** Record details about the server-side component of `Jimber SASE Platform`.
- **Service Logs:** Contain information about the `Jimber SASE Service`, the local background service responsible for managing connectivity and other essential tasks.
- **Launcher Logs:** Track activities related to launching and updating the Jimber applications.
- **Debug Logs:** Special empty files that enable enhanced logging in the other log files when present.

> [!WARNING]
> The `debug.log` file itself does **not** contain logs. Instead, when present, it enables verbose logging across the client, server, and service layers to assist in diagnosing issues

---

### Enabling Debug Logging

To activate extended debug logging, create an **empty** file named `debug.log` in the appropriate directory for your platform:

- **Windows:** `%PROGRAMFILES%\Jimber\`
- **Linux / macOS / Network Controllers:** `/var/log/jimber/`

Once created, the system will produce more detailed logs that can help identify issues.

---

### Log File Locations by Platform

#### Windows

##### Desktop (User Devices)
- Client log: `%LocalAppData%\Jimber\client.log`
- Service log: `%PROGRAMFILES%\Jimber\service.log`
- Launcher log: `%PROGRAMFILES%\Jimber\launcher.log`
- Debug trigger file: `%PROGRAMFILES%\Jimber\debug.log`

##### Server
- Server log: `%PROGRAMFILES%\Jimber\server.log`
- Launcher log: `%PROGRAMFILES%\Jimber\launcher.log`
- Debug trigger file: `%PROGRAMFILES%\Jimber\debug.log`

---

#### Linux

##### Desktop (User Devices)
- Client log: `~/.local/share/jimber/client.log`
- Service log: `/var/log/jimber/service.log`
- Launcher log: `/var/log/jimber/launcher.log`
- Debug trigger file: `/var/log/jimber/debug.log`

##### Server
- Server log: `/var/log/jimber/server.log`
- Launcher log: `/var/log/jimber/launcher.log`
- Debug trigger file: `/var/log/jimber/debug.log`

---

#### macOS

##### Desktop (User Devices)
- Client log: `~/Library/Application Support/Jimber/client.log`
- Service log: `/var/log/Jimber/service.log`
- Launcher log: `/var/log/Jimber/launcher.log`
- Debug trigger file: `/var/log/Jimber/debug.log`

---

#### Network Controller / NIAC / Synology / Raspberry Pi

- Server log: `/var/log/jimber/server.log`
- Launcher log: `/var/log/jimber/launcher.log`
- Debug trigger file: `/var/log/jimber/debug.log`

---

### Notes and Best Practices

- Creating the `debug.log` file is recommended only when troubleshooting specific issues, as it increases log verbosity and can generate large log files.
- Regularly monitor and archive logs in production environments to prevent excessive disk usage.
- When reporting issues to support, including relevant log files (especially with debug logging enabled) will accelerate diagnosis.

