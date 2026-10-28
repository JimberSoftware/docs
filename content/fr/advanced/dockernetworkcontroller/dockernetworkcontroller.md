# Comment configurer un contrôleur réseau basé sur Docker

## Avertissement - avancé

> [!WARNING]
> Il s’agit d’une procédure avancée, qui s’applique dans certains cas. Veuillez contacter Jimber pour plus d’informations.

## Obtenir le client Docker

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
- Jeton : le jeton du contrôleur réseau que vous avez créé dans la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_**
- Sous-réseau : le sous-réseau de l’adaptateur sur votre réseau LAN
- Passerelle : l’adresse IP de la passerelle sur votre réseau LAN
- IP : l’adresse IP que vous souhaitez attribuer à votre contrôleur réseau (il est préférable de ne pas l’inclure dans votre plage DHCP)
- TAG : la version de la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_**. Cette valeur sera préremplie et ne doit pas être modifiée

Vous pouvez démarrer le contrôleur réseau à l’aide de Docker Compose. Pour en savoir plus sur Docker Compose, consultez la [documentation officielle](https://docs.docker.com/compose/).

Après le démarrage du conteneur Docker, le contrôleur réseau devrait apparaître en ligne dans la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_**.

Les appareils connectés au même réseau LAN pourront désormais accéder au conteneur Docker.

> [!WARNING]
> Le conteneur Docker ne sera pas accessible depuis l’hôte. Pour autoriser cet accès, vous devez ajouter une route persistante.

Pour ajouter une route non persistante (afin de tester la connexion), vous pouvez exécuter la commande suivante :
(Remplacez {{IP}} par l’adresse IP que vous avez choisie pour votre conteneur)

```
ip route add {{IP}}/32 via 192.168.254.2
```

Vous pouvez ajouter des routes persistantes selon la configuration de votre système. (Exécutez la commande ci-dessus à l’aide d’un crontab, ou configurez netplan,...)
