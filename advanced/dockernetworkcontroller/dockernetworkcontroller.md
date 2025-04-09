# How to setup a Docker based Network Controller

## Warning - advanced

> [!WARNING]
> This is an advanced procedure, applicable in certain cases. Please contact Jimber for more information.

## Get the docker client

In the Linux terminal, execute these commands

```
wget https://signal.jimber.io/clients/ncdocker-latest.zip
unzip ncdocker-latest.zip
cd jimbernc_docker
```

In this directory you will find an .env file

```
ADAPTER=eth0 #Your LAN adapter
TOKEN=token #Token in signalserver
SUBNET=192.168.2.0/24 #subnet of your network
GATEWAY=192.168.2.240 #your gateway
IP=192.168.2.249 #network ip of the NC
TAG=v1.14.0-docker06 #Version of Jimber NI (no need to change)

```

- Adapter: The adapter that is connected to your LAN network
- Token: The token from the networkcontroller you created in the Jimber Network Isolation platform
- Subnet: The subnet of the adapter on your LAN network
- Gateway: The gateway ip on your LAN network
- IP: The ip address you desire for your Network Controller (you should keep this out of your DHCP range)
- TAG: The version of Jimber Network Isolation. This will be prefilled and you should not change the value

You can start the network controller using Docker Compose. For more information on Docker Compose, refer to the [official documentation](https://docs.docker.com/compose/).

After starting the docker container, the network controller should appear online in the Jimber Network Isolation platform.

The Docker container will now be reachable by devices on the same LAN network.

> [!WARNING]
> The Docker container won't be reachable by the host. If you want to allow this, you need to add a persistent route.

To add a non persistent route (to test the connection), you can run the following command:
(Replace {{IP}} with the IP address you chose for your container)

```
ip route add {{IP}}/32 via 192.168.254.2
```

Persistent routes can be added depending on your system setup. (Run the above command as a crontab, or configure netplan,...)
