# Comment configurer un contrôleur réseau basé sur Docker

## Avertissement — avancé

> [!WARNING]
> Il s’agit d’une procédure avancée, applicable dans certains cas. Veuillez contacter Jimber pour plus d’informations.

## Télécharger le client Docker

Dans le terminal Linux, exécutez ces commandes

```
wget https://signal.jimber.io/clients/ncdocker-latest.zip
unzip ncdocker-latest.zip
cd jimbernc_docker
```

Vous trouverez un fichier .env dans ce répertoire

```
ADAPTER=eth0 #Your LAN adapter
TOKEN=token #Token in signalserver
SUBNET=192.168.2.0/24 #subnet of your network
GATEWAY=192.168.2.240 #your gateway
IP=192.168.2.249 #network ip of the NC
TAG=v1.14.0-docker06 #Version of Jimber NI (no need to change)

```

- Adaptateur : l’adaptateur connecté à votre réseau LAN
- Jeton : le jeton du contrôleur réseau que vous avez créé dans la `Jimber SASE Platform`
- Sous-réseau : le sous-réseau de l’adaptateur sur votre réseau LAN
- Passerelle : l’adresse IP de la passerelle sur votre réseau LAN
- IP : l’adresse IP que vous souhaitez attribuer à votre contrôleur réseau (vous devez la choisir en dehors de votre plage DHCP)
- TAG : la version de Jimber Network Isolation. Ce champ sera prérempli et vous ne devez pas modifier sa valeur

Vous pouvez démarrer le contrôleur réseau à l’aide de Docker Compose. Pour plus d’informations sur Docker Compose, consultez la [documentation officielle](https://docs.docker.com/compose/).

Après le démarrage du conteneur Docker, le contrôleur réseau devrait apparaître en ligne dans la `Jimber SASE Platform`.

Le conteneur Docker sera alors accessible aux appareils connectés au même réseau LAN.

> [!WARNING]
> Le conteneur Docker ne sera pas accessible depuis l’hôte. Pour autoriser cet accès, vous devez ajouter une route persistante.

Pour ajouter une route non persistante (afin de tester la connexion), vous pouvez exécuter la commande suivante :
(Remplacez {{IP}} par l’adresse IP choisie pour votre conteneur)

```
ip route add {{IP}}/32 via 192.168.254.2
```

Vous pouvez ajouter des routes persistantes en fonction de la configuration de votre système. (Exécutez la commande ci-dessus dans une crontab ou configurez netplan,...)
