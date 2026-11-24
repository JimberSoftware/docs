# Ajouter un Active Directory à une installation SASE

Ce guide explique comment installer **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_** sur un contrôleur de domaine et garantir une communication fiable au sein du domaine.

## Table des matières

1. [Installer Jimber SASE Client sur le contrôleur de domaine](#_1-install-network-isolation-on-the-domain-controller)
    - [Prérequis](#prerequisites)
        - [Désactiver IPv6](#disable-ipv6)
        - [Définir des ports RPC statiques](#setting-static-rpc-ports)
        - [Définir l’interface d’écoute du gestionnaire DNS](#set-dns-manager-listening-interface)
    - [Installation](#installation)
        <!-- - [Configuring settings.json](#configuring-settingsjson) -->
        - [Vérifier que les paramètres DNS et la connectivité sont corrects](#verify-correct-dns-settings-and-connectivity)
        - [Configurer le transfert DNS pour le serveur SASE](#configuring-dns-forwarding-for-SASE-server)
        - [Configurer le transfert DNS pour le contrôleur de domaine](#configuring-dns-forwarding-for-the-domain-controller)
2. [Configuration du serveur SASE](#_2-sase-server-configuration)
 <!--  - [Port configuration on SASE server](#port-configuration-on-SASE-server)
    - [Required ports](#required-ports)
    - [Optional ports](#optional-ports)
  - [Domain Client Testing - Enabling Device isolation](#domain-client-testing-enabling-device-isolation) -->
3. [Test du client de domaine](#_3-domain-client-testing)
4. [Test / vérification de la communication du domaine](#_4-testing-verification-of-domain-communication)
5. [Comment mapper des partages SMB](#_5-mapping-smb-shares)
6. [Comment joindre un nouvel utilisateur à un domaine avec un contrôleur de domaine sur lequel l’isolation des appareils est activée](#_6-step-by-step-guide-domain-joining-a-new-user-with-device-isolation-enabled-on-the-domain-controller)

### 1. Installer Jimber SASE Client sur le contrôleur de domaine

### Prérequis

- #### Désactiver IPv6
    - Il est recommandé de désactiver la communication IPv6 sur votre réseau, conformément aux bonnes pratiques. L’utilisation d’IPv6 présente peu d’avantages et sa désactivation simplifie la sécurisation du réseau avec **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_**.

![Désactiver IPv6](./screenshots/ad-disable-ipv6.png ':size=300')

- #### Définir des ports RPC statiques

    Pour attribuer une petite plage de ports RPC statiques, modifiez les valeurs suivantes dans le registre.

    > [!NOTE]
    > Documentation Microsoft : [Configurer l’allocation dynamique des ports RPC avec des pare-feu](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/configure-rpc-dynamic-port-allocation-with-firewalls#example)

Vous pouvez télécharger [ici](https://docs.jimber.io/advanced/activedirectory/Rpc.reg) un fichier .reg pour appliquer automatiquement les modifications.

Chemin de la clé : HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Rpc

![Ports RPC statiques](./screenshots/ad-static-rpc-ports.png ':size=500')

- #### Définir l’interface d’écoute du gestionnaire DNS

> [!IMPORTANT]
> Isolation des appareils uniquement - Interrompt la fonctionnalité de communication du domaine sur le réseau natif !

Lorsque vous activez l’isolation des appareils, veillez à ce que l’écoute soit effectuée sur la bonne interface afin que les adresses IP associées au domaine soient correctement résolues lors des requêtes AD. Remplacez l’adresse IP ci-dessous par l’adresse IP qui vous est attribuée via l’isolation réseau.

```powershell
$DnsServerSettings = Get-DnsServerSetting -ALL
$DnsServerSettings.ListeningIpAddress = @("198.18.0.7")
Set-DNSServerSetting $DnsServerSettings
```

> [!NOTE]
> Cette modification n’est pas permanente. Au redémarrage du contrôleur de domaine ou du serveur, ces paramètres sont rétablis à leurs valeurs par défaut.

### Installation

Vous trouverez le programme d’installation [ici](https://SASE.jimber.io/clients/windows-server-latest.msi). Pour effectuer l’installation, il suffit d’exécuter le fichier MSI en tant qu’administrateur.

Au démarrage de Jimber SASE, une boîte de dialogue s’affiche :

![jimber_server_settings.png](./screenshots/jimber_server_settings.png ':size=400')

Le jeton requis peut être récupéré dans l’onglet « Servers » de l’interface du serveur SASE. Sélectionnez et modifiez simplement le serveur approprié pour le trouver.

![token.png](./screenshots/token.png ':size=500')

Après avoir renseigné le jeton et cliqué sur le bouton d’envoi, une fenêtre contextuelle indique que la configuration du serveur a été envoyée et que le service a été redémarré :

![settings_updated.png](./screenshots/settings_updated.png ':size=300')

<!-- - #### Configuring settings.json

  - To correctly configure Network Isolation to connect back to SASE, we need to change the settings file.
    Once installed, open the following: "C:\Program Files\Jimber\settings.json" in Notepad or any other editor.
    By default, it will only contain a privateKey and a publicKey.

  ```json
  {
    "privateKey": "ZwcayfO6zvVWj6emhJr1j+FBa3ETt88IzXFxcMHkGY/L7sdabpyIa4B8SHa8HU72/L5TtYCClO5RE8pZgzo7GA==",
    "publicKey": "y+7HWm6ciGuAfEh2vB1O9vy+U7WAgpTuURPKWYM6Oxg="
  }
  ```

  We need to add the token, which is to be found by editing the server on SASE.


![ad-light-edit-server.png](/ad-light-edit-server.png ':size=600x')

  Edit the settings.json accordingly:

  ```json
  {
    "privateKey": "ZwcayfO6zvVWj6emhJr1j+FBa3ETt88IzXFxcMHkGY/L7sdabpyIa4B8SHa8HU72/L5TtYCClO5RE8pZgzo7GA==",
    "publicKey": "y+7HWm6ciGuAfEh2vB1O9vy+U7WAgpTuURPKWYM6Oxg=",
    "token": "9hrkprdl05kbjopg"
  }
  ```

> [!WARNING]
> **Attention**! Don't forget the comma at the end of lines and the quotation marks!
Ensure to save the changes made to the file. -->

Accédez aux services de votre contrôleur de domaine et redémarrez **_<span style="color: darkblue;">Jimber SASE Service</span>_**.

![Redémarrage du service](./screenshots/ad-restarting-the-service.png ':size=500')

- #### Vérifier que les paramètres DNS et la connectivité sont corrects

    Vérifiez que vos paramètres DNS sont corrects. Vous devriez maintenant être connecté à l’isolation réseau.

    > [!WARNING]
    > Il est possible que vos paramètres DNS aient été réinitialisés après la configuration du fichier settings.json. Si cela se produit, vous devrez peut-être saisir à nouveau manuellement les informations DNS correctes.

    Une icône de connexion verte à côté du nom de votre serveur de contrôleur de domaine indique qu’il est connecté.

![ad-light-connected.png](./screenshots/ad-light-connected.png ':size=500')

Redémarrez maintenant le contrôleur de domaine afin que tous les services reconnaissent correctement la nouvelle interface réseau de l’isolation réseau.

- #### Configurer le transfert DNS pour le serveur SASE

Accédez à la page de votre serveur SASE, puis à la section Integrations. En haut de la page, vous trouverez un paramètre permettant de configurer le redirecteur DNS. Les clients pour lesquels le remplacement DNS est activé seront filtrés par notre service DNS, mais les requêtes spécifiques au domaine continueront d’être résolues par le serveur que vous spécifiez dans ce champ. Ajoutez l’adresse IP d’isolation réseau du contrôleur de domaine.

![Redirecteur du serveur SASE](./screenshots/ad-signal-server-forwarder_2.png ':size=600')

- #### Configurer le transfert DNS pour le contrôleur de domaine
    - Ouvrez le Gestionnaire de serveur, puis le Gestionnaire DNS.

![Gestionnaire DNS](./screenshots/ad-dns-manager.png ':size=600')

- Ouvrez les propriétés du serveur DNS.

![Propriétés DNS](./screenshots/ad-dns-properties.png ':size=400')

Vous pouvez également configurer ici les serveurs DNS de transfert :

![Redirecteurs DNS](./screenshots/ad-dns-forwarders.png ':size=300')

> [!NOTE]
> Vous pouvez les configurer comme vous le souhaitez.
> Une fois la configuration terminée, redémarrez le contrôleur de domaine afin de vous assurer que tous les enregistrements sont correctement définis.

### 2. Configuration du serveur SASE

Vous trouverez [ici](/./rules/groupconfiguration/groupconfiguration.md) des instructions pour configurer le serveur plus en détail.

<!-- ### Port configuration on SASE server

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
  - TCP port 49443: ADFS

  A lot of different services and ports can be used throughout AD and the applications you can host on it. Please enable other ports you might need.

![ad-light-allowed-services.png](./screenshots/ad-light-allowed-services.png ':size=700') -->

<!-- - #### Domain Client Testing - Enabling Device isolation -->

### 3. Test du client de domaine

Pour tester correctement la communication du domaine, activez l’isolation des appareils pour le client et le contrôleur de domaine avec lesquels vous allez effectuer le test. Il est possible de tester sans l’isolation des appareils, mais vous ne pouvez alors pas garantir que l’isolation réseau sera utilisée. Cela dépend de la manière dont le contrôleur de domaine répondra à ses requêtes NetBIOS et DNS.

Vous trouverez [ici](/./company/users/users) comment activer l’isolation des appareils pour un client.

<!--   Enabling Device isolation ensures that other devices on your native network will not be able to connect to you. Only connections from Network Isolation will be allowed.<br /><br />

  In order to properly test domain communication, enable Device isolation for the client and domain controller we are now going to test with. It is possible to test without Device isolation, but then we cannot guarantee that Network Isolation will be used. It depends on how the domain controller will respond to its NetBIOS and DNS queries.<br /><br /> -->

<!-- ![ad-light-enable-secure-mode.png](./screenshots/ad-light-enable-secure-mode.png ':size=700') -->

### 4. Test / vérification de la communication du domaine

- Vérifiez à quel domaine vous êtes connecté, quel que soit l’état actuel de la connexion. Cette commande affiche donc le domaine même si la connexion au domaine ne fonctionne pas.<br />

    Shell : **Invite de commandes (cmd.exe)**

    ```
    systeminfo | findstr "Domain:"
    ```

- Résultat attendu :
    ```
    Domain:                    isolationcorp.local
    ```
- Vérifiez à quel domaine vous êtes connecté, quel que soit l’état actuel de la connexion. Cette commande affiche donc le domaine même si la connexion au domaine ne fonctionne pas.<br />

    Shell : **Powershell (powershell.exe)**

    ```cmd
    $env:USERDOMAIN
    ```

- Résultat attendu :
    ```info
    ISOLATIONCORP
    ```
- Récupérez les informations pertinentes sur le domaine. **Cette commande ne s’exécute que lorsqu’il existe une communication avec le domaine**. Elle restera bloquée en l’absence de communication ou si certains services ne sont pas disponibles.<br />

    Shell : **Powershell (powershell.exe)**
    Remarque : l’exécution de cette commande peut prendre une minute.

    ```cmd
    gpresult /r
    ```

- Résultat attendu :

    ```info
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

- Vérifiez à quel domaine vous êtes connecté, quel que soit l’état actuel de la connexion. Cette commande affiche donc le domaine même si la connexion au domaine ne fonctionne pas.<br />

    Shell : **Powershell (powershell.exe)**

    ```cmd
    net config workstation
    ```

- Résultat attendu :

    ```info
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

- Vérifiez à quel domaine vous êtes connecté, quel que soit l’état actuel de la connexion. Cette commande affiche donc le domaine même si la connexion au domaine ne fonctionne pas.<br />

    Shell : **Powershell (powershell.exe)**

    ```cmd
    nltest /dsgetdc:$env:USERDOMAIN
    ```

- Résultat attendu :

    ```info
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

Consultez la section Configuration IP de Windows. Elle contient également des informations générales sur le domaine. Une connexion active n’est pas nécessaire pour récupérer ces données.

- Vérifiez à quel domaine vous êtes connecté, quel que soit l’état actuel de la connexion. Cette commande affiche donc le domaine même si la connexion au domaine ne fonctionne pas.<br />

    Shell : **Invite de commandes (cmd.exe) / Powershell (powershell.exe)**

    ```cmd
    ipconfig/all
    ```

- Résultat attendu :

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

### 5. Mapper des partages SMB

- Le mappage de partages SMB peut poser des difficultés, notamment lorsque vous essayez de réutiliser des mappages existants associés à des noms de domaine. Le problème vient du fait que Windows met ces entrées en cache et tente continuellement de se connecter à des partages obsolètes. Même si les adresses IP d’isolation réseau qui s’affichent sont correctes lorsque vous résolvez le nom de domaine dans l’invite de commandes ou dans un navigateur, Windows a tendance à conserver les anciennes associations.

- Pour contourner ce problème, il est conseillé de supprimer puis de remapper les partages SMB une fois qu’une connexion fonctionnelle est établie, ou de modifier les politiques et les scripts existants. Vous pourrez ainsi assurer la mise à disposition automatique et transparente de cette fonctionnalité essentielle.

### 6. Guide étape par étape : joindre un nouvel utilisateur à un domaine avec l’isolation des appareils activée sur le contrôleur de domaine

Pour joindre un nouvel utilisateur à un domaine avec l’isolation des appareils activée sur le contrôleur de domaine, suivez précisément les étapes ci-dessous afin de garantir la réussite de la configuration.

#### Étape 1 : Vérifier que l’utilisateur a été créé

Avant de continuer, assurez-vous que le nouveau compte utilisateur a été créé sur le contrôleur de domaine.

#### Étape 2 : Se connecter en tant qu’administrateur local

1. **Connectez-vous à l’appareil** en tant qu’**administrateur local**.

#### Étape 3 : Installer et configurer Jimber SASE Client

1. Installez **_<span style="color: darkblue;">Jimber SASE Client</span>_** s’il ne l’est pas déjà.
2. **Configurez** **_<span style="color: darkblue;">Jimber SASE Client</span>_** conformément aux politiques de votre organisation.

#### Étape 4 : Joindre l’utilisateur au domaine

1. **Joignez l’utilisateur au domaine.**
2. **Redémarrez l’appareil** une fois le processus de jonction au domaine terminé.

#### Étape 5 : Se reconnecter en tant qu’administrateur local

1. **Connectez-vous à nouveau à l’appareil** en tant qu’**administrateur local**.
2. Démarrez **_<span style="color: darkblue;">Jimber SASE Client</span>_**.

#### Étape 6 : Changer d’utilisateur ou verrouiller l’appareil

**Changez d’utilisateur** ou **verrouillez l’appareil**. **Ne vous déconnectez pas.**

#### Étape 7 : Se connecter avec l’utilisateur joint au domaine

1. **Connectez-vous avec l’utilisateur joint au domaine**.
2. Effectuez la première connexion.
3. **Redémarrez l’appareil** une fois la première connexion terminée.

En suivant ces étapes, le nouvel utilisateur sera correctement joint au domaine avec l’isolation des appareils activée sur le contrôleur de domaine.
