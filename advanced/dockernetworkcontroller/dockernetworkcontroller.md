# How to setup a Docker based Network Controller

## Warning - advanced

>[!WARNING]
> This is an advanced procedure, applicable in certain cases. Please contact Jimber for more information.

## Get the docker client
In the Linux terminal, execute these commands

```
wget https://signal.jimber.io/clients/ncdocker-latest.zip
unzip ncdocker-latest.zip
cd jimbernc_docker
```

In this directory you will find a config.env file

```
ADAPTER=eth0 #Your LAN adapter
TOKEN=token #Token in signalserver
COMPANY=companyname #Company name in signal server
WANIP=199.199.199 #WAN IP of the network of the NC
SUBNET=192.168.2.0/24 #subnet of your network
GATEWAY=192.168.2.240 #your gateway
IP=192.168.2.249 #network ip of the NC
TAG=v1.11.0-docker01 #Version of Jimber NI (no need to change)

```

- Adapter: The adapter that is connected to your LAN network
- Token: The token from the networkcontroller you created in the Jimber Network Isolation platform
- Company: The name of your company
- WAN IP: The public ip address your networkcontroller uses to reach the internet
- Subnet: The subnet of the adapter on your LAN network
- Gateway: The gateway ip on your LAN network
- IP: The ip address you desire for your Network Controller (you should keep this out of your DHCP range)
- TAG: The version of Jimber Network Isolation. This will be prefilled and you should not change the value


You can start the network controller with this command (as root)

```
./start_with_bridge.sh
```

After initialization, the network controller should appear online in the Jimber Network Isolation platform. You can make sure that it restarts on reboot by adding it to the crontab:

```
crontab -e
```

Add following line:

```
@reboot cd /root/jimbernc_docker/ && ./start_with_bridge.sh
```

Replace the path with the path where you extracted the jimbernc_docker folder.