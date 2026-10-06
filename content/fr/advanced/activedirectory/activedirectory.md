# Ajouter un Active Directory à une installation SASE

Ce guide fournit des instructions pour installer **_<span style="color: darkblue;">Jimber SASE Platform</span>_** sur un contrôleur de domaine et garantir une communication fiable au sein du domaine.

## Table des matières

1. [Installer Jimber SASE Client sur le contrôleur de domaine](#install-network-isolation-on-the-domain-controller)
   - [Prérequis](#prerequisites)
     - [Désactiver IPv6](#disable-ipv6)
     - [Définir des ports RPC statiques](#setting-static-rpc-ports)
     - [Définir l’interface d’écoute du gestionnaire DNS](#set-dns-manager-listening-interface)
   - [Installation](#installation)
     - [Configurer settings.json](#configuring-settingsjson)
     - [Vérifier les paramètres DNS et la connectivité](#verify-correct-dns-settings-and-connectivity)
     - [Configurer le transfert DNS vers le serveur SASE](#configuring-dns-forwarding-for-SASE-server)
     - [Configurer le transfert DNS pour le contrôleur de domaine](#configuring-dns-forwarding-for-the-domain-controller)
2. [Configuration du serveur SASE](#SASE-server-configuration)
   - [Configuration des ports sur le serveur SASE](#port-configuration-on-SASE-server)
     - [Ports requis](#required-ports)
     - [Ports facultatifs](#optional-ports)
   - [Test du client de domaine : activation du mode sécurisé](#domain-client-testing-enabling-secure-mode)
3. [Test / vérification de la communication avec le domaine](#testing--verification-of-domain-communication)
4. [Comment mapper des partages SMB](#mapping-smb-shares)
5. [Comment joindre un nouveau compte à un domaine avec un contrôleur de domaine dont le mode sécurisé est activé](#_5-step-by-step-guide-domain-joining-a-new-user-with-secure-mode-enabled-on-the-domain-controller)


### 1. Installer Jimber SASE Client sur le contrôleur de domaine

### Prérequis

- #### Désactiver IPv6

  - Il est recommandé de désactiver les communications IPv6 sur votre réseau, conformément aux bonnes pratiques. Les avantages de l’utilisation d’IPv6 sont minimes et sa désactivation simplifie la sécurisation du réseau avec **_<span style="color: darkblue;">Jimber SASE Platform</span>_**.
    
![Désactiver IPv6](./screenshots/ad-disable-ipv6.png ':size=300')

- #### Définir des ports RPC statiques

  Pour attribuer une petite plage de ports RPC statiques, veuillez modifier les valeurs suivantes dans le registre. 
  >[!NOTE]
  > Documentation Microsoft : [Configurer l’allocation dynamique des ports RPC avec des pare-feu](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/configure-rpc-dynamic-port-allocation-with-firewalls#example)

 Vous pouvez télécharger [ici](https://docs.jimber.io/advanced/activedirectory/Rpc.reg) un fichier .reg permettant d’appliquer automatiquement les modifications.
    
 Chemin de la clé : HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Rpc
  
![Ports RPC statiques](./screenshots/ad-static-rpc-ports.png ':size=500')

- #### Définir l’interface d’écoute du gestionnaire DNS

> [!IMPORTANT]
> Mode sécurisé uniquement — interrompt la fonctionnalité de communication du domaine sur le réseau natif !

  Lorsque vous activez le mode sécurisé, veillez à ce que l’écoute se fasse sur la bonne interface afin que les adresses IP liées au domaine soient correctement résolues lors des requêtes adressées à l’AD. Remplacez l’adresse IP ci-dessous par l’adresse IP qui vous a été attribuée via Network Isolation.
  ```powershell
  $DnsServerSettings = Get-DnsServerSetting -ALL
  $DnsServerSettings.ListeningIpAddress = @("198.18.0.7")
  Set-DNSServerSetting $DnsServerSettings
  ```
  > [!NOTE]
  > Ce paramètre n’est pas permanent. Au redémarrage du contrôleur de domaine ou du serveur, les paramètres reprendront leurs valeurs par défaut.
     


### Installation

Le programme d’installation est disponible [ici](https://SASE.jimber.io/clients/windows-server-latest.msi). Pour procéder à l’installation, il suffit d’exécuter le fichier MSI en tant qu’administrateur.

Au démarrage de Jimber SASE, une boîte de dialogue apparaît : 

![jimber_server_settings.png](./screenshots/jimber_server_settings.png ':size=400')

Le jeton requis peut être récupéré dans l’onglet « Servers » de l’interface du serveur SASE. Sélectionnez et modifiez le serveur concerné pour le trouver.

![token.png](./screenshots/token.png ':size=400')

Après avoir renseigné le jeton et cliqué sur le bouton d’envoi, une fenêtre contextuelle indique que la configuration du serveur a été envoyée et que le service a été redémarré :


![settings_updated.png](./screenshots/settings_updated.png ':size=300')


<!-- - #### Configuration de settings.json

  - Pour configurer correctement Network Isolation afin qu’il se connecte au serveur SASE, nous devons modifier le fichier de paramètres.
    Une fois le logiciel installé, ouvrez le fichier suivant : "C:\Program Files\Jimber\settings.json" dans le Bloc-notes ou tout autre éditeur.
    Par défaut, il contient uniquement une clé privée et une clé publique.

  ```json
  {
    "privateKey": "ZwcayfO6zvVWj6emhJr1j+FBa3ETt88IzXFxcMHkGY/L7sdabpyIa4B8SHa8HU72/L5TtYCClO5RE8pZgzo7GA==",
    "publicKey": "y+7HWm6ciGuAfEh2vB1O9vy+U7WAgpTuURPKWYM6Oxg="
  }
  ```

  Nous devons ajouter le jeton, que vous trouverez en modifiant le serveur dans SASE.

    
![ad-light-edit-server.png](/ad-light-edit-server.png ':size=600x')

  Modifiez le fichier settings.json en conséquence :

  ```json
  {
    "privateKey": "ZwcayfO6zvVWj6emhJr1j+FBa3ETt88IzXFxcMHkGY/L7sdabpyIa4B8SHa8HU72/L5TtYCClO5RE8pZgzo7GA==",
    "publicKey": "y+7HWm6ciGuAfEh2vB1O9vy+U7WAgpTuURPKWYM6Oxg=",
    "token": "9hrkprdl05kbjopg"
  }
  ```

> [!WARNING]
> **Attention !** N’oubliez pas la virgule à la fin des lignes et les guillemets !
Veillez à enregistrer les modifications apportées au fichier. -->

  Veuillez accéder aux services sur votre contrôleur de domaine et redémarrer le `Jimber SASE service`.


![Redémarrage du service](./screenshots/ad-restarting-the-service.png ':size=500')

- #### Vérifier les paramètres DNS et la connectivité

  Vérifiez que vos paramètres DNS sont corrects. Vous devriez maintenant être connecté à Network Isolation.
  >[!WARNING]
  >Il est possible que vos paramètres DNS aient été réinitialisés après la configuration du fichier settings.json. Dans ce cas, vous devrez peut-être saisir manuellement les informations DNS correctes.

  Une icône de connexion verte à côté du nom de votre serveur DC indique que celui-ci est connecté.
  
![ad-light-connected.png](./screenshots/ad-light-connected.png ':size=500')

Redémarrez maintenant le contrôleur de domaine afin que tous les services reconnaissent correctement la nouvelle interface réseau de Network Isolation.

- #### Configurer le transfert DNS vers le serveur SASE

 Accédez à la page de votre serveur SASE, puis à la section Integrations. En haut de la page, vous trouverez un paramètre permettant de configurer le redirecteur DNS. Les clients pour lesquels le remplacement DNS est activé seront redirigés vers notre service DNS, mais les requêtes propres au domaine seront toujours résolues par le serveur que vous indiquez dans ce champ. Vous devez ajouter l’adresse IP Network Isolation du contrôleur de domaine.
    
![Redirecteur du serveur SASE](./screenshots/ad-signal-server-forwarder_2.png ':size=600' )

- #### Configurer le transfert DNS pour le contrôleur de domaine
  - Ouvrez le Gestionnaire de serveur, puis le Gestionnaire DNS.
    
![Gestionnaire DNS](./screenshots/ad-dns-manager.png ':size=600')
  
  - Ouvrez les propriétés du serveur DNS.
    
![Propriétés DNS](./screenshots/ad-dns-properties.png ':size=400')

Il est également possible de configurer les serveurs DNS de transfert ici : 
    
![Redirecteurs DNS](./screenshots/ad-dns-forwarders.png ':size=300')

> [!NOTE]
> Vous pouvez les configurer comme bon vous semble.
> Une fois la configuration terminée, redémarrez le contrôleur de domaine pour vous assurer que tous les enregistrements sont correctement définis.

### 2. Configuration du serveur SASE

### Configuration des ports sur le serveur SASE

- #### Ports requis

  - Protocole : ICMP — autoriser
  - Port TCP/UDP 53 : DNS
  - Port TCP/UDP 88 : authentification Kerberos
  - Port TCP/UDP 135 : RPC
  - Port TCP/UDP 137-138 : NetBIOS
  - Port TCP/UDP 389 : LDAP
  - Port TCP/UDP 445 : SMB
  - Port TCP/UDP 464 : changement de mot de passe Kerberos
  - Port TCP/UDP 636 : LDAP SSL
  - Port TCP/UDP 3268-3269 : catalogue global
  - Port TCP/UDP 50000-51000 : ports RPC aléatoires (Remarque : la modification du registre doit être appliquée !)

- #### Ports facultatifs

  - Port TCP 80 : HTTP
  - Port TCP 443 : HTTPS
  - Port TCP 49443 : ADFS

  De nombreux services et ports différents peuvent être utilisés dans AD et dans les applications que vous pouvez y héberger. Veuillez activer les autres ports dont vous pourriez avoir besoin.
  
![ad-light-allowed-services.png](./screenshots/ad-light-allowed-services.png ':size=700')

- #### Test du client de domaine : activation du mode sécurisé
  L’activation du mode sécurisé empêche les autres appareils de votre réseau natif de se connecter à votre appareil. Seules les connexions provenant de Network Isolation seront autorisées.<br /><br />

  Pour tester correctement la communication avec le domaine, activez le mode sécurisé sur le client et le contrôleur de domaine que nous allons tester. Il est possible d’effectuer le test sans activer le mode sécurisé, mais nous ne pouvons alors pas garantir que Network Isolation sera utilisé. Cela dépend de la manière dont le contrôleur de domaine répondra aux requêtes NetBIOS et DNS.<br /><br />
 
  
![ad-light-enable-secure-mode.png](./screenshots/ad-light-enable-secure-mode.png ':size=700')

### 3. Test / vérification de la communication avec le domaine


  - Déterminez à quel domaine vous êtes joint, quel que soit l’état actuel de la connexion. Cette commande affiche donc le domaine même si votre connexion au domaine ne fonctionne pas.<br />
  
  	Shell : **Invite de commandes (cmd.exe)**
    ```
    systeminfo | findstr "Domain:"
    ```

  - Résultat attendu : 
    ```
    Domain:                    isolationcorp.local
    ```
    
    
  - Déterminez à quel domaine vous êtes joint, quel que soit l’état actuel de la connexion. Cette commande affiche donc le domaine même si votre connexion au domaine ne fonctionne pas.<br />  
  
  	Shell : **Powershell (powershell.exe)**
    ```cmd
    $env:USERDOMAIN
    ```

  - Résultat attendu : 
    ``` info
    ISOLATIONCORP
    ```
    
  - Récupérez les informations pertinentes sur le domaine. **Cette commande ne s’exécute que si la communication avec le domaine est établie.** Elle restera bloquée si la communication n’est pas établie ou si certains services ne sont pas disponibles.<br />  
  
  	Shell : **Powershell (powershell.exe)**
    Remarque : l’exécution de cette commande peut prendre une minute.
    ```cmd
    gpresult /r
    ```

  - Résultat attendu : 
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

  - Déterminez à quel domaine vous êtes joint, quel que soit l’état actuel de la connexion. Cette commande affiche donc le domaine même si votre connexion au domaine ne fonctionne pas.<br />  
  
  	Shell : **Powershell (powershell.exe)**
    ```cmd
    net config workstation
    ```

  - Résultat attendu : 
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
    
    
  - Déterminez à quel domaine vous êtes joint, quel que soit l’état actuel de la connexion. Cette commande affiche donc le domaine même si votre connexion au domaine ne fonctionne pas.<br />  
  
  	Shell : **Powershell (powershell.exe)**
    ```cmd
    nltest /dsgetdc:$env:USERDOMAIN
    ```

  - Résultat attendu : 
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

Consultez la section Configuration IP de Windows. Elle contient également des informations générales sur le domaine. Aucune connexion active n’est nécessaire pour récupérer ces données. 

  - Déterminez à quel domaine vous êtes joint, quel que soit l’état actuel de la connexion. Cette commande affiche donc le domaine même si votre connexion au domaine ne fonctionne pas.<br />  
  
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

### 4. Mapper des partages SMB

  - Le mappage de partages SMB peut présenter des difficultés, notamment lorsque vous tentez de réutiliser des mappages existants associés à des noms de domaine. Le problème vient du fait que Windows met ces entrées en cache et continue d’essayer de se connecter à des partages obsolètes. Même si des adresses IP correctes de Network Isolation apparaissent lorsque le nom de domaine est résolu dans l’invite de commandes ou dans un navigateur, Windows a tendance à conserver les anciennes associations.

   - Pour contourner ce problème, il est conseillé de supprimer puis de mapper à nouveau les partages SMB une fois la connexion fonctionnelle, ou de modifier les stratégies et scripts existants. Vous vous assurez ainsi que cette fonctionnalité essentielle est fournie de façon fluide et automatique.

### 5. Guide étape par étape : joindre au domaine un nouvel utilisateur lorsque le mode sécurisé est activé sur le contrôleur de domaine

Pour joindre un nouvel utilisateur à un domaine lorsque le mode sécurisé est activé sur le contrôleur de domaine, suivez précisément les étapes ci-dessous afin de garantir la réussite de la configuration.

#### Étape 1 : Vérifier que l’utilisateur a été créé
Avant de poursuivre, assurez-vous que le nouveau compte utilisateur a été créé sur le contrôleur de domaine.

#### Étape 2 : Se connecter en tant qu’administrateur local
1. **Connectez-vous à l’appareil** en tant qu’**administrateur local**.

#### Étape 3 : Installer et configurer Jimber SASE
1. Installez le logiciel Network Isolation s’il ne l’est pas déjà.
2. **Configurez Network Isolation** conformément aux politiques de votre organisation.


#### Étape 4 : Joindre l’utilisateur au domaine
1. **Joignez l’utilisateur au domaine.**
2. **Redémarrez l’appareil** une fois le processus de jonction au domaine terminé.


#### Étape 5 : Se reconnecter en tant qu’administrateur local
1. **Connectez-vous à nouveau à l’appareil** en tant qu’**administrateur local**.
2. Démarrez Network Isolation.

#### Étape 6 : Changer d’utilisateur ou verrouiller l’appareil
1. **Changez d’utilisateur** ou **verrouillez l’appareil**. **Ne vous déconnectez pas.**

#### Étape 7 : Se connecter avec l’utilisateur joint au domaine
1. **Connectez-vous avec l’utilisateur joint au domaine**.
2. Terminez le processus de première connexion.
3. **Redémarrez l’appareil** une fois la première connexion terminée.


En suivant ces étapes, le nouvel utilisateur sera correctement joint au domaine alors que le mode sécurisé est activé sur le contrôleur de domaine.
