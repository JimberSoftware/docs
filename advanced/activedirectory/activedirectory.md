# Integrating Active Directory

This guide provides instructions for installing Network Isolation on a domain controller and ensuring reliable communication within the domain.

## Table of contents

1. [Install Network Isolation on the Domain Controller](#install-network-isolation-on-the-domain-controller)
   - [Prerequisites](#prerequisites)
     - [Disable IPv6](#disable-ipv6)
     - [Setting Static RPC Ports](#setting-static-rpc-ports)
     - [Set DNS Manager Listening Interface](#set-dns-manager-listening-interface)
   - [Installation](#installation)
     - [Configuring settings.json](#configuring-settingsjson)
     - [Verify Correct DNS Settings and Connectivity](#verify-correct-dns-settings-and-connectivity)
     - [Configuring dns forwarding for signal server](#configuring-dns-forwarding-for-signal-server)
     - [Configuring dns forwarding for the domain controller](#configuring-dns-forwarding-for-the-domain-controller)
2. [Signal Server Configuration](#signal-server-configuration)
   - [Port configuration on signal server](#port-configuration-on-signal-server)
     - [Required ports](#required-ports)
     - [Optional ports](#optional-ports)
   - [Domain Client Testing - Enabling Secure Mode](#domain-client-testing-enabling-secure-mode)
3. [Testing / Verification of Domain Communication](#testing--verification-of-domain-communication)
4. [How to Map SMB shares](#mapping-smb-shares)
5. [How to domain join a new use with a domain controller that has secure mode enabled](#_5-step-by-step-guide-domain-joining-a-new-user-with-secure-mode-enabled-on-the-domain-controller)


## Install Network Isolation on the Domain Controller

### Prerequisites

- #### Disable IPv6

  - It is recommended to turn off IPv6 communication in your network for best practices. The advantages of using IPv6 are minimal, and disabling it simplifies securing the network with Network Isolation.
    
![Disable IPv6](/ad-disable-ipv6.png)

- #### Setting Static RPC Ports

  - In order to assign a small range of static RPC ports, please edit the following values in the registry. 
  >[!NOTE]
  > Microsoft documentation: [Configure RPC Dynamic Port Allocation with Firewalls](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/configure-rpc-dynamic-port-allocation-with-firewalls#example)

 You can download a .reg file to update the changes automatically [here](https://docs.jimber.io/advanced/activedirectory/Rpc.reg)
    
 Path of key: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Rpc
  
![Static RPC Ports](/ad-static-rpc-ports.png)

- #### Set DNS Manager Listening Interface (Secure Mode Only - Breaks Native Network Domain Communication Functionality!)
  - When enabling secure mode, ensure that the correct interface is being listened to so that the domain-related IPs are correctly resolved when the AD gets queried. Change the IP below to the corresponding IP you are assigned through network isolation.
  ```powershell
  $DnsServerSettings = Get-DnsServerSetting -ALL
  $DnsServerSettings.ListeningIpAddress = @("198.18.0.7")
  Set-DNSServerSetting $DnsServerSettings
  ```
  > [!NOTE]
  > This is not permanent. When the domain controller or server reboots, these settings will reset back to default.
     


### Installation

The installer can be found [here](https://signal.jimber.io/clients/windows-server-latest.msi). The installation is done by simply executing the MSI as an administrator.

- #### Configuring settings.json

  - To correctly configure network isolation to connect back to Signal, we need to change the settings file.
    Once installed, open the following: "C:\Program Files\Jimber\settings.json" in Notepad or any other editor.
    By default, it will only contain a privateKey and a publicKey.

  ```json
  {
    "privateKey": "ZwcayfO6zvVWj6emhJr1j+FBa3ETt88IzXFxcMHkGY/L7sdabpyIa4B8SHa8HU72/L5TtYCClO5RE8pZgzo7GA==",
    "publicKey": "y+7HWm6ciGuAfEh2vB1O9vy+U7WAgpTuURPKWYM6Oxg="
  }
  ```

  We need to add the token and the noDns flag.

  > [!NOTE]
  >   Enabling the nodns flag ensures that the Network Isolation client does not alter the computer's DNS settings.
  

  We can find the token if we edit the server on Signal.

  
![ad-light-edit-server.png](/ad-light-edit-server.png ':size=600x')

  Edit the settings.json accordingly:

  ```json
  {
    "privateKey": "ZwcayfO6zvVWj6emhJr1j+FBa3ETt88IzXFxcMHkGY/L7sdabpyIa4B8SHa8HU72/L5TtYCClO5RE8pZgzo7GA==",
    "publicKey": "y+7HWm6ciGuAfEh2vB1O9vy+U7WAgpTuURPKWYM6Oxg=",
    "token": "9hrkprdl05kbjopg",
    "nodns": true
  }
  ```

> [!WARNING]
> **Attention**! Don't forget the comma at the end of lines and the quotation marks!
Ensure to save the changes made to the file.

  Please go to the services on your domain controller and restart the "JimberNetworkIsolation" service.

  
![Restarting the Service](/ad-restarting-the-service.png)

- #### Verify Correct DNS Settings and Connectivity

  Verify that your DNS settings are correct and you should now be connected to Network Isolation.
  >[!WARNING]
  >It's possible that your DNS settings were reset after you configured the settings.json file. If this occurs, you may need to manually re-enter the correct DNS information.

  Seeing a green connection icon next to your DC server name indicates that it is connected.
  
![ad-light-connected.png](/ad-light-connected.png)

Restart the domain controller now so that all services properly recognize the new network interface from Network Isolation.

- #### Configuring dns forwarding for signal server

 Go to your Signal server page and head to settings. On the top, you will find a setting to configure the DNS forwarder. Clients that have DNS override enabled will be filtered through our DNS service, but domain-specific queries will still be resolved by the server you specify in this field. You should add the Network Isolation IP of the Domain Controller.
    
![Signal Server Forwarder](/ad-signal-server-forwarder.png)

- #### Configuring dns forwarding for the domain controller
  - Open up the Server Manager and open the DNS Manager.
    
![DNS Manager](/ad-dns-manager.png)
  
  - Open up the DNS server's properties.
    
![DNS Properties](/ad-dns-properties.png)

It is also possible to configure the forwarding DNS servers here: .
    
![DNS Forwarders](/ad-dns-forwarders.png)

> [!NOTE]
> You can configure them how you see fit.
> Once configured, reboot to ensure all records are properly set by the DC.

### Port configuration on signal server

- #### Required ports

  - Protocol: ICMP - allow
  - TCP/UDP port 53: DNS
  - TCP/UDP port 88: Kerberos authentication
  - TCP/UDP port 135: RPC
  - TCP/UDP port 137-138: NetBIOS
  - TCP/UDP port 389: LDAP
  - TCP/UDP port 445: SMB
  - TCP/UDP port 464: Kerberos password change
  - TCP/UDP port 636: LDAP SSL
  - TCP/UDP port 3268-3269: Global catalog
  - TCP/UDP port 50000-51000: Random RPC ports (Note: Must apply registry change!)

- #### Optional ports

  - TCP port 80: HTTP
  - TCP port 443: HTTPS
  - TCP port 49443: ADFS<br /><br />

  A lot of different services and ports can be used throughout AD and the applications you can host on it. Please enable other ports you might need.
  
![ad-light-allowed-services.png](/ad-light-allowed-services.png ':size=900x')

- #### Domain Client Testing - Enabling Secure Mode
  Enabling secure mode ensures that other devices on your native network will not be able to connect to you. Only connections from Network Isolation will be allowed.<br /><br />

  In order to properly test domain communication, enable secure mode for the client and domain controller we are now going to test with. It is possible to test without secure mode, but then we cannot guarantee that Network Isolation will be used. It depends on how the domain controller will respond to its NetBIOS and DNS queries.<br /><br />
 
  
![ad-light-enable-secure-mode.png](/ad-light-enable-secure-mode.png ':size=900x')

### Testing / Verification of Domain Communication


  - Find out which domain you are joined, regardless of the current state of the connection. So this will show the domain regardless of the fact that you have a working domain connection.<br />
  
  	Shell: **Command prompt (cmd.exe)**
    ```
    systeminfo | findstr "Domain:"
    ```

  - Expected output: 
    ```
    Domain:                    isolationcorp.local
    ```
    
    
  - Find out which domain you are joined, regardless of the current state of the connection. So this will show the domain regardless of the fact that you have a working domain connection.<br />  
  
  	Shell: **Powershell (powershell.exe)**
    ```cmd
    $env:USERDOMAIN
    ```

  - Expected output: 
    ``` info
    ISOLATIONCORP
    ```
    
  - Get relevant domain information, **this command will only execute when there is domain communication**. It will remain stuck when there is non or certain services are not available.<br />  
  
  	Shell: **Powershell (powershell.exe)**
    Note: It can take a minute to execute this command
    ```cmd
    gpresult /r
    ```

  - Expected output: 
    ``` info
      Microsoft (R) Windows (R) Operating System Group Policy Result tool v2.0
      © Microsoft Corporation. All rights reserved.

      Created on ‎11/‎30/‎2023 at 2:20:13 PM

      RSOP data for ISOLATIONCORP\mathias on MATHIAS-PC : Logging Mode
      -----------------------------------------------------------------

      OS Configuration:            Member Workstation
      OS Version:                  10.0.22621
      Site Name:                   N/A
      Roaming Profile:             N/A
      Local Profile:               C:\Users\mathias
      Connected over a slow link?: No

      USER SETTINGS
      --------------

          Last time Group Policy was applied: 11/30/2023 at 2:17:40 PM
          Group Policy was applied from:      dc.isolationcorp.local
          Group Policy slow link threshold:   500 kbps
          Domain Name:                        ISOLATIONCORP
          Domain Type:                        Windows 2008 or later

          Applied Group Policy Objects
          -----------------------------
              N/A

          The following GPOs were not applied because they were filtered out
          -------------------------------------------------------------------
              Local Group Policy
                  Filtering:  Not Applied (Empty)

          The user is a part of the following security groups
          ---------------------------------------------------
              Domain Users
              Everyone
              BUILTIN\Users
              NT AUTHORITY\INTERACTIVE
              CONSOLE LOGON
              NT AUTHORITY\Authenticated Users
              This Organization
              LOCAL
              Developers
              NetworkIsolation
              System Administrators
              Authentication authority asserted identity
              Medium Mandatory Level

    ```

  - Find out which domain you are joined, regardless of the current state of the connection. So this will show the domain regardless of the fact that you have a working domain connection.<br />  
  
  	Shell: **Powershell (powershell.exe)**
    ```cmd
    net config workstation
    ```

  - Expected output: 
    ``` info
    Computer name                        \\MATHIAS-PC
    Full Computer name                   MATHIAS-PC.isolationcorp.local
    User name                            mathias

    Workstation active on
            NetBT_Tcpip_{76F9AC05-9E6F-4D0E-BA16-1D59389D34AA} (000000000000)

    Software version                     Windows 10 Pro

    Workstation domain                   ISOLATIONCORP
    Workstation Domain DNS Name          isolationcorp.local
    Logon domain                         ISOLATIONCORP

    COM Open Timeout (sec)               0
    COM Send Count (byte)                16
    COM Send Timeout (msec)              250
    The command completed successfully.

    ```
    
    
  - Find out which domain you are joined, regardless of the current state of the connection. So this will show the domain regardless of the fact that you have a working domain connection.<br />  
  
  	Shell: **Powershell (powershell.exe)**
    ```cmd
    nltest /dsgetdc:$env:USERDOMAIN
    ```

  - Expected output: 
    ``` info
               DC: \\DC
          Address: \\198.18.0.7
         Dom Guid: 6e400f03-975a-43b4-9763-519970b7cb57
         Dom Name: ISOLATIONCORP
      Forest Name: isolationcorp.local
     Dc Site Name: Default-First-Site-Name
    Our Site Name: Default-First-Site-Name
            Flags: PDC GC DS LDAP KDC TIMESERV GTIMESERV WRITABLE DNS_FOREST CLOSE_SITE FULL_SECRET WS DS_8 DS_9 DS_10 KEYLIST
    The command completed successfully

    ```

Check the Windows IP Configuration section. This section also contains some generic domain information. It does not need an active connection to retrieve this data. 

  - Find out which domain you are joined, regardless of the current state of the connection. So this will show the domain regardless of the fact that you have a working domain connection.<br />  
  
  	Shell: **Command prompt (cmd.exe) / Powershell (powershell.exe)**
     ```cmd
    ipconfig/all
    ```

  - Expected output: 
    ```cmd

    Windows IP Configuration

       Host Name . . . . . . . . . . . . : MATHIAS-PC
       Primary Dns Suffix  . . . . . . . : isolationcorp.local
       Node Type . . . . . . . . . . . . : Mixed
       IP Routing Enabled. . . . . . . . : No
       WINS Proxy Enabled. . . . . . . . : No
       DNS Suffix Search List. . . . . . : isolationcorp.local
                                           localdomain

    Unknown adapter jimber:

       Connection-specific DNS Suffix  . :
       Description . . . . . . . . . . . : WireGuard Tunnel #2
       Physical Address. . . . . . . . . :
       DHCP Enabled. . . . . . . . . . . : No
       Autoconfiguration Enabled . . . . : Yes
       IPv4 Address. . . . . . . . . . . : 198.18.0.8(Preferred)
       Subnet Mask . . . . . . . . . . . : 255.254.0.0
       Default Gateway . . . . . . . . . :
       DNS Servers . . . . . . . . . . . : 198.18.0.2
       NetBIOS over Tcpip. . . . . . . . : Enabled

    Ethernet adapter Ethernet0:

       Connection-specific DNS Suffix  . : localdomain
       Description . . . . . . . . . . . : Intel(R) 82574L Gigabit Network Connection
       Physical Address. . . . . . . . . : 00-0C-29-4A-E0-23
       DHCP Enabled. . . . . . . . . . . : Yes
       Autoconfiguration Enabled . . . . : Yes
       IPv4 Address. . . . . . . . . . . : 10.155.0.189(Preferred)
       Subnet Mask . . . . . . . . . . . : 255.255.255.0
       Lease Obtained. . . . . . . . . . : Thursday, November 30, 2023 2:07:41 PM
       Lease Expires . . . . . . . . . . : Thursday, November 30, 2023 4:02:21 PM
       Default Gateway . . . . . . . . . : 10.155.0.1
       DHCP Server . . . . . . . . . . . : 10.155.0.1
       DNS Servers . . . . . . . . . . . : 198.18.0.2
       NetBIOS over Tcpip. . . . . . . . : Enabled
    ```

### Mapping SMB shares

  - The process of mapping SMB shares can present challenges, particularly when attempting to reuse existing mappings tied to domain names. The intricacy arises from Windows caching these entries and persistently attempting to connect to outdated shares. Despite accurate network isolation IP addresses appearing when resolving the domain name in the command prompt or a browser, Windows tends to cling to the old associations.

   - To circumvent this issue, it is advisable to either remove and remap the SMB shares once a functional connection is established or to modify existing policies and scripts. By doing so, you ensure the seamless and automatic provision of this essential functionality.

### 5 Step-by-Step Guide: Domain Joining a New User with Secure Mode Enabled on the Domain Controller

Joining a new user to a domain with secure mode enabled on the domain controller requires precise steps to ensure successful configuration. Follow these steps carefully to complete the process.

## Step 1: Ensure User is Created
Before proceeding, make sure that the new user account is created in the domain controller.

## Step 2: Login as Local Administrator
1. **Log in to the device** as a **local administrator**.

## Step 3: Install and Configure Network Isolation
1. Install network isolation software if it’s not already installed.
2. **Configure network isolation** according to your organization's policies.


## Step 4: Domain Join the User
1. **Domain join the user.**
2. **Restart the device** after the domain join process is complete.


## Step 5: Login as Local Administrator Again
1. **Log in to the device** as a **local administrator** once more.
2. Start network isolation.

## Step 6: Switch User or Lock the Device
1. **Switch user** or **lock the device**. **Do not log out.**

## Step 7: Login with the Domain Joined User
1. **Login with the domain joined user**.
2. Complete the first login process.
3. **Restart the device** after the first login is complete.


Following these steps ensures that the new user is successfully joined to the domain with secure mode enabled on the domain controller.