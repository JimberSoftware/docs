### Guide: Installing Software on Teltonika RUT950/RUT955 with OpenWRT

This guide provides step-by-step instructions for installing and configuring OpenWRT on a Teltonika RUT950 or RUT955 device and installing the necessary software to use the device as a Network Controller within Jimber SASE.

---

### Prerequisites

- Teltonika RUT950/RUT955 device
- OpenWRT firmware file (`openwrt-23.05.0-ath79-generic-teltonika_rut955-squashfs-factory.bin`) [here](https://downloads.openwrt.org/releases/23.05.0/targets/ath79/generic/openwrt-23.05.0-ath79-generic-teltonika_rut955-squashfs-factory.bin)
- SSH access to the device (use user root with the admin password)
- Device connected to the internet

---

### 1. Install OpenWRT on Teltonika RUT950/RUT955

1. **Transfer the OpenWRT firmware to the device:**

   Open a terminal and execute the following SCP command to upload the OpenWRT firmware to the Teltonika device:

   ```bash
   scp openwrt-23.05.0-ath79-generic-teltonika_rut955-squashfs-factory.bin root@192.168.1.1:/tmp/
   ```

2. **SSH into the Teltonika device:**

   ```bash
   ssh root@192.168.1.1
   ```

3. **Flash the firmware using `sysupgrade`:**

   Navigate to the `/tmp` directory where the firmware was uploaded:

   ```bash
   cd /tmp/
   ```

   Run the following commands to upgrade the firmware:

   ```bash
   sysupgrade -F -v openwrt-23.05.0-ath79-generic-teltonika_rut955-squashfs-factory.bin
   ```

---

### 2. Resolving SSH Key Issues

If the SSH host key changes, you may encounter the following warning:

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
```

To resolve this:

1. Remove the old host key using the following command:

   ```bash
   ssh-keygen -f "/home/yourusername/.ssh/known_hosts" -R "192.168.1.1"
   ```

2. After removing the old key, reconnect to the device:

   ```bash
   ssh root@192.168.1.1
   ```

---

### 3. Configure OpenWRT and Install Required Packages

1. **Ensure the device is connected to the internet.**  
   Then update the package lists:

   ```bash
   opkg update
   ```

   If you encounter a `wget returned 5` error, run:

   ```bash
   opkg update --no-check-certificate
   ```

2. **Stop unnecessary services:**

   Disable and stop the firewall and web server:

   ```bash
   /etc/init.d/firewall stop
   /etc/init.d/firewall disable
   /etc/init.d/uhttpd disable
   /etc/init.d/uhttpd stop
   ```

3. **Install essential packages:**

   Install the necessary software components:

   ```bash
   opkg install wireguard-tools redis-server nano iptables-mod-nfqueue iptables kmod-ipt-nat iptables-mod-conntrack-extra bash libnetfilter-queue coreutils-stat
   ```

---

### 4. Install the Software Client

1. **Download the software client IPK file:**

   ```bash
   cd /tmp/
   wget https://signal.jimber.io/clients/linux-router-openwrt-latest.ipk
   ```

2. **Install the software client:**

   ```bash
   opkg install linux-router-openwrt-latest.ipk
   ```

3. **Expected installation output:**

   During the installation, you should see output similar to:

   ```bash
   Installing jimberfw (v1.12.0-router_openwrt22) to root...
   Configuring jimberfw.
   Downloading binaries...
   Download completed.
   Starting jimberfw...
   ```

---

### 5. Verify the Installation

1. **Check the version of the installed software:**

   ```bash
   jimberfw -version
   ```

   Example output:

   ```
   -------------------------------------------------------------
   Version: v1.12.0-router-openwrt11
   Launcher version: v1.4.0-router02
   Build date: 2024-08-09T06:31:24
   Environment: production
   SHA commit hash: 492c3ce92cc71bf5a1d6ff4bb8a4e032ae7bbd9c
   Signal server endpoint: https://signal.jimber.io
   Websocket endpoint: wss://signal.jimber.io:443
   -------------------------------------------------------------
   ```

---

### 6. Configure the Jimber Firewall

1. **Locate the settings file:**

   Open the settings file using `nano`:

   ```bash
   nano /etc/jimber/settings.json
   ```

2. **Update the file with your token, WAN IP, and interface:**

   Modify the file to include the required details:

   ```json
   {
     "alwaysOn": false,
     "privateKey": "8PHRDemPvmyTBBg2ByUbLTdky/aL7SDZNOaQ7Tw/RbH1QNjYxOthS+iWHhaGwM/4nM1v28gCH2b0YfgvyUFOBw==",
     "publicKey": "9UDY2MTrYUvolh4WhsDP+JzNb9vIAh9GH4L8lBTgc=",
     "useDirectConnections": false,
     "token": "q1an1hxq1q9neviy",
     "wanIp": "1.2.3.4",
     "wanInterface": "eth1"
   }
   ```
    You can find the token in the configured Network Controller in Signal, the WAN IP is the ip the device uses to connect to internet resources (public IP).
3. **Save the file and exit nano:**

   - Press `CTRL+O` to save the file.
   - Press `CTRL+X` to exit.

---

### 7. Verify Network Controller Connectivity

Once the configuration is complete, the network controller should connect, and you should see a green status indicator in the Signal web interface.

---

### Conclusion

Your Teltonika RUT950/RUT955 device is now set up with OpenWRT and the necessary software installed. You can check and monitor the network controller connectivity to ensure everything is working as expected.