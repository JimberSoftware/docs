# Ajouter un Active Directory à une installation SASE

Ce guide explique comment installer la **_Plateforme Jimber SASE_** sur un contrôleur de domaine et assurer une communication fiable au sein du domaine.

## Table des matières

1. [Installer le client Jimber SASE sur le contrôleur de domaine](#install-network-isolation-on-the-domain-controller)
   - [Prérequis](#prerequisites)
     - [Désactiver IPv6](#disable-ipv6)
     - [Configurer des ports RPC statiques](#setting-static-rpc-ports)
     - [Définir l’interface d’écoute du gestionnaire DNS](#set-dns-manager-listening-interface)
   - [Installation](#installation)
     - [Configurer settings.json](#configuring-settingsjson)
     - [Vérifier les paramètres DNS et la connectivité](#verify-correct-dns-settings-and-connectivity)
     - [Configurer le transfert DNS pour le serveur SASE](#configuring-dns-forwarding-for-SASE-server)
     - [Configurer le transfert DNS pour le contrôleur de domaine](#configuring-dns-forwarding-for-the-domain-controller)
2. [Configuration du serveur SASE](#SASE-server-configuration)
   - [Configuration des ports sur le serveur SASE](#port-configuration-on-SASE-server)
     - [Ports requis](#required-ports)
     - [Ports facultatifs](#optional-ports)
   - [Test du client de domaine - Activer le mode sécurisé](#domain-client-testing-enabling-secure-mode)
3. [Test / vérification de la communication avec le domaine](#testing--verification-of-domain-communication)
4. [Comment mapper des partages SMB](#mapping-smb-shares)
5. [Comment joindre au domaine un nouvel utilisateur avec un contrôleur de domaine dont le mode sécurisé est activé](#_5-step-by-step-guide-domain-joining-a-new-user-with-secure-mode-enabled-on-the-domain-controller)


## 1. Installer le client Jimber SASE sur le contrôleur de domaine

### Prérequis

- #### Désactiver IPv6

  - Il est recommandé de désactiver la communication IPv6 sur votre réseau selon les bonnes pratiques. Les avantages de l’utilisation d’IPv6 sont minimes et sa désactivation simplifie la sécurisation du réseau avec la `Jimber SASE Platform`.
    
![Désactiver IPv6](./screenshots/ad-disable-ipv6.png ':size=300')

- #### Configurer des ports RPC statiques

  Pour attribuer une petite plage de ports RPC statiques, modifiez les valeurs suivantes dans le registre. 
  >[!NOTE]
  > Documentation Microsoft : [Configurer l’allocation dynamique des ports RPC avec des pare-feu](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/configure-rpc-dynamic-port-allocation-with-firewalls#example)

 Vous pouvez télécharger un fichier .reg pour appliquer automatiquement les modifications [ici](https://docs.jimber.io/advanced/activedirectory/Rpc.reg)
    
 Chemin de la clé : HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Rpc
  
![Ports RPC statiques](./screenshots/ad-static-rpc-ports.png ':size=500')

- #### Définir l’interface d’écoute du gestionnaire DNS 

> [!IMPORTANT]
> Mode sécurisé uniquement - Interrompt les fonctionnalités de communication du domaine sur le réseau natif !

  Lorsque vous activez le mode sécurisé, vérifiez que le gestionnaire écoute sur la bonne interface afin que les adresses IP liées au domaine soient résolues correctement lorsque des requêtes sont envoyées à Active Directory. Remplacez l’adresse IP ci-dessous par l’adresse correspondante qui vous est attribuée via Network Isolation.
  ```powershell
  $DnsServerSettings = Get-DnsServerSetting -ALL
  $DnsServerSettings.ListeningIpAddress = @("198.18.0.7")
  Set-DNSServerSetting $DnsServerSettings
  ```
  > [!NOTE]
  > Ce paramètre n’est pas permanent. Au redémarrage du contrôleur de domaine ou du serveur, les paramètres seront réinitialisés à leurs valeurs par défaut.
     


### Installation

Le programme d’installation est disponible [ici](https://SASE.jimber.io/clients/windows-server-latest.msi). Pour l’installer, il suffit d’exécuter le MSI en tant qu’administrateur.

Au démarrage de Jimber SASE, une boîte de dialogue apparaît : 

![jimber_server_settings.png](./screenshots/jimber_server_settings.png ':size=400')

Vous pouvez récupérer le jeton requis dans l’onglet « Servers » de l’interface du serveur SASE. Sélectionnez et modifiez le serveur concerné pour le trouver.

![token.png](./screenshots/token.png ':size=400')

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

  Accédez aux services de votre contrôleur de domaine et redémarrez le `Jimber SASE service`.


![Redémarrer le service](./screenshots/ad-restarting-the-service.png ':size=500')

- #### Vérifier les paramètres DNS et la connectivité

  Vérifiez que vos paramètres DNS sont corrects. Vous devriez maintenant être connecté à Network Isolation.
  >[!WARNING]
  >Il est possible que vos paramètres DNS aient été réinitialisés après la configuration du fichier settings.json. Dans ce cas, vous devrez peut-être saisir à nouveau manuellement les informations DNS correctes.

  Une icône de connexion verte à côté du nom de votre serveur DC indique qu’il est connecté.
  
![ad-light-connected.png](./screenshots/ad-light-connected.png ':size=500')

Redémarrez maintenant le contrôleur de domaine afin que tous les services reconnaissent correctement la nouvelle interface réseau de Network Isolation.

- #### Configurer le transfert DNS pour le serveur SASE

 Accédez à la page de votre serveur SASE, puis à la section Integrations. En haut de la page, vous trouverez un paramètre permettant de configurer le redirecteur DNS. Les clients pour lesquels le remplacement DNS est activé seront filtrés par notre service DNS, mais les requêtes spécifiques au domaine continueront d’être résolues par le serveur indiqué dans ce champ. Ajoutez l’adresse IP Network Isolation du contrôleur de domaine.
    
![Redirecteur du serveur SASE](./screenshots/ad-SASE-server-forwarder_2.png ':size=600' )

- #### Configurer le transfert DNS pour le contrôleur de domaine
  - Ouvrez le Gestionnaire de serveur, puis le Gestionnaire DNS.
    
![Gestionnaire DNS](./screenshots/ad-dns-manager.png ':size=600')
  
  - Ouvrez les propriétés du serveur DNS.
    
![Propriétés DNS](./screenshots/ad-dns-properties.png ':size=400')

Vous pouvez également configurer les serveurs DNS de transfert ici : 
    
![Redirecteurs DNS](./screenshots/ad-dns-forwarders.png ':size=300')

> [!NOTE]
> Vous pouvez les configurer comme vous le souhaitez.
> Une fois la configuration terminée, redémarrez le contrôleur de domaine pour vous assurer que tous les enregistrements sont correctement définis.

## 2. Configuration du serveur SASE

### Configuration des ports sur le serveur SASE

- #### Ports requis

  - Protocole : ICMP - autoriser
  - Port TCP/UDP 53 : DNS
  - Port TCP/UDP 88 : authentification Kerberos
  - Port TCP/UDP 135 : RPC
  - Port TCP/UDP 137-138 : NetBIOS
  - Port TCP/UDP 389 : LDAP
  - Port TCP/UDP 445 : SMB
  - Port TCP/UDP 464 : modification du mot de passe Kerberos
  - Port TCP/UDP 636 : LDAP SSL
  - Port TCP/UDP 3268-3269 : catalogue global
  - Port TCP/UDP 50000-51000 : ports RPC aléatoires (Remarque : la modification du registre doit être appliquée !)

- #### Ports facultatifs

  - Port TCP 80 : HTTP
  - Port TCP 443 : HTTPS
  - Port TCP 49443 : ADFS

  De nombreux services et ports différents peuvent être utilisés avec AD et les applications que vous pouvez y héberger. Veuillez activer les autres ports dont vous pourriez avoir besoin.
  
![ad-light-allowed-services.png](./screenshots/ad-light-allowed-services.png ':size=900x')

- #### Test du client de domaine - Activer le mode sécurisé
  L’activation du mode sécurisé empêche les autres appareils de votre réseau natif de se connecter à vous. Seules les connexions provenant de Network Isolation seront autorisées.<br /><br />

  Pour tester correctement la communication avec le domaine, activez le mode sécurisé pour le client et le contrôleur de domaine que nous allons tester. Il est possible d’effectuer le test sans activer le mode sécurisé, mais nous ne pouvons alors pas garantir que Network Isolation sera utilisé. Cela dépend de la manière dont le contrôleur de domaine répondra aux requêtes NetBIOS et DNS.<br /><br />
 
  
![ad-light-enable-secure-mode.png](./screenshots/ad-light-enable-secure-mode.png ':size=900x')

## 3. Test / vérification de la communication avec le domaine


  - Découvrez à quel domaine vous êtes joint, quel que soit l’état actuel de la connexion. Cette commande affiche donc le domaine, que votre connexion au domaine fonctionne ou non.<br />
  
  	Interpréteur de commandes : **Invite de commandes (cmd.exe)**
    ```
    systeminfo | findstr "Domain:"
    ```

  - Résultat attendu : 
    ```
    Domain:                    isolationcorp.local
    ```
    
    
  - Découvrez à quel domaine vous êtes joint, quel que soit l’état actuel de la connexion. Cette commande affiche donc le domaine, que votre connexion au domaine fonctionne ou non.<br />  
  
  	Interpréteur de commandes : **Powershell (powershell.exe)**
    ```cmd
    $env:USERDOMAIN
    ```

  - Résultat attendu : 
    ``` info
    ISOLATIONCORP
    ```
    
  - Obtenez des informations pertinentes sur le domaine. **Cette commande ne s’exécutera que si la communication avec le domaine est établie**. Elle restera bloquée si la communication est inexistante ou si certains services ne sont pas disponibles.<br />  
  
  	Interpréteur de commandes : **Powershell (powershell.exe)**
    Remarque : l’exécution de cette commande peut prendre une minute
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

  - Découvrez à quel domaine vous êtes joint, quel que soit l’état actuel de la connexion. Cette commande affiche donc le domaine, que votre connexion au domaine fonctionne ou non.<br />  
  
  	Interpréteur de commandes : **Powershell (powershell.exe)**
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
    
    
  - Découvrez à quel domaine vous êtes joint, quel que soit l’état actuel de la connexion. Cette commande affiche donc le domaine, que votre connexion au domaine fonctionne ou non.<br />  
  
  	Interpréteur de commandes : **Powershell (powershell.exe)**
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

Consultez la section Configuration IP de Windows. Elle contient également des informations génériques sur le domaine. Une connexion active n’est pas nécessaire pour récupérer ces données. 

  - Découvrez à quel domaine vous êtes joint, quel que soit l’état actuel de la connexion. Cette commande affiche donc le domaine, que votre connexion au domaine fonctionne ou non.<br />  
  
  	Interpréteur de commandes : **Invite de commandes (cmd.exe) / Powershell (powershell.exe)**
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

  - Le mappage des partages SMB peut poser des difficultés, notamment lorsque vous essayez de réutiliser des mappages existants associés à des noms de domaine. Le problème vient du fait que Windows met ces entrées en cache et tente continuellement de se connecter aux anciens partages. Même si les adresses IP correctes de l’isolation réseau s’affichent lorsque vous résolvez le nom de domaine dans l’invite de commandes ou dans un navigateur, Windows a tendance à conserver les anciennes associations.

   - Pour contourner ce problème, il est conseillé de supprimer puis de mapper à nouveau les partages SMB une fois qu’une connexion fonctionnelle est établie, ou de modifier les politiques et scripts existants. Vous vous assurez ainsi que cette fonctionnalité essentielle est fournie de manière transparente et automatique.

### 5. Guide étape par étape : joindre au domaine un nouvel utilisateur avec le mode sécurisé activé sur le contrôleur de domaine

Pour joindre au domaine un nouvel utilisateur lorsque le mode sécurisé est activé sur le contrôleur de domaine, suivez précisément les étapes ci-dessous afin de garantir la réussite de la configuration.

#### Étape 1 : Vérifier que l’utilisateur est créé
Avant de poursuivre, assurez-vous que le nouveau compte utilisateur a été créé sur le contrôleur de domaine.

#### Étape 2 : Se connecter en tant qu’administrateur local
1. **Connectez-vous à l’appareil** en tant qu’**administrateur local**.

#### Étape 3 : Installer et configurer Jimber SASE
1. Installez le logiciel d’isolation réseau s’il ne l’est pas déjà.
2. **Configurez l’isolation réseau** conformément aux politiques de votre organisation.


#### Étape 4 : Joindre l’utilisateur au domaine
1. **Joignez l’utilisateur au domaine.**
2. **Redémarrez l’appareil** une fois le processus de jonction au domaine terminé.


#### Étape 5 : Se reconnecter en tant qu’administrateur local
1. **Connectez-vous à nouveau à l’appareil** en tant qu’**administrateur local**.
2. Démarrez l’isolation réseau.

#### Étape 6 : Changer d’utilisateur ou verrouiller l’appareil
1. **Changez d’utilisateur** ou **verrouillez l’appareil**. **Ne vous déconnectez pas.**

#### Étape 7 : Se connecter avec l’utilisateur joint au domaine
1. **Connectez-vous avec l’utilisateur joint au domaine**.
2. Terminez le processus de première connexion.
3. **Redémarrez l’appareil** une fois la première connexion terminée.


En suivant ces étapes, le nouvel utilisateur sera correctement joint au domaine avec le mode sécurisé activé sur le contrôleur de domaine.
