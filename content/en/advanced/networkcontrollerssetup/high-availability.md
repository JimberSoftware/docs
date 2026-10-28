# High availability for Network Controllers

High availability (HA) runs two Network Controllers as an active/standby pair.
The primary Network Controller handles traffic during normal operation. The
secondary Network Controller remains in standby and takes over when it can no
longer reach the primary.

Both Network Controllers use the same Network Controller token and communicate
over a dedicated physical HA link. Heartbeats over this link are authenticated
with the shared token.

## How failover works

- The primary runs normally and sends an authenticated heartbeat every second.
- The secondary keeps all interfaces except its loopback and HA interfaces down
  while the primary is available.
- After three consecutive failed heartbeat sessions, the secondary restores its
  network interfaces and becomes active.
- When the primary returns and sends three consecutive ready heartbeats, the
  secondary stops its active services, cleans up, and returns to standby.

The HA link uses `198.51.100.1/30` on the primary, `198.51.100.2/30` on the
secondary, and TCP port `49152`. These settings are applied automatically. Do
not configure IP addresses on the HA interfaces manually.

> [!WARNING]
> The secondary treats a lost HA connection as a primary failure. Use a reliable,
> dedicated physical link to prevent both Network Controllers from becoming
> active at the same time.

## Requirements

Before starting, make sure that:

- Two Network Controllers are installed and have equivalent WAN and LAN
  connectivity.
- Both Network Controllers use the same Network Controller token.
- A dedicated physical network interface is available on each Network
  Controller.
- The dedicated interfaces are connected directly to each other.
- The primary Network Controller is configured and ready before configuring the
  secondary.

> [!TIP]
> As a best practice, use the last available network interface on each Network
> Controller for HA. For example, if `ens18` and `ens19` are available and
> `ens18` is used for normal traffic, use `ens19` for the HA link. Never use the
> WAN interface for HA.

## Configure the primary Network Controller

1. Complete the installation and network configuration steps in
   [Installation of a Network Controller](/./advanced/networkcontrollerssetup/SettingUpServer.md).
2. On the **Configure token (3/4)** page, enter the Network Controller token.
3. Select **High availability**.
4. Set **Role** to **Primary**.
5. Under **High availability interface**, select the dedicated interface. Use
   the last available network interface whenever possible.
6. Select **Next** and wait for the connection verification to complete.

![Primary Network Controller HA configuration](./screenshots/high-availability-primary.png ':size=700')

Leave the primary Network Controller running before continuing with the
secondary.

## Configure the secondary Network Controller

1. Complete the installation and network configuration steps on the second
   Network Controller.
2. Connect its dedicated HA interface directly to the primary's dedicated HA
   interface.
3. On the **Configure token (3/4)** page, enter the same Network Controller token
   used by the primary.
4. Select **High availability**.
5. Set **Role** to **Secondary**.
6. Under **High availability interface**, select the interface connected to the
   primary. Use the last available network interface whenever possible.
7. Select **Next**.

![Secondary Network Controller HA configuration](./screenshots/high-availability-secondary.png ':size=700')

During configuration, the secondary temporarily configures its HA interface and
authenticates to the primary. When the primary is reachable and ready, the
secondary confirms the connection and enters standby.

![Secondary Network Controller connected to the primary](./screenshots/high-availability-secondary-ready.png ':size=700')

## Test failover and handback

Perform a controlled test after both Network Controllers are configured:

1. Shut down the primary Network Controller while leaving the HA cable
   connected.
2. Verify that the secondary restores its normal network interfaces and takes
   over traffic.
3. Start the primary Network Controller again.
4. Verify that the primary becomes ready and the secondary returns to standby.

Do not test failover by disconnecting only the HA cable. A broken HA link can
make the secondary become active while the primary is still serving traffic.

## Troubleshooting

If the secondary cannot connect to the primary during configuration, check that:

- Both Network Controllers use the same token.
- The primary is configured with the **Primary** role and is running.
- The selected HA interfaces are connected directly to each other.
- The selected HA interface is not the WAN interface.
- The selected interfaces are connected and available to the operating system.
