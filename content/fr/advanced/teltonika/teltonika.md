File: advanced/teltonika/teltonika.md

### Guide : installer des logiciels sur les Teltonika RUT950/RUT955 avec OpenWRT

Ce guide fournit des instructions étape par étape pour installer et configurer OpenWRT sur un appareil Teltonika RUT950 ou RUT955, puis installer les logiciels nécessaires pour utiliser l’appareil comme contrôleur réseau au sein de Jimber SASE.

---

### Prérequis

- Appareil Teltonika RUT950/RUT955
- Fichier du micrologiciel OpenWRT (`openwrt-23.05.0-ath79-generic-teltonika_rut955-squashfs-factory.bin`) [ici](https://downloads.openwrt.org/releases/23.05.0/targets/ath79/generic/openwrt-23.05.0-ath79-generic-teltonika_rut955-squashfs-factory.bin)
- Accès SSH à l’appareil (utilisez l’utilisateur root avec le mot de passe administrateur)
- Appareil connecté à Internet

---

---

### Limitations

En raison des limitations matérielles, la fonctionnalité suivante n’est pas disponible sur les appareils Teltonika : 
- Filtrage DNS à l’aide de listes de filtres

---



### 1. Installer OpenWRT sur le Teltonika RUT950/RUT955

1. **Transférer le micrologiciel OpenWRT vers l’appareil :**

   Ouvrez un terminal et exécutez la commande SCP suivante pour téléverser le micrologiciel OpenWRT sur l’appareil Teltonika :

   ```bash
   scp openwrt-23.05.0-ath79-generic-teltonika_rut955-squashfs-factory.bin root@192.168.1.1:/tmp/
   ```

2. **Se connecter à l’appareil Teltonika via SSH :**

   ```bash
   ssh root@192.168.1.1
   ```

3. **Flasher le micrologiciel avec `sysupgrade` :**

   Accédez au répertoire `/tmp` dans lequel le micrologiciel a été téléversé :

   ```bash
   cd /tmp/
   ```

   Exécutez les commandes suivantes pour mettre à niveau le micrologiciel :

   ```bash
   sysupgrade -F -v openwrt-23.05.0-ath79-generic-teltonika_rut955-squashfs-factory.bin
   ```

---

### 2. Résoudre les problèmes liés aux clés SSH

Si la clé d’hôte SSH change, l’avertissement suivant peut s’afficher :

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
```

Pour résoudre ce problème :

1. Supprimez l’ancienne clé d’hôte à l’aide de la commande suivante :

   ```bash
   ssh-keygen -f "/home/yourusername/.ssh/known_hosts" -R "192.168.1.1"
   ```

2. Une fois l’ancienne clé supprimée, reconnectez-vous à l’appareil :

   ```bash
   ssh root@192.168.1.1
   ```

---

### 3. Configurer OpenWRT et installer les paquets requis

1. **Assurez-vous que l’appareil est connecté à Internet.**  
   Mettez ensuite à jour les listes de paquets :

   ```bash
   opkg update
   ```

   Si l’erreur `wget returned 5` s’affiche, exécutez la commande suivante :

   ```bash
   opkg update --no-check-certificate
   ```

2. **Arrêter les services inutiles :**

   Désactivez et arrêtez le pare-feu et le serveur web :

   ```bash
   /etc/init.d/firewall stop
   /etc/init.d/firewall disable
   /etc/init.d/uhttpd disable
   /etc/init.d/uhttpd stop
   /etc/init.d/dnsmasq disable
   /etc/init.d/dnsmasq stop
   
   ```

3. **Installer les paquets essentiels :**

   Installez les composants logiciels nécessaires :

   ```bash
   opkg install wireguard-tools redis-server nano iptables-mod-nfqueue iptables kmod-ipt-nat iptables-mod-conntrack-extra bash libnetfilter-queue coreutils-stat
   ```

---

### 4. Installer le client logiciel

1. **Télécharger le fichier IPK du client logiciel :**

   ```bash
   cd /tmp/
   wget https://signal.jimber.io/clients/linux-router-openwrt-latest.ipk
   ```

2. **Installer le client logiciel :**

   ```bash
   opkg install linux-router-openwrt-latest.ipk
   ```

3. **Résultat attendu de l’installation :**

   Pendant l’installation, une sortie semblable à celle-ci devrait s’afficher :

   ```bash
   Installing jimberfw (v1.12.0-router_openwrt22) to root...
   Configuring jimberfw.
   Downloading binaries...
   Download completed.
   Starting jimberfw...
   ```

---

### 5. Vérifier l’installation

1. **Vérifier la version du logiciel installé :**

   ```bash
   jimberfw -version
   ```

   Exemple de sortie :

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

### 6. Configurer le pare-feu Jimber

1. **Localiser le fichier de paramètres :**

   Ouvrez le fichier de paramètres avec `nano` :

   ```bash
   nano /etc/jimber/settings.json
   ```

2. **Mettre à jour le fichier avec votre jeton, votre IP WAN et votre interface :**

   Modifiez le fichier pour inclure les informations requises :

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
    Vous trouverez le jeton dans le contrôleur réseau configuré dans Signal. L’IP WAN correspond à l’IP utilisée par l’appareil pour accéder aux ressources Internet (IP publique).
3. **Enregistrer le fichier et quitter nano :**

   - Appuyez sur `CTRL+O` pour enregistrer le fichier.
   - Appuyez sur `CTRL+X` pour quitter.

---

### 7. Vérifier la connectivité du contrôleur réseau

Une fois la configuration terminée, le contrôleur réseau devrait se connecter et un indicateur d’état vert devrait apparaître dans l’interface web de Signal.

---

### Conclusion

Votre appareil Teltonika RUT950/RUT955 est maintenant configuré avec OpenWRT et les logiciels nécessaires sont installés. Vous pouvez vérifier et superviser la connectivité du contrôleur réseau pour vous assurer que tout fonctionne comme prévu.
